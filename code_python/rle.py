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


def encode_a(text):
    """
    Returns a run-length encoded string from an input string.
    Note: This function will not return the character count in the return
    string if only a single instance of the character is found.

    Args:
        text (str): A string to encode

    Returns:
        str: A run length encoded string

    Example:
        input: "aaabbcdddd"
        returns: "3a2bc4d"
    """

    count = 1
    previous = ""
    mapping = list()

    for character in text:
        if character != previous:
            if previous:
                mapping.append((previous, count))
            count = 1
            previous = character
        else:
            count += 1
    else:
        mapping.append((character, count))

    result = ""

    for character, count in mapping:
        if count == 1:
            result += character
        else:
            result += str(count)
            result += character

    return result


def main():
    f = open("./original_files/bible.txt")
    text = f.read()
    f.close()
    print(getEntropia(encode_a(text)))


if __name__ == "__main__":
    main()
