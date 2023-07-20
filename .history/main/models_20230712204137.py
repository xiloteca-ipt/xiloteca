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
    title=models.CharField(max_length=10)
    nome=models.CharField(max_length=100)

    def __str__(self):
        return self().title
 
    
 `Cod_Genero` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `Nome_Genero` varchar(100) DEFAULT NULL,

class Color(models.Model):
    title=models.CharField(max_length=100)
    color_codigo=models.CharField(max_length=100)

    def __str__(self):
        return self().title
    
class Madeira(models.Model):
    Cod_Madeira=models.CharField(max_length=10)
    Data_Cadastro=models.DateField()
    Desc_Obs_Madeira=models.CharField(max_length=200)
    Desc_Obs_Ocorrência=models.CharField(max_length=200)
    Nome_Cientifico=models.CharField(max_length=200)
    Nome_Popular=models.CharField(max_length=200)
    Nome_Internacional=models.CharField(max_length=200)
    Caracteristica_GeralNome_Popular=models.CharField(max_length=200)
    Durabilidade=models.CharField(max_length=200)
    Caracteristica_de_rocessamento=models.CharField(max_length=200)
    Propriedades_Fisicas=models.CharField(max_length=200)
    Propriedadde_Mecânicas=models.CharField(max_length=200)
    Outras_Propriedades=models.CharField(max_length=200)
    Usos=models.CharField(max_length=200)
    Espécie=models.CharField(max_length=200)
    Genero=models.CharField(max_length=200)
    Familia=models.CharField(max_length=200)
    image=models.ImageField(upload_to="MADEIRAS_imgs/")
    color=models.ForeignKey(Color,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    detail=models.TextField()
    status=models.BooleanField(default=True)

    def __str__(self):
        return self().title

class MadeirasAttribute(models.Model):
    madeira=models.ForeignKey(Madeira,on_delete=models.CASCADE)
    #color=models.ForeignKey(Color,on_delete=models.CASCADE)
  
    def __str__(self):
        return self.madeira.title