# ****************
# SUMANDO MATRICES
# ****************
import filecmp
from pathlib import Path


def run(matrix1_path: Path, matrix2_path: Path) -> bool:
    result_path = 'data/sum_matrix/result.dat'
    with open(matrix1_path) as f1:
        matrix1_list = []
        for line in f1:
            for num in line.strip().split():
                matrix1_list.append(int(num))
                print(matrix1_list)
            
    with open(matrix2_path) as f2:
        matrix2_list = []
        for line in f2:
            for num in line.strip().split():
                matrix2_list.append(int(num))

    result = []
    for matrix1_num in range(len(matrix1_list)):
        row = []
        for matrix2_num in range(len(matrix2_list)):
            r = matrix1_list[matrix1_num] + matrix2_list[matrix2_num]
            row.append(r)
        result.append(r)

    with open(result_path, 'w') as f:
        for row in result:
            buffer = ' '.join(str(v) for v in row)
            f.write(f'{buffer}\n')
    return filecmp.cmp(result_path, 'data/sum_matrix/.expected', shallow=False)


if __name__ == '__main__':
    run('data/sum_matrix/matrix1.dat', 'data/sum_matrix/matrix2.dat')