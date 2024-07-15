from lib import utilities as util


class LineCompare:

    def lineCompare_min_length(self, line_no, line1, line2):
        line1_ans = line1
        line2_ans = line2

        min_length = min(len(line1), len(line2))

        diff = ""
        start_index = -1
        for i in range(min_length):
            if line1[i] != line2[i]:
                diff = "".join([diff, line2[i]])
                if start_index == -1:
                    start_index = i
            elif len(diff) > 0:
                print("diff in line " + str(line_no) + " chars:" + diff)
                line1_ans = util.color_diff_for_line(
                    line1, start_index, len(diff), "magenta"
                )
                line2_ans = util.color_diff_for_line(
                    line2, start_index, len(diff), "magenta"
                )
                diff = ""

        return line1_ans, line2_ans

    def lineCompare(self, line_no, line1, line2):
        line1 = util.clean_line(line1)
        line2 = util.clean_line(line2)

        if line1 == line2:
            return line1, line2

        line1_ans = line1
        line2_ans = line2

        min_length = min(len(line1), len(line2))
        max_length = max(len(line1), len(line2))
        line1_ans, line2_ans = self.lineCompare_min_length(line_no, line1, line2)

        if min_length < max_length and max_length == len(line1):
            line1_ans = util.color_diff_for_line(line1, min_length, max_length, "magenta")
        elif min_length < max_length and max_length == len(line2):
            line2_ans = util.color_diff_for_line(line2, min_length, max_length, "magenta")

        return line1_ans, line2_ans

    def lineCompare_words(self, line1, line2):
        line1 = util.clean_line(line1)
        line2 = util.clean_line(line2)
        if line1 == line2:
            return line1, line2

        words1 = line1.split(" ")
        words2 = line2.split(" ")
        index1 = 0
        index2 = 0
        while True:
            while (
                index1 < len(words1)
                and index2 < len(words2)
                and words1[index1] == words2[index2]
            ):
                index1 += 1
                index2 += 1

            if index1 >= len(words1) or index2 >= len(words2):
                break
            if words1[index1] not in words2[index2:]:
                words1[index1] = util.color_diff_for_word(words1[index1], "red")
                index1 += 1
            else:
                while (
                    index1 < len(words1)
                    and index2 < len(words2)
                    and words1[index1] != words2[index2]
                ):
                    words2[index2] = util.color_diff_for_word(words2[index2], "red")
                    index2 += 1

        line1 = " ".join(words1)
        line2 = " ".join(words2)

        return line1, line2
