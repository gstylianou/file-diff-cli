from lib import utilities as util
from lib import line_compare_async, line_compare, chunk_compare_async
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
        # lc = line_compare_async.LineCompareAsync()
        chunk = chunk_compare_async.ChunkCompareAsync()

        # mapped = await util.map_async(
        #     lc.line_compare_async, file1[:min_length], file2[:min_length]
        # )

        num_chunks = 129  # min_length / 10
        step = int(min_length / num_chunks)
        tasks = []
        for i in range(0, num_chunks):
            tasks.append(chunk.compare_async(file1, file2, i, step))

        mapped = await asyncio.gather(*tasks)

        for item in mapped:
            file1_new.extend(item[0])
            file2_new.extend(item[1])

        file1_new = file1_new + [
            util.color_diff_for_word(util.clean_line(n), "red")
            for n in file1[min_length:]
        ]
        file2_new = file2_new + [
            util.color_diff_for_word(util.clean_line(n), "magenta")
            for n in file2[min_length:]
        ]

        return file1_new, file2_new
