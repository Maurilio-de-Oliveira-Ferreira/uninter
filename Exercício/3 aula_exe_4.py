                               # EXERCICIO DE TRIANGULO

a = int(input('Digite 1° lado do triangulo:'))
b = int(input('Digite 1° lado do triangulo:'))
c = int(input('Digite 1° lado do triangulo:'))

if ((a > 0 and b > 0 and c > 0) and (a + b > c and a + c > b and b + c > a)):
    # Se chegou até aqui é porque é valido!
    if (a != b and a != c and b != c ):
        print('triângulo escaleno! ')
    else:
        if (a ==b and b ==c): 
            print('triângulo equilatero!')
        else:
            print('triângulo isosceles!' )
else:    
    (' Ao menos um dos valores indicados não servem para formar um triãngulo.')          