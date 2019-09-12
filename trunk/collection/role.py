#!/usr/bin/env python
# -*- coding:UTF-8 -*-
'''
@Description: 权限控制器
@Author: Zpp
@Date: 2019-09-10 16:01:46
@LastEditTime: 2019-09-12 14:04:35
@LastEditors: Zpp
'''
from models.base import db
from models.user import Role


class RoleModel():
    def QueryRoleByParamRequest(self, page=1, page_size=20, order_by='-id'):
        '''
        权限列表
        '''
        s = db.session()
        try:
            result = Role.query.order_by(order_by).paginate(page, page_size, error_out=False)

            data = []
            for value in result.items:
                data.append(value.to_json())

            return {'data': data, 'total': result.total}
        except Exception as e:
            print e
            return str(e.message)
        finally:
            s.close()

    def CreateRoleRequest(self, params):
        '''
        新建权限
        '''
        s = db.session()
        try:
            item = Role(
                name=params['name'],
                type=int(params['type'])
            )
            s.add(item)
            s.commit()
            return True
        except Exception as e:
            s.rollback()
            print e
            return str(e.message)
        finally:
            s.close()

    def GetRoleRequest(self, role_id):
        '''
        查询权限
        '''
        s = db.session()
        try:
            role = s.query(Role).filter(Role.id == role_id).first()
            if not role:
                return str('数据不存在')

            return role.to_json()
        except Exception as e:
            print e
            return str(e.message)
        finally:
            s.close()

    def ModifyRoleRequest(self, role_id, name):
        '''
        修改权限信息
        '''
        s = db.session()
        try:
            role = s.query(Role).filter(Role.id == role_id).first()
            if not role:
                return str('数据不存在')

            role.name = name
            s.commit()
            return True
        except Exception as e:
            print e
            s.rollback()
            return str(e.message)
        finally:
            s.close()

    def LockRoleRequest(self, role_id):
        '''
        禁用权限
        '''
        s = db.session()
        try:
            for key in role_id:
                role = s.query(Role).filter(Role.role_id == key).first()
                if not role:
                    continue
                role.isLock = False
                s.commit()
            return True
        except Exception as e:
            print e
            s.rollback()
            return str(e.message)
        finally:
            s.close()

    def QueryRouteByParamRequest(self, params, page=1, page_size=20, order_by='-id'):
        '''
        权限列表
        '''
        s = db.session()
        try:
            Int = ['isLock']
            data = {}

            for i in Int:
                if params.has_key(i):
                    data[i] = params[i]

            result = Route.query.filter_by(*data).filter(
                Route.name.like("%" + params['name'] + "%") if params.has_key('name') else ''
            ).order_by(order_by).paginate(page, page_size, error_out=False)

            data = []
            for value in result.items:
                data.append(value.to_json())

            return {'data': data, 'total': result.total}
        except Exception as e:
            print e
            return str(e.message)
        finally:
            s.close()
