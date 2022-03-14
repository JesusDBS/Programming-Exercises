#Prime Number:
# Write a program to check whether a number is prime or not.
# Once this is done, print the prime numbers between 1 and 100.

def main():
    n = int(input("insert a number: "))

    assert n > 1, 'n must be a positive integer greater than 1'
    prime_number(n)

    for number in range (1,n):
        if prime_number(number):
            print(number)


def prime_number(n):
    if n > 1:
        for number in range(2,n):
            if n%number == 0:
                return False

        return True

    
if __name__ == "__main__":
    main()