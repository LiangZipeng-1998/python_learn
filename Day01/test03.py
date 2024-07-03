# 快速创建 python 模块。  alt + insert

'''
    关键字：有些单词被 python 语法赋予了“特殊含义”，这些单词我们在编程中是不可以直接使用的。
    关键字是编程语言里事先定义好并赋予了特殊含义的单词，也称为‘保留字’

    ['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break',
    'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global',
    'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try',
    'while', 'with', 'yield']
    Python中的关键字一共有36个。

    思考：程序编程中，如何定义自己需要的一些名称呢？
    名称：变量，函数，类型，对象名 ... 统称为标识符。
    思考：定义标识符有哪些规则呢？
    1、数字不能开头
    2、只能使用 a-z A-Z 0-9 _（下划线）其他符号全部非法。
    3、Python语言严格区分大小写。username 不等于 UserName

    命名规则：函数/功能：（坦克撞击墙壁）
    1、小驼峰命名规则：tankHitWall
    2、大驼峰命名规则：TankHitWall
    3、下划线命名规则：tank_hit_wall

    TANK_HIT_WALL 这样是正确的，但是不可以，因为这样不符合编程的命名规范。
    全部大写：常量（不会发生变化的数据）PI, ID...
'''

# 1、导入系统的 keyword 库/模块
import keyword

# 2、输出查看系统的关键字列表
print(keyword.kwlist)

# 3、输出查看系统的关键字列表的总长度
print(len(keyword.kwlist))