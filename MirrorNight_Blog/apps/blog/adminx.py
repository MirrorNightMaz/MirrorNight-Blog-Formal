import xadmin
from .models import Categories, Archives, Contacts, PhotoAlbums, Photos


class CategoriesAdmin(object):
    list_display = ['title', 'add_time']
    list_filter = ['title', 'add_time']
    search_fields = ['title']
    ordering = ['-add_time']


class ArchivesAdmin(object):
    list_display = ['title']
    list_filter = ['title']
    ordering = ['-title']


class ContactsAdmin(object):
    list_display = ['name', 'email', 'contact', 'send_time', 'has_read']
    list_filter = ['name', 'email', 'contact', 'send_time', 'has_read']
    search_fields = ['name', 'email', 'contact']
    ordering = ['-send_time']


class PhotoAlbumsAdmin(object):
    list_display = ['title', 'add_time']
    list_filter = ['title', 'add_time']
    search_fields = ['title']
    ordering = ['-add_time']


class PhotosAdmin(object):
    list_display = ['photoalbum', 'photo', 'add_time']
    list_filter = ['photoalbum__title', 'add_time']
    search_fields = ['photoalbum__title']
    ordering = ['-add_time']


xadmin.site.register(Categories, CategoriesAdmin)
xadmin.site.register(Archives, ArchivesAdmin)
xadmin.site.register(Contacts, ContactsAdmin)
xadmin.site.register(PhotoAlbums, PhotoAlbumsAdmin)
xadmin.site.register(Photos, PhotosAdmin)