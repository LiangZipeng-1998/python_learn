'''
if ... else ...
如果 ... 否则 ...
需求：如果你儿子的成绩及格了，就奖励他，否则，打死他。
'''

# 1. 定义变量，提示并接收用户的输入
score = int(input('亲，请输入您儿子的考试成绩：'))

# 2. 判断
if score >= 60:
    # 及格
    print('恭喜你，你儿子真棒，奖励你儿子一辆BMW。')
    print('再奖励你儿子一个儿媳妇。')
else:
    # 不及格
    print('很遗憾，您儿子已经被打死了。')
    print('准备再生一个吧。')

print('程序继续向后执行...')