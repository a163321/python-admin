#!/usr/bin/env python
# -*- coding:UTF-8 -*-
'''
@Description: 路由控制器
@Author: Zpp
@Date: 2019-09-10 16:00:22
@LastEditTime : 2019-12-23 15:51:00
@LastEditors  : Zpp
'''
from flask import request
from models.base import db
from models.system import Route
from sqlalchemy import text
import uuid


class RouteModel():
    def QueryRouteByParamRequest(self, params):
        '''
        路由列表
        '''
        s = db.session()
        try:
            data = {}
            if params.has_key('isLock'):
                data['isLock'] = params['isLock']

            result = Route.query.filter_by(**data).filter(
                Route.name.like("%" + params['name'] + "%") if params.has_key('name') else text('')
            ).order_by(Route.id).all()

            return [value.to_json() for value in result]
        except Exception as e:
            print e
            return str(e.message)

    def CreateRouteRequest(self, params):
        '''
        新建路由
        '''
        s = db.session()
        try:
            item = Route(
                route_id=uuid.uuid4(),
                parent_id=params['parent_id'],
                name=params['name'],
                title=params['title'],
                path=params['path'],
                component=params['component'],
                componentPath=params['componentPath'],
                cache=params['cache']
            )
            s.add(item)
            s.commit()
            return True
        except Exception as e:
            s.rollback()
            print e
            return str(e.message)

    def GetRouteRequest(self, route_id):
        '''
        查询路由
        '''
        s = db.session()
        try:
            route = s.query(Route).filter(Route.route_id == route_id).first()
            if not route:
                return str('路由不存在')

            return route.to_json()
        except Exception as e:
            print e
            return str(e.message)

    def ModifyRouteRequest(self, route_id, params):
        '''
        修改路由信息
        '''
        s = db.session()
        try:
            route = s.query(Route).filter(Route.route_id == route_id).first()
            if not route:
                return str('路由不存在')

            AllowableFields = ['parent_id', 'name', 'path', 'title', 'component', 'componentPath', 'cache']
            data = {}

            for i in params:
                if i in AllowableFields and params.has_key(i):
                    data[i] = params[i]

            s.query(Route).filter(Route.route_id == route_id).update(data)
            s.commit()
            return True
        except Exception as e:
            print e
            s.rollback()
            return str(e.message)

    def LockRouteRequest(self, route_id, isLock):
        '''
        禁用路由
        '''
        s = db.session()
        try:
            s.query(Route).filter(Route.route_id.in_(route_id)).update({Route.isLock: isLock})
            s.commit()
            return True
        except Exception as e:
            print e
            s.rollback()
            return str(e.message)
