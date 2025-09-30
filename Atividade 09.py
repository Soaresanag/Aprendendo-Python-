def calculadora(a, b, operacao):
    if operacao == '+':
        return a + b
    elif operacao == '-':
        return a - b
    elif operacao == '*':
        return a * b
    elif operacao == '/':
        if b != 0:
            return a / b
        else:
            return "Erro: divisão por zero!"
    else:
        return "Operação inválida."

a = float(input("primeiro numero: "))
b = float(input("segundo numero"))
ope = input("operacao")
print(calculadora(a, b, ope))  

