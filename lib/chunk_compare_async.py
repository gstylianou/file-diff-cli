from lib import utilities as util
from lib import line_compare_async, line_compare
import asyncio
import functools
import threading


# class ChunkCompareAsync:
#     def compare_async(self, file1, file2, chunk_index, chunk_size):
#         """compare two files"""
#         print("compare async is running")
#         file1_new = []
#         file2_new = []
#         lc = line_compare.LineCompare()
#         # print("start/end", chunk_index * chunk_size, (chunk_index + 1) * chunk_size)
#         for i in range(chunk_index * chunk_size, (chunk_index + 1) * chunk_size):
#             line1, line2 = lc.line_compare(file1[i], file2[i])
#             file1_new.append(line1)
#             file2_new.append(line2)

#         return file1_new, file2_new


# @util.thread_decorator
def compare_async1(file1, file2, chunk_index, chunk_size):
    """compare two files"""
    current_thread = threading.current_thread()
    thread_id = current_thread.ident
    print("thread id", thread_id)
    # print('compare async is running')
    file1_new = []
    file2_new = []
    lc = line_compare.LineCompare()
    # print(
    #     f"start/end thread {thread_id} params",
    #     chunk_index * chunk_size,
    #     (chunk_index + 1) * chunk_size,
    # )
    for i in range(chunk_index * chunk_size, (chunk_index + 1) * chunk_size):
        line1, line2 = lc.line_compare(file1[i], file2[i])
        file1_new.append(line1)
        file2_new.append(line2)
    # print(f"Thread {thread_id} finished")
    return file1_new, file2_new
