# 需求：判断一个人是否为男性，并且大与18岁

gender = input('亲，请输入您的性别：')
age = int(input('亲，请输入您的年龄：'))

# 判断
# and 并且    特点：一假即假
result = gender == '男' and age >= 18
print(f'result = {result}')
