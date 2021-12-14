import numpy as np


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
    f = open(r"original_files\random.txt", 'r')
    string = f.read()
    stringBWT=bwt(string)
    f.close()
    fW=open(r"bwtRandom.txt",'w')
    fW.write(stringBWT)
    fW.close()


if __name__ == "__main__":
    main()
