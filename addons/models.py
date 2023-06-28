from django.db import models
from django.contrib.auth.models import User

# name
class Whitelist(models.Model):

    name = models.CharField(max_length=16, verbose_name='Ник игрока в вайтлисте')

    class Meta:
        verbose_name = 'Ник игрока в вайтлисте'
        verbose_name_plural = 'Ники игроков в вайтлисте'

# uuid, type | добавить в admin.py
class Allow(models.Model):
    
    uuid = models.BinaryField(max_length=16, null=False, verbose_name='uuid')
    type = models.PositiveSmallIntegerField(null=False, verbose_name='type')
    
    class Meta:
        verbose_name = 'Litebans_Allow'
        verbose_name_plural = 'Litebans_Allow'

# img, msg, time | добавить в admin.py
class Sync(models.Model):
    
    info = models.PositiveIntegerField(null=False, verbose_name='info')
    msg = models.CharField(max_length=4096, null=False, verbose_name='msg')
    time = models.DateTimeField(auto_now_add=True, null=False, verbose_name='time')
    
    class Meta:
        verbose_name = 'Litebans_Sync'
        verbose_name_plural = 'Litebans_Sync'

# name, uuid, date | добавить в admin.py
class Servers(models.Model):
    
    name = models.CharField(max_length=32, null=False, verbose_name='name')
    uuid = models.CharField(max_length=32, null=False, verbose_name='uuid')
    date = models.DateTimeField(auto_now_add=True, null=True, verbose_name='date')
    
    class Meta:
        verbose_name = 'Litebans_Servers'
        verbose_name_plural = 'Litebans_Servers'

# version, build, timezone | добавить в admin.py
class Config(models.Model):
    
    version = models.CharField(max_length=128, null=False, verbose_name='version')
    build = models.CharField(max_length=128, null=False, verbose_name='build')
    timezone = models.CharField(max_length=64, null=False, default='+00:00', verbose_name='timezone')
    
    class Meta:
        verbose_name = 'Litebans_Config'
        verbose_name_plural = 'Litebans_Config'

class MySQLBooleanField(models.BooleanField):

    def to_python(self, value):
        if isinstance(value, bool):
            return value
        return bytearray(value)[0]

    def from_db_value(self, value):
        return '\x01' if value else '\x00'

# uuid, ip, reason, banned_by_uuid, banned_by_name, removed_by_uuid, removed_by_name, removed_by_reason, removed_by_date, time, until, template, server_scope, server_origin, silent, ipban, ipban_wildcard, active | добавить в admin.py
class Bans(models.Model):
    
    uuid = models.CharField(max_length=36, null=True, default=None, verbose_name='uuid')
    ip = models.CharField(max_length=45, null=True, default=None, verbose_name='ip')
    reason = models.CharField(max_length=2048, null=True, default=None, verbose_name='reason')
    banned_by_uuid = models.CharField(max_length=36, null=False, verbose_name='banned_by_uuid')
    banned_by_name = models.CharField(max_length=128, null=True, default=None, verbose_name='banned_by_name')
    removed_by_uuid = models.CharField(max_length=36, null=True, default=None, verbose_name='removed_by_uuid')
    removed_by_name = models.CharField(max_length=128, null=True, default=None, verbose_name='removed_by_name')
    removed_by_reason = models.CharField(max_length=2048, null=True, default=None, verbose_name='removed_by_reason')
    removed_by_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name='removed_by_date')
    time = models.BigIntegerField(null=False, verbose_name='time')
    until = models.BigIntegerField(null=False, verbose_name='until')
    template = models.PositiveSmallIntegerField(null=False, default=255, verbose_name='template')
    server_scope = models.CharField(max_length=32, null=True, default=None, verbose_name='server_scope')
    server_origin = models.CharField(max_length=32, null=True, default=None, verbose_name='server_origin')
    silent = MySQLBooleanField(null=True)
    ipban = MySQLBooleanField(null=True)
    ipban_wildcard = MySQLBooleanField(null=True, default=b'0')
    active = MySQLBooleanField(null=True)
    
    class Meta:
        verbose_name = 'Litebans_Bans'
        verbose_name_plural = 'Litebans_Bans'

# date, name, uuid, ip | добавить в admin.py
class History(models.Model):
    
    date = models.DateTimeField(auto_now_add=True, null=True, verbose_name='date')
    name = models.CharField(max_length=16, null=True, default=None, verbose_name='name')
    uuid = models.CharField(max_length=36, null=True, default=None, verbose_name='uuid')
    ip = models.CharField(max_length=45, null=True, default=None, verbose_name='ip')
    
    class Meta:
        verbose_name = 'Litebans_History'
        verbose_name_plural = 'Litebans_History'

