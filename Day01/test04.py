'''
    Python 中有哪些数据类型？
    格式：
        变量名 = 变量值

    查看变量的类型：type(变量名)
'''

# 1、整形数据 int（integer）
num1 = 999
# print(f'num1 = {num1}')  输出的固定格式。f -> format 格式化，特点就是在单引号字符串中能够书写 {}，大括号中可以放入‘变量名’。
print(f'num1 = {num1}, type(num1) = {type(num1)}')  # 格式化的输出
print(num1)     # 直接输出变量值
print(type(num1))

# 2、浮点型（小数）float
num2 = 66.6     # float num2 = 66.6
print(f'num2 = {num1}, type(num2) = {type(num2)}')

# 3、bool 布尔型 => 只有两个结果，真或者假。（True / False）
is_visited = True   # False
print(f'is_visited = {is_visited}, type(is_visited) = {type(is_visited)}')

# 4、字符串类型 => 有三种书写格式。1️⃣单引号 2️⃣双引号 3️⃣三引号（多行数据书写）   str => string 字符串类型
# 好处：嵌套书写非常简单。不需要转义。
# 复制的快捷键 ctrl + d
name1 = '玛丽亚'
name2 = "玛丽亚"
name3 = '''玛丽亚'''
name4 = """玛丽亚"""
print(f'name1 = {name1}, type(name1) = {type(name1)}')

# Python 中的一些高级数据类型（存储多个数据的类型）
# 5、列表类型：特点，有序，可重复，可扩展
names = ['张三', '李四', '王五', '张三', '李四']
print(f'names = {names}, type(names) = {type(names)}')

# 6、元组类型：特点， 有序，可重复，不可扩展
names = ('张三', '李四', '王五', '张三', '李四')
print(f'names = {names}, type(names) = {type(names)}')

# 7、集合类型：特点， 无序，不可重复，可扩展
# 无序：内部是通过一套算法实现的，可能使用到了当前时间戳变量。
names = {'张三', '李四', '王五', '张三', '李四'}
print(f'names = {names}, type(names) = {type(names)}')

# 8、字典类型：key -> value   键值对/夫妻对 dict => dictionary
stu_dit = {'stu_id': '1001', 'name': '张三', 'age': 18, 'score': 100}
print(f'stu_dit = {stu_dit}, type(stu_dit) = {type(stu_dit)}')