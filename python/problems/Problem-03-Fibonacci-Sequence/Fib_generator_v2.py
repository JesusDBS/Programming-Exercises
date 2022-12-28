# Fibonacci Sequence:
# Write a program that prints the first 50 numbers of the Fibonacci sequence starting at 0.
#   - The Fibonacci series consists of a succession of numbers in which the next number is always the sum of the previous two.
#   -0, 1, 1, 2, 3, 5, 8, 13...

def fib(num):
    for n in range(num + 1):
        if n == 0:
            n_1 = n
            yield n, n_1
            continue
        if n == 1:
            n_2 = n
            yield n, n_2
            continue
        if n >= 2:
            n_current = n_1 + n_2
            n_1 = n_2
            n_2 = n_current
            yield n, n_current


if __name__ == "__main__":

    for n in fib(50):
        print(f'{n[0]}: {n[1]}')
