#Fibonacci Sequence:
# Write a program that prints the first 50 numbers of the Fibonacci sequence starting at 0.
#   - The Fibonacci series consists of a succession of numbers in which the next number is always the sum of the previous two.
#   -0, 1, 1, 2, 3, 5, 8, 13...

#Exceptions
class NumberError(Exception):
    """Check if n is a positive integer.
    """
    def __init__(self, n, message="n must be a non zero positive integer"):
        self.n = n
        self.message = message

        super().__init__(self.message)

    def __str__(self):
        return f"{self.n}! --> {self.message}"


#main program
def main():
    n = int(input("insert a number: "))

    if n <= 0:
        raise NumberError(n)
        
    print(fibonacci_sequence(n))


#Defining fibonacci sequence function
def fibonacci_sequence(n):
    sequence = []

    if n == 1:
        sequence.append(0)
        return sequence
    
    else:
        for num in range(0,n):
            if num < 2:
                sequence.append(num)

            else:
                num = sequence[-2] + sequence[-1]
                sequence.append(num)
    
    return sequence


if __name__ == "__main__":
    main()

 