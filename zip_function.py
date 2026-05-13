# ============================================================
# PROGRAM 1: ZIP ELEMENTS OF TWO SETS
# ============================================================

# 1) Create first set named `s1`:
#    a) Store values: 2, 3, 1

# 2) Create second set named `s2`:
#    a) Store values: 'b', 'a', 'c'

# 3) Use `zip(s1, s2)`:
#    a) Pair elements of both sets together.

# 4) Convert zip object into list using `list()`:
#    a) Store result in variable `s3`.

# 5) Print `s3`.

# ============================================================
# PROGRAM 2: ZIP TWO LISTS IN REVERSE ORDER
# ============================================================

# 1) Create list named `list1`:
#    a) Store values: 10, 20, 30, 40

# 2) Create second list named `list2`:
#    a) Store values: 100, 200, 300, 400

# 3) Use `list2[::-1]`:
#    a) Reverse the second list.

# 4) Use `zip(list1, list2[::-1])`:
#    a) Pair first list with reversed second list.

# 5) Use for loop:
#    a) Store first value in variable `x`.
#    b) Store second value in variable `y`.

# 6) Print `x` and `y`.

# ============================================================
# PROGRAM 3: CREATE DICTIONARY USING ZIP
# ============================================================

# 1) Create list named `stocks`:
#    a) Store values:
#       'reliance', 'infosys', 'tcs'

# 2) Create list named `prices`:
#    a) Store values:
#       2175, 1127, 2750

# 3) Use `zip(stocks, prices)`:
#    a) Pair each stock with its price.

# 4) Use dictionary comprehension:
#    a) Store stock name in variable `stocks`.
#    b) Store price in variable `prices`.

# 5) Create dictionary named `new_dict`.

# 6) Print `new_dict`.
s1 ={2, 3, 1}
s2 ={'b', 'a', 'c'}
s3 =list(zip(s1, s2))
print(s3)
list1 =[10, 20, 30, 40]
list2 =[100, 200, 300, 400]
a = list2[::-1]
b = list(zip(list1, list2[::-1]))
for i,j in zip(list1, list2[::-1]):
    print(i, j)
stocks =['reliance', 'infosys', 'tcs']
prices = [2175, 1127, 2750]
new_dict = {stocks: prices for stocks,prices in zip(stocks, prices)}
print('\n{}'.format(new_dict))