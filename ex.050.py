n = int(input('Digite um número que você gostaria de ver a tabuada: '))
c = 0
m = 0
for c in range (-1, 10):
    c = c + 1
    m = n * c
    print(n, 'x', c, '=', m)
print('FIM')