# **********************
# FRECUENCIA DE PALABRAS
# **********************
from pathlib import Path


def run(input_path: Path, lower_bound: int) -> dict:
    
    with open(input_path) as f:
        freq = {}
        for line in f:
            words = line.lower().strip().split()
            for word in words:
                freq[word] = freq.get(word, 0) + 1
    freq = {key: value for key, value in freq.items() if value >= lower_bound}
    
    return freq


if __name__ == '__main__':
    run('data/word_freq/cistercian.txt', 9)