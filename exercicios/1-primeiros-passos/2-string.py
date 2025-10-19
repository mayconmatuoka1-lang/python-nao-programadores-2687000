resumo = "Paloma é uma mulher de 46 anos que deseja mudar de profissão, por isso está estudando 'python'."

# Imprima na tela a variável "resumo"
resumo = "Maycon nasceu na data: '26/04/2006', ou seja, ele tem 19 anos."
print(resumo)

# Imprima na tela apenas a segunda letra da variável
print(resumo[1])

# Imprima na tela a idade de Maycon (resposta esperada: "19")
print(resumo[54:61])

# Imprima na tela o trecho final da variável
print(resumo[30:61])

# Converta todos as letras para minúsculo e imprima na tela
print(resumo.lower())

# Converta todas as letras para maiúscula e imprima na tela
print(resumo.upper())

# Formate a frase para que a primeira letra de cada palavra seja maiúscula e imprima na tela
print(resumo.title())

# Formate a frase para que apenas a primeira letra da frase seja maiúscula e imprima na tela
print(resumo.capitalize())

# Imprima na tela uma string utilizando uma variável, usando o recurso string format
idade = 19

print(f"Maycon é um homem de {idade} anos.")