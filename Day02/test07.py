# 课堂练习：某超市TShirt的单价是56.5，裤子的单价是89.8
# 凤姐买了3件TShirt，5条裤子，请写程序计算凤姐一共该给多少钱？
# 如果是老板生日，全场打88折，凤姐又需要付多少钱呢？

# 1. 定义变量，接收用户的输入
t_shift = float(input('亲，请输入t_shift的单价：'))
pants = float(input('亲，请输入裤子的单价：'))

t_shift_count = float(input('亲，你买了几件t_shift呀？'))
pants_count = float(input('亲，你买了几件条裤子呀？'))

# 2. 数值运算
normal_price = t_shift * t_shift_count + pants * pants_count
print(f'normal_price = {normal_price}')

# 折扣
discount = 0.88

# 计算折扣价
discount_price = normal_price * discount
print(f'discount_price = {discount_price}')
