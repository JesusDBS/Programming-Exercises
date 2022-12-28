# Fibonacci Sequence:
# Write a program that prints the first 50 numbers of the Fibonacci sequence starting at 0.
#   - The Fibonacci series consists of a succession of numbers in which the next number is always the sum of the previous two.
#   -0, 1, 1, 2, 3, 5, 8, 13...

def fib(num):
    iterator = iter(range(num + 1))
    while True:
        try:
            n = next(iterator)
            if n == 0:
                print(f'{n}: {n}')
                n_1 = n
                continue

            if n == 1:
                print(f'{n}: {n}')
                n_2 = n
                continue

            if n >= 2:
                n_current = n_1 + n_2
                print(f'{n}: {n_current}')
                n_1 = n_2
                n_2 = n_current

        except StopIteration:
            break


if __name__ == "__main__":
    fib(50)
