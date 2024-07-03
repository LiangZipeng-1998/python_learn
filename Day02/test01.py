'''
转义字符：
    t   字符 t        \t 水平字表符（类似四个空格）
    n   字符 n        \n 换行符
    \   字符反斜杠     \\
'''

print('She say: \'I love you\'')

# print输出函数，默认会自动换行
# print('hello', end='')  # end=空字符串
print('hello', end='\t')
print('world')  # end='\n' 默认为换行

# print 函数可以跟多个变量
num1 = 10
num2 = 20
print(num1, num2)

# print(f'')
print(f'num1 = {num1}, num2 = {num2}')

# .format() 填充参数
# 计算机只能识别 0 跟 1
print('num1 = {0}, num2 = {1}' .format(num1, num2))
