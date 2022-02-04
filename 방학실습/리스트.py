a = [1,2,3]
b = ['Life', 'is', 'too', 'short']
c = [1,2,'Life','is']
d = [1,2,[3,4],['Life','is']]

d[0]    # 1
d[2]    # [3,4]
d[3]    # ['Life','is']
d[3][-1]    # 'is' 
d[0:3]  # [1,2,[3,4]]

a+b # [1,2,3,'Life','is','too','short']
b[0] + " hi~ ^_^;"  # 'Life hi~ ^_^;'
a[0] + " hi~ ^_^;"  # 에러

a * 3   # [1,2,3,1,2,3,1,2,3]
a[2]    # 99
a   # [1,2,99]

a[1:2] = ['a','b','c']
a   # [1,'a','b','c',99]


