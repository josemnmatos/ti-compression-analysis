from os import system
import sfe
import numpy as np


def getEntropia(fonte):
    fonteArray = np.array(list(fonte))
    alfabetoTxt = np.array([])

    mask = np.isin(np.unique(fonteArray), alfabetoTxt)
    for i in range(len(mask)):
        if (mask[i] == False):
            alfabetoTxt = np.append(alfabetoTxt, np.unique(fonteArray)[i])

    return calculaEntropia(fonteArray, alfabetoTxt)


def contaOcorrencias(fonte, alfabeto):
    arrayOcorrencias = np.zeros(alfabeto.size, int)
    for elemento in fonte:
        arrayOcorrencias[elemento == alfabeto] += 1
    return arrayOcorrencias


def calculaEntropia(fonte, alfabeto):
    numOcorrencias = contaOcorrencias(fonte, alfabeto)
    ns = np.sum(numOcorrencias)

    m = numOcorrencias/ns
    m = m[m > 0]
    entropia = -np.sum(m*np.log2(m))
    return entropia


def run_length_encode_ascii(x):
    y = np.empty(x.shape[0] * 2, dtype=np.int32)
    v = x[0]
    length = 0
    count = 0
    for i in x:
        if i == v:
            length += 1
        else:
            y[count] = ord(v)
            count += 1
            y[count] = length
            count += 1
            v = i
            length = 1

    y[count] = ord(v)
    count += 1
    y[count] = length

    return y[:count + 1]


def main():
    f = open('adaptiveBible.txt', 'r')
    fonte = f.read()
    fonteArray = np.fromstring(fonte,sep="")
    fonteArrayRle=run_length_encode_ascii(fonteArray)
    
    print(fonteArray)


if __name__ == "__main__":
    main()
