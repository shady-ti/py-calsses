a = 5   # 0101
b = 13  # 1101

potensial_result = a * b
potensial_result = a / b
potensial_result = a + b
potensial_result = a - b
potensial_result = a ** b
potensial_result = a ** (1 / b)

# bitwise-operators (https://en.wikipedia.org/wiki/Bitwise_operation)
potensial_result = a & b    # 0101      5
print(potensial_result)
potensial_result = a | b    # 1101      13
print(potensial_result)
potensial_result = a ^ b    # 1000      8
print(potensial_result)
potensial_result = ~a       # 1010      10, actually -6 because of 2s compliment
                            #           notation (https://en.wikipedia.org/wiki/Two%27s_complement)
print(potensial_result)

# right shift
potensial_result = b >> 2   # 0011
print(potensial_result)

# left shift
potensial_result = b << 2   # 110100
print(potensial_result)

# additional notes, uses of bitwise operators: https://suragch.medium.com/working-with-bytes-in-dart-6ece83455721

# complex number, use 'j' instead of 'i'
c = 3+3j

# decimal
d = 2.3