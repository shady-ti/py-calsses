sample_dict = {
    #   key : value,
    "bleh": "hello",
    2: "there",
    "general": 3,
    4: [1, 2, 3, 4, 5],
}

# print(sample_dict[4]) = print(sample_dict.get(4))

for x in sample_dict:
    print(x)

print("----------------------------------")

for x in sample_dict.keys():  # iterates over keys
    print(x)

print("----------------------------------")

for x in sample_dict.values():  # iterates over values
    print(x)

print("----------------------------------")

for k, v in sample_dict.items():  # iterates over tuple(key, value)
    print(k)
    print(v)

print("----------------------------------")

print(sample_dict.get("bleh"))

print("----------------------------------")

print(sample_dict)
x = sample_dict.pop("bleh")
print(x)
print(sample_dict)
