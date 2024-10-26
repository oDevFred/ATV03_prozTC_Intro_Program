# Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.

# Escreva um código que imprima todos os números exceto o número 13.
# Escreva mais dois códigos que resolvam o mesmo problema, mas dessa vez usando os outros dois tipos de laços de repetição aprendidos.

# Como desafio, imprima eles em ordem decrescente (20, 19, 18...)

# Fazendo contar de 1 a 20
for i in range(1, 21):
    # Se i for 13
    if i == 13:
        # Pule o número e continue o código
        continue;
    print(i);

# Definindo variável
andar = 1;

# Enquanto andar for menor ou igual a 20
while andar <= 20:
    # Se o nosso andar for o 13
    if andar == 13:
        # Adicione mais um andar
        andar += 1;
        # Pule ele e continue o código
        continue;
    # Informe o andar
    print(andar);
    # Adiciona mais 1 andar
    andar += 1;

# Fazendo em ordem decrescente
# O -1 indica no range que você quer ir em ordem decrescente
for i in range(20, 0, -1):
    # Se i for 13
    if i == 13:
        # Pule e continue o código
        continue;
    print(i);