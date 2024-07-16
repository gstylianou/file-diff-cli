from lib import utilities as util
from lib import line_compare_async, line_compare, chunk_compare_async
import asyncio
import functools
import time


class FileCompareAsync:
    def export(self, tuple):
        return tuple[0], tuple[1]

    def compare_async(self, file1, file2):
        """compare two files"""
        min_length = min(len(file1), len(file2))
        file1_new = []
        file2_new = []

        num_chunks = 10
        step = int(min_length / num_chunks)

        start_time = time.time()

        threads = []

        for i in range(0, num_chunks):
            t = chunk_compare_async.compare_async1(file1, file2, i, step)
            threads.append(t)
            t.start()

        [n.join() for n in threads]

        end_time = time.time()
        elapsed_time_ms = (end_time - start_time) * 1000
        print(f"Thread Execution time: {elapsed_time_ms:.2f} milliseconds\n\n")

        # print("result", threads[3].result[1])

        for item in threads:
            # print('item result',item.result)
            file1_new.extend(item.result[0])
            file2_new.extend(item.result[1])

        file1_new = file1_new + [
            util.color_diff_for_word(util.clean_line(n), "red")
            for n in file1[min_length:]
        ]
        file2_new = file2_new + [
            util.color_diff_for_word(util.clean_line(n), "magenta")
            for n in file2[min_length:]
        ]

        return file1_new, file2_new
