def media(a, b, c):
    return (a + b + c) / 3

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media_aluno = media(nota1, nota2, nota3)
print(f"Média: {media_aluno:.2f}")

if media_aluno >= 7:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")
