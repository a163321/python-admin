#!/usr/bin/env python
# -*- coding:UTF-8 -*-
'''
@Description: 
@Author: Zpp
@Date: 2019-09-05 16:07:19
@LastEditTime: 2019-10-14 16:54:12
@LastEditors: Zpp
'''
from flask import Flask
import models
import routes
import services
import logs
import logging


def create_app():
    app = Flask(__name__)
    models.init_app(app)
    routes.init_app(app)
    services.init_app(app)
    return app


logs.init_app()
# 初始化
logging.info(u'-----初始化项目-----')
app = create_app()
logging.info('--------------------')


@app.errorhandler(404)
def handle_404_error(error):
    return "出现了404错误，错误信息：%s" % error


@app.errorhandler(500)
def handle_500_error(error):
    return "出现了500错误，错误信息：%s" % error

try:
    logging.info(u'------启动成功------')
    app.run()
except Exception as e:
    logging.error(u'------启动失败------')
