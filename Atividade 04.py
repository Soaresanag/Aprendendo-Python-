nota = float(input("Digite uma nota de 0 a 10: "))

if nota < 5:
    print("Reprovado")
elif 5 <= nota <= 6.9:
    print("Recuperação")
else:
    print("Aprovado")