# uuid, ip, reason, banned_by_uuid, banned_by_name, time, until, template, server_scope, server_origin, silent, ipban, ipban_wildcard, active | добавить в admin.py
class Kicks(models.Model):
    
    uuid = models.CharField(max_length=36, null=True, default=None, verbose_name='uuid')
    ip = models.CharField(max_length=45, null=True, default=None, verbose_name='ip')
    reason = models.CharField(max_length=2048, null=True, default=None, verbose_name='reason')
    banned_by_uuid = models.CharField(max_length=36, null=False, verbose_name='banned_by_uuid')
    banned_by_name = models.CharField(max_length=128, null=True, default=None, verbose_name='banned_by_name')
    time = models.BigIntegerField(null=False, verbose_name='time')
    until = models.BigIntegerField(null=False, verbose_name='until')
    template = models.PositiveSmallIntegerField(null=False, default=255, verbose_name='template')
    server_scope = models.CharField(max_length=32, null=True, default=None, verbose_name='server_scope')
    server_origin = models.CharField(max_length=32, null=True, default=None, verbose_name='server_origin')
    silent = MySQLBooleanField(null=True)
    ipban = MySQLBooleanField(null=True)
    ipban_wildcard = MySQLBooleanField(null=True, default=b'0')
    active = MySQLBooleanField(null=True)
    
    class Meta:
        verbose_name = 'Litebans_Kicks'
        verbose_name_plural = 'Litebans_Kicks'

# uuid, ip, reason, banned_by_uuid, banned_by_name, removed_by_uuid, removed_by_name, removed_by_reason, removed_by_date, time, until, template, server_scope, server_origin, silent, ipban, ipban_wildcard, active, warned | добавить в admin.py
class Warnings(models.Model):
    
    uuid = models.CharField(max_length=36, null=True, default=None, verbose_name='uuid')
    ip = models.CharField(max_length=45, null=True, default=None, verbose_name='ip')
    reason = models.CharField(max_length=2048, null=True, default=None, verbose_name='reason')
    banned_by_uuid = models.CharField(max_length=36, null=False, verbose_name='banned_by_uuid')
    banned_by_name = models.CharField(max_length=128, null=True, default=None, verbose_name='banned_by_name')
    removed_by_uuid = models.CharField(max_length=36, null=True, default=None, verbose_name='removed_by_uuid')
    removed_by_name = models.CharField(max_length=128, null=True, default=None, verbose_name='removed_by_name')
    removed_by_reason = models.CharField(max_length=2048, null=True, default=None, verbose_name='removed_by_reason')
    removed_by_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name='removed_by_date')
    time = models.BigIntegerField(null=False, verbose_name='time')
    until = models.BigIntegerField(null=False, verbose_name='until')
    template = models.PositiveSmallIntegerField(null=False, default=255, verbose_name='template')
    server_scope = models.CharField(max_length=32, null=True, default=None, verbose_name='server_scope')
    server_origin = models.CharField(max_length=32, null=True, default=None, verbose_name='server_origin')
    silent = MySQLBooleanField(null=True)
    ipban = MySQLBooleanField(null=True)
    ipban_wildcard = MySQLBooleanField(null=True, default=b'0')
    active = MySQLBooleanField(null=True)
    warned = MySQLBooleanField(null=True)
    
    class Meta:
        verbose_name = 'Litebans_Warnings'
        verbose_name_plural = 'Litebans_Warnings'

# uuid, ip, reason, banned_by_uuid, banned_by_name, removed_by_uuid, removed_by_name, removed_by_reason, removed_by_date, time, until, template, server_scope, server_origin, silent, ipban, ipban_wildcard, active | добавить в admin.py
class Mutes(models.Model):
    
    uuid = models.CharField(max_length=36, null=True, default=None, verbose_name='uuid')
    ip = models.CharField(max_length=45, null=True, default=None, verbose_name='ip')
    reason = models.CharField(max_length=2048, null=True, default=None, verbose_name='reason')
    banned_by_uuid = models.CharField(max_length=36, null=False, verbose_name='banned_by_uuid')
    banned_by_name = models.CharField(max_length=128, null=True, default=None, verbose_name='banned_by_name')
    removed_by_uuid = models.CharField(max_length=36, null=True, default=None, verbose_name='removed_by_uuid')
    removed_by_name = models.CharField(max_length=128, null=True, default=None, verbose_name='removed_by_name')
    removed_by_reason = models.CharField(max_length=2048, null=True, default=None, verbose_name='removed_by_reason')
    removed_by_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name='removed_by_date')
    time = models.BigIntegerField(null=False, verbose_name='time')
    until = models.BigIntegerField(null=False, verbose_name='until')
    template = models.PositiveSmallIntegerField(null=False, default=255, verbose_name='template')
    server_scope = models.CharField(max_length=32, null=True, default=None, verbose_name='server_scope')
    server_origin = models.CharField(max_length=32, null=True, default=None, verbose_name='server_origin')
    silent = MySQLBooleanField(null=True)
    ipban = MySQLBooleanField(null=True)
    ipban_wildcard = MySQLBooleanField(null=True, default=b'0')
    active = MySQLBooleanField(null=True)
    
    class Meta:
        verbose_name = 'Litebans_Mutes'
        verbose_name_plural = 'Litebans_Mutes'
