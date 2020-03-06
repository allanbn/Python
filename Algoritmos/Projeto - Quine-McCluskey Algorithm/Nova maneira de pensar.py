import sys
import string

'''
Esse lixo de codigo nao funciona se a entrada das saidas nao puderem serem comparadas
Corrigir erros e refazer com recursividade!!!
'''
_author_ = 'Allan Quine & Moabe McCluskey'

abcxyz = string.ascii_uppercase
indices = []
simples = {}


def entrada():
    try:
        numero_de_termos = int(input('Digite a quantidade de variáveis: '))
        if numero_de_termos < 0:
            print('Valor inválido. Digite um inteiro positivo!')
            entrada()
        elif numero_de_termos == 0:
            print('Quantidade de variáveis inválida. Digite um valor acima de zero (0)!')
            entrada()
        elif numero_de_termos > 8:
            print('Digite um número abaixo de 8')
            entrada()
    except ValueError:
        print('A entrada não suporta o tipo String. Digite um inteiro!')
    return bigbang(numero_de_termos)


def bigbang(numero_de_termos):
    global indices
    implicantes_indices = {}
    tabela_vdd = gerador_tt(numero_de_termos)
    saida_tabela = input('Digite os termos. (Ex: 0 1 3 4 5...): ').split(' ')
    if len(saida_tabela) > (2 ** numero_de_termos):
        print('Valores além da quantidade permitida.')
        bigbang(numero_de_termos)
    else:
        for i in saida_tabela:
            try:
                if int(i) in tabela_vdd.keys():
                    implicantes_indices[i] = tabela_vdd[int(i)]
                    indices.append(int(i))
                else:
                    print('Digite novamente')
                    bigbang(numero_de_termos)
            except ValueError:
                print('Bote apenas números na entrada.')
                bigbang(numero_de_termos)
    if len(implicantes_indices) == (2 ** numero_de_termos):
        print('')
        print('S: 1')
        sys.exit()
    else:
        indices.sort()
        return dontcare(implicantes_indices, tabela_vdd, numero_de_termos)


def dontcare(implicantes_indices, tabela_vdd, numero_de_termos):
    dont_care = input('Digite os Don\'t Cares como acima. (aperte enter se não'
                      ' quiser usá-los): ')
    if len(dont_care) > 0:
        dont_care = dont_care.split(' ')
        for i in dont_care:
            try:
                if int(i) in tabela_vdd and int(i) not in implicantes_indices.keys():
                    implicantes_indices[i] = tabela_vdd[int(i)]
                else:
                    print('Um dos termos digitados já está presente nos implicantes, '
                          'não será don\'t care')
                    dontcare(implicantes_indices, tabela_vdd, numero_de_termos)
            except ValueError:
                print('Digite apenas números!')
                dontcare(implicantes_indices, tabela_vdd, numero_de_termos)
    return diferenca(implicantes_indices, numero_de_termos, {})


def gerador_tt(termos):
    truth_table = {}
    for i in range(2 ** termos):
        truth_table[i] = ('{0:b}'.format(i).zfill(termos))
    return truth_table


def diferenca(implicantes, n, main_list):
    if implicantes == main_list:
        od = dict(sorted(implicantes.items(), key=lambda x: x[1].count('1')))
        return chart(od)
    else:
        main_list = {}
        results = []
        for x in implicantes.keys():
            cont1 = 0
            for z in implicantes.keys():
                if z != x:
                    indexs = []
                    str_values = ''
                    cont = 0
                    for y in range(n):
                        if implicantes[x][y] != implicantes[z][y]:
                            str_values += '-'
                            cont += 1
                        elif implicantes[x][y] == '0' and implicantes[z][y] == '0':
                            str_values += '0'
                        elif implicantes[x][y] == '1' and implicantes[z][y] == '1':
                            str_values += '1'
                        elif implicantes[x][y] == '-' and implicantes[z][y] == '-':
                            str_values += '-'
                    if cont == 1:
                        if str_values not in results:
                            results.append(str_values)
                            f = x, z
                            for i in f:
                                if type(i) != tuple:
                                    indexs.append(int(i))
                                else:
                                    for j in i:
                                        indexs.append(int(j))
                            main_list[tuple(indexs)] = str_values
                    if cont > 1:
                        cont1 += 1
                if cont1 == (len(implicantes) - 1):
                    if type(x) != tuple:
                        l_primes = [int(x)]
                        main_list[tuple(l_primes)] = implicantes[x]
                    else:
                        main_list[x] = implicantes[x]
        if implicantes != main_list and len(main_list) > 0:
            implicantes = main_list
            diferenca(implicantes, n, main_list)


