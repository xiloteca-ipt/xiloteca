-- Jatobá (cod_madeira 14)
select Nome_Popular
from Madeira_Nome_Popular
where Ind_Nome_Principal = 1
  AND Cod_Madeira = 14;

-- nome científico
select G.Nome_Genero, E.Nome_Especie, ',', F.Nome_Familia
from Madeira_Nome_Cientifico MNC
         join Familia F on MNC.Cod_Familia = F.Cod_Familia
         join Genero G on MNC.Cod_Genero = G.Cod_Genero
         join Especie E on MNC.Cod_Especie = E.Cod_Especie
where MNC.Cod_Madeira = 14;

-- outros nomes populares
select Nome_Popular
from Madeira_Nome_Popular
where Ind_Nome_Principal = 0
  AND Cod_Madeira = 14;

-- Observação
select Desc_Obs_Nome_Cientifico
from Madeira
where Cod_Madeira = 14;

-- nomes internacionais
Select R.Nome_Referencia, F.Desc_Num_Fonte, MNI.Nome_Internacional, O.Nome_Ocorrencia
from Madeira_Nome_Internacional MNI
         left join Madeira_Nome_Intern_Ocorr MNIO
                   on MNI.Cod_Madeira = MNIO.Cod_Madeira and MNI.Cod_Nome_Internacional = MNIO.Cod_Nome_Internacional
         left join Ocorrencia O on MNIO.Cod_Ocorrencia = O.Cod_Ocorrencia
         left join Madeira_Nome_Intern_Fonte MNIF
                   on MNI.Cod_Madeira = MNIF.Cod_Madeira and MNI.Cod_Nome_Internacional = MNIF.Cod_Nome_Internacional
         left Join Fonte F on MNIF.Cod_Fonte = F.Cod_Fonte
         left join Referencia R on F.Cod_Referencia = R.Cod_Referencia
Where MNI.Cod_Madeira = 14
order by MNI.Nome_Internacional, O.Nome_Ocorrencia;

-- Ocorrencia
select O.Cod_Tipo_Ocorrencia, Desc_Tipo_Ocorrencia, Nome_Ocorrencia
from Madeira_Ocorrencia MO
         join Madeira M on MO.Cod_Madeira = M.Cod_Madeira
         join Ocorrencia O on MO.Cod_Ocorrencia = O.Cod_Ocorrencia
         join Tipo_Ocorrencia T on O.Cod_Tipo_Ocorrencia = T.Cod_Tipo_Ocorrencia
where M.Cod_Madeira = 14;

-- caracteristicas gerais
SELECT I.Cod_Item, I.Nome_Item, MI.Desc_Item
from Madeira_Item MI
         join Item I on MI.Cod_Item = I.Cod_Item
where MI.Cod_Madeira = 14
  AND I.Cod_Item > 0
  AND I.Cod_Item < 13;

-- Fonte
SELECT *
from Madeira_Item_Observacao
where Cod_Madeira = 14
  and Cod_Item = 3
ORDER BY Cod_Item, Num_Obs, Num_Linha;

-- Durabilidade / Tratamento
SELECT I.Cod_Item, I.Nome_Item, MI.Desc_Item
from Madeira_Item MI
         join Item I on MI.Cod_Item = I.Cod_Item
where MI.Cod_Madeira = 14
  AND I.Cod_Item IN (13, 14, 15);

-- Características de processamento
SELECT I.Cod_Item, I.Nome_Item, MI.Desc_Item
from Madeira_Item MI
         join Item I on MI.Cod_Item = I.Cod_Item
where MI.Cod_Madeira = 14
  AND I.Cod_Item IN (16, 17, 18);

-- item-observação (não possui título visível)
SELECT *
from Madeira_Item_Observacao
where Cod_Madeira = 14
  and Cod_Item = 18
ORDER BY Cod_Item, Num_Obs, Num_Linha;

-- propriedades físicas
SELECT I.Cod_Item, I.Nome_Item, MI.Valor_Inteiro, MI.Valor_Decimal, I.Desc_Unidade_Medida
from Madeira_Item MI
         left join Item I on MI.Cod_Item = I.Cod_Item
where MI.Cod_Madeira = 14
  AND I.Cod_Item > 18
  AND I.Cod_Item < 30;

SELECT *
from Madeira_Item_Observacao
where Cod_Madeira = 14
  and Cod_Item = 25
ORDER BY Cod_Item, Num_Obs, Num_Linha;


-- propriedades mecanicas
SELECT I.Cod_Item, I.Nome_Item, MI.Valor_Inteiro, MI.Valor_Decimal, I.Desc_Unidade_Medida
from Madeira_Item MI
         left join Item I on MI.Cod_Item = I.Cod_Item
where MI.Cod_Madeira = 14
  AND I.Cod_Item > 29
  AND I.Cod_Item < 39;

SELECT *
from Madeira_Item_Observacao
where Cod_Madeira = 14
  and Cod_Item = 31
ORDER BY Cod_Item, Num_Obs, Num_Linha;

SELECT I.Cod_Item, I.Nome_Item, MI.Valor_Inteiro, MI.Valor_Decimal, I.Desc_Unidade_Medida
from Madeira_Item MI
         left join Item I on MI.Cod_Item = I.Cod_Item
where MI.Cod_Madeira = 14
  AND I.Cod_Item > 38
  AND I.Cod_Item < 51;

SELECT *
from Madeira_Item_Observacao
where Cod_Madeira = 14
  and Cod_Item = 39
ORDER BY Cod_Item, Num_Obs, Num_Linha;

SELECT I.Cod_Item, I.Nome_Item, MI.Valor_Inteiro, MI.Valor_Decimal, I.Desc_Unidade_Medida
from Madeira_Item MI
         left join Item I on MI.Cod_Item = I.Cod_Item
where MI.Cod_Madeira = 14
  AND I.Cod_Item > 50
  AND I.Cod_Item < 63;

SELECT *
from Madeira_Item_Observacao
where Cod_Madeira = 14
  and Cod_Item = 51
ORDER BY Cod_Item, Num_Obs, Num_Linha;

-- USOS
SELECT I.Cod_Item, I.Nome_Item, C.Desc_Conteudo
from Madeira_Item MI
         left join Item I on MI.Cod_Item = I.Cod_Item
         left join Item_Conteudo IC on I.Cod_Item = IC.Cod_Item
         left join Conteudo C on IC.Cod_Conteudo = C.Cod_Conteudo
where MI.Cod_Madeira = 14
  AND I.Cod_Item > 62
  AND I.Cod_Item < 77;

-- campos usados apenas para pesquisa
SELECT I.Cod_Item, I.Nome_Item, C.Desc_Conteudo
from Madeira_Item MI
         left join Item I on MI.Cod_Item = I.Cod_Item
         left join Item_Conteudo IC on I.Cod_Item = IC.Cod_Item
         join Conteudo C on IC.Cod_Conteudo = C.Cod_Conteudo AND MI.Cod_Conteudo = C.Cod_Conteudo
where MI.Cod_Madeira = 14
  AND I.Cod_Item > 76;

-- sao usados apenas como filtro de pesquisa os itens com Cod_Item > 76

-- não há registros para o Cod_Item > 81