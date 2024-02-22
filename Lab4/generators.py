#TASK 1
def squares(N):
    for i in range(1, N + 1):
        yield i ** 2

N = 5
s_generator = squares(N)

for square in s_generator:
    print(square)

#TASK 2
def even(N):
    for i in range(N + 1):
        if i % 2 == 0:
            yield i

def main():
    try:
        n = int(input())
        print(end=" ")
        for number in even(n):
            print(number, end=", ")
    except ValueError:
        print("Error")

if __name__ == "__main__":
    main()
#TASK 3
def d3_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

def main():
    try:
        n = int(input("Enter a number: "))
        if n < 0:
            print("Please enter a positive number.")
            return
        print("Numbers divisible by both 3 and 4 between 0 and", n, ":", end=" ")
        gen = d3_4(n)
        print(*gen, sep=", ")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
#TASK 4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

def main():
    try:
        a = int(input("Enter the starting number: "))
        b = int(input("Enter the ending number: "))
        
        print("Squares of numbers from", a, "to", b, ":")
        for square in squares(a, b):
            print(square)
    except ValueError:
        print("Please enter valid integers for the range.")

if __name__ == "__main__":
    main()
#TASK 5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

def main():
    try:
        n = int(input("Enter a number to start countdown from: "))
        if n < 0:
            print("Please enter a non-negative number.")
            return
        
        print("Countdown from", n, "to 0:")
        for num in countdown(n):
            print(num)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
