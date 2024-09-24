def fibonacci_sequencia(n):
    sequencia = [0, 1]
    
    
    while True:
        proximoValor = sequencia[-1] + sequencia[-2]
        if proximoValor > n:
            break
        sequencia.append(proximoValor)
    
    return sequencia


numero = int(input("Informe um número: "))


fibonacci_sequencia = fibonacci_sequencia(numero)


if numero in fibonacci_sequencia:
    print(f"O número {numero} pertence à sequência de Fibonacci {fibonacci_sequencia}.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")