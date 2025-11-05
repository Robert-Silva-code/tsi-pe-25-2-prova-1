# Programação Estruturada: Prova 01

## Instruções

### Execução manual

Para executar o seu programa: Altere o código no arquivo main com a sua solução e execute no terminal o comando a seguir:

```sh
python main.py
```

### Teste com pytest

Para testar o seu programa com pytest: Altere o código no arquivo main com a sua solução e execute no terminal o comando a seguir:

```sh
pytest
```

Ao concluir, salve e envie com os comandos a seguir:
```sh
git add .
git commit -m "resolução"
git push
```

## Questão Exemplo:

Faça um programa para imprimir os numeros pares maiores que 0 até o número máximo digitado pelo usuário

### Entrada

- n

### Saída

- n1, n2, n3

### Exemplo 1

Entrada: 

- 10

Saída: 

- 2, 4, 6, 8, 10

## Questão 1:

Faça um programa que leia 3 números inteiros e os imprima em ordem crescente.

### Formato de entrada

O usuário deve digitar 03 números inteiros sequencialmente.

### Formato de saída

O programa deve exibir os 03 números lidos impressos em ordem crescente, cada um em uma linha

### Exemplo 1:

Entrada:

- 555
  
- 777
  
- 666

Saída:

- 555
  
- 666
  
- 777

## Questão 2:

A Locadora de Veículos Eudora lançou uma grande promoção esse mês: pagando apenas R$ 90 por diária, o cliente pode alugar um carro de passeio. Para cada diária, o cliente recebe uma cota de quilometragem de 100 Km. Cada quilômetro a mais custará uma taxa extra de R$ 12.

Escreva um programa que receba como entrada a quantidade de dias e a quilometragem total rodada por um cliente dessa locadora e exiba o valor total a ser pago com duas casas decimais

### Formato de entrada

Dois valores inteiros, separados por uma quebra de linha

### Formato de saída

Um valor real com duas casas decimais

### Exemplo 1:

Entrada:

- 1

- 80

Saída:

- 90.00

## Questão 3:

Zelda e seus amigos tiveram uma brilhante ideia durante as aulas da monitoria da cadeira de introdução a programação: que tal fazer um programa que, dado um número n (1 <= n <= 40) printa na tela os numeros de 1 até o número da iteração atual, sendo que serão feitas n iterações, como demonstrado no exemplo a seguir:

Supondo para n = 5:

(primeira iteração):   1

(segunda iteração):    1 2

(terceira iteração):   1 2 3

(quarta iteração):     1 2 3 4

(quinta iteração):     1 2 3 4 5

### Formato de entrada

Um inteiro n (1 <= n <= 40)

### Formato de saída

A sequência (1 ... M), onde M é o numero da iteração atual do laço, que será executada n vezes.


### Exemplo 1:

Entrada:

- 10

Saída:

1

1 2

1 2 3

1 2 3 4

1 2 3 4 5

1 2 3 4 5 6

1 2 3 4 5 6 7

1 2 3 4 5 6 7 8

1 2 3 4 5 6 7 8 9

1 2 3 4 5 6 7 8 9 10


## Questão 4

Um professor precisa saber qual a média das notas de uma sala e pediu sua ajuda para construir um programa que permita inserir as notas finais de cada aluno e, ao final, exibir a média da sala. Lembre-se que as notas variam de 0 a 10 e o professor digitará -1 quando quiser encerrar as entradas. Obs.: use variáveis de ponto flutuante de dupla precisão.

### Entrada

Diversos valores reais, um por linha, simbolizando as notas finais de cada aluno.

### Saída

Um número real, com duas casas decimais, simbolizando a média das notas da sala.


### Exemplo

#### Entrada

10.00

-1

#### Saída

10.00

#### Entrada

10.00

7.00

5.00

-1

#### Saída

7.33
