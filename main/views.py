"""
视图文件，打印各种交互信息
"""


def init():
    """
    初始界面，选择身份
    :return:
    """
    print('请选择你的身份')
    print('1----- 学生')
    print('2----- 老师')
    print('3----- 管理员')


def student():
    """
    学生界面
    :return:
    """
    print('选择你要执行的功能')
    print('1----- 查询个人信息')
    print('2----- 查询本人所有的成绩')
    print('3----- 查询本人选课信息')
    print('4----- 计算自己目前的加权平均分')
    print('5----- 退出')


def teacher():
    """
    老师界面
    :return:
    """
    print('选择你要执行的功能')
    print('1----- 查询个人信息')
    print('2----- 查询本人授课信息')
    print('3----- 退出')


def check_administrators():
    """
    验证管理员的用户名、密码是否正确
    :return:
    """
    print('请输入管理员的用户名和密码')
    print('用户名')
    a = input()
    print('密码')
    b = input()
    if a == 'admin' and b == 'admin':
        print('验证成功')
        return True
    else:
        print('验证失败')
        return False


def administrators():
    """
    管理员界面
    :return:
    """
    print('选择你要执行的功能')
    print('1----- 查询所有学生的信息')
    print('2----- 查询所有老师的信息')
    print('3----- 查询所有课程的信息')
    print('4----- 查询加权平均分前3名')
    print('5----- 增加一条信息')
    print('6----- 删除一条信息')
    print('7----- 修改一条信息')
    print('8----- 退出')


def success_connect():
    print('***数据库连接成功***')
    print('*****************')


def add():
    print('选择你要执行的功能')
    print('1----- 增加一个学生的信息')
    print('2----- 增加一个老师的信息')
    print('3----- 增加一个课程的信息')
    print('4----- 增加一个成绩的信息')


def delete():
    print('选择你要执行的功能')
    print('1----- 删除一个学生的信息')
    print('2----- 删除一个老师的信息')
    print('3----- 删除一个课程的信息')


def alter():
    print('选择你要执行的功能')
    print('1----- 修改一个学生的信息')
    print('2----- 修改一个老师的信息')