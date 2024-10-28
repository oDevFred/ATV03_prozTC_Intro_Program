# Impressão de Números dos Andares de um Hotel (Excluindo o 13º Andar)

Este projeto foi desenvolvido como parte do curso de Introdução à Programação oferecido pela Proz em parceria com a AWS no programa Talento Cloud. O objetivo é imprimir o número de cada andar de um hotel com 20 andares, mas sem o supersticioso 13º andar. Esse exercício reforça o uso de laços de repetição e controle de fluxo em Python.

## Funcionalidade do Programa

O código realiza a contagem de andares de um hotel, imprimindo todos os números de 1 a 20, exceto o 13. Para isso, o código usa três abordagens, uma para cada estrutura de repetição em Python:

1. **Laço `for` em ordem crescente:** Imprime do 1º ao 20º andar, excluindo o 13º.
2. **Laço `while` em ordem crescente:** Realiza a mesma tarefa, mas usando um laço `while`.
3. **Laço `for` em ordem decrescente:** Imprime os andares de 20 a 1, excluindo o 13º.

### Descrição dos Códigos

1. **Laço `for` Crescente**
   - Utiliza `for` com `range(1, 21)`.
   - A condição `if i == 13` usa `continue` para pular o 13º andar.

2. **Laço `while` Crescente**
   - Define uma variável `andar = 1` e executa enquanto `andar <= 20`.
   - A condição `if andar == 13` usa `continue` para pular o 13º andar.

3. **Laço `for` Decrescente**
   - Utiliza `for` com `range(20, 0, -1)` para contagem decrescente.
   - A condição `if i == 13` usa `continue` para pular o 13º andar.

## Exemplo de Saída

### Laço `for` Crescente e `while` Crescente
```plaintext
1
2
3
...
12
14
15
...
20
```

### Laço `for` Decrescente
```plaintext
20
19
18
...
14
12
11
...
1
```

## Tecnologias e Conceitos Utilizados

- **Python**: Linguagem de programação.
- **Estruturas de Repetição**: `for` e `while`.
- **Controle de Fluxo**: `continue` para pular valores específicos.

## Autor

Caio Frederico, como parte do curso Talento Cloud da Proz e AWS.
