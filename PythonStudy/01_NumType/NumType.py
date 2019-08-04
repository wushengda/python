# 普通输出
print("Hello World")

# 输入输出
# x = input("Please input x:")
# print(x)

# 输出数组
arr = [1, 2, 'c', "String"]
print(arr)

# 输出List
list = {'a': 1, 'b': 2, 'c': ['b', 'b']}

# 格式化输出
s = "Hello"
x = len(s)
print("The length of %s is %d" % (s, x))

pi = 3.141592653
print("%10.3f" % pi) #字段宽10,精度3
print("pi = %.*f" % (10, pi))  # 用*从后面的元组中读取字段宽度或精度
print("pi = %.*f" % (3, pi))  # 用*从后面的元组中读取字段宽度或精度
print("%010.3f" % pi) #用0填充空白
print("%-10.3f" % pi) #左对齐
print('%+f' % pi) #显示正负号

# print不换行
for x in range(1,11):
    print(x, end="")
print()

for x in range(1,100):
    print(x, end="")
print()

# 拼接字符串
front = "Hello"
back = "Word"
print(front + " " + back)

