from django.db import models
from datetime import date


class Banner(models.Model):
    image=models.CharField(max_length=250)
    alt_ext = models.CharField(max_length=300)
    
class Category(models.Model):
    title=models.CharField(max_length=180)
    image=models.ImageField(upload_to="cat_imgs/")

    def __str__(self):
        return self().title
    

class Determinador(models.Model):
    cod_determinador = models.AutoField(db_column='Cod_Determinador', primary_key=True)  # Field name made lowercase.
    nome_determinador = models.CharField(db_column='Nome_Determinador', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Determinador'

class Conteudo(models.Model):
    cod_conteudo = models.AutoField(db_column='Cod_Conteudo', primary_key=True)  # Field name made lowercase.
    desc_conteudo = models.CharField(db_column='Desc_Conteudo', max_length=80, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Conteudo'

class Especie(models.Model):
    cod_especie = models.AutoField(db_column='Cod_Especie', primary_key=True)  # Field name made lowercase.
    nome_especie = models.CharField(db_column='Nome_Especie', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Especie'


class Familia(models.Model):
    cod_familia = models.AutoField(db_column='Cod_Familia', primary_key=True)  # Field name made lowercase.
    nome_familia = models.CharField(db_column='Nome_Familia', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Familia'


class Fonte(models.Model):
    cod_fonte = models.AutoField(db_column='Cod_Fonte', primary_key=True)  # Field name made lowercase.
    cod_referencia = models.IntegerField(db_column='Cod_Referencia', blank=True, null=True)  # Field name made lowercase.
    desc_num_fonte = models.CharField(db_column='Desc_Num_Fonte', max_length=50, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    desc_obs_fonte = models.TextField(db_column='Desc_Obs_Fonte', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Fonte'


class Genero(models.Model): 
    cod_genero = models.AutoField(db_column='Cod_Genero', primary_key=True)  # Field name made lowercase.
    nome_genero = models.CharField(db_column='Nome_Genero', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Genero'


class Item(models.Model):
    cod_item = models.AutoField(db_column='Cod_Item', primary_key=True)  # Field name made lowercase.
    nome_item = models.CharField(db_column='Nome_Item', max_length=200, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cod_item_pai = models.IntegerField(db_column='Cod_Item_Pai', blank=True, null=True)  # Field name made lowercase.
    cod_nivel_item = models.IntegerField(db_column='Cod_Nivel_Item', blank=True, null=True)  # Field name made lowercase.
    cod_tipo_item = models.CharField(db_column='Cod_Tipo_Item', max_length=3, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    num_parte_inteira = models.DecimalField(db_column='Num_Parte_Inteira', max_digits=8, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    num_parte_decimal = models.DecimalField(db_column='Num_Parte_Decimal', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    desc_unidade_medida = models.CharField(db_column='Desc_Unidade_Medida', max_length=50, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ind_exibir_ficha = models.IntegerField(db_column='Ind_Exibir_Ficha', blank=True, null=True)  # Field name made lowercase.
    cod_tipo_pesquisa = models.CharField(db_column='Cod_Tipo_Pesquisa', max_length=3, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    num_ordem_item = models.IntegerField(db_column='Num_Ordem_Item', blank=True, null=True)  # Field name made lowercase.
    desc_obs_item = models.TextField(db_column='Desc_Obs_Item', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cod_status_item = models.CharField(db_column='Cod_Status_Item', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ind_exibir_pesquisa = models.IntegerField(db_column='Ind_Exibir_Pesquisa', blank=True, null=True)  # Field name made lowercase.
    cod_tipo_parametro = models.CharField(db_column='Cod_Tipo_Parametro', max_length=3, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Item'


class ItemConteudo(models.Model):
    cod_item = models.IntegerField(db_column='Cod_Item')  # Field name made lowercase.
    cod_conteudo = models.IntegerField(db_column='Cod_Conteudo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Item_Conteudo'


class Madeira(models.Model):
    cod_madeira = models.AutoField(db_column='Cod_Madeira', primary_key=True)  # Field name made lowercase.
    data_cadastro = models.DateField(db_column='Data_Cadastro', blank=True, null=True)  # Field name made lowercase.
    desc_obs_madeira = models.TextField(db_column='Desc_Obs_Madeira', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    desc_obs_ocorrencia = models.TextField(db_column='Desc_Obs_Ocorrencia', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    desc_obs_nome_cientifico = models.TextField(db_column='Desc_Obs_Nome_Cientifico', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cod_status_madeira = models.CharField(db_column='Cod_Status_Madeira', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Madeira'


class MadeiraFoto(models.Model):
    cod_madeira = models.IntegerField(db_column='Cod_Madeira', primary_key=True)  # Field name made lowercase. The composite primary key (Cod_Madeira, Cod_Foto) found, that is not supported. The first column is selected.
    cod_foto = models.IntegerField(db_column='Cod_Foto')  # Field name made lowercase.
    nome_arquivo_foto = models.CharField(db_column='Nome_Arquivo_Foto', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cod_tipo_foto = models.IntegerField(db_column='Cod_Tipo_Foto', blank=True, null=True)  # Field name made lowercase.
    desc_obs_foto = models.CharField(db_column='Desc_Obs_Foto', max_length=200, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nome_arquivo_zoom = models.CharField(db_column='Nome_Arquivo_Zoom', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Madeira_Foto'
        unique_together = (('cod_madeira', 'cod_foto'),)


class MadeiraItem(models.Model):
    cod_madeira = models.IntegerField(db_column='Cod_Madeira', primary_key=True)  # Field name made lowercase. The composite primary key (Cod_Madeira, Cod_Item, Num_Linha) found, that is not supported. The first column is selected.
    cod_item = models.IntegerField(db_column='Cod_Item')  # Field name made lowercase.
    num_linha = models.IntegerField(db_column='Num_Linha')  # Field name made lowercase.
    desc_item = models.TextField(db_column='Desc_Item', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    valor_inteiro = models.DecimalField(db_column='Valor_Inteiro', max_digits=8, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    valor_decimal = models.DecimalField(db_column='Valor_Decimal', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    cod_conteudo = models.IntegerField(db_column='Cod_Conteudo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Madeira_Item'
        unique_together = (('cod_madeira', 'cod_item', 'num_linha'),)


class MadeiraItemFonte(models.Model):
    cod_madeira = models.IntegerField(db_column='Cod_Madeira', primary_key=True)  # Field name made lowercase. The composite primary key (Cod_Madeira, Cod_Item, Num_Linha, Num_Ordem_Fonte) found, that is not supported. The first column is selected.
    cod_item = models.IntegerField(db_column='Cod_Item')  # Field name made lowercase.
    num_linha = models.IntegerField(db_column='Num_Linha')  # Field name made lowercase.
    num_ordem_fonte = models.IntegerField(db_column='Num_Ordem_Fonte')  # Field name made lowercase.
    cod_fonte = models.IntegerField(db_column='Cod_Fonte', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Madeira_Item_Fonte'
        unique_together = (('cod_madeira', 'cod_item', 'num_linha', 'num_ordem_fonte'),)


class MadeiraItemObsFonte(models.Model):
    cod_madeira = models.IntegerField(db_column='Cod_Madeira', primary_key=True)  # Field name made lowercase. The composite primary key (Cod_Madeira, Cod_Item, Num_Linha, Num_Obs, Num_Ordem_Fonte) found, that is not supported. The first column is selected.
    cod_item = models.IntegerField(db_column='Cod_Item')  # Field name made lowercase.
    num_linha = models.IntegerField(db_column='Num_Linha')  # Field name made lowercase.
    num_obs = models.IntegerField(db_column='Num_Obs')  # Field name made lowercase.
    num_ordem_fonte = models.IntegerField(db_column='Num_Ordem_Fonte')  # Field name made lowercase.
    cod_fonte = models.IntegerField(db_column='Cod_Fonte', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Madeira_Item_Obs_Fonte'
        unique_together = (('cod_madeira', 'cod_item', 'num_linha', 'num_obs', 'num_ordem_fonte'),)


class MadeiraItemObservacao(models.Model):
    cod_madeira = models.IntegerField(db_column='Cod_Madeira', primary_key=True)  # Field name made lowercase. The composite primary key (Cod_Madeira, Cod_Item, Num_Linha, Num_Obs) found, that is not supported. The first column is selected.
    cod_item = models.IntegerField(db_column='Cod_Item')  # Field name made lowercase.
    num_linha = models.IntegerField(db_column='Num_Linha')  # Field name made lowercase.
    num_obs = models.IntegerField(db_column='Num_Obs')  # Field name made lowercase.
    desc_obs = models.TextField(db_column='Desc_Obs', db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Madeira_Item_Observacao'
        unique_together = (('cod_madeira', 'cod_item', 'num_linha', 'num_obs'),)


class MadeiraNomeCientifico(models.Model):
    cod_madeira = models.AutoField(db_column='Cod_Madeira', primary_key=True)  # Field name made lowercase. The composite primary key (Cod_Madeira, Cod_Nome_Cientifico) found, that is not supported. The first column is selected.
    cod_nome_cientifico = models.IntegerField(db_column='Cod_Nome_Cientifico')  # Field name made lowercase.
    cod_familia = models.IntegerField(db_column='Cod_Familia', blank=True, null=True)  # Field name made lowercase.
    cod_genero = models.IntegerField(db_column='Cod_Genero', blank=True, null=True)  # Field name made lowercase.
    cod_especie = models.IntegerField(db_column='Cod_Especie', blank=True, null=True)  # Field name made lowercase.
    cod_determinador = models.IntegerField(db_column='Cod_Determinador', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Madeira_Nome_Cientifico'
        unique_together = (('cod_madeira', 'cod_nome_cientifico'),)


class MadeiraNomeInternFonte(models.Model):
    cod_madeira = models.IntegerField(db_column='Cod_Madeira', primary_key=True)  # Field name made lowercase. The composite primary key (Cod_Madeira, Cod_Nome_Internacional, Num_Ordem_Fonte) found, that is not supported. The first column is selected.
    cod_nome_internacional = models.IntegerField(db_column='Cod_Nome_Internacional')  # Field name made lowercase.
    num_ordem_fonte = models.IntegerField(db_column='Num_Ordem_Fonte')  # Field name made lowercase.
    cod_fonte = models.IntegerField(db_column='Cod_Fonte', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Madeira_Nome_Intern_Fonte'
        unique_together = (('cod_madeira', 'cod_nome_internacional', 'num_ordem_fonte'),)


class MadeiraNomeInternOcorr(models.Model):
    cod_madeira = models.IntegerField(db_column='Cod_Madeira', primary_key=True)  # Field name made lowercase. The composite primary key (Cod_Madeira, Cod_Nome_Internacional, Cod_Ocorrencia) found, that is not supported. The first column is selected.
    cod_nome_internacional = models.IntegerField(db_column='Cod_Nome_Internacional')  # Field name made lowercase.
    cod_ocorrencia = models.IntegerField(db_column='Cod_Ocorrencia')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Madeira_Nome_Intern_Ocorr'
        unique_together = (('cod_madeira', 'cod_nome_internacional', 'cod_ocorrencia'),)


class MadeiraNomeInternacional(models.Model):
    cod_madeira = models.IntegerField(db_column='Cod_Madeira', primary_key=True)  # Field name made lowercase. The composite primary key (Cod_Madeira, Cod_Nome_Internacional) found, that is not supported. The first column is selected.
    cod_nome_internacional = models.IntegerField(db_column='Cod_Nome_Internacional')  # Field name made lowercase.
    nome_internacional = models.CharField(db_column='Nome_Internacional', max_length=80, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Madeira_Nome_Internacional'
        unique_together = (('cod_madeira', 'cod_nome_internacional'),)


class MadeiraNomePopular(models.Model):
    cod_madeira = models.IntegerField(db_column='Cod_Madeira', primary_key=True)  # Field name made lowercase. The composite primary key (Cod_Madeira, Cod_Nome_Popular) found, that is not supported. The first column is selected.
    cod_nome_popular = models.IntegerField(db_column='Cod_Nome_Popular')  # Field name made lowercase.
    nome_popular = models.CharField(db_column='Nome_Popular', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ind_nome_principal = models.IntegerField(db_column='Ind_Nome_Principal', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Madeira_Nome_Popular'
        unique_together = (('cod_madeira', 'cod_nome_popular'),)


class MadeiraOcorrencia(models.Model):
    cod_madeira = models.IntegerField(db_column='Cod_Madeira', primary_key=True)  # Field name made lowercase. The composite primary key (Cod_Madeira, Cod_Ocorrencia) found, that is not supported. The first column is selected.
    cod_ocorrencia = models.IntegerField(db_column='Cod_Ocorrencia')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Madeira_Ocorrencia'
        unique_together = (('cod_madeira', 'cod_ocorrencia'),)


class Ocorrencia(models.Model):
    cod_ocorrencia = models.AutoField(primary_key=True)  # Field name made lowercase.
    nome_ocorrencia = models.CharField(db_column='Nome_Ocorrencia', max_length=80, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cod_tipo_ocorrencia = models.IntegerField(db_column='Cod_Tipo_Ocorrencia', blank=True, null=True)  # Field name made lowercase.
    cod_origem = models.CharField(db_column='Cod_Origem', max_length=1, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ocorrencia'


class Referencia(models.Model):
    cod_referencia = models.AutoField(db_column='Cod_Referencia', primary_key=True)  # Field name made lowercase.
    nome_referencia = models.CharField(db_column='Nome_Referencia', max_length=50, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nome_completo_referencia = models.CharField(db_column='Nome_Completo_Referencia', max_length=150, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    desc_endereco_site = models.CharField(db_column='Desc_Endereco_Site', max_length=200, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Referencia'


class TipoFoto(models.Model):
    cod_tipo_foto = models.AutoField(db_column='Cod_Tipo_Foto', primary_key=True)  # Field name made lowercase.
    desc_tipo_foto = models.CharField(db_column='Desc_Tipo_Foto', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    num_ordem_tipo_foto = models.IntegerField(db_column='Num_Ordem_Tipo_Foto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tipo_Foto'


class TipoOcorrencia(models.Model):
    cod_tipo_ocorrencia = models.AutoField(db_column='Cod_Tipo_Ocorrencia', primary_key=True)  # Field name made lowercase.
    desc_tipo_ocorrencia = models.CharField(db_column='Desc_Tipo_Ocorrencia', max_length=80, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tipo_Ocorrencia'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, db_collation='Latin1_General_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, db_collation='Latin1_General_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, db_collation='Latin1_General_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, db_collation='Latin1_General_CI_AS')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, db_collation='Latin1_General_CI_AS')
    first_name = models.CharField(max_length=150, db_collation='Latin1_General_CI_AS')
    last_name = models.CharField(max_length=150, db_collation='Latin1_General_CI_AS')
    email = models.CharField(max_length=254, db_collation='Latin1_General_CI_AS')
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(db_collation='Latin1_General_CI_AS', blank=True, null=True)
    object_repr = models.CharField(max_length=200, db_collation='Latin1_General_CI_AS')
    action_flag = models.SmallIntegerField()
    change_message = models.TextField(db_collation='Latin1_General_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, db_collation='Latin1_General_CI_AS')
    model = models.CharField(max_length=100, db_collation='Latin1_General_CI_AS')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, db_collation='Latin1_General_CI_AS')
    name = models.CharField(max_length=255, db_collation='Latin1_General_CI_AS')
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40, db_collation='Latin1_General_CI_AS')
    session_data = models.TextField(db_collation='Latin1_General_CI_AS')
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
