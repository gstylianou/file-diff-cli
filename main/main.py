import os
import sys

from rich import print

from lib import file_compare, file_reader, file_compare_thread


def main(argv):
    """main"""
    fr1 = file_reader.FileReader(os.path.realpath(argv[0]))
    file1 = fr1.read()
    fr2 = file_reader.FileReader(os.path.realpath(argv[1]))
    file2 = fr2.read()

    if len(file1) == 0 or len(file2) == 0:
        print("one of the files is not found or is empty")
        return
    fc = file_compare.FileCompare()
    file1, file2 = fc.compare(file1, file2)
    for item in file1:
        print(item)
    for item in file2:
        print(item)

if __name__ == "__main__":
    main(sys.argv[1:])

# todo
# diff when file1 has more lines than file2
# test other linecompare file
