# *****************
# ALFABETO CIRCULAR
# *****************

# Utilizar función generadora
# Utilizar módulo for i in range(n):
#                     (n + i) % n

def gen_nums(max_letters):
    ALPHA = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(max_letters):
        index_text = i % len(ALPHA)
        yield ALPHA[index_text]

def run(max_letters): 
    return ''.join(list(gen_nums(max_letters)))

if __name__ == "__main__":
    run(0)
