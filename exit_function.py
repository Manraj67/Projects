# 1) Create a for loop using `range(10)`:

# 2) Inside loop, check condition:
#    a) If `i == 5`.

# 3) Inside the condition:
#    a) Print `exit`.
#    b) Use `exit()` to terminate the program immediately.

# 4) Outside the condition but inside loop:
#    a) Print the current value of `i`.

# 5) The program should stop completely once `i` becomes 5.
for i in range(10):
    if i==5:
        print("exit")
        exit()
    print(i)