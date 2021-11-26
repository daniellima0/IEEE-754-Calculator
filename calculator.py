def converterDecimalParaBinario(decimal):
    resultado = ""
    num_max = 32 - 2    # número máximo de bits que a parte decimal convertida em binário pode ter 

    while num_max:
        decimal = str(decimal * 2)
        primeiro_digito = decimal[0:1]
        decimal = float(decimal)

        if primeiro_digito == "1":
            decimal = decimal - 1

        resultado += primeiro_digito
        num_max -= 1

    return resultado

tipo = 32  # 32 bits
numero = input("Digite um número decimal: ")  # supondo número 263.3

# salva o sinal do número
if float(numero) >= 0:
    sinal = "0"
else:
    sinal = "1"

# transforma o número inserido em positivo para realizar os cálculos
numero = abs(float(numero))

# Passo 1: Tranformar as partes inteira e decimal em binário
inteiro = str(numero).split(".")[0]  # 263
decimal = numero - int(inteiro)  # 0.3

print("\nParte inteira:", inteiro)
print("Parte decimal:", decimal)

inteiro_binario = bin(int(inteiro)).lstrip("0b")  # 100000111
decimal_binario = converterDecimalParaBinario(
    decimal)  # 01001100110011001100110

print("\nParte inteira em binário:", inteiro_binario)
print("Parte decimal em binário:", decimal_binario)

# Passo 2: Encontrar as devidas partes da representação (Sinal, Expoente e Mantissa)
print("\nSinal:", sinal)

qtd_algarismo_significativo = 1  # número de algarismos significativos da notação científica
comprimento_expoente = len(inteiro_binario) - qtd_algarismo_significativo  # 8
bias = 127
expoente = bin(127 + comprimento_expoente).lstrip("0b") # 10000111
print("Expoente:", expoente)

mantissa = inteiro_binario[1:] + decimal_binario    # 00000111010011001100110011001100110011
mantissa_aproximada = mantissa[0:23]    # 00000111010011001100110
print("Mantissa:", mantissa_aproximada)

# Passo 3: Juntar todas as partes
numero_convertido = sinal + expoente + mantissa_aproximada  # 01000011100000111010011001100110
print("\nResultado:", numero_convertido, "\n")

# To Do List:
# - Descobrir por que a parte decimal adquire uns números nas casas mais à direita
# - Converter resultado em binário para hexadecimal
# - Criar uma versão para 64 bits
