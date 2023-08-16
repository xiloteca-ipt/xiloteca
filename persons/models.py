from django.db import models
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

class Nome_Popular(models.Model):
    cod_nome_popular = models.IntegerField(db_column='Cod_Nome_Popular',  primary_key=True)  # Field name made lowercase.
    nome_popular = models.CharField(db_column='Nome_Popular', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Nome_Popular'


class Madeira(models.Model):
    cod_madeira = models.IntegerField(db_column='Cod_Madeira', primary_key=True)  # Field name made lowercase. The composite primary key (Cod_Madeira, Cod_Nome_Popular) found, that is not supported. The first column is selected.
    cod_nome_popular = models.IntegerField(db_column='Cod_Nome_Popular')  # Field name made lowercase.
    nome_popular = models.CharField(db_column='Nome_Popular', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ind_nome_principal = models.IntegerField(db_column='Ind_Nome_Principal', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Madeira_Nome_Popular'
        #unique_together = (('cod_madeira', 'cod_nome_popular'),)
   
    def __str__(self):
        return self.nome_popular
  
class Person(models.Model):
    cod_nome_popular =  models.ForeignKey(Nome_Popular, on_delete=models.CASCADE)
    cod_madeira =  models.ForeignKey(Madeira,  on_delete=models.CASCADE)
    #nome_popular = models.CharField(db_column='Nome_Popular', max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
  
    class Meta:
        managed = False
        db_table = 'Person_Madeira'
        #unique_together = (('cod_madeira', 'nome_popular'),)

    def __str__(self):
        return self.nome_popular
    