def chart(houaiss):
    global indices
    mapa = []
    windex = list(houaiss.keys())
    for i in range(len(houaiss)):
        init = []
        for j in range(len(indices)):
            init.append(' ')
        mapa.append(init)
    for i in houaiss.keys():
        for j in i:
            if j in indices:
                mapa[windex.index(i)][indices.index(j)] = 'º'
    return redux(houaiss, mapa)


def redux(aurelio, karnough):
    global simples, indices
    keys = list(aurelio.keys())
    cont_fora = 0
    for i in range(len(indices)):
        cont = 0
        chave = ''
        for k in keys:
            if karnough[keys.index(k)][i] == 'º':
                cont += 1
                chave = k
        if cont == 1:
            cont_fora += 1
            if chave not in simples.keys():
                simples[chave] = aurelio[chave]
                del aurelio[chave]
    for i in simples.keys():
        for j in i:
            if j in indices:
                del indices[indices.index(j)]
        if len(indices) == 0:
            break
    if cont_fora == 0:
        return petrick(aurelio, karnough)
    elif len(indices) > 0:
        return reduc(aurelio)
    else:
        return print_primes(simples)


def reduc(ruth_rocha):
    global simples
    keys = list(ruth_rocha)
    for i in simples.keys():
        for j in keys:
            a = i.count(j)
            if a > 0:
                del ruth_rocha[j]
    return chart(ruth_rocha)


def distributiva(a, b):
    resultado = []
    if len(a) == 0 and len(b) == 0:
        return resultado
    elif len(a) == 0:
        return b
    elif len(b) == 0:
        return a
    else:
        for i in a:
            for j in b:
                if i == j:
                    if i not in resultado:
                        # continue
                        resultado.append(i)
                else:
                    kek = list(set(i+j))
                    if kek not in resultado:

                        resultado.append(kek)
        return resultado


def petrick(aurelio, mapa):
    global simples, indices
    print('')
    print('Petrick OK')
    cont = 0
    petkovic = {}
    for i in aurelio.keys():
        petkovic['P' + str(cont)] = aurelio[i]
        cont += 1
    indcs = list(petkovic.keys())
    petrick_1 = []
    for i in indices:
        lista = []
        for j in indcs:
            if mapa[indcs.index(j)][indices.index(i)] == 'º':
                lista.append([j])
        petrick_1.append(lista)
    for i in range(len(petrick_1) - 1):
        petrick_1[i+1] = distributiva(petrick_1[i], petrick_1[i+1])
    petrick_1 = sorted(petrick_1[len(petrick_1) - 1], key=len)
    for i in petrick_1[0]:
        if i in petkovic.keys():
            simples[i] = petkovic[i]
    return print_primes(simples)


def print_primes(implicantesdict):
    lista = []
    global abcxyz
    for k in implicantesdict.keys():
        str_grp = ''
        for g in range(len(implicantesdict[k])):
            if g == 0:
                if implicantesdict[k][g] == '0':
                    str_grp = (u'{}\u0304'.format(abcxyz[g]))
                elif implicantesdict[k][g] == '1':
                    str_grp = abcxyz[g]
            else:
                if len(str_grp) == 0:
                    if implicantesdict[k][g] == '0':
                        str_grp = (u'{}\u0304'.format(abcxyz[g]))
                    elif implicantesdict[k][g] == '1':
                        str_grp = abcxyz[g]
                else:
                    if implicantesdict[k][g] == '0':
                        str_grp += (u'{}\u0304'.format(abcxyz[g]))
                    elif implicantesdict[k][g] == '1':
                        str_grp += abcxyz[g]
        lista.append(str_grp)
    last_str = ''
    for i in range(len(lista)):
        if i == 0:
            last_str = lista[i]
        elif i > 0:
            last_str += lista[i]
        if i < (len(lista) - 1):
            last_str += ' + '
    print('\nS: ' + last_str)


entrada()
