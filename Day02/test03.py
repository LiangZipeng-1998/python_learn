'''
    input 是 python 语言提供的输入函数。
    格式：
        input(提示信息) 该函数会返回用户在键盘中输入的结果，但一定要小心，因为返回的结果都是 str 类型
    说明：
        由于 input 输入函数会返回结果，所以程序中必须要定义一个变量接收 input 函数返回的结果。
        input 是一个阻塞函数，如果用户不输入，程序就不会继续向下执行。
'''

name = input('亲，请输入您的姓名：')
age = input('亲，请输入您的年龄：')
gender = input('亲，请输入您的性别：')    # gender    (sex)   F(Female)   M(Male)
print(f'大家好，我叫{name}，我今年{age}岁了，性别{gender}。')
