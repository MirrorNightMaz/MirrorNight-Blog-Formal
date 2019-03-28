import xadmin
from .models import MyUsers, EmailVerificationCodes
from xadmin import views
from xadmin.plugins.auth import UserAdmin


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = 'MirrorNight&Blog后台管理系统'
    site_footer = 'MirrorNight'
    menu_style = 'accordion'
    apps_icons = {'high': 'fa fa-cloud', 'blog': 'fa fa-trophy', 'appearance': 'fa fa-picture-o'}


class MyUsersAdmin(UserAdmin):
    list_display = ['username', 'email', 'is_active', 'is_staff', 'is_superuser', 'date_joined']
    list_filter = ['username', 'email', 'is_active', 'is_staff', 'is_superuser', 'date_joined']
    search_fields = ['username', 'email']
    ordering = ['-date_joined']


class EmailVerificationCodesAdmin(UserAdmin):
    list_display = ['user_id', 'type', 'code', 'send_time', 'duration']
    list_filter = ['user_id', 'type', 'code', 'send_time', 'duration']
    search_fields = ['user_id', 'type', 'code', 'duration']
    ordering = ['-send_time']


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.unregister(MyUsers)
xadmin.site.register(MyUsers, MyUsersAdmin)
xadmin.site.register(EmailVerificationCodes, EmailVerificationCodesAdmin)