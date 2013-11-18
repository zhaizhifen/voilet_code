#!/usr/bin/env python
#-*- coding: utf-8 -*-
#=============================================================================
#     FileName:
#         Desc:
#       Author: 苦咖啡
#        Email: voilet@qq.com
#     HomePage: http://blog.kukafei520.net
#      Version: 0.0.1
#   LastChange: 2013-02-20 14:52:11
#      History:
#=============================================================================

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
import xadmin
xadmin.autodiscover()

# from xadmin.plugins import xversion
# xversion.registe_models()

urlpatterns = patterns('',
    url(r'admin/', include(xadmin.site.urls)),
    url(r'^voilet/test/$', 'server_idc.value_class.index.Index'),
    #用户登录注册
    #(r'^accounts/login/$', 'django.contrib.auth.views.login',{'template_name': 'login.html'}),
    (r'^accounts/login/$', 'accounts.account.user_login',),
    (r'^accounts/register/$', 'accounts.views.register'),
    (r'^accounts/loginout/$', 'accounts.views.logout_view'),
    #url(r'^$', 'op.views.index'),
    url(r'^op/$', 'op.views.index'),
    url(r'^opadd/$', 'op.views.OP_POST'),
    #搜索
    # url(r'^search/$', 'assets.views.search'),
    #编缉器
    url(r'^ueditor_imgup$','ueditor.Ueditor.views.ueditor_ImgUp'),
    url(r'^ueditor_fileup$','ueditor.Ueditor.views.ueditor_FileUp'),
    url(r'^ueditor_getRemoteImage$','ueditor.Ueditor.views.ueditor_getRemoteImage'),
    url(r'^ueditor_scrawlUp$','ueditor.Ueditor.views.ueditor_ScrawUp'),
    url(r'^ueditor_getMovie$','ueditor.Ueditor.views.ueditor_getMovie'),
    url(r'^ueditor_imageManager$','ueditor.Ueditor.views.ueditor_imageManager'),
    #报障终级页
    url(r'^op/list/(?P<id>\d+)/$', 'op.views.OP_select'),
    #用户列表
    url(r'^op/user_list/(?P<id>\d+)/$', 'op.views.user_id'),
    #修改
    url(r'^op/user_edit/(?P<id>\d+)/$', 'op.views.OP_edit'),
    #salt_ui
    url(r'^$','salt_ui.views.index.auto'),
    url(r'^overview$','salt_ui.views.index.overview'),
    url(r'^minions$','salt_ui.views.index.minions'),
    url(r'^minion$','salt_ui.views.index.minion'),
    url(r'^execute$','salt_ui.views.index.execute'),
    url(r'^detail$','salt_ui.views.index.detail'),
    url(r'^getjobinfo$','salt_ui.views.index.getjobinfo'),
    url(r'^service$','salt_ui.views.index.service'),
)

