import xadmin
from .models import Welcome_bg, Banners, Newest_bg, Declare_bg, Bloglist_bg, Detail_bg, Commenta_bg, Commentb_bg, Contact_bg, Login_bg, Register_bg, Forget_bg, Reset_bg, Words


class Welcome_bgAdmin(object):
    list_display = ['welcome_bg', 'remark', 'add_time']
    list_filter = ['add_time']
    search_fields = ['remark']
    ordering = ['-add_time']


class BannersAdmin(object):
    list_display = ['banner', 'remark', 'add_time']
    list_filter = ['add_time']
    search_fields = ['remark']
    ordering = ['-add_time']


class Newest_bgAdmin(object):
    list_display = ['newest_bg', 'remark', 'add_time']
    list_filter = ['add_time']
    search_fields = ['remark']
    ordering = ['-add_time']


class Declare_bgAdmin(object):
    list_display = ['declare_bg', 'remark', 'add_time']
    list_filter = ['add_time']
    search_fields = ['remark']
    ordering = ['-add_time']


class Bloglist_bgAdmin(object):
    list_display = ['bloglist_bg', 'remark', 'add_time']
    list_filter = ['add_time']
    search_fields = ['remark']
    ordering = ['-add_time']


class Detail_bgAdmin(object):
    list_display = ['detail_bg', 'remark', 'add_time']
    list_filter = ['add_time']
    search_fields = ['remark']
    ordering = ['-add_time']


class Commenta_bgAdmin(object):
    list_display = ['commenta_bg', 'remark', 'add_time']
    list_filter = ['add_time']
    search_fields = ['remark']
    ordering = ['-add_time']


class Commentb_bgAdmin(object):
    list_display = ['commentb_bg', 'remark', 'add_time']
    list_filter = ['add_time']
    search_fields = ['remark']
    ordering = ['-add_time']


class Contact_bgAdmin(object):
    list_display = ['contact_bg', 'remark', 'add_time']
    list_filter = ['add_time']
    search_fields = ['remark']
    ordering = ['-add_time']


class Login_bgAdmin(object):
    list_display = ['login_bg', 'remark', 'add_time']
    list_filter = ['add_time']
    search_fields = ['remark']
    ordering = ['-add_time']


class Register_bgAdmin(object):
    list_display = ['register_bg', 'remark', 'add_time']
    list_filter = ['add_time']
    search_fields = ['remark']
    ordering = ['-add_time']


class Forget_bgAdmin(object):
    list_display = ['forget_bg', 'remark', 'add_time']
    list_filter = ['add_time']
    search_fields = ['remark']
    ordering = ['-add_time']


class Reset_bgAdmin(object):
    list_display = ['reset_bg', 'remark', 'add_time']
    list_filter = ['add_time']
    search_fields = ['remark']
    ordering = ['-add_time']


class WordsAdmin(object):
    list_display = ['update_time']
    list_filter = ['update_time']
    ordering = ['-update_time']


xadmin.site.register(Welcome_bg, Welcome_bgAdmin)
xadmin.site.register(Banners, BannersAdmin)
xadmin.site.register(Newest_bg, Newest_bgAdmin)
xadmin.site.register(Declare_bg, Declare_bgAdmin)
xadmin.site.register(Bloglist_bg, Bloglist_bgAdmin)
xadmin.site.register(Detail_bg, Detail_bgAdmin)
xadmin.site.register(Commenta_bg, Commenta_bgAdmin)
xadmin.site.register(Commentb_bg, Commentb_bgAdmin)
xadmin.site.register(Contact_bg, Contact_bgAdmin)
xadmin.site.register(Login_bg, Login_bgAdmin)
xadmin.site.register(Register_bg, Register_bgAdmin)
xadmin.site.register(Forget_bg, Forget_bgAdmin)
xadmin.site.register(Reset_bg, Reset_bgAdmin)
xadmin.site.register(Words, WordsAdmin)