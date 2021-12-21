from Database import Database
import views as v

if __name__ == '__main__':
    db = Database('root', 'kkb123')
    while True:
        v.init()
        a = int(input())
        if a == 1:
            """
            学生界面
            """
            print('请输入学生的学号和登录密码')
            print('学号')
            a = input()
            print('登录密码')
            b = input()
            correct = db.query_student_passwd(a)
            if correct == b:
                while True:
                    v.student()
                    op = int(input())
                    if op == 1:
                        db.query_one_student(a)
                    elif op == 2:
                        db.query_one_grade(a)
                    elif op == 3:
                        db.query_self_course(a)
                    elif op == 4:
                        print(db.calculation_aver_score(a))
                    else:
                        break
            else:
                print('验证失败')

        elif a == 2:
            """
            老师界面
            """

            """
            验证老师身份的工号和密码
            """
            print('请输入教师的工号和登录密码')
            print('工号')
            a = input()
            print('登录密码')
            b = input()
            correct = db.query_teacher_passwd(a)

            if correct == b:
                while True:
                    v.teacher()
                    op = int(input())
                    if op == 1:
                        db.query_one_teacher(a)
                    elif op == 2:
                        db.query_teach_course(a)
                    else:
                        break
            else:
                print('验证失败')

        else:
            """
            管理员模式
            """
            if v.check_administrators() is True:
                while True:
                    v.administrators()
                    op = int(input())
                    if op == 1:
                        """
                        查询所有学生的信息
                        """
                        db.query_student()
                    elif op == 2:
                        """
                        查询所有老师的信息
                        """
                        db.query_teacher()
                    elif op == 3:
                        """
                        查询所有课程的信息
                        """
                        db.query_course()
                    elif op == 4:
                        """
                        查询加权平均分前3名
                        """
                        db.calculation()
                    else:
                        break
            else:
                print('验证失败')
