# define a list
drinks = ['coca-cola', 'pepsi', 'nestle', 'red-bull', 'bacardi', 'heineken']
print("drinks type %s"%type(drinks))   # drinks type <class 'int'>
print(drinks)  # ['coca-cola', 'pepsi', 'nestle', 'red-bull', 'bacardi', 'heineken']
print(drinks[1])  # pepsi

for item in drinks:
    print(item)

del drinks[-1]          # delete element on index
print(drinks)  # ['coca-cola', 'pepsi', 'nestle', 'red-bull', 'bacardi']
print(drinks[-0])  # coca-cola   same as drinks[0]

print(len(drinks))  # 5
t_len = len(drinks)
print(type(t_len))  # <class 'int'>

e_num = 0
while e_num < t_len:
    print("drinks[", e_num, "]", drinks[e_num])
    # but better
    #print("drinks[%d]: %s" % (e_num, drinks[e_num]))
    # note no space inbetween brackets
    e_num += 1
