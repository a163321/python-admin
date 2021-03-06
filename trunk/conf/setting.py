#!/usr/bin/env python
# -*- coding:UTF-8 -*-
'''
@Description: 基本配置信息
@Author: Zpp
@Date: 2019-09-02 15:53:39
@LastEditTime : 2019-12-24 10:43:00
@LastEditors  : Zpp
'''
import hashlib
import os

basedir = os.path.abspath(os.path.dirname(__file__) + '/..')

token_info = {
    'expiration': 30 * 24 * 3600,
    'SECRET_KEY': 'k#6@1%8)a'
}

# 启动服务参数 字典类型
server_info = {
    "host": '0.0.0.0',
    "port": 5000,  # 启动服务的端口号
}

# 文档路径
document_dir = os.path.join(basedir, 'document')

# 日志
log_info = {
    'LOG_FILE_BACKUP_COUNT': 0,
    'LOG_PATH_INFO': os.path.join(os.path.join(basedir, 'logs'), 'info.log')
}

# session参数
session_info = {
    'SESSION_TYPE': 'filesystem',
    'SESSION_FILE_DIR': os.path.join(basedir, 'sessions'),
    'SESSION_FILE_THRESHOLD': 500,
    'SESSION_FILE_MODE': 384
}

# cache参数
cache_info = {
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': os.path.join(basedir, 'caches'),
    'CACHE_THRESHOLD': 500
}

# 初始化路由配置
init_route = [
    {
        'name': 'System',
        'path': '/system',
        'component': 'layoutHeaderAside',
        'componentPath': 'layout/header-aside',
        'title': u'系统设置',
        'cache': True,
        'children': [
            {
                'name': 'MenuPage',
                'path': '/system/menu',
                'component': 'menu',
                'componentPath': 'sys/menu/index',
                'title': u'菜单管理',
                'cache': True
            },
            {
                'name': 'RoutePage',
                'path': '/system/route',
                'component': 'route',
                'componentPath': 'sys/route/index',
                'title': u'路由管理',
                'cache': True
            },
            {
                'name': 'InterfacePage',
                'path': '/system/interface',
                'component': 'interface',
                'componentPath': 'sys/interface/index',
                'title': u'接口管理',
                'cache': True
            },
            {
                'name': 'DocumentPage',
                'path': '/system/document',
                'component': 'document',
                'componentPath': 'sys/document/index',
                'title': u'文档管理',
                'cache': True
            }
        ]
    },
    {
        'name': 'Role',
        'path': '/role',
        'component': 'layoutHeaderAside',
        'componentPath': 'layout/header-aside',
        'title': u'权限管理',
        'cache': True,
        'children': [
            {
                'name': 'AdminPage',
                'path': '/role/admin',
                'component': 'admin',
                'componentPath': 'sys/admin/index',
                'title': u'管理员用户',
                'cache': True
            },
            {
                'name': 'RolePage',
                'path': '/role/role',
                'component': 'role',
                'componentPath': 'sys/role/index',
                'title': u'角色管理',
                'cache': True
            }
        ]
    },
    {
        'name': 'Log',
        'path': '/log',
        'component': 'layoutHeaderAside',
        'componentPath': 'layout/header-aside',
        'title': u'日志管理',
        'cache': True,
        'children': [
            {
                'name': 'LogLogin',
                'path': '/log/login',
                'component': 'login',
                'componentPath': 'sys/login/index',
                'title': u'登录日志',
                'cache': True
            },
            {
                'name': 'LogHander',
                'path': '/log/hander',
                'component': 'hander',
                'componentPath': 'sys/hander/index',
                'title': u'操作日志',
                'cache': True
            },
            {
                'name': 'LorError',
                'path': '/log/error',
                'component': 'error',
                'componentPath': 'sys/error/index',
                'title': u'异常日志',
                'cache': True
            }
        ]
    }
]

