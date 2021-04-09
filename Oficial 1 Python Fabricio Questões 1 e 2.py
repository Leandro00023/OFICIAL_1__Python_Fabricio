import random
import timeit

def selection_sort(list_func):
    n = len(list_func)
    for i in range(0, n):
        index_min = i
        for j in range(i+1, n):
            if list_func[j] < list_func[index_min]:
                index_min = j
        list_func[i], list_func[index_min] = list_func[index_min], list_func[i]
    return list_func

def bublle_sort(list):
    n = len(list)
    for i in range(n - 1):
        for j in range(n - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list

def insertion_sort(list):
    n = len(list)
    for i in range(1, n):
        insert_value = list[i]
        j = i - 1
        while j >= 0 and list[j] > insert_value:
            list[j+1] = list[j]
            j -= 1
        list[j + 1] = insert_value
    return list

soma1 = 0
soma2 = 0
soma3 = 0

for i in range(1, 4):
    print()

    list = random.sample(range(100_000), 50_000)

    #print(list)
    start_time = timeit.default_timer()
    selection_sort(list)
    #print(f'SELECTION_SORT: {selection_sort(list)}')
    tempo1 = timeit.default_timer() - start_time
    print(f'TEMPO DE EXECUÇÃO DO SELECTION_SORT: {timeit.default_timer() - start_time:.5f}')

    #print(list)
    start_time = timeit.default_timer()
    bublle_sort(list)
    #print(f'BUBLLE_SORT: {bublle_sort(list)}')
    tempo2 = timeit.default_timer() - start_time
    print(f'TEMPO DE EXECUÇÃO DO BUBLLE_SORT:    {timeit.default_timer() - start_time:.5f}')

    #print(list)
    start_time = timeit.default_timer()
    insertion_sort(list)
    #print(f'INSERTION_SORT: {insertion_sort(list)}')
    tempo3 = timeit.default_timer() - start_time
    print(f'TEMPO DE EXECUÇÃO DO INSERTION_SORT: {timeit.default_timer() - start_time:.5f}')

    soma1 = tempo1 + soma1
    soma2 = tempo2 + soma2
    soma3 = tempo3 + soma3

media1 = soma1 / 3
media2 = soma2 / 3
media3 = soma3 / 3

print()
print(f'MÉDIA DO SELECTION_SORT:  {media1:.6f}')
print(f'MÉDIA DO BUBLLE_SORT:     {media2:.6f}')
print(f'MÉDIA DO INSERTION_SORT:  {media3:.6f}')

#-----------------------------------------------------------------------------------------------------------
# e)Em seguida, justifique qual teve o melhor desempenho em sua opinião.

# O algoritomo de insertion_sort tem o melhor desempenho pois ele percorre toda a lista compara qaul é o
# menor e tras para a posição correta de uma unica vez.


#-----------------------------------------------------------------------------------------------------------
# 2.Explique porque o algoritmo de busca binária possui desempenho superior ao algoritmo de busca linear.

# a busca binaria quebra o conjunto de entrada em conjutos menores, assim dividindo o conjunto ao meio e
# verificando se a cheve que esta sendo procurada é maior ou menor que o elemento central.
# Exemplo: se for menor  ele pega a primeira parte da lista quebra ela no meio e comprara de novo, se
# for maior ele pega a segunda parte da lista quebra ela no meio e comprara de novo. E esse processo
# se repete ate encontrar o a chave que esta sendo procurada ou caso não tenha a cheve que esta sendo
# procurada o algoritimo em execução é encerrado, com  isso ele consegue encontrar os elementos com
# uma velocidade bem maior do que com a busca linear, sua unica exigencia e que a lista esteja ordenada.
#-----------------------------------------------------------------------------------------------------------
