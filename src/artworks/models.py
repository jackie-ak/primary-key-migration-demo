from base_common.fields import ShortUUIDField

from django.conf import settings
from django.db import models
from django.db.models import JSONField
from django.utils.translation import gettext_lazy as _


class Album(models.Model):
    """Specific users can create their own collections of artworks."""

    id = ShortUUIDField(
        primary_key=True,
    )

    title = models.CharField(verbose_name=_('Title'), max_length=255)
    slides = JSONField(verbose_name=_('Slides'), default=list, blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('User'),
        on_delete=models.CASCADE,
    )
    permissions = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        verbose_name=_('Permissions'),
        through='PermissionsRelation',
        symmetrical=False,
        related_name='permissions',
    )
    last_changed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('Last changed by'),
        related_name='last_album_changes',
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return f'{self.title} (ID: {self.id})'


class PermissionsRelation(models.Model):
    PERMISSION_CHOICES = tuple((p, _(p)) for p in settings.PERMISSIONS)

    album = models.ForeignKey(Album, related_name='album', on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='user',
        on_delete=models.CASCADE,
    )
    permissions = models.CharField(
        max_length=20,
        choices=PERMISSION_CHOICES,
        default=settings.DEFAULT_PERMISSIONS[0],
    )

    def __str__(self):
        return f'{self.user}: Album {self.album} Permission {self.permissions}'


class Folder(models.Model):
    # unique id
    id = ShortUUIDField(
        primary_key=True,
    )
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=255,
        blank=False,
        null=False,
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('User'),
        on_delete=models.CASCADE,
        related_name='folder_owner',
    )
    parent = models.ForeignKey(
        'Folder',
        on_delete=models.CASCADE,
        related_name='folder_to_parent',
        null=True,
        blank=True,
    )
    albums = models.ManyToManyField(
        Album,
        verbose_name=_('Albums'),
        through='FolderAlbumRelation',
        related_name='folder_to_albums',
    )

    def __str__(self):
        return f'{self.title} (ID: {self.id})'


class FolderAlbumRelation(models.Model):
    album = models.ForeignKey(
        Album,
        related_name='rel_to_album',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='rel_to_user',
        on_delete=models.CASCADE,
    )
    folder = models.ForeignKey(
        Folder,
        related_name='rel_to_folder',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.user}: Folder {self.folder} Album {self.album}'
