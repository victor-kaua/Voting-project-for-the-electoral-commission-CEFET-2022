"""
Arquivcs necessários: 
* Arquivo com as matrículas válidas dos alunos.
* Arquivo com a votação do dia, que contenha a matrícula e voto dos alunos.
* O arquivo com os votos válidos é criado pelo programa, mostrando os votos válidos e as respectivas matrículas dos alunos mais o seu número de matrícula.
"""

import csv
lista1 = {} #Guarda todas as votações do dia, contendo a matrícula e o voto do aluno

with open('votos_do_dia.csv') as arq1: #Abertura do Arquivo.
    csv_reader1 = csv.reader(arq1, delimiter=';') #Delimita por ;

    csv_reader1.__next__()

    for row in arq1: #ler linha por linha
        i = 0 #Indice inicial a ser lido
        matricula = ''
        voto = ''
        while i < len(row):
            if i < row.index(';'):  # Matricula;Voto
                matricula += row[i]
            else:
                 if row[i] != '\n' and row[i] != ';':
                     voto += row[i]
            i += 1
        lista1[matricula] = voto

for tupla in lista1.items(): #Enquanto tiver Tuplas(contendo matrícula do aluno + voto),será amostrado no terminal seus respectivos valores
    print(tupla)


lista2 = [] #A Lista Guarda as matrículas válidas contidas no aqruivo .csv

with open('matriculas_validas.csv') as arq2:
    csv_reader2 = csv.reader(arq2, delimiter=';')
    csv_reader2.__next__()

    for row in arq2: #ler linha por linha
        i = 0 #indice da linha a ser lido.
        matricula = '' #Matricula q vai ser adicionada
        while i < len(row): #percorre a linha
            if row[i] != '\n': #percorrer até o índice da linha ser igual a i = 11.(Quantidade de Alfanúmericos Contidos na Matrícula)
                matricula += row[i]
            i +=1
        lista2.append(matricula) # Ao final da condição, adiciona a matrícula a lista.

print(lista2) #Lista com as matrículas válidas a serem comparadas


votFinal = open('Resultado_Votos_do_dia.csv', 'a') #abertura e criação do arquivo contendo o resultado válido


for i in range(len(lista2)): #Enquanto houver linhas a serem lidas na lista 2, a condição será verdadeira.
    for chave, valor in lista1.items(): # enquanto tiver matriculas e votos vai escrevendo e lendo as outras linhas
        if chave == lista2[i]:
        #If the Matricula estiver que está sendo lida no primeiro arquivo de votação,
        #for igual ao contido no documento das matriculas válidas, o voto será computado.
            votFinal.write(f'{lista2[i]};{valor}\n') #A Escrita do voto válido no documento final 'Matricula[i]'+'voto'

votFinal.close()