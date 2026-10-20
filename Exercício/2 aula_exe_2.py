                     #exercio 02

'''Escreva um programa que pergunte a quantidade de km percorridos 
por um carro alugado pelo usuario, assim como a quantidade de dias
pelos quais o carro foi aliugado.
   Calcule o preco a pagar, sabendo que o carro custa R$ 60 por dia
e R$ 0,15 por km rodado
'''

km = int(input('Quantos Km foram percorridos? '))
dias = int(input('Quantos dias foram percorridos? '))

preco = 60 * dias + 0.15 * km
print(f'km = {km}. dias: {dias}. ')
print(f'valor a ser pago: {preco} ')

