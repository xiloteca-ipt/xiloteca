-- Jatobá (cod_madeira 14)
select Nome_Popular from Madeira_Nome_Popular where Ind_Nome_Principal = 1 AND Cod_Madeira = 14;

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
select Desc_Obs_Nome_Cientifico from Madeira where Cod_Madeira = 14;

-- nomes internacionais
Select R.Nome_Referencia, F.Desc_Num_Fonte, MNI.Nome_Internacional, O.Nome_Ocorrencia
from Madeira_Nome_Internacional MNI
         left join Madeira_Nome_Intern_Ocorr MNIO
                   on MNI.Cod_Madeira = MNIO.Cod_Madeira and MNI.Cod_Nome_Internacional = MNIO.Cod_Nome_Internacional
    left join Ocorrencia O on MNIO.Cod_Ocorrencia = O.Cod_Ocorrencia
    left join Madeira_Nome_Intern_Fonte MNIF on MNI.Cod_Madeira = MNIF.Cod_Madeira and MNI.Cod_Nome_Internacional = MNIF.Cod_Nome_Internacional
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

