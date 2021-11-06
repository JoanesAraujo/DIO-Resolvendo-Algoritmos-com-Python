# QUESTÃO
# A seguinte sequência de números 0 1 1 2 3 5 8 13 21... é conhecida como
# série de Fibonacci. Nessa sequência, cada número, depois dos 2 primeiros,
# é igual à soma dos 2 anteriores. Escreva um algoritmo que leia um inteiro
# N (N < 46) e mostre os N primeiros números dessa série.
#
# ENTRADA
# O arquivo de entrada contém um valor inteiro N (0 < N < 46).
# SAÍDA
# Os valores devem ser mostrados na mesma linha, separados por um espaço
# em branco. Não deve haver espaço após o último valor.

n = int(input())
fib_list = []
#n = n - 1
for i in range(n):
  if i == 0 or i == 1:
    fib_list.append(i)
  if i > 1:
    aux = fib_list[i-2] + fib_list[i-1]
    fib_list.append(aux)
i = i + 1
for j in range(0, n):
    fib_list[j] =str(fib_list[j])

fib_string = ' '.join(fib_list)
print(fib_string)