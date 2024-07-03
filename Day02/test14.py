# 需求：判断一个人是否为男性，或者大与18岁

gender = input('亲，请输入您的性别：')
age = int(input('亲，请输入您的年龄：'))

# 判断
# or 或者    特点：一真即真，全假为假
result = gender == '男' or age >= 18
print(f'result = {result}')
