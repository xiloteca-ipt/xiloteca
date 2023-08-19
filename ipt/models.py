# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Conteudo(models.Model):
    cod_conteudo = models.AutoField(db_column='Cod_Conteudo', primary_key=True)  # Field name made lowercase.
    desc_conteudo = models.CharField(db_column='Desc_Conteudo', max_length=80, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return str(self.desc_conteudo) if self.desc_conteudo else ''


    class Meta:
        managed = True
        db_table = 'Conteudo'


class Determinador(models.Model):
    cod_determinador = models.AutoField(db_column='Cod_Determinador', primary_key=True)  # Field name made lowercase.
    nome_determinador = models.CharField(db_column='Nome_Determinador', max_length=100, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return str(self.nome_determinador) if self.nome_determinador else ''


    class Meta:
        managed = True
        db_table = 'Determinador'


class Especie(models.Model):
    cod_especie = models.AutoField(db_column='Cod_Especie', primary_key=True)  # Field name made lowercase.
    nome_especie = models.CharField(db_column='Nome_Especie', max_length=100, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return str(self.nome_especie) if self.nome_especie else ''


    class Meta:
        managed = True
        db_table = 'Especie'


class Familia(models.Model):
    cod_familia = models.AutoField(db_column='Cod_Familia', primary_key=True)  # Field name made lowercase.
    nome_familia = models.CharField(db_column='Nome_Familia', max_length=100, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return str(self.nome_familia) if self.nome_familia else ''


    class Meta:
        managed = True
        db_table = 'Familia'


class Fonte(models.Model):
    cod_fonte = models.PositiveIntegerField(db_column='Cod_Fonte', primary_key=True)  # Field name made lowercase.
    cod_referencia = models.ForeignKey('Referencia', models.DO_NOTHING, db_column='Cod_Referencia')  # Field name made lowercase.
    desc_num_fonte = models.CharField(db_column='Desc_Num_Fonte', max_length=50, blank=True, null=True)  # Field name made lowercase.
    desc_obs_fonte = models.TextField(db_column='Desc_Obs_Fonte', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return str(self.desc_obs_fonte) if self.desc_num_fonte else ''


    class Meta:
        managed = True
        db_table = 'Fonte'


class Genero(models.Model):
    cod_genero = models.AutoField(db_column='Cod_Genero', primary_key=True)  # Field name made lowercase.
    nome_genero = models.CharField(db_column='Nome_Genero', max_length=100, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return str(self.nome_genero) if self.nome_genero else ''


    class Meta:
        managed = True
        db_table = 'Genero'


class Item(models.Model):
    cod_item = models.PositiveIntegerField(db_column='Cod_Item', primary_key=True)  # Field name made lowercase.
    nome_item = models.CharField(db_column='Nome_Item', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cod_item_pai = models.PositiveIntegerField(db_column='Cod_Item_Pai', blank=True, null=True)  # Field name made lowercase.
    cod_nivel_item = models.PositiveIntegerField(db_column='Cod_Nivel_Item', blank=True, null=True)  # Field name made lowercase.
    cod_tipo_item = models.CharField(db_column='Cod_Tipo_Item', max_length=3, blank=True, null=True)  # Field name made lowercase.
    num_parte_inteira = models.DecimalField(db_column='Num_Parte_Inteira', max_digits=8, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    num_parte_decimal = models.DecimalField(db_column='Num_Parte_Decimal', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    desc_unidade_medida = models.CharField(db_column='Desc_Unidade_Medida', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ind_exibir_ficha = models.PositiveIntegerField(db_column='Ind_Exibir_Ficha', blank=True, null=True)  # Field name made lowercase.
    cod_tipo_pesquisa = models.CharField(db_column='Cod_Tipo_Pesquisa', max_length=3, blank=True, null=True)  # Field name made lowercase.
    num_ordem_item = models.PositiveIntegerField(db_column='Num_Ordem_Item', blank=True, null=True)  # Field name made lowercase.
    desc_obs_item = models.TextField(db_column='Desc_Obs_Item', blank=True, null=True)  # Field name made lowercase.
    cod_status_item = models.CharField(db_column='Cod_Status_Item', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ind_exibir_pesquisa = models.PositiveIntegerField(db_column='Ind_Exibir_Pesquisa', blank=True, null=True)  # Field name made lowercase.
    cod_tipo_parametro = models.CharField(db_column='Cod_Tipo_Parametro', max_length=3, blank=True, null=True)  # Field name made lowercase.


    def __str__(self):
        return self.nome_item + " " + " ".join([str(self.cod_item), str(self.cod_item_pai), str(self.cod_nivel_item), str(self.cod_tipo_item), str(self.cod_tipo_pesquisa), str(self.cod_status_item), str(self.cod_tipo_parametro)])



    class Meta:
        managed = True
        db_table = 'Item'


class ItemConteudo(models.Model):
    cod_item = models.OneToOneField(Item, models.DO_NOTHING, db_column='Cod_Item', primary_key=True)  # Field name made lowercase. The composite primary key (Cod_Item, Cod_Conteudo) found, that is not supported. The first column is selected.
    cod_conteudo = models.ForeignKey(Conteudo, models.DO_NOTHING, db_column='Cod_Conteudo')  # Field name made lowercase.
    def __str__(self):
        return str(self.cod_item) if self.cod_item else ''


    class Meta:
        managed = True
        db_table = 'Item_Conteudo'
        unique_together = (('cod_item', 'cod_conteudo'),)


class Madeira(models.Model):
    cod_madeira = models.PositiveIntegerField(db_column='Cod_Madeira', primary_key=True)  # Field name made lowercase.
    data_cadastro = models.DateField(db_column='Data_Cadastro', blank=True, null=True)  # Field name made lowercase.
    desc_obs_madeira = models.TextField(db_column='Desc_Obs_Madeira', blank=True, null=True)  # Field name made lowercase.
    desc_obs_ocorrencia = models.TextField(db_column='Desc_Obs_Ocorrencia', blank=True, null=True)  # Field name made lowercase.
    desc_obs_nome_cientifico = models.TextField(db_column='Desc_Obs_Nome_Cientifico', blank=True, null=True)  # Field name made lowercase.
    cod_status_madeira = models.CharField(db_column='Cod_Status_Madeira', max_length=1, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return str(self.cod_madeira) if self.cod_madeira else ''


    class Meta:
        managed = True
        db_table = 'Madeira'


class MadeiraFoto(models.Model):
    cod_madeira = models.OneToOneField(Madeira, models.DO_NOTHING, db_column='Cod_Madeira', primary_key=True)  # Field name made lowercase. The composite primary key (Cod_Madeira, Cod_Foto) found, that is not supported. The first column is selected.
    cod_foto = models.PositiveIntegerField(db_column='Cod_Foto')  # Field name made lowercase.
    nome_arquivo_foto = models.CharField(db_column='Nome_Arquivo_Foto', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cod_tipo_foto = models.ForeignKey('TipoFoto', models.DO_NOTHING, db_column='Cod_Tipo_Foto', blank=True, null=True)  # Field name made lowercase.
    desc_obs_foto = models.CharField(db_column='Desc_Obs_Foto', max_length=200, blank=True, null=True)  # Field name made lowercase.
    nome_arquivo_zoom = models.CharField(db_column='Nome_Arquivo_Zoom', max_length=100, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return str(self.cod_madeira) if self.cod_madeira else ''


    class Meta:
        managed = True
        db_table = 'Madeira_Foto'
        unique_together = (('cod_madeira', 'cod_foto'),)


class MadeiraItem(models.Model):
    cod_madeira = models.OneToOneField(Madeira, models.DO_NOTHING, db_column='Cod_Madeira', primary_key=True)  # Field name made lowercase. The composite primary key (Cod_Madeira, Cod_Item, Num_Linha) found, that is not supported. The first column is selected.
    cod_item = models.ForeignKey(Item, models.DO_NOTHING, db_column='Cod_Item')  # Field name made lowercase.
    num_linha = models.PositiveIntegerField(db_column='Num_Linha')  # Field name made lowercase.
    desc_item = models.TextField(db_column='Desc_Item', blank=True, null=True)  # Field name made lowercase.
    valor_inteiro = models.DecimalField(db_column='Valor_Inteiro', max_digits=8, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    valor_decimal = models.DecimalField(db_column='Valor_Decimal', max_digits=2, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    cod_conteudo = models.PositiveIntegerField(db_column='Cod_Conteudo', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return str(self.cod_madeira) if self.cod_madeira else ''


    class Meta:
        managed = True
        db_table = 'Madeira_Item'
        unique_together = (('cod_madeira', 'cod_item', 'num_linha'),)


class MadeiraItemFonte(models.Model):
    cod_madeira = models.OneToOneField(Madeira, models.DO_NOTHING, db_column='Cod_Madeira', primary_key=True)  # Field name made lowercase. The composite primary key (Cod_Madeira, Cod_Item, Num_Linha, Num_Ordem_Fonte) found, that is not supported. The first column is selected.
    cod_item = models.ForeignKey(Item, models.DO_NOTHING, db_column='Cod_Item')  # Field name made lowercase.
    num_linha = models.PositiveIntegerField(db_column='Num_Linha')  # Field name made lowercase.
    num_ordem_fonte = models.PositiveIntegerField(db_column='Num_Ordem_Fonte')  # Field name made lowercase.
    cod_fonte = models.ForeignKey(Fonte, models.DO_NOTHING, db_column='Cod_Fonte', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return str(self.cod_madeira) if self.cod_madeira else ''


    class Meta:
        managed = True
        db_table = 'Madeira_Item_Fonte'
        unique_together = (('cod_madeira', 'cod_item', 'num_linha', 'num_ordem_fonte'),)


class MadeiraItemObsFonte(models.Model):
    cod_madeira = models.OneToOneField(Madeira, models.DO_NOTHING, db_column='Cod_Madeira', primary_key=True)  # Field name made lowercase. The composite primary key (Cod_Madeira, Cod_Item, Num_Linha, Num_Obs, Num_Ordem_Fonte) found, that is not supported. The first column is selected.
    cod_item = models.ForeignKey(Item, models.DO_NOTHING, db_column='Cod_Item')  # Field name made lowercase.
    num_linha = models.PositiveIntegerField(db_column='Num_Linha')  # Field name made lowercase.
    num_obs = models.PositiveIntegerField(db_column='Num_Obs')  # Field name made lowercase.
    num_ordem_fonte = models.PositiveIntegerField(db_column='Num_Ordem_Fonte')  # Field name made lowercase.
    cod_fonte = models.ForeignKey(Fonte, models.DO_NOTHING, db_column='Cod_Fonte', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return str(self.cod_madeira) if self.cod_madeira else ''


    class Meta:
        managed = True
        db_table = 'Madeira_Item_Obs_Fonte'
        unique_together = (('cod_madeira', 'cod_item', 'num_linha', 'num_obs', 'num_ordem_fonte'),)


class MadeiraItemObservacao(models.Model):
    cod_madeira = models.OneToOneField(Madeira, models.DO_NOTHING, db_column='Cod_Madeira', primary_key=True)  # Field name made lowercase. The composite primary key (Cod_Madeira, Cod_Item, Num_Linha, Num_Obs) found, that is not supported. The first column is selected.
    cod_item = models.ForeignKey(Item, models.DO_NOTHING, db_column='Cod_Item')  # Field name made lowercase.
    num_linha = models.PositiveIntegerField(db_column='Num_Linha')  # Field name made lowercase.
    num_obs = models.PositiveIntegerField(db_column='Num_Obs')  # Field name made lowercase.
    desc_obs = models.TextField(db_column='Desc_Obs', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return str(self.cod_madeira) if self.cod_madeira else ''


    class Meta:
        managed = True
        db_table = 'Madeira_Item_Observacao'
        unique_together = (('cod_madeira', 'cod_item', 'num_linha', 'num_obs'),)


class MadeiraNomeCientifico(models.Model):
    cod_madeira = models.OneToOneField(Madeira, models.DO_NOTHING, db_column='Cod_Madeira', primary_key=True)  # Field name made lowercase. The composite primary key (Cod_Madeira, Cod_Nome_Cientifico) found, that is not supported. The first column is selected.
    cod_nome_cientifico = models.PositiveIntegerField(db_column='Cod_Nome_Cientifico')  # Field name made lowercase.
    cod_familia = models.ForeignKey(Familia, models.DO_NOTHING, db_column='Cod_Familia', blank=True, null=True)  # Field name made lowercase.
    cod_genero = models.ForeignKey(Genero, models.DO_NOTHING, db_column='Cod_Genero', blank=True, null=True)  # Field name made lowercase.
    cod_especie = models.ForeignKey(Especie, models.DO_NOTHING, db_column='Cod_Especie', blank=True, null=True)  # Field name made lowercase.
    cod_determinador = models.ForeignKey(Determinador, models.DO_NOTHING, db_column='Cod_Determinador', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return str(self.cod_madeira) if self.cod_madeira else ''


    class Meta:
        managed = True
        db_table = 'Madeira_Nome_Cientifico'
        unique_together = (('cod_madeira', 'cod_nome_cientifico'),)


class MadeiraNomeInternFonte(models.Model):
    cod_madeira = models.OneToOneField('MadeiraNomeInternacional', models.DO_NOTHING, db_column='Cod_Madeira', primary_key=True)  # Field name made lowercase. The composite primary key (Cod_Madeira, Cod_Nome_Internacional, Num_Ordem_Fonte) found, that is not supported. The first column is selected.
    cod_nome_internacional = models.PositiveIntegerField(db_column='Cod_Nome_Internacional')  # Field name made lowercase.
    num_ordem_fonte = models.PositiveIntegerField(db_column='Num_Ordem_Fonte')  # Field name made lowercase.
    cod_fonte = models.ForeignKey(Fonte, models.DO_NOTHING, db_column='Cod_Fonte', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return str(self.cod_madeira) if self.cod_madeira else ''


    class Meta:
        managed = True
        db_table = 'Madeira_Nome_Intern_Fonte'
        unique_together = (('cod_madeira', 'cod_nome_internacional', 'num_ordem_fonte'),)


class MadeiraNomeInternOcorr(models.Model):
    cod_madeira = models.OneToOneField('MadeiraNomeInternacional', models.DO_NOTHING, db_column='Cod_Madeira', primary_key=True)  # Field name made lowercase. The composite primary key (Cod_Madeira, Cod_Nome_Internacional, Cod_Ocorrencia) found, that is not supported. The first column is selected.
    cod_nome_internacional = models.PositiveIntegerField(db_column='Cod_Nome_Internacional')  # Field name made lowercase.
    cod_ocorrencia = models.ForeignKey('Ocorrencia', models.DO_NOTHING, db_column='Cod_Ocorrencia')  # Field name made lowercase.
    def __str__(self):
        return str(self.cod_madeira) if self.cod_madeira else ''


    class Meta:
        managed = True
        db_table = 'Madeira_Nome_Intern_Ocorr'
        unique_together = (('cod_madeira', 'cod_nome_internacional', 'cod_ocorrencia'),)


class MadeiraNomeInternacional(models.Model):
    cod_madeira = models.OneToOneField(Madeira, models.DO_NOTHING, db_column='Cod_Madeira', primary_key=True)  # Field name made lowercase. The composite primary key (Cod_Madeira, Cod_Nome_Internacional) found, that is not supported. The first column is selected.
    cod_nome_internacional = models.PositiveIntegerField(db_column='Cod_Nome_Internacional')  # Field name made lowercase.
    nome_internacional = models.CharField(db_column='Nome_Internacional', max_length=80, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return str(self.nome_internacional) if self.nome_internacional else ''


    class Meta:
        managed = True
        db_table = 'Madeira_Nome_Internacional'
        unique_together = (('cod_madeira', 'cod_nome_internacional'),)


class MadeiraNomePopular(models.Model):
    cod_madeira = models.OneToOneField(Madeira, models.DO_NOTHING, db_column='Cod_Madeira', primary_key=True)  # Field name made lowercase. The composite primary key (Cod_Madeira, Cod_Nome_Popular) found, that is not supported. The first column is selected.
    cod_nome_popular = models.PositiveIntegerField(db_column='Cod_Nome_Popular')  # Field name made lowercase.
    nome_popular = models.CharField(db_column='Nome_Popular', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ind_nome_principal = models.IntegerField(db_column='Ind_Nome_Principal', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return str(self.nome_popular) if self.nome_popular else ''


    class Meta:
        managed = True
        db_table = 'Madeira_Nome_Popular'
        unique_together = (('cod_madeira', 'cod_nome_popular'),)


class MadeiraOcorrencia(models.Model):
    cod_madeira = models.OneToOneField(Madeira, models.DO_NOTHING, db_column='Cod_Madeira', primary_key=True)  # Field name made lowercase. The composite primary key (Cod_Madeira, Cod_Ocorrencia) found, that is not supported. The first column is selected.
    cod_ocorrencia = models.ForeignKey('Ocorrencia', models.DO_NOTHING, db_column='Cod_Ocorrencia')  # Field name made lowercase.
    def __str__(self):
        return str(self.cod_madeira) if self.cod_madeira else ''


    class Meta:
        managed = True
        db_table = 'Madeira_Ocorrencia'
        unique_together = (('cod_madeira', 'cod_ocorrencia'),)


class Ocorrencia(models.Model):
    cod_ocorrencia = models.AutoField(db_column='Cod_Ocorrencia', primary_key=True)  # Field name made lowercase.
    nome_ocorrencia = models.CharField(db_column='Nome_Ocorrencia', max_length=80, blank=True, null=True)  # Field name made lowercase.
    cod_tipo_ocorrencia = models.ForeignKey('TipoOcorrencia', models.DO_NOTHING, db_column='Cod_Tipo_Ocorrencia', blank=True, null=True)  # Field name made lowercase.
    cod_origem = models.CharField(db_column='Cod_Origem', max_length=1, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return str(self.nome_ocorrencia) if self.nome_ocorrencia else ''


    class Meta:
        managed = True
        db_table = 'Ocorrencia'


class Referencia(models.Model):
    cod_referencia = models.AutoField(db_column='Cod_Referencia', primary_key=True)  # Field name made lowercase.
    nome_referencia = models.CharField(db_column='Nome_Referencia', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nome_completo_referencia = models.CharField(db_column='Nome_Completo_Referencia', max_length=150, blank=True, null=True)  # Field name made lowercase.
    desc_endereco_site = models.CharField(db_column='Desc_Endereco_Site', max_length=200, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return str(self.nome_referencia) if self.nome_referencia else ''


    class Meta:
        managed = True
        db_table = 'Referencia'


class TipoFoto(models.Model):
    cod_tipo_foto = models.AutoField(db_column='Cod_Tipo_Foto', primary_key=True)  # Field name made lowercase.
    desc_tipo_foto = models.CharField(db_column='Desc_Tipo_Foto', max_length=100, blank=True, null=True)  # Field name made lowercase.
    num_ordem_tipo_foto = models.PositiveIntegerField(db_column='Num_Ordem_Tipo_Foto', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return str(self.desc_tipo_foto) if self.desc_tipo_foto else ''


    class Meta:
        managed = True
        db_table = 'Tipo_Foto'


class TipoOcorrencia(models.Model):
    cod_tipo_ocorrencia = models.AutoField(db_column='Cod_Tipo_Ocorrencia', primary_key=True)  # Field name made lowercase.
    desc_tipo_ocorrencia = models.CharField(db_column='Desc_Tipo_Ocorrencia', max_length=80, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return str(self.desc_tipo_ocorrencia) if self.desc_tipo_ocorrencia else ''


    class Meta:
        managed = True
        db_table = 'Tipo_Ocorrencia'