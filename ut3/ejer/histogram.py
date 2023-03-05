# **********
# HISTOGRAMA
# **********
import filecmp
from pathlib import Path


def run(data_path: Path) -> bool:
    histogram_path = 'data/histogram/histogram.txt'
    with open(data_path) as f:
        letters = []
        histogram = {}
        num_letters = 0
        for line in f:
            for letter in line.strip().split():
                letters.append(letter)
                if letter in letters:
                    num_letters += 1
        

    with open(histogram_path, 'w') as f:
        histogram = {}
        histogram[letter] = num_letters
        f.write(histogram)
        print(histogram)

    return filecmp.cmp(histogram_path, 'data/histogram/.expected', shallow=False)


if __name__ == '__main__':
    run('data/histogram/data.txt')