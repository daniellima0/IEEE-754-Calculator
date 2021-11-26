numero = input("Digite um número decimal: ") # supondo número 10.20

print("Número digitado: ", numero)

# Passo 1: Tranformar as partes à esquerda vírgula (parte inteira) e à direita da vírgula (parte decimal) em binário
partes_do_numero = numero.split('.') # array [10, 20]

[inteiro, decimal] = [partes_do_numero[0], partes_do_numero[1]]

print("Parte inteira: ", inteiro)
print("Parte decimal: ", decimal)

[inteiro_binario, decimal_binario] = [bin(int(inteiro)), bin(int(decimal))]

print("Parte inteira em binário: ", inteiro_binario)
print("Parte decimal em binário: ", decimal_binario)