# 初始化菜单和下属的接口
init_menu = [
    {
        "title": "系统",
        "path": "/system",
        "icon": "cog",
        "children": [
            {
                "title": "菜单管理",
                "path": "/system/menu",
                "icon": "th-list",
                "interface": [
                    {
                        "path": "/v1/Menu/CreateMenu",
                        "method": "POST",
                        "name": "CreateMenu",
                        "description": "添加菜单",
                        "identification": "add_menu"
                    },
                    {
                        "path": "/v1/Menu/QueryMenuByParam",
                        "method": "POST",
                        "name": "QueryMenuByParam",
                        "description": "获取菜单列表",
                        "identification": "get_menu_list"
                    },
                    {
                        "path": "/v1/Menu/ModifyMenu",
                        "method": "POST",
                        "name": "ModifyMenu",
                        "description": "修改菜单信息",
                        "identification": "set_menu"
                    },
                    {
                        "path": "/v1/Menu/LockMenu",
                        "method": "POST",
                        "name": "LockMenu",
                        "description": "禁用菜单",
                        "identification": "lock_menu"
                    },
                    {
                        "path": "/v1/Menu/GetMenu",
                        "method": "GET",
                        "name": "GetMenu",
                        "description": "根据ID获取菜单",
                        "identification": "get_menu_item"
                    }
                ]
            },
            {
                "title": "路由管理",
                "path": "/system/route",
                "icon": "share-alt",
                "interface": [
                    {
                        "path": "/v1/Route/CreateRoute",
                        "method": "POST",
                        "name": "CreateRoute",
                        "description": "添加路由",
                        "identification": "add_router"
                    },
                    {
                        "path": "/v1/Route/QueryRouteByParam",
                        "method": "POST",
                        "name": "QueryRouteByParam",
                        "description": "获取路由列表",
                        "identification": "get_router_list"
                    },
                    {
                        "path": "/v1/Route/ModifyRoute",
                        "method": "POST",
                        "name": "ModifyRoute",
                        "description": "修改路由信息",
                        "identification": "set_router"
                    },
                    {
                        "path": "/v1/Route/LockRoute",
                        "method": "POST",
                        "name": "LockRoute",
                        "description": "禁用路由",
                        "identification": "lock_router"
                    }
                ]
            },
            {
                "title": "接口管理",
                "path": "/system/interface",
                "icon": "send",
                "interface": [
                    {
                        "path": "/v1/Interface/CreateInterface",
                        "method": "POST",
                        "name": "CreateInterface",
                        "description": "添加接口",
                        "identification": "add_interface"
                    },
                    {
                        "path": "/v1/Interface/QueryInterfaceByParam",
                        "method": "POST",
                        "name": "QueryInterfaceByParam",
                        "description": "获取接口列表",
                        "identification": "get_interface_list"
                    },
                    {
                        "path": "/v1/Interface/ModifyInterface",
                        "method": "POST",
                        "name": "ModifyInterface",
                        "description": "修改接口信息",
                        "identification": "set_interface"
                    },
                    {
                        "path": "/v1/Interface/LockInterface",
                        "method": "POST",
                        "name": "LockInterface",
                        "description": "禁用接口",
                        "identification": "lock_interface"
                    }
                ]
            },
            {
                "title": "文档管理",
                "path": "/system/document",
                "icon": "folder-open-o",
                "interface": [
                    {
                        "path": "/v1/Document/CreateDocument",
                        "method": "POST",
                        "name": "CreateDocument",
                        "description": "添加文档",
                        "identification": "add_document"
                    },
                    {
                        "path": "/v1/Document/QueryDocumentByParam",
                        "method": "POST",
                        "name": "QueryDocumentByParam",
                        "description": "获取文档列表",
                        "identification": "get_document_list"
                    },
                    {
                        "path": "/v1/Document/DownDocument",
                        "method": "GET",
                        "name": "DownDocument",
                        "description": "下载文档",
                        "identification": "down_document"
                    },
                    {
                        "path": "/v1/Document/DelDocument",
                        "method": "POST",
                        "name": "DelDocument",
                        "description": "删除文档",
                        "identification": "del_document"
                    },
                    {
                        "path": "/v1/Document/RetrieveDocument",
                        "method": "POST",
                        "name": "RetrieveDocument",
                        "description": "回收文档",
                        "identification": "retrieve_document"
                    },
                    {
                        "path": "/v1/Folder/CreateFolder",
                        "method": "POST",
                        "name": "CreateFolder",
                        "description": "创建文件夹",
                        "identification": "create_folder"
                    },
                    {
                        "path": "/v1/Folder/DelFolder",
                        "method": "POST",
                        "name": "DelFolder",
                        "description": "删除文件夹",
                        "identification": "del_folder"
                    },
                    {
                        "path": "/v1/Folder/ModifyFolder",
                        "method": "POST",
                        "name": "ModifyFolder",
                        "description": "修改文件夹",
                        "identification": "modify_folder"
                    },
                    {
                        "path": "/v1/Folder/QueryFolderByParam",
                        "method": "POST",
                        "name": "QueryFolderByParam",
                        "description": "获取文档列表",
                        "identification": "query_folder"
                    }
                ]
            }
        ]
    },
    {
        "title": "权限",
        "path": "/role",
        "icon": "shield",
        "children": [
            {
                "title": "管理员用户",
                "path": "/role/admin",
                "icon": "user",
                "interface": [
                    {
                        "path": "/v1/Admin/CreateAdmin",
                        "method": "POST",
                        "name": "CreateAdmin",
                        "description": "注册管理员",
                        "identification": "add_admin"
                    },
                    {
                        "path": "/v1/Admin/QueryAdminByParam",
                        "method": "POST",
                        "name": "QueryAdminByParam",
                        "description": "获取管理员列表",
                        "identification": "get_admin_list"
                    },
                    {
                        "path": "/v1/Admin/ModifyAdmin",
                        "method": "POST",
                        "name": "ModifyAdmin",
                        "description": "修改管理员信息",
                        "identification": "set_admin"
                    },
                    {
                        "path": "/v1/Admin/LockAdmin",
                        "method": "POST",
                        "name": "LockAdmin",
                        "description": "禁用管理员",
                        "identification": "lock_admin"
                    },
                    {
                        "path": "/v1/Admin/Logout",
                        "method": "GET",
                        "name": "Logout",
                        "description": "注销管理员",
                        "identification": "logout_admin"
                    },
                    {
                        "path": "/v1/Admin/CreateDrop",
                        "method": "GET",
                        "name": "CreateDrop",
                        "description": "初始化数据库",
                        "identification": "init_admin"
                    }
                ]
            },
            {
                "title": "角色管理",
                "path": "/role/role",
                "icon": "group",
                "interface": [
                    {
                        "path": "/v1/Role/CreateRole",
                        "method": "POST",
                        "name": "CreateRole",
                        "description": "添加角色",
                        "identification": "add_role"
                    },
                    {
                        "path": "/v1/Role/QueryRoleByParam",
                        "method": "POST",
                        "name": "QueryRoleByParam",
                        "description": "获取角色列表",
                        "identification": "get_role_list"
                    },
                    {
                        "path": "/v1/Role/ModifyRole",
                        "method": "POST",
                        "name": "ModifyRole",
                        "description": "修改角色信息",
                        "identification": "set_role"
                    },
                    {
                        "path": "/v1/Role/LockRole",
                        "method": "POST",
                        "name": "LockRole",
                        "description": "禁用角色",
                        "identification": "lock_role"
                    }
                ]
            }
        ]
    },
    {
        "title": "日志",
        "path": "/log",
        "icon": "bullseye",
        "children": [
            {
                "title": "登录日志",
                "path": "/log/login",
                "icon": "street-view",
                "interface": [
                    {
                        "path": "/v1/Log/QueryLogByParam",
                        "method": "POST",
                        "name": "QueryLogByParam",
                        "description": "获取日志列表",
                        "identification": "get_log_list"
                    }
                ]
            },
            {
                "title": "操作日志",
                "path": "/log/hander",
                "icon": "dot-circle-o"
            },
            {
                "title": "异常日志",
                "path": "/log/error",
                "icon": "bug"
            }
        ]
    }
]


class Config():
    def __init__(self):
        # mysql 配置信息
        self.host = '127.0.0.1'
        self.port = 3306
        self.admin = 'root'
        self.password = 'intersky'
        self.db = 'flask'
        self.charset = 'utf8'

    def get_sql_url(self):
        return "mysql://%s:%s@%s:%s/%s?charset=utf8" % (self.admin, self.password, self.host, self.port, self.db)

    def get_md5(self, m):
        h = hashlib.md5()
        h.update(m.encode('utf-8'))
        return h.hexdigest()
