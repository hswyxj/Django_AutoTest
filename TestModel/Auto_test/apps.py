# Auto_test/apps.py

from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem


class SuitConfig(DjangoSuitConfig):
    ##layout这个参数决定你的网页是初始样式是垂直样式还是水平样式，可选参数为‘horizontal’或‘vertical’
    layout = 'vertical'

    #
    menu = (
        ParentItem('自动化管理', children=[
            ChildItem(model='TestModel.Column'),
            ChildItem(model='TestModel.Article'),
            ChildItem(model='TestModel.Testpage'),
            ChildItem(model='TestModel.Testcase'),
            ChildItem('自动化项目管理', url='/admin/Auto_test/column/'),
            ChildItem('Jenkins集成平台', url='http://192.168.86.128:8001/',target_blank=True),
            #ChildItem('页面管理', url='/admin/TestModel/testpage/'),
            #ChildItem('用例管理', url='/admin/TestModel/testcase/'),
        ], icon='fa fa-leaf'),

        #ParentItem('Jenkins集成平台', children=[
        #   ChildItem('Jenkins集成平台', url='http://192.168.20.62:8080/',target_blank=True),
        #], icon='fa fa-leaf'),

        ParentItem('用户管理', children=[
            ChildItem(model='auth.user'),
            ChildItem('组别', 'auth.group'),
        ], icon='fa fa-users'),

        ParentItem('个人中心', children=[
            ChildItem('修改密码', url='admin:password_change'),
            #ChildItem('测试打开google', url='http://google.com', target_blank=True),
        ], align_right=True, icon='fa fa-cog'),
    )



    def ready(self):
        super(SuitConfig, self).ready()


    def prevent_user_last_login(self):
        """
        Disconnect last login signal
        """
        from django.contrib.auth import user_logged_in
        from django.contrib.auth.models import update_last_login
        user_logged_in.disconnect(update_last_login)
