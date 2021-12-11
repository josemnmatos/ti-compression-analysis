from collections import OrderedDict
import numpy as np


def getEntropia(fonte):
    fonteArray = np.array(list(fonte))
    range1 = np.arange(65, 91)
    range2 = np.arange(97, 123)
    alfabetoTxt = np.concatenate((range1, range2))

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


def bwt(s):
    """Apply Burrows-Wheeler transform to input string."""
    assert "\002" not in s and "\003" not in s, "Input string cannot contain STX and ETX characters"
    s = "\002" + s + "\003"  # Add start and end of text marker
    table = sorted(s[i:] + s[:i]
                   for i in range(len(s)))  # Table of rotations of string
    last_column = [row[-1:] for row in table]  # Last characters of each row
    return "".join(last_column)  # Convert list of characters into string


def ibwt(r):
    """Apply inverse Burrows-Wheeler transform."""
    table = [""] * len(r)  # Make empty table
    for i in range(len(r)):
        table = sorted(r[i] + table[i]
                       for i in range(len(r)))  # Add a column of r
    # Find the correct row (ending in ETX)
    s = [row for row in table if row.endswith("\003")][0]
    return s.rstrip("\003").strip("\002")  # Get rid of start and end markers


def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data:
        return ''

    for char in data:
        # If the prev and current characters
        # don't match...
        if char != prev_char:
            # ...then add the count and character
            # to our encoding
            if prev_char:
                if(count > 1):
                    encoding += str(count) + prev_char
                else:
                    encoding += prev_char
            count = 1
            prev_char = char
        else:
            # Or increment our counter
            # if the characters do match
            count += 1
    else:
        # Finish off the encoding
        if(count > 1):
            encoding += str(count) + prev_char
        else:
            encoding += prev_char

        return encoding


def main():
    f = open(r"C:\Users\josemnmatos\Documents\TP2\project\dataset\random.txt", 'r')
    string = f.read()
    f.close()
    stringBWT = bwt(string)
    stringBWT_RLE = rle_encode(stringBWT)
    print("Entropia normal->", getEntropia(string))
    print("Entropia apos bwt e rle->", getEntropia(stringBWT_RLE))


if __name__ == "__main__":
    main()
