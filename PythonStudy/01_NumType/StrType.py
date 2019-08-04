str = "AbcdeFGhijKlmNopQrst";

# python 可以取负值，表示从末尾提取，最后一个为 -1，倒数第二个为 -2，即程序认为可以从结束处反向计数。
print('str[0].__add__(str[-2]) '
      '' + str[0].__add__(str[-2])) # As
print('str[0:] ' + str[0:]);
print('str[str.find("K"):] ' + str[str.find("K"):]);
print('str[str.find("K"):str.find("A")] ' + str[str.find("K"):str.find("A")]);
print('str[0:1] ' + str[0:1]);
print('str[0:str.__len__():1] ' + str[0:str.__len__():2]);

# count()方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。
print('str.count(str) ' + str.count(str).__str__());
print('str.count("A") ' + str.count("A").__str__());

print('str.__len__() ' + str.__len__().__str__())

print('"ssss".__len__() ' + "ssss".__len__().__str__())

# __add__相当于拼接字符串
print(str.__add__(" Hello World"))

# __str__()相当于toString()
print(str.__str__())

# 转成小写
str = str.lower();
print(str)

# 转成大写
str = str.upper();
print(str)

# 首字母大写，后面的全小写
str = str.capitalize();
print(str)

# 查找,找打了会返回索引，没找到返回-1
v = str.find("A");
print(v);

# 找打了返回索引，没找到报错
v = str.index("A");
print(v);
# v = str.index("xx");
# print(v);

