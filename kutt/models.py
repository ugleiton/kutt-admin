# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils.safestring import mark_safe
import bcrypt
import base64
import hashlib

class Domains(models.Model):
    banned = models.BooleanField()
    banned_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True,related_name='domains_banned')
    address = models.CharField(unique=True, max_length=255)
    homepage = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True,related_name='domains')
    uuid = models.UUIDField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'domains'
        


class Hosts(models.Model):
    address = models.CharField(unique=True, max_length=255)
    banned = models.BooleanField()
    banned_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True,related_name='hosts')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hosts'


class Ips(models.Model):
    ip = models.CharField(unique=True, max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ips'


class KnexMigrations(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    batch = models.IntegerField(blank=True, null=True)
    migration_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'knex_migrations'


class KnexMigrationsLock(models.Model):
    index = models.AutoField(primary_key=True)
    is_locked = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'knex_migrations_lock'


class Links(models.Model):
    address = models.CharField(verbose_name='URL Curta',max_length=255)
    description = models.CharField(verbose_name='Descrição',max_length=255, blank=True, null=True)
    banned = models.BooleanField(verbose_name='Banido')
    banned_by = models.ForeignKey('Users', models.CASCADE, blank=True, null=True,related_name='links_banned')
    domain = models.ForeignKey(Domains, models.DO_NOTHING, blank=True, null=True)
    password = models.CharField(max_length=255,verbose_name="Senha", blank=True, null=True)
    expire_in = models.DateTimeField(blank=True, null=True,verbose_name="Expira em")
    target = models.CharField(verbose_name="URL Original",max_length=2040)
    user = models.ForeignKey('Users', models.DO_NOTHING,verbose_name="Usuário", blank=True, null=True,related_name='links')
    visit_count = models.IntegerField(verbose_name="Quantidade de visitas")
    created_at = models.DateTimeField(verbose_name="Criado em")
    updated_at = models.DateTimeField(verbose_name="Atualizado em")
    uuid = models.UUIDField()

    class Meta:
        managed = False
        db_table = 'links'
        verbose_name = "Link"
        verbose_name_plural = "Links"

    def __str__(self):
        return "{}".format(self.target)

    def _opcoes(self):
        opcoes = f"""
        <button type="button" class="el-button el-button--button el-button--mini" onclick="window.location.href='/kutt/links/{self.pk}/change'" style="float: left; margin-right: 10px; margin-bottom: 10px;">
            <i class="fas fa-edit"></i><span> <span>Editar</span></span>
        </button>
        <button type="button" class="el-button el-button--danger el-button--mini" onclick="window.location.href='/kutt/links/{self.pk}/delete'" style="float: left; margin-right: 10px; margin-bottom: 10px;">
            <i class="fas fa-trash-alt"></i><span> <span>Apagar</span></span>
        </button>
        """
        return mark_safe(opcoes)
    _opcoes.short_description = "Opções"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_password = self.password

    #alterar a senha do usuario usando criptografia bcrypt https://github.com/thedevs-network/kutt/blob/0bc0e6629ba7d14bbe1ef0857ca9caf7110e953c/server/queries/link.ts#L126
    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.password != self.__original_password:
            hashed = bcrypt.hashpw(self.password.encode(),bcrypt.gensalt(12))
            self.password = hashed.decode()
            self.__original_password = hashed.decode()
        super().save(force_insert, force_update, *args, **kwargs)


class Users(models.Model):
    apikey = models.CharField(max_length=255, blank=True, null=True)
    banned = models.BooleanField(verbose_name='Banido')
    banned_by = models.ForeignKey('self', models.DO_NOTHING,verbose_name='Banido por', blank=True, null=True,related_name='users_banned')
    cooldowns = models.TextField(blank=True, null=True)  # This field type is a guess.
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255,verbose_name="Senha")
    reset_password_expires = models.DateTimeField(blank=True, null=True)
    reset_password_token = models.CharField(max_length=255, blank=True, null=True)
    change_email_expires = models.DateTimeField(blank=True, null=True)
    change_email_token = models.CharField(max_length=255, blank=True, null=True)
    change_email_address = models.CharField(max_length=255, blank=True, null=True)
    verification_expires = models.DateTimeField(blank=True, null=True)
    verification_token = models.CharField(max_length=255, blank=True, null=True)
    verified = models.BooleanField(verbose_name="Verificado")
    created_at = models.DateTimeField(verbose_name='Criado em')
    updated_at = models.DateTimeField(verbose_name='Atualizado em')

    class Meta:
        managed = False
        db_table = 'users'
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return "{}".format(self.email)
    def _opcoes(self):
        opcoes = f"""
        <button type="button" class="el-button el-button--button el-button--mini" onclick="window.location.href='/kutt/users/{self.pk}/change'" style="float: left; margin-right: 10px; margin-bottom: 10px;">
            <i class="fas fa-edit"></i><span> <span>Editar</span></span>
        </button>
        <button type="button" class="el-button el-button--danger el-button--mini" onclick="window.location.href='/kutt/users/{self.pk}/delete'" style="float: left; margin-right: 10px; margin-bottom: 10px;">
            <i class="fas fa-trash-alt"></i><span> <span>Apagar</span></span>
        </button>
        <button type="button" class="el-button el-button--info el-button--mini" onclick="window.location.href='/kutt/links/?user__id__exact={self.pk}'" style="float: left; margin-right: 10px; margin-bottom: 10px;">
            <i class="fas fa-bars"></i><span> <span>Links</span></span>
        </button>
        """
        return mark_safe(opcoes)
    _opcoes.short_description = "Opções"


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_password = self.password

    #alterar a senha do usuario usando criptografia bcrypt https://github.com/thedevs-network/kutt/blob/0bc0e6629ba7d14bbe1ef0857ca9caf7110e953c/server/handlers/auth.ts#L114
    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.password != self.__original_password:
            hashed = bcrypt.hashpw(self.password.encode(),bcrypt.gensalt(12))
            self.password = hashed.decode()
            self.__original_password = hashed.decode()
        super().save(force_insert, force_update, *args, **kwargs)

class Visits(models.Model):
    countries = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    link = models.ForeignKey(Links, models.CASCADE)
    referrers = models.JSONField(blank=True, null=True)
    total = models.IntegerField()
    br_chrome = models.IntegerField()
    br_edge = models.IntegerField()
    br_firefox = models.IntegerField()
    br_ie = models.IntegerField()
    br_opera = models.IntegerField()
    br_other = models.IntegerField()
    br_safari = models.IntegerField()
    os_android = models.IntegerField()
    os_ios = models.IntegerField()
    os_linux = models.IntegerField()
    os_macos = models.IntegerField()
    os_other = models.IntegerField()
    os_windows = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'visits'
        verbose_name = "Visita"
        verbose_name_plural = "Visitas"
