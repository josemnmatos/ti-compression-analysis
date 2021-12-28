import datetime
import subprocess
from os.path import exists
import os
from pathlib import Path
import timeit


begin_time = datetime.datetime.now()
subprocess.run(["7z", "a", "-t7z", "-bt",
               "./benchmark_files/bible.7z", "./dataset/bible.txt"])

print("\ncode time:", datetime.datetime.now() - begin_time)

begin_time = datetime.datetime.now()
subprocess.run(["7z", "e","-y","-o.\decompressed_files", "./benchmark_files/bible.7z"])
print("\ndecode time:", datetime.datetime.now() - begin_time)
