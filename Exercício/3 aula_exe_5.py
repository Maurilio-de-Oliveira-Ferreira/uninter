                                           #  CALCULADORA

print('calculadora')
print('+ adicão')
print('- subtração')
print('* mutiplicação')
print('/ divisão')
print('Pressione qualquer outra tecla para sair. ')

op = input('Qual operação deseja realizar? ')
x = int(input('Digete o primeiro valor: '))
y = int(input('Digete o segundo valor: '))

if (op == '+'):
    res = x + y
    print(f'resultado: {x} + {y} = {res}')

elif (op == '-'): 
    res = x - y 
    print(f'resultado: {x} - {y} = {res}')

elif (op == '*'): 
    res = x * y 
    print(f'resultado: {x} * {y} = {res}')  

elif (op == '/'): 
    res = x / y 
    print(f'resultado: {x} / {y} = {res}')

else:
    print(' Encerrado o programa... ')




