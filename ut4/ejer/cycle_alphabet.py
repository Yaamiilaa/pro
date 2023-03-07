# *****************
# ALFABETO CIRCULAR
# *****************

# Utilizar función generadora
# Utilizar módulo for i in range(n):
#                     (n + i) % n
def gen_nums(max_letters):
    for i in range(max_letters):
        index_text = i % max_letters
        yield index_text



if __name__ == "__main__":
    run(0)
