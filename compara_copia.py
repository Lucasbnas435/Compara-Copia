import re

def main():
    b = le_original()
    a = le_textos()
    n = avalia_textos(a, b)
    print("O texto", n, "provavelmente foi copiado.")

def le_original():
    print("Bem-vindo ao detector automático de textos copiados.")
    print("Informe os dados do texto original:")

    
    medio_sentenca = float(input("Digite o tamanho médio de sentença: "))
    razao_tt = float(input("Digite a relação Type-Token: "))
    razao_hl = float(input("Digite a Razão Hapax-Legomana: "))
    medio_palavra = float(input("Digite o tamanho médio de palavra: "))
    medio_frase = float(input("Digite o tamanho médio de frase: "))
    complexidade_sentenca = float(input("Digite a complexidade média da sentença: "))

    return [medio_sentenca, razao_tt, razao_hl, medio_palavra, medio_frase, complexidade_sentenca]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + ". Tecle enter para sair. ")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto" + str(i) + ". Tecle enter para sair. ")

    return textos

def separa_sentencas(texto):
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    return frase.split()

def n_palavras_unicas(lista_palavras):
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    cal = 0
    controle = 0
    while controle < 6:
        cal = cal + abs(as_a[controle] - as_b[controle])
        controle = controle + 1
    similaridade = cal / 6
    return similaridade

def lista_palavras(texto):
    a = separa_sentencas(texto)
    controle = 0
    controle2 = 0
    c = []
    while controle < len(a):
        b = separa_frases(a[controle])
        while controle2 < len(b):
            c.append(b[controle2])
            controle2 = controle2 + 1
        controle2 = 0
        controle = controle + 1
    controle = 0
    controle2 = 0
    e = []
    while controle < len(c):
        d = separa_palavras(c[controle])
        while controle2 < len(d):
            e.append(d[controle2])
            controle2 = controle2 + 1
        controle2 = 0
        controle = controle + 1
    return e

def calcula_primeiro(e):
    tamanho_total = 0
    controle = 0
    while controle < len(e):
        tamanho_total = tamanho_total + len(e[controle])
        controle = controle + 1
    retornar = tamanho_total / len(e)
    return retornar

def calcula_segundo(e):
    n = n_palavras_diferentes(e)
    a = n / len(e)
    return a

def calcula_terceiro(e):
    n = n_palavras_unicas(e)
    a = n / len(e)
    return a

def calcula_quarto(texto):
    a = separa_sentencas(texto)
    soma = 0
    controle = 0
    while controle < len(a):
        soma = soma + len(a[controle])
        controle = controle + 1
    retornar = soma / len(a)
    return retornar

def calcula_quinto(texto):
    a = separa_sentencas(texto)
    controle = 0
    controle2 = 0
    c = []
    while controle < len(a):
        b = separa_frases(a[controle])
        while controle2 < len(b):
            c.append(b[controle2])
            controle2 = controle2 + 1
        controle2 = 0
        controle = controle + 1
    retornar = len(c) / len(a)
    return retornar

def calcula_sexto(texto):
    a = separa_sentencas(texto)
    controle = 0
    controle2 = 0
    c = []
    while controle < len(a):
        b = separa_frases(a[controle])
        while controle2 < len(b):
            c.append(b[controle2])
            controle2 = controle2 + 1
        controle2 = 0
        controle = controle + 1
    controle = 0
    soma = 0
    while controle < len(c):
        soma = soma + len(c[controle])
        controle = controle + 1
    retornar = soma / len(c)
    return retornar

def calcula_assinatura(texto):
    e = lista_palavras(texto)
    retornar = []
    retornar.append(calcula_primeiro(e))
    retornar.append(calcula_segundo(e))
    retornar.append(calcula_terceiro(e))
    retornar.append(calcula_quarto(texto))
    retornar.append(calcula_quinto(texto))
    retornar.append(calcula_sexto(texto))
    return retornar

def avalia_textos(textos, ass_cp):
    controle = 0
    lista_similaridades = []
    while controle < len(textos):
        lista_similaridades.append(compara_assinatura(calcula_assinatura(textos[controle]), ass_cp))
        controle = controle + 1
    lista_similaridades1 = sorted(lista_similaridades)
    num = 0
    for x in range(len(lista_similaridades)):
        if lista_similaridades[x] == lista_similaridades1[0]:
            num = x
    return num + 1


main()
