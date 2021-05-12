import numpy as np
#重复给定的字符串数组的所有元素三次。
a=np.array(['spam','egg','bacon'])
a=list(a)
a[0]=3*a[0]
a[1]=3*a[1]
a[2]=3*a[2]
a=np.array(a)
print(a)
#删除一个给定数组中所有元素的前导空格和后导空格。
b=[' spam ',' egg  ','   bacon']
b[0]=b[0].strip(' ')
b[1]=b[1].strip(' ')
b[2]=b[2].strip(' ')
print(b)
#将以下给定数组元素中的 "PHP "替换为 "Python"
L=['PHP Exercises', 'Practice', 'Solution']
for i in range(0,len(L)):
    Z=L[i].replace("PHP","Python")
    L[i]=Z
print(L)

