from aritmetica.operacoes import *
from geometria.formas import *
def main():
    
    a = float(input("digite o primeiro número:"))
    b = float(input("digite o segundo número:"))
    resultado_soma = soma(a, b)
    print (f'A soma de {a} e {b} é {soma(a,b)}')

    largura = float(input("Digite a largura:"))
    altura = float(input("Digite a altura:"))
    area = area_retangulo(largura, altura)
    print(f"A área do retângulo de largura {largura} e altura {altura} é: {area}")

    a = float(input("digite o primeiro número:"))
    b = float(input("digite o segundo número:"))
    print (f'A divisão de {a} e {b} é {divisao(a,b)}')



if __name__ == "__main__":

    main()