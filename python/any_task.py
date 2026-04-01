import sys

# считывание списка из входного потока (список lst_in не менять)
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)

author = {a.split(': ')[0] for a in lst_in}
d = {a : {b.split(': ')[1] for b in lst_in if b.split(': ')[0] == a} for a in author }

print(d)