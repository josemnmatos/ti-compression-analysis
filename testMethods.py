from LZ77 import LZ77Compressor


def main():
    compressor = LZ77Compressor(window_size=20)
    inputFile = "original_files//bible.txt"
    outputFile = "lz77Bible.txt"
    compressor.compress(inputFile, outputFile)


if __name__ == "__main__":
    main()
 