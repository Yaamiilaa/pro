# ********************
# LA PALABRA MÁS LARGA
# ********************
from pathlib import Path


def run(input_path: Path) -> str:
    
    with open(input_path) as f:
        for line in f:
            max_length = 0
            words_len = []
            long_word = []
            for word in line.strip().split():
                words_len.append(len(word))
                long_word.append(word.strip(',.;:()').split(' '))
                for word_len in words_len:
                    if word_len >= max_length:
                        max_length = word_len
                        longest_word = ''.join(long_word)

    return longest_word


if __name__ == '__main__':
    run('data/longest_word/python.txt')# ********************
# LA PALABRA MÁS LARGA
# ********************
from pathlib import Path

STRIP_CHARS = '.,:;()'


def run(input_path: Path) -> str:
    f = open(input_path)
    max_length, longest_word = 0, ''
    for line in f:
        words = line.strip().split()
        clean_words = [w.strip(STRIP_CHARS) for w in words]
        for word in clean_words:
            if len(word) >= max_length:
                max_length = len(word)
                longest_word = word
    return longest_word


if __name__ == '__main__':
    run('data/longest_word/python.txt')