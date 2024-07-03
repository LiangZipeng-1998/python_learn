'''
    课堂练习：
    1、定义字符串变量 name，输出 我的名字叫 小明，请多多关照！
    2、定义字符串变量 name，age，输出 我的名字叫小明，今年18岁，请多多关照！
    3、定义整数变量 student_no，输出 我的学号是000001
    4、定义小数 price，weight，money，输出 苹果单价9.0元/斤，购买了5.0斤，需要支付45.0元
    5、定义小数 scale，输出 数据比例是10.0%
'''

name = '小明'
print(f'我的名字叫{name}，请多多关照！')

age = 18
print(f'我的名字叫{name}，今年{age}岁，请多多关照！')
# %s 表示字符串的占位符
print(f'我的名字叫 %s，今年 %d 岁，请多多关照！' % (name, age))

student_no = 1  # 整形数值是不能以 0 开头
# 说明：整形的占位符为 %d
# %06d 整数必须是 6 位数，如果不足 6 位，用 0 补齐
print('我的学号是 %06d' % student_no)
print('我的学号是 %d' % (student_no))

price = 9.00
weight = 5.00
money = price * weight
print(f"苹果单价{price}元/斤，购买了{weight}斤，需要支付{money}元")
# %f 表示浮点型占位符   %.1f / %.2f 表示保留1位 / 2位 小数
print(f"苹果单价 %.1f 元/斤，购买了 %.1f 斤，需要支付 %.1f 元" % (price, weight, money))

scale = 10.00
print(f"数据比例是{scale}%")
# % 是 python中的特殊字符，如果要输出一个 %，需要书写 %%
print(f"数据比例是 %.2f%%" % (scale,))


