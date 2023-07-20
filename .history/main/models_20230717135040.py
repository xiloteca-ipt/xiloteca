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
    
class Especie(models.Model):
    codigo_esp=models.CharField(max_length=10)
    nome=models.CharField(max_length=100)

    def __str__(self):
        return self().title
 
class Genero(models.Model):
    codogo_gen=models.CharField(max_length=10)
    nome=models.CharField(max_length=100)

    def __str__(self):
        return self().codogo_gen
    
class Color(models.Model):
    title=models.CharField(max_length=100)
    color_codigo=models.CharField(max_length=100)

    def __str__(self):
        return self().title

       
class conteudo(models.Model):
    cod_conteudo=models.CharField(max_length=100)
    color_nomepopular=models.CharField(max_length=100)

    def __str__(self):
        return self().cod_conteudo
    
       cod_tipo_ocorrencia = models.AutoField(db_column='Cod_Tipo_Ocorrencia', primary_key=True)  # Field name made lowercase.
    desc_tipo_ocorrencia = models.CharField(db_column='Desc_Tipo_Ocorrencia', max_length=80, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tipo_Ocorrencia'
    