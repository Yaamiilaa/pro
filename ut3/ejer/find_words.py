# ***********************************
# ¿DÓNDE ESTÁN LAS PALABRAS? MATARILE
# ***********************************
from pathlib import Path


def run(data_path: Path, target_word: str) -> list:
    with open(data_path) as f:
        CHARACTERS = ".,:;()'¡!-"
        num_line = 0
        matches = []
        words = []
        for line in f:
            num_line += 1
            for word in line.strip().split():
                clean_word = ''.join(character for character in word if character not in CHARACTERS)
                if clean_word.upper() == target_word.upper():
                    matches_tuple = (num_line, line.index(clean_word) + 1)
                    matches.append(matches_tuple)
                

                

    return matches


if __name__ == '__main__':
    run('data/find_words/bzrp.txt', 'persona')