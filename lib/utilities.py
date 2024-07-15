def split_line_at_three(line, start_index, length):
    line_left = line[:start_index]
    line_mid = line[start_index: start_index + length]
    line_right = line[start_index + length:]
    return line_left, line_mid, line_right


def color_diff_for_word(word, color):
    word = "".join(["[bold ", color, "]", word, "[/bold ", color, "]"])
    return word


def clean_line(line):
    """Deletes new line and extra spaces"""
    line = " ".join(line.split())
    line = line.replace("\n", "")
    return line


def color_diff_for_line(line, start_index, length, color):
    """colorizes a line segment"""
    line_left, line_mid, line_right = split_line_at_three(line, start_index, length)
    line = "".join(
        [line_left, "[bold ", color, "]", line_mid, "[/bold ", color, "]", line_right]
    )
    return line
