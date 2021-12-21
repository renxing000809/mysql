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
                    elif op == 5:
                        """
                        增加一个信息
                        """
                        v.add()
                        a = int(input())
                        if a == 1:
                            """
                            增加一个学生
                            """
                            print('请输入学生学号')
                            num = input()
                            print('请输入学生姓名')
                            name = input()
                            print('请输入学生性别')
                            sex = input()
                            print('请输入学生院系')
                            dept = input()
                            print('请输入学生籍贯')
                            place = input()
                            print('请输入学生登录密码')
                            passwd = input()
                            db.add_student(num, name, sex, dept, place, passwd)
                        elif a == 2:
                            """
                            增加一个老师
                            """
                            print('请输入教师的工号')
                            num = input()
                            print('请输入教师的姓名')
                            name = input()
                            print('请输入教师的登录密码')
                            passwd = input()
                            print('请输入教师的邮箱')
                            tele = input()
                            db.add_teacher(num, name, passwd, tele)
                        elif a == 3:
                            """
                            增加一个课程的信息
                            """
                            print('请输入课程号')
                            num = input()
                            print('请输入课程名')
                            name = input()
                            print('请输入授课老师姓名')
                            teacher = input()
                            db.add_course(num, name, teacher)
                        elif a == 4:
                            """
                            增加一个成绩的信息
                            """
                            print('请输入学号')
                            num = input()
                            print('请输入学分')
                            proportion = input()
                            print('请输入课程号')
                            cid = input()
                            print('请输入课程名')
                            cname = input()
                            print('请输入分数')
                            score = input()
                            db.add_grade(num, proportion, cid, cname, score)
                    elif op == 6:
                        v.delete()
                        a = int(input())
                        """
                        删除一个信息
                        """
                        if a == 1:
                            """
                            删除一个学生信息
                            """
                            print('请输入要删除学生的学号')
                            num = input()
                            db.delete_student(num)
                            print('删除成功')
                        elif a == 2:
                            """
                            删除一个教师信息
                            """
                            print('请输入要删除教师的工号')
                            num = input()
                            db.delete_teacher(num)
                            print('删除成功')
                        elif a == 3:
                            """
                            删除一个课程信息
                            """
                            print('请输入要删除的课程号')
                            num = input()
                            db.delete_course(num)
                            print('删除成功')

                    elif op == 7:
                        v.alter()
                        a = int(input())

                        """
                        修改一个信息
                        """
                        if a == 1:
                            """
                            修改一个学生信息
                            """

                            print('请输要修改的学生学号')
                            num = input()
                            print('请输入学生姓名')
                            name = input()
                            print('请输入学生性别')
                            sex = input()
                            print('请输入学生院系')
                            dept = input()
                            print('请输入学生籍贯')
                            place = input()
                            print('请输入学生登录密码')
                            passwd = input()
                            db.alter_student(num, name, sex, dept, place, passwd)
                        elif a == 2:
                            """
                            修改一个教师信息
                            """
                            print('请输入教师的工号')
                            num = input()
                            print('请输入教师的姓名')
                            name = input()
                            print('请输入教师的登录密码')
                            passwd = input()
                            print('请输入教师的邮箱')
                            tele = input()
                            db.alter_teacher(num, name, passwd, tele)
                    else:
                        break
            else:
                print('验证失败')
