def verificar_aprovacao(lista_de_notas,media_corte):
    print('---Verificando situação dos Alunos---')
    for nota in lista_de_notas:
        if nota >= media_corte:
            print(f'Nota {nota}: Aprovado!')
        else:
            print(f'Nota {nota}: Reprovado.')

 # Usando a função:
notas_semestre = [4.5, 7.0, 9.5, 6.0]
verificar_aprovacao(notas_semestre, 5.0)           