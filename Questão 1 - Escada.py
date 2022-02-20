quantidadeDegraus = 6
for linha in range(quantidadeDegraus):
    aux = quantidadeDegraus - linha - 1
    for coluna in range(quantidadeDegraus):
        if coluna < aux:
            print(' ', end = '')
        else:
            print('*', end = '')

    print('')
