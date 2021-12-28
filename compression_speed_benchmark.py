import time
import subprocess
from os.path import exists
import os
from pathlib import Path


# 7ZIP FUNCTIONS
# ----------------------------------------
def compress_LZMA2(inputFile, outputFile):
    subprocess.run(["7z", "a", "-t7z", "-bt", outputFile, inputFile])


def compress_Bzip2(inputFile, outputFile):
    subprocess.run(["7z", "a", "-tbzip2","-bt", outputFile, inputFile])


def compress_Deflate(inputFile, outputFile):
    subprocess.run(["7z", "a", "-tgzip","-bt", outputFile, inputFile])
# ----------------------------------------

def benchmark(file):
    # leaves only name of file ex:"bible", removes path and extensions
    filename = Path(file).stem

    LZMA2_time, Bzip2_time, Deflate_time = 0, 0, 0

    # number of runs for benchmark
    NUMBER_OF_RUNS = 10

    # LZMA2
    for run in range(NUMBER_OF_RUNS):
        start_time = time.time()
        # run commmand
        compress_LZMA2(file, "./compressed_files/"+filename+".7z")
        while(True):
            end_time = time.time()
            if(exists(file)):
                break
        print("finished execution")
        print("--- %s seconds ---" % (end_time - start_time))
        LZMA2_time += (end_time - start_time)

    # BZIP2
    for run in range(NUMBER_OF_RUNS):

        start_time = time.time()
        # run commmand
        compress_Bzip2(file, "./compressed_files/"+filename+".bz2")
        while(True):
            end_time = time.time()
            if(exists(file)):
                break
        print("finished execution")
        print("--- %s seconds ---" % (end_time - start_time))
        Bzip2_time += (end_time - start_time)

    # DEFLATE
    for run in range(NUMBER_OF_RUNS):
        start_time = time.time()
        # run commmand
        compress_Deflate(file, "./compressed_files/"+filename+".gz")
        while(True):
            end_time = time.time()
            if(exists(file)):
                break
        print("finished execution")
        print("--- %s seconds ---" % (end_time - start_time))
        Deflate_time += (end_time - start_time)

    return LZMA2_time/NUMBER_OF_RUNS, Bzip2_time/NUMBER_OF_RUNS, Deflate_time/NUMBER_OF_RUNS



def compressionSpeed(time,size):
    return (size*0.000001)/time
# ----------------------------------------


def main():

    # data directory to benchmark
    dir = "dataset"
    resultdir = "compressed_files"
    try:
        # create benchmark directory
        os.mkdir(resultdir)
    except FileExistsError:
        print("directory already exists")

    results = open("compression_benchmark_results.txt", 'w')
    results.write("RESULTS FROM COMPRESSION SPEED BENCHMARK\n\n")
    # run through dataset
    for filename in os.listdir(dir):
        print(filename)
        f = os.path.join(dir, filename)
        if os.path.isfile(f):
            # run benchmark on file
            LZMA2_time, Bzip2_time, Deflate_time = benchmark(f)
            results.write("FILE: "+filename+"\n")
            results.write("SIZE: "+str(os.stat(f).st_size)+" bytes\n")
            results.write("LZMA2: "+str(LZMA2_time)+" s\n")
            results.write("LZMA2 CS: "+str(compressionSpeed(LZMA2_time,os.stat(f).st_size))+" MB/s\n")
            results.write("BZIP2: "+str(Bzip2_time)+" s\n")
            results.write("BZIP2 CS: "+str(compressionSpeed(Bzip2_time,os.stat(f).st_size))+" MB/s\n")
            results.write("DEFLATE: "+str(Deflate_time)+" s\n")
            results.write("DEFLATE CS: "+str(compressionSpeed(Deflate_time,os.stat(f).st_size))+" MB/s\n\n")
    results.close()
    print("BENCHMARK COMPLETE.")


if __name__ == "__main__":
    main()
