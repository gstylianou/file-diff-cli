import os
import sys
import asyncio
import time
from rich import print

from lib import file_compare, file_reader
from lib import file_compare_async


async def main(argv):
    """main"""
    fr1 = file_reader.FileReader(os.path.realpath(argv[0]))
    file1 = fr1.read()
    fr2 = file_reader.FileReader(os.path.realpath(argv[1]))
    file2 = fr2.read()

    if len(file1) == 0 or len(file2) == 0:
        print("one of the files is not found or is empty")
        return
    fc = file_compare_async.FileCompareAsync()
    start_time = time.time()
    file1, file2 = await fc.compare_async(file1, file2)
    end_time = time.time()

    elapsed_time_ms = (end_time - start_time)*1000

    print(f"Execution time: {elapsed_time_ms:.2f} milliseconds\n\n")

    # for item in file1:
    #     print(item)
    # for item in file2:
    #     print(item)

  


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1:]))

# todo
# diff when file1 has more lines than file2
# test other linecompare file
