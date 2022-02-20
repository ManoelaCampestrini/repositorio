import sys

def quantidadeCaracteres(senha):
    if len(senha) < 6:
        print('A senha deve conter no mínimo 6 caracteres')
        sys.exit()

senha = input('Digite sua senha: ')

checkNumero = False
checkMaiusculo = False
checkMinusculo = False
checkEspecial = False

quantidadeCaracteres(senha)

for i in senha:
    if i.isdigit():
        checkNumero = True
    if i.isupper():
        checkMaiusculo = True
    if i.islower():
        checkMinusculo = True
    if not i.isalnum:
        checkEspecial = True

if not checkNumero or checkMaiusculo or checkMinusculo or checkEspecial:
    print('A senha deve conter:')
    print('No mínimo 6 caracteres,')
    print('Um número,')
    print('Uma letra maiúscula,')
    print('Uma letra minúscula,')
    print('E um caracter especial.')












