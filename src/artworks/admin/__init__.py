from django.contrib import admin

from ..models import Album, Folder, FolderAlbumRelation, PermissionsRelation


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'user',
        'last_changed_by',
    )


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'parent',
        'owner',
    )


@admin.register(FolderAlbumRelation)
class FolderAlbumAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'folder',
        'album',
    )


@admin.register(PermissionsRelation)
class PermissionsRelationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'album',
        'user',
        'permissions',
    )
