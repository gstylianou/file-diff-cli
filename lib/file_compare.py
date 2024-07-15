from lib import line_compare
from lib import utilities as util


class FileCompare:
    def compare(self, file1, file2):
        '''compare two files'''
        min_length = min(len(file1), len(file2))
        file1_new = []
        file2_new = []
        lc = line_compare.LineCompare()
        for i in range(min_length):
            line1, line2 = lc.line_compare(file1[i], file2[i])
            file1_new.append(line1)
            file2_new.append(line2)

        if len(file1) > min_length:
            file1_new = file1_new + [
                util.color_diff_for_word(util.clean_line(n), "red")
                for n in file1[min_length:]
            ]
        if len(file2) > min_length:
            file2_new = file2_new + [
                util.color_diff_for_word(util.clean_line(n), "magenta")
                for n in file2[min_length:]
            ]

        return file1_new, file2_new
