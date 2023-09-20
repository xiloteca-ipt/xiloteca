import json
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import render
from ipt.forms import BuscaForm
from ipt.models import Madeira, Consulta

def index(request):
    return render(request,'index.html')

def busca(request):
    form = BuscaForm()
    if request.method == "POST":
        form =BuscaForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "busca.html", {"form": form})


def ficha(request):
    try:
        cod_madeira_param = request.GET.get('id')
        resultados = Consulta.objects.raw('''
            select A.Cod_Madeira, A.Nome_Popular, B.Cod_Status_Madeira, B.Desc_Obs_Madeira, B.Desc_Obs_Nome_Cientifico,B.Desc_Obs_Ocorrencia
            from Madeira_Nome_Popular A
            INNER join Madeira B on A.Cod_Madeira = B.Cod_Madeira
             WHERE A.Cod_Madeira = %s
        ''', [cod_madeira_param])
        if not resultados:
            raise Consulta.DoesNotExist

        query_result_1 = Consulta.objects.raw('''
            select Cod_Madeira, Nome_Popular from Madeira_Nome_Popular 
            where Ind_Nome_Principal = 1 AND Cod_Madeira = %s
        ''', [cod_madeira_param])

        query_result_2 = Consulta.objects.raw('''
            select Cod_Madeira, G.Nome_Genero, E.Nome_Especie, ',', F.Nome_Familia
            from Madeira_Nome_Cientifico MNC
                join Familia F on MNC.Cod_Familia = F.Cod_Familia
                join Genero G on MNC.Cod_Genero = G.Cod_Genero
                join Especie E on MNC.Cod_Especie = E.Cod_Especie
            where MNC.Cod_Madeira = %s
        ''', [cod_madeira_param])

        query_result_3 = Consulta.objects.raw('''
            select Cod_Madeira, Nome_Popular
            from Madeira_Nome_Popular
            where Ind_Nome_Principal = 0
              AND Cod_Madeira = %s
        ''', [cod_madeira_param])

        query_result_4 = Consulta.objects.raw('''
            select Cod_Madeira, Desc_Obs_Nome_Cientifico
            from Madeira
            where Cod_Madeira = %s
        ''', [cod_madeira_param])

        query_result_5 = Consulta.objects.raw('''
            Select MNI.Cod_Madeira, R.Nome_Referencia, F.Desc_Num_Fonte, MNI.Nome_Internacional, O.Nome_Ocorrencia
              from Madeira_Nome_Internacional MNI
            left join Madeira_Nome_Intern_Ocorr MNIO
                    on MNI.Cod_Madeira = MNIO.Cod_Madeira and MNI.Cod_Nome_Internacional = MNIO.Cod_Nome_Internacional
            left join Ocorrencia O on MNIO.Cod_Ocorrencia = O.Cod_Ocorrencia
            left join Madeira_Nome_Intern_Fonte MNIF
                    on MNI.Cod_Madeira = MNIF.Cod_Madeira and MNI.Cod_Nome_Internacional = MNIF.Cod_Nome_Internacional
            left Join Fonte F on MNIF.Cod_Fonte = F.Cod_Fonte
            left join Referencia R on F.Cod_Referencia = R.Cod_Referencia
            Where MNI.Cod_Madeira = %s 
            order by MNI.Nome_Internacional, O.Nome_Ocorrencia
            ''', [cod_madeira_param])

        query_result_6 = Consulta.objects.raw('''
            select M.Cod_Madeira, O.Cod_Tipo_Ocorrencia, Desc_Tipo_Ocorrencia, Nome_Ocorrencia
            from Madeira_Ocorrencia MO
                    join Madeira M on MO.Cod_Madeira = M.Cod_Madeira
                    join Ocorrencia O on MO.Cod_Ocorrencia = O.Cod_Ocorrencia
                    join Tipo_Ocorrencia T on O.Cod_Tipo_Ocorrencia = T.Cod_Tipo_Ocorrencia
            where M.Cod_Madeira = %s
        ''', [cod_madeira_param])

        #caracteristicas gerais
        query_result_7 = Consulta.objects.raw('''
            SELECT Cod_Madeira, I.Cod_Item, I.Nome_Item, MI.Desc_Item
            from Madeira_Item MI
                    join Item I on MI.Cod_Item = I.Cod_Item
            where MI.Cod_Madeira = %s
            AND I.Cod_Item > 0
            AND I.Cod_Item < 13
          ''', [cod_madeira_param])

          #Fonte
        query_result_8 = Consulta.objects.raw('''
            SELECT Cod_Madeira, Desc_Obs
            from Madeira_Item_Observacao
            where Cod_Madeira = %s
            and Cod_Item = 3
            ORDER BY Cod_Item, Num_Obs, Num_Linha
         ''', [cod_madeira_param])

        #Durabilidade / Tratamento
        query_result_9 = Consulta.objects.raw('''
            SELECT I.Cod_Item, I.Nome_Item, MI.Desc_Item
            from Madeira_Item MI
                    join Item I on MI.Cod_Item = I.Cod_Item
            where MI.Cod_Madeira = %s
            AND I.Cod_Item IN (13, 14, 15)
        ''', [cod_madeira_param])

        #Características de processamento
        query_result_10 = Consulta.objects.raw('''
          SELECT I.Cod_Item, I.Nome_Item, MI.Desc_Item
            from Madeira_Item MI
                    join Item I on MI.Cod_Item = I.Cod_Item
            where MI.Cod_Madeira = %s
            AND I.Cod_Item IN (16, 17, 18)
          ''', [cod_madeira_param])

        return render(request, 'ficha.html', {
        'resultados': resultados,  
        'query_result_1': query_result_1,
        'query_result_2': query_result_2,
        'query_result_3': query_result_3,
        'query_result_4': query_result_4,
        'query_result_5': query_result_5,
        'query_result_6': query_result_6,
        'query_result_7': query_result_7,
        'query_result_8': query_result_8,
        'query_result_9': query_result_9,
        'query_result_10': query_result_10
    })

    except Consulta.DoesNotExist:
        return render(request, 'ficha.html', {'resultados': []})

def wood(request):
    data = json.loads(request.body)
    wood = Madeira.objects.filter(cod_nome_popular=data['user_id'])
    return JsonResponse(list(wood.values("cod_madeira", "nome_popular")), safe=False)

def nomep(request):
    data = json.loads(request.body)
    nomep = Madeira.objects.filter(cod_nome_popular=data['user_id'])
    return JsonResponse(list(nomep.values("cod_nome_popular", "nome_popular")), safe=False)
