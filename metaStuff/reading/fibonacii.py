print('press enter for next number in the fibonacci series/enter "quit" to exit:')

num1 = 0
num2 = 1

if input().lower() != "quit":
    print(f"{0:>5}th term: {num1}")

if input().lower() != "quit":
    print(f"{1:>5}th term: {num2}")

x = 2

while input().lower() != "quit":
    temp_num = num1
    num1 = num2
    num2 = temp_num + num1

    print(f"{x:>5}th term: {num2}")
    x += 1
