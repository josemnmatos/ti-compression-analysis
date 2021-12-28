import time
import subprocess
from os.path import exists
import os
from pathlib import Path


# 7ZIP FUNCTIONS
# ----------------------------------------
def decompress(inputFile, outputFile):
    subprocess.run(["7z", "e", "-y", "-o"+outputFile, inputFile])
# ----------------------------------------


def benchmark(file):
    # leaves only name of file ex:"bible", removes path and extensions
    filename = Path(file).stem

    decompress_time, Bzip2_time, Deflate_time = 0, 0, 0

    # number of runs for benchmark
    NUMBER_OF_RUNS = 10

    # LZMA2
    for run in range(NUMBER_OF_RUNS):
        start_time = time.time()
        # run commmand
        decompress(file, "./decompressed_files/"+filename+".txt")
        while(True):
            end_time = time.time()
            if(exists(file)):
                break
        print("finished execution")
        print("--- %s seconds ---" % (end_time - start_time))
        decompress_time += (end_time - start_time)

    return decompress_time/NUMBER_OF_RUNS


def decompressionSpeed(time, size):
    return (size*0.000001)/time
# ----------------------------------------


def main():

    # data directory to benchmark
    dir = "compressed_files"
    resultdir = "decompressed_files"
    try:
        # create benchmark directory
        os.mkdir(resultdir)
    except FileExistsError:
        print("directory already exists")

    results = open("decompression_benchmark_results.txt", 'w')
    results.write("RESULTS FROM DECOMPRESSION SPEED BENCHMARK\n\n")
    # run through dataset
    for filename in os.listdir(dir):
        print(filename)
        f = os.path.join(dir, filename)
        if os.path.isfile(f):
            # run benchmark on file
            decompress_time = benchmark(f)
            results.write("FILE: "+filename+"\n")
            results.write("SIZE: "+str(os.stat(f).st_size)+" bytes\n")
            results.write("DT: "+str(decompress_time)+" s\n")
            results.write(
                "DS: "+str(decompressionSpeed(decompress_time, os.stat(f).st_size))+" MB/s\n\n")

    results.close()
    print("BENCHMARK COMPLETE.")


if __name__ == "__main__":
    main()
