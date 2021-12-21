# capitalize first letter or each string

test_str = "helLo thEre. i'm A stAr wars fAn. i eXPect you tO s.a.y 'gNERal kenobi' when i say hello there."

# print(test_str.upper())
# print(test_str.lower())
# print(test_str.capitalize())
# print(test_str.split(' '))
# print(test_str.split('t'))
# print('<->'.join(['12', '15', '23']))
# print(test_str.find('test'))
# print(test_str[0:6])
# print(test_str[5:])
# print(test_str[:6])
# print(test_str.replace('t', '.@#!'))

#convert to lowercase
new_test_str = test_str.lower()
print(new_test_str)
#split each sentence using ". "
strings_list=new_test_str.split('. ')
print(strings_list)
#capatilize each sentence oh the list
#concatenate all the strings
final_string=""
for s in strings_list:
    y=s.capitalize()
    final_string +=  y+". "
print(final_string)






# =======================================
# === print the first m prime numbers ===
# =======================================
 
# 1. write out yout process steps with indentation
# 2. write code for each segment and run it repeatedly

#introduce number,divisor,remainder,m
number = 2
m = 69
prime_count = 0

while prime_count != m:
    is_prime = True
    for divisor in range (2,number):
        remainder = number%divisor 
        if remainder == 0:
            is_prime = False
            break

    if is_prime:
        prime_count += 1
        print(number)

    number+=1

# setup variables
prime_count = 0
m = 999

num = 1

while prime_count != m:
    # increment num starting at 2
    num += 1
    
    is_composite = False
    
    # increment div from 2 upto num - 1 for each num
    for div in range(2, int(num/2) + 1):
        # check if num non divisible for for each div
        if num % div == 0:
            is_composite = True
            break
    
    # if yes -> print num move to next num, increment prime_count untill prime_count == m
    if not is_composite:
        print(num)
        prime_count += 1
#while number < m 
#check remainder for divisor < number
#if remiander never 0 number is prime print number increment number



