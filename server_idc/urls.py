#!/usr/bin/env python
#-*- coding: utf-8 -*-
#=============================================================================
#     FileName:
#         Desc:
#       Author: 苦咖啡
#        Email: voilet@qq.com
#     HomePage: http://blog.kukafei520.net
#      Version: 0.0.1
#   LastChange: 
#      History:
#=============================================================================

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# import xadmin
#import op.views
# xadmin.autodiscover()

urlpatterns = patterns('',
    #资产管理
    url(r'edit_id/(?P<id>\d+)/$', 'server_idc.value_class.index.server_edit'),
    url(r'update_id/(?P<id>\d+)/$', 'server_idc.value_class.service_update.server_update'),
    url(r'server/server_type/(?P<id>\d+)/$', 'server_idc.value_class.index.server_type_list'),
    url(r'server/node_id/(?P<id>\d+)/$', 'server_idc.value_class.index.services_list_id'),
    url(r'server/type/add/', 'server_idc.value_class.index.server_type_add'),
    url(r'server/type/list/', 'server_idc.value_class.index.auth_server_type_list'),
    url(r'server/type/edit/(?P<id>\d+)/$', 'server_idc.value_class.index.auth_server_type_edit'),
    url(r'server/type/del/', 'server_idc.value_class.service_type.auth_server_type_delete'),
    url(r'server/type/notid/', 'server_idc.value_class.service_type.server_type_notnode'),
    url(r'server/edit/log/', 'server_idc.idc_edit_log.idc_log.server_log_list'),
    url(r'server/list/', 'server_idc.value_class.index.services_list_all'),
    url(r'server/install/', 'server_idc.value_class.index.services_install_all'),
    url(r'server/install_error/', 'server_idc.value_class.index.services_install_error'),
    url(r'server/add/', 'server_idc.value_class.index.Index_add'),
    url(r'server/room/', 'server_idc.value_class.Engine_room.Engine_Room'),
    url(r'server/node_del/(?P<id>\d+)/$', 'server_idc.value_class.index.server_id_delete'),

    url(r'/', 'server_idc.value_class.index.services_list_all'),

)


