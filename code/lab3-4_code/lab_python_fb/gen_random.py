import random

def gen_random(num_count, begin, end):
    rand_numbers = [random.randint(begin,end) for i in range(num_count)]
    return rand_numbers

print(gen_random(5,1,3))