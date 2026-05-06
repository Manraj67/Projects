test_dict = {"Codingal" : 2, "is" : 2, "best" : 2, "for" : 2, "Coding" : 1}
print("The original dictionary : " , (test_dict))
K = 2
res = 0
for i in test_dict:
    if test_dict[i] == K:
        res = res + 1
print("Frequency of K is : " + str(res))