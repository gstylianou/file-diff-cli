from lib import utilities as util
from lib import line_compare_async, line_compare
import asyncio
import functools


class FileCompareAsync:
    def export(self, tuple):
        return tuple[0], tuple[1]

    async def compare_async(self, file1, file2):
        """compare two files"""
        min_length = min(len(file1), len(file2))
        file1_new = []
        file2_new = []
        lc = line_compare_async.LineCompareAsync()
 
        mapped = await util.map_async(
            lc.line_compare_async, file1[:min_length], file2[:min_length]
        )

        for item in mapped:
            file1_new.append(item[0])
            file2_new.append(item[1])

            file1_new = file1_new + [
                util.color_diff_for_word(util.clean_line(n), "red")
                for n in file1[min_length:]
            ]
            file2_new = file2_new + [
                util.color_diff_for_word(util.clean_line(n), "magenta")
                for n in file2[min_length:]
            ]

        return file1_new, file2_new
