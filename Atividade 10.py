# 1. Número secreto
numero_secreto = 7

# 2. Pede para o usuário digitar um número
numero_usuario = int(input("Digite um número: "))

if numero_usuario == numero_secreto:
    print("Acertou!")
elif numero_usuario < numero_secreto:
    print("Muito baixo!")
else:
    print("Muito alto!")
