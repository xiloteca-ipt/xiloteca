from django.contrib import admin

from.models import *

admin.site.register(Conteudo)
admin.site.register(Determinador)
admin.site.register(Especie)
admin.site.register(Familia)
admin.site.register(Fonte)
admin.site.register(Genero)
admin.site.register(Item)
admin.site.register(ItemConteudo)
admin.site.register(Madeira)
admin.site.register(MadeiraFoto)
admin.site.register(MadeiraItem)
admin.site.register(MadeiraItemFonte)
admin.site.register(MadeiraItemObsFonte)
admin.site.register(MadeiraItemObservacao)
admin.site.register(MadeiraNomeCientifico)
admin.site.register(MadeiraNomeInternFonte)
admin.site.register(MadeiraNomeInternOcorr)
admin.site.register(MadeiraNomeInternacional)
admin.site.register(MadeiraNomePopular)
admin.site.register(MadeiraOcorrencia)
admin.site.register(Ocorrencia)
admin.site.register(Referencia)
admin.site.register(TipoFoto)
admin.site.register(TipoOcorrencia)

admin.site.site_header = "Administração Portal Xiloteca"
admin.site.site_title = "Administração Portal Xiloteca"
admin.site.index_title = "Boas-vindas ao portal de adminstração da Xiloteca"