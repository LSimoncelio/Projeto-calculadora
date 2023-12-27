#Calculadora Python

def soma(x, y):
    return x + y

def subtração(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y!= 0:
        return x / y
    else:
        return "Divisão por zero não é permitida."
    
def calculadora():

    while True:
        print("Selecione a operação: ")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("0. Sair")

        escolha = input ("Digite a opção (0, 1, 2, 3, 4: ")

        if escolha == '0':
            print("Calculadora encerrada.")
            print()
            break

            continue

        if escolha in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Entrada inválida. Por favor, insira números válidos!")
                continue

            resultado = None
            if escolha == '1':
                resultado = soma(num1, num2)
            elif escolha == '2':
                resultado = subtração(num1, num2)
            elif escolha == '3':
                resultado = multiplicacao(num1, num2)
            elif escolha == '4':
                resultado = divisao(num1, num2)
            
            operacao = f"{num1} + {num2} = {resultado}"

            print("Resultado", resultado)
        
        else:
            print("Opção inválida, tente novamente!")

if __name__ == "__main__":
    calculadora()