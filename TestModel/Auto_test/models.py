
from django.db import models
from django.utils.six import python_2_unicode_compatible

# Create your models here.


@python_2_unicode_compatible
class Column(models.Model):
    # 编辑Story状态
    STATUS_CHOICES = (
     (1, '待执行'),
     (2, '已执行'),
     (3, '待再次执行'),
      )
    STATUS_CHOICES1 = (
        (1, 'app'),
        (2, 'wap'),
        (3, 'web'),
    )
    STATUS_CHOICES2 = (
        (1, 'web或者wap'),
        (2, 'app1.7'),
        (3, 'app2.2'),

    )
    name = models.CharField('项目名称', max_length=50)
    slug = models.IntegerField(choices=STATUS_CHOICES2, default=1, verbose_name=u'项目版本',db_index=True)
    platform = models.IntegerField(choices=STATUS_CHOICES1, default=1, verbose_name=u'项目平台')
    author = models.ForeignKey('auth.User', blank=True, null=True, verbose_name='添加用户')
    intro = models.TextField('项目简介', default='')
    #status = models.IntegerField(choices=STATUS_CHOICES, default=1, verbose_name=u'执行测试状态')
    pub_date = models.DateTimeField('创建时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '自动化项目管理'
        verbose_name_plural = '自动化项目管理'
        ordering = ['name']  # 按照哪个栏目排序


@python_2_unicode_compatible
class Appconfig(models.Model):
    column = models.ForeignKey(Column)

    name = models.CharField('设备系统',default='Android', max_length=20)
    version = models.CharField('设备系统版本', max_length=20)
    devicename = models.CharField('设备名称(deviceName)', max_length=20)
    apppath = models.CharField('绝对路径（设置此项后两项可不填，反之同理）', blank=True, null=True, max_length=256)
    apppackage = models.CharField('appPackage',blank=True,null=True, max_length=80)
    appactivity= models.CharField('appActivity',blank=True,null=True,max_length=80)

    #content = models.TextField('备注', default='', blank=True)

    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '设备管理'
        verbose_name_plural = '设备管理'

@python_2_unicode_compatible
class Testpage(models.Model):
    column = models.ManyToManyField(Column, verbose_name='归属项目')

    name = models.CharField('页面名称', max_length=80)
    #slug = models.CharField('测试版本', max_length=256, db_index=True)
    intro = models.TextField('页面简介', default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '页面管理'
        verbose_name_plural = '页面管理'
        ordering = ['name']  # 按照哪个栏目排序


@python_2_unicode_compatible
class Testcase(models.Model):
    Testpage = models.ManyToManyField(Testpage, verbose_name='归属页面')

    name = models.CharField('英文名称', max_length=80)
    step = models.CharField('测试步骤', max_length=256)
    approach = models.CharField('定位方法', max_length=256)
    element = models.CharField('定位元素', max_length=256)

    author = models.ForeignKey('auth.User', blank=True, null=True, verbose_name='用户')
    content = models.TextField('备注', default='', blank=True)

    published = models.BooleanField('正式发布', default=True)
    pub_date = models.DateTimeField('添加时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '用例管理'
        verbose_name_plural = '用例管理'
