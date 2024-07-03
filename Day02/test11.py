'''
    逗号表达式
'''

# num1 = 10
# num2 = 20
# num3 = 30

# 说明：在编程中，规则大于语法。
num1, num2, num3 = 10, 20, 30

# ValueError: too many values to unpack (expected 3)  太多的值参与了解包过程
# num1, num2, num3 = (10, 20, 30, 40)

# 原理：元祖解包
print(f'num1={num1}, num2={num2}, num3={num3}')
