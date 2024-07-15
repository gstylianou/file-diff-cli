from lib import utilities as util


class LineCompare:
    """Line Compare"""

    def line_compare(self, line1, line2):
        """lineCompare words"""
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
