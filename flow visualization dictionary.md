<!-- mdformat-toc start --slug=github --no-anchors --maxlevel=6 --minlevel=1 -->

- [The rules](#the-rules)
- [Simple Stuff](#simple-stuff)
- [Comparatively complex stuff](#comparatively-complex-stuff)

<!-- mdformat-toc end -->

# The rules

1. You can't use text other than that provided in the question

2. You can't use operator symbols (eg. `[]`, `%=`, `+`, `==`, etc...) unless representing
   mathematical operations on numbers

3. your diagram should represent the action/process/flow of the given question, not the initial
   and/or final states. It should be the most generalized possible representation.

# Simple Stuff

01. ```python
    x = 12
    ```

02. ```python
    "Hello there"
    ```

03. ```python
    [1, 2, 3, "a", "b", "c"]
    ```


04. ```python
    (1, 2, 3)
    ```


05. ```python
    "tHe DaRk KnIgHt".lower()
    ```


06. ```python
    12 + 3j
    ```


07. ```python
    "tHe DaRk KnIgHt".capitalize()
    ```


08. ```python
    {"a": 1, "b": 2, "c": 3}.items()
    ```


09. ```python
    {"a": 1, "b": 2, "c": 3}
    ```


10. ```python
    some_list[3] = "new value"
    ```


11. ```python
    "tHe DaRk KnIgHt".title()
    ```


12. ```python
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ```


13. ```python
    {"a": 1, "b": 2, "c": 3}.keys()
    ```


14. ```python
    ~13
    ```


15. ```python
    15 << 3
    ```


16. ```python
    12 | 5
    ```


17. ```python
    set([1, 2, 3, 4, 2, 2])
    ```


18. ```python
    "tHe DaRk KnIgHt"[2:-2]
    ```


19. ```python
    [1, 2, 3, 4, 5][3]
    ```


20. ```python
    x %= 2
    ```


21. ```python
    {"a": 1, "b": 2, "c": 3}.values()
    ```


22. ```python
    "tHe DaRk KnIgHt".split(" ")
    ```


23. ```python
    {"a": 1, "b": 2, "c": 3}["b"]
    ```


24. ```python
    y = [1, 2, 3].copy()
    ```


25. ```python
    [1, 2, 3, 4, 5, 6][2:-2]
    ```


26. ```python
    a, b, c, d = (1, 2, 3, 4)
    ```


27. ```python
    (1, 2, 3, 4, 5)[1:-1]
    ```


28. ```python
    [1, 2, 3, 4, 5].insert(3, 0)
    ```


29. ```python
    "tHe DaRk KnIgHt".replace(" ", "-")
    ```


30. ```python
    x = 12
    f"{x} is even"
    ```


# Comparatively complex stuff

01. ```python
    if x % 2 == 0:
        print("x is even")
    ```

    ![](imgs/placeholder.jpg)

02. ```python
    for value in [1, 3, 5, 7, 11]:
        print(f"{value} is prime")
    ```

    ![](imgs/placeholder.jpg)

03. ```python
    [i for i in [1, 2, 3, 4]]
    ```

    ![](imgs/placeholder.jpg)

04. ```python
    for n in range(10):
        print(2 ** n)
    ```

    ![](imgs/placeholder.jpg)

05. ```python
    [i for i in range(5)]
    ```

    ![](imgs/placeholder.jpg)

06. ```python
    if x > 0:
        print("value is positive")
    elif x < 0:
        print("value is negative")
    elif x == 0:
        print("value is neutral")
    else:
        print("value is an alien shaolin monk who knows magic and wants Stan Lee's autograph")
    ```

    BONUS QN: why not check if `x` is negative before x is positive? or if `x` is zero first? why
    that specific order?

    ![](imgs/placeholder.jpg)

07. ```python
    while x < 10:
        print(2 ** x)
        x += 1
    ```

    ![](imgs/placeholder.jpg)

08. ```python
    [2 ** i for i in range(5)]
    ```

    ![](imgs/placeholder.jpg)

09. ```python
    for i in range(5):
        print([i * n for n in range(5)])
    ```

    ![](imgs/placeholder.jpg)

10. ```python
    for i in range(5):
        for value in [i * n for n in range(5)]:
            print(value)
    ```

    ![](imgs/placeholder.jpg)

11. ```python
    for x in range(10):
        print(2 ** x)
    ```

    ![](imgs/placeholder.jpg)

12. ```python
    for value in [i * n for i in range(5) for n in range(5)]:
        print(value)
    ```

    ![](imgs/placeholder.jpg)

13. ```python
    matrix = []

    for i in range(3):
        row = []
        for n in range(3):
            row.append(i * n)

        matrix.append(row)
    ```

    ![](imgs/placeholder.jpg)

14. ```python
    matrix = [[i * n for n in range(3)] for i in range(3)]
    ```

    NOTE: pay attention to the order, then have a look qt QN.13 when done

    ![](imgs/placeholder.jpg)

15. ```python
    for x in range(5):
        for n in range(5):
            print(x * n)
    ```

    ![](imgs/placeholder.jpg)

16. ```python
    for x in range(5):
        for n in range(x):
            print(x * n)
    ```

    ![](imgs/placeholder.jpg)

17. ```python
    for value in number_list:
        if value % 5 == 2:
            break

    print("a 5n+2 value exists")
    ```

    ![](imgs/placeholder.jpg)

18. ```python
    for value in number_list:
        if value % 2 == 0:
            continue

        print("value is odd")
    ```

    ![](imgs/placeholder.jpg)

19. ```python
    for value in [1, 2, 3, 4, 5, 6]:
        do_something(value)
    ```

    ![](imgs/placeholder.jpg)

20. ```python
    primeFlag = False

    for value in number_list:
        if is_prime(value):
            primeFlag = True
            break
    ```

    ![](imgs/placeholder.jpg)

21. ```python
    if x % 2 == 0:
        print("x is even")

    if x % 5 == 2:
        print("x is 5n+2 for some n ∈ N")
    else:
        print("x is of no concern to us")
    ```

    ![](imgs/placeholder.jpg)

22. ```python
    while True:
        if break_condon(some_value):
            break

        do_some_stuff(some_other_value)

        checked_value_count += 1
    ```

    ![](imgs/placeholder.jpg)

23. ```python
    sin(x)
    ```

    ![](imgs/placeholder.jpg)

24. ```python
    sin(cos(x))
    ```

    ![](imgs/placeholder.jpg)

25. ```python
    calc_dct([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
    ```

    ![](imgs/placeholder.jpg)

26. ```python
    dct_value = calc_dct([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
    compress(dct_value)
    ```

    ![](imgs/placeholder.jpg)

27. ```python
    compress(calc_dct([[1, 2, 3], [2, 3, 4], [3, 4, 5]]))
    ```

    ![](imgs/placeholder.jpg)

28. ```python
    auto_gen_fn = a_function_that_returns_another_function(x)
    auto_gen_fn(return_fn_value)
    ```

    ![](imgs/placeholder.jpg)

29. ```python
    a_function_that_returns_another_function(x)(return_fn_value)
    ```

    ![](imgs/placeholder.jpg)
