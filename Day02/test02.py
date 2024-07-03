'''
字符串，整形，浮点型之间的类型转换：
格式：
    1、整形    int(变量)
    2、浮点型   float(变量)
    3、字符串类型 str(变量)
'''

# 字符串类型
num1 = '10'
num2 = '20'

# 思考：字符串 + 字符串 = ???  result = 1020     两个字符串相加，其结果就是字符串的相拼接
# 网页中的输入框：input 标签（网页中的输入框获取的数据，都是字符串类型的。）
result = num1 + num2
print(f'type(num1) = {type(num1)}, type(num2) = {type(num2)}')
print(f'result = {result}')

# 需求：将字符串类型转换为整形
n1 = int(num1)
n2 = int(num2)

# 思考：int + int 就是数学运算。
result = n1 + n2
print(f'type(n1) = {type(n1)}, type(n2) = {type(n2)}')
print(f'result = {result}')  # 30

# int(str + str)   int(1020)
result = int(num1 + num2)  # 这样可以吗？ result = 1020
print(f'result = {result}')

# float 浮点型
f1 = 66.66
f2 = 88.88
result = f1 + f2
print(f'result = {result}')  # 155.54

# 浮点型转换为整形是直接丢弃掉小数部分。（精度丢失）
i1 = int(f1)
i2 = int(f2)
result = i1 + i2
print(f'result = {result}')  # 66 + 88 = 154

# int -> float
n3 = 10
n4 = 20

f3 = float(n3)
f4 = float(n4)
result = f3 + f4
print(f'result = {result}')  # 30.0

# int + float => float      只要有浮点数参与运算，其结果就是浮点型。
n = 10
f = 6.66
result = n + f
print(f'result = {result}') # 16.6
