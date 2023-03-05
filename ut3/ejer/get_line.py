# *****************
# HAN CANTADO LÍNEA
# *****************
from pathlib import Path


def run(input_path: Path, line_no: int) -> str:
    
    with open(input_path) as f:
        num_line = 0
        for line in f:
            num_line += 1
            if num_line == line_no:
                line = line[line_no].strip()
            else:
                line = None

    return line


if __name__ == '__main__':
    run('data/get_line/nasdaq.txt', 20)