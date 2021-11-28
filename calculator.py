from os import system


def converterDecimalParaBinario(decimal, tipo):
    resultado = ""
    num_max = tipo - 2  # número máximo de bits que a parte decimal convertida em binário pode ter

    while num_max:
        decimal = str(decimal * 2)
        primeiro_digito = decimal[0:1]
        decimal = float(decimal)

        if primeiro_digito == "1":
            decimal = decimal - 1

        resultado += primeiro_digito
        num_max -= 1

    return resultado


# Escolha do tipo de precisão
while (True):
    try:
        escolha = float(
            input(
                "Escolha uma opção:\n\n1) Notação de Ponto Flutuante (8 bits)\n2) Precisão de Ponto Flutuante IEEE754 32 bits\n3) Precisão de Ponto Flutuante IEEE754 64 bits\n\n-> "
            ))
    except:
        system('cls')
        print("Tente novamente\n")

    if escolha == 1 or escolha == 2 or escolha == 3:
        break

    system('cls')
    print("Tente novamente\n")

if (escolha == 1):
    tipo = 8
elif (escolha == 2):
    tipo = 32
elif (escolha == 3):
    tipo = 64

# Inserção do número a ser convertido
try:
    numero = float(input("\nDigite um número decimal:\n-> "))
except:
    print("Digite um número válido\n")

if numero >= 0:  # salva o sinal do número
    sinal = "0"
else:
    sinal = "1"

numero = abs(
    numero
)  # transforma o número inserido em positivo para realizar os cálculos

# Passo 1: Tranformar as partes inteira e decimal em binário
inteiro = str(numero).split(".")[0]
decimal = float('0' + str(numero)[str(numero).index('.'):])
inteiro_binario = bin(int(inteiro)).lstrip("0b")
decimal_binario = converterDecimalParaBinario(decimal, tipo)

# Passo 2: Encontrar as devidas partes da representação (Sinal, Expoente e Mantissa)
print("\nSinal:", sinal)

qtd_algarismo_significativo = 1  # número de algarismos significativos da notação científica

if numero >= 1:
    expoente = len(inteiro_binario) - qtd_algarismo_significativo  # 8
elif numero < 1 and numero > 0:
    qtd_zeros_a_direita = -1

    for letter in str(decimal):
        if letter == '0':
            qtd_zeros_a_direita += 1

    expoente = qtd_zeros_a_direita + 1

if tipo == 32:
    bias = 127
elif tipo == 64:
    bias = 1023

if numero >= 1:
    expoente_binario = bin(bias + expoente).lstrip("0b")
elif numero < 1 and numero > 0:
    expoente_binario = bin(bias - expoente).lstrip("0b")

while len(str(expoente_binario)) < 8:
    expoente_binario = '0' + expoente_binario

print("Expoente:", expoente_binario)

if numero >= 1:
    mantissa = inteiro_binario[1:] + decimal_binario
elif numero < 1 and numero > 0:
    mantissa = decimal_binario[expoente:]

if tipo == 32:
    mantissa_aproximada = mantissa[0:23]
elif tipo == 64:
    mantissa_aproximada = mantissa[0:52]
print("Mantissa:", mantissa_aproximada)

# Passo 3: Juntar todas as partes
resultado_binario = sinal + expoente_binario + mantissa_aproximada
print("\nResultado em binário:", resultado_binario)

# Passo 4: Converter para hexadecimal
resultado_hexadecimal = hex(int(resultado_binario, 2))
print("\nResultado em hexadecimal:", resultado_hexadecimal, "\n")

# To Do List:
# - Implementar conversão para ponto fixo
# - Implementar restrições de valores inseridos para cada caso de conversão (ponto fixo 8 bits, ponto flutuante 32 e 64)
# - Descobrir por que a parte decimal adquire uns números nas casas mais à direita (não aparenta ser muito significante)