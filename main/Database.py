import pymysql
import views as v


class Database:
    """
    数据库工具类
    增：学生、老师、课程、成绩
    删：学生、老师、课程
    改：学生、老师、课程、成绩
    查：学生、老师、课程、成绩
    视图： 每个查询功能都建立一个视图
    索引： 1.要注意的是，建立太多的索引将会影响更新和插入的速度，因为它需要同样更新每个
         索引文件。对于一个经常需要更新和插入的表格，就没有必要为一个很少使用的where
         字句单独建立索引了，对于比较小的表，排序的开销不会很大，也没有必要建立另外的索引。
         2.建立索引会占用磁盘空间
    """

    def __init__(self, user, password):
        """
        初始化连接数据库
        :param user: 云主机数据库的用户名
        :param password: 云主机数据库的密码
        """
        #  打开数据库连接
        try:
            self.con = pymysql.connect(host="182.92.122.200",
                                       user=user,
                                       password=password,
                                       database="dbw")
            # 创建游标对象
            self.cur = self.con.cursor()
            v.success_connect()

        except Exception as e:
            print(e)

    def add_student(self, num, name, sex, dept, place, passwd):
        """
        添加学生信息
        :param num: 学生学号
        :param name: 学生姓名
        :param sex: 学生性别
        :param dept: 学生院系
        :param place: 学生籍贯
        :param passwd: 学生登录密码
        :return:
        """
        try:
            sql = 'insert into dbw.student values(%s, %s, %s, %s, %s, %s)'
            add_data = [num, name, sex, dept, place, passwd]
            self.cur.execute(sql, add_data)
            self.con.commit()
        except Exception as e:
            print(e)
            self.con.rollback()

    def add_teacher(self, num, name, passwd, tele):
        """
        添加教师信息
        :param num: 教师工号
        :param name: 教师姓名
        :param passwd: 教师登录密码
        :param tele: 教师电话
        :return:
        """
        try:
            sql = 'insert into dbw.teacher values(%s, %s, %s, %s)'
            add_data = [num, name, passwd, tele]
            self.cur.execute(sql, add_data)
            self.con.commit()
        except Exception as e:
            print(e)
            self.con.rollback()
        finally:
            self.cur.close()
            self.con.close()

    def add_course(self, num, name, teacher):
        """
        添加课程信息
        :param num: 课程号
        :param name: 课程名
        :param teacher: 授课教师
        :return:
        """
        try:
            sql = 'insert into dbw.course values(%s, %s, %s)'
            add_data = [num, name, teacher]
            self.cur.execute(sql, add_data)
            self.con.commit()
        except Exception as e:
            print(e)
            self.con.rollback()
        finally:
            self.cur.close()
            self.con.close()

    def add_grade(self, num, proportion, cid, cname, score):
        """
        添加一个成绩
        :param num: 学号
        :param proportion: 学分
        :param cid: 课程号
        :param cname: 课程名称
        :param score: 课程分数
        :return:
        """
        try:
            sql = "insert into dbw.grade values(%s, %s, %s, %s, %s)"
            add_data = [num, proportion, cid, cname, score]
            self.cur.execute(sql, add_data)
            self.con.commit()
        except Exception as e:
            print(e)
            self.con.rollback()
        finally:
            self.cur.close()
            self.con.close()

    def delete_student(self, num):
        """
        按照学生学号删除学生信息
        :param num: 学生学号
        :return:
        """
        try:
            sql = 'delete from dbw.student where id = %s'
            data = [num]
            self.cur.execute(sql, data)
            self.con.commit()
        except Exception as e:
            print(e)
            self.con.rollback()
        finally:
            self.cur.close()
            self.con.close()

    def delete_teacher(self, num):
        """
        根据教师工号删除老师信息
        :param num: 教师工号
        :return:
        """
        try:
            sql = 'delete from dbw.teacher where id = %s'
            data = [num]
            self.cur.execute(sql, data)
            self.con.commit()
        except Exception as e:
            print(e)
            self.con.rollback()
        finally:
            self.cur.close()
            self.con.close()

    def delete_course(self, num):
        """
        根据课程号删除一个课程信息
        :param num: 课程号
        :return:
        """
        try:
            sql = 'delete from dbw.course where dbw.course.id = %s'
            data = [num]
            self.cur.execute(sql, data)
            self.con.commit()
        except Exception as e:
            print(e)
            self.con.rollback()
        finally:
            self.cur.close()
            self.con.close()

    def alter_student(self, num, name, sex, dept, place, passwd):
        """
        根据学生学号修改学生信息
        :param num: 学生学号
        :param name: 学生姓名
        :param sex: 学生性别
        :param dept: 学生院系
        :param place: 学生籍贯
        :param passwd: 学生登录密码
        :return:
        """
        try:
            sql = 'update dbw.student set name=%s, sex=%s, dept=%s, place=%s, passwd=%s where dbw.student.id = %s'
            data = [name, sex, dept, place, passwd, num]
            self.cur.execute(sql, data)
            self.con.commit()
        except Exception as e:
            print(e)
            self.con.rollback()
        finally:
            self.cur.close()
            self.con.close()

    def alter_teacher(self, num, name, passwd, tele):
        """
        根据教师工号来修改教师的信息
        :param num: 教师工号
        :param name: 教师姓名
        :param passwd: 教师登录密码
        :param tele: 教师电话
        :return:
        """
        try:
            sql = 'update dbw.teacher set name= %s, passwd=%s, tele=%s where dbw.teacher.id=%s'
            data = [name, passwd, tele, num]
            self.cur.execute(sql, data)
            self.con.commit()
        except Exception as e:
            print(e)
            self.con.rollback()
        finally:
            self.cur.close()
            self.con.close()

    def alter_grade(self, num1, num2, proportion, cname, score):
        """
        根据学生的学号和课程号来修改成绩信息
        :param num1: 学号
        :param num2: 课程号
        :param proportion: 学分
        :param cname: 课程名称
        :param score: 分数
        :return:
        """
        try:
            sql = 'update dbw.grade set proportion=%s, cname=%s, score=%s ' \
                  'where dbw.grade.id = %s and dbw.grade.cid = ' \
                  '%s '
            data = [proportion, cname, score, num1, num2]
            self.cur.execute(sql, data)
            self.con.commit()
        except Exception as e:
            print(e)
            self.con.rollback()
        finally:
            self.cur.close()
            self.con.close()

    def alter_course(self, num, name, teacher):
        """
        根据课程号修改成绩表
        :param num: 课程号
        :param name: 课程名称
        :param teacher: 课程老师
        :return:
        """
        try:
            sql = 'update course set name=%s, teacher=%s where course.id = %s'
            data = [name, teacher, num]
            self.cur.execute(sql, data)
            self.con.commit()
        except Exception as e:
            print(e)
            self.con.rollback()
        finally:
            self.cur.close()
            self.con.close()

    def query_one_student(self, num):
        """
        根据学号查询该学生的信息
        :param num: 学生学号
        :return:
        """
        try:
            sql = 'select * from student where id=%s'
            data = [num]
            self.cur.execute(sql, data)
            result = self.cur.fetchall()
            print(result)

        except Exception as e:
            print(e)

    def query_student(self):
        """
        查询学生的全部信息
        :return:
        """
        try:
            sql = 'select * from student'
            self.cur.execute(sql)
            result = self.cur.fetchall()
            for x in result:
                for y in x:
                    print(y, end='\t\t')
                print()

        except Exception as e:
            print(e)

    def query_teacher(self):
        """
        查询老师的全部信息
        :return:
        """
        try:
            sql = 'select * from teacher'
            self.cur.execute(sql)
            result = self.cur.fetchall()
            for x in result:
                for y in x:
                    print(y, end='\t\t\n')
                print()

        except Exception as e:
            print(e)

    def query_grade(self):
        """
        查询所有成绩信息
        :return:
        """
        try:
            sql = 'select * from grade'
            self.cur.execute(sql)
            result = self.cur.fetchall()
            for x in result:
                for y in x:
                    print(y, end='\t\t\n')
                print()

        except Exception as e:
            print(e)

    def query_course(self):
        """
        查询所有课程信息
        :return:
        """
        try:
            sql = 'select * from course'
            self.cur.execute(sql)
            result = self.cur.fetchall()
            for x in result:
                for y in x:
                    print(y, end='\t\t')
                print()
        except Exception as e:
            print(e)

    def calculation(self):
        """
        计算加权平均分的前三名
        :return:
        """
        try:
            sql = 'select sid, name, sum(score), sum(proportion) ' \
                  'from student_grade ' \
                  'group by sid ' \
                  'order by sum(score) / sum(proportion) ' \
                  'limit 3;'
            self.cur.execute(sql)
            result = self.cur.fetchall()
            print(result)
        except Exception as e:
            print(e)

    def query_teacher_passwd(self, num):
        """
        根据工号查询老师的登录密码
        :param num: 老师的工号
        :return:
        """
        try:
            sql = 'select passwd from teacher where id = %s'
            data = [num]
            self.cur.execute(sql, data)
            result = self.cur.fetchall()
            return result[0][0]
        except Exception as e:
            print(e)

    def query_one_teacher(self, num):
        """
        根据工号查找该老师的个人信息
        :param num: 工号
        :return:
        """
        try:
            sql = 'select * from teacher where id = %s'
            data = [num]
            self.cur.execute(sql, data)
            result = self.cur.fetchall()
            for x in result:
                print(x, end='\t\t\n')
        except Exception as e:
            print(e)

    def query_teach_course(self, num):
        """
        根据教师工号找到该老师所教的所有课程
        :param num: 教师工号
        :return:
        """
        try:
            sql = 'select cname from teacher_course where tid = %s'
            data = [num]
            self.cur.execute(sql, data)
            result = self.cur.fetchall()
            for x in result:
                print(x, end='\t\t\n')
        except Exception as e:
            print(e)

    def query_student_passwd(self, num):
        """
        根据学号查询学生登录密码是否正确
        :param num: 学生学号
        :return:
        """
        try:
            sql = 'select passwd from student where id = %s'
            data = [num]
            self.cur.execute(sql, data)
            result = self.cur.fetchall()
            return result[0][0]
        except Exception as e:
            print(e)

    def query_one_grade(self, num):
        """
        根据学号查询本人所有成绩
        :param num: 学号
        :return:
        """
        try:
            sql = 'select cname, score from student_grade where sid = %s'
            data = [num]
            self.cur.execute(sql, data)
            result = self.cur.fetchall()
            for x in result:
                for y in x:
                    print(y, end='\t\t')
                print()
        except Exception as e:
            print(e)

    def query_self_course(self, num):
        """
        根据学号查询自己的选课信息
        :param num: 学生学号
        :return:
        """
        try:
            sql = 'select cname from student_grade where sid = %s'
            data = [num]
            self.cur.execute(sql, data)
            result = self.cur.fetchall()
            for x in result:
                for y in x:
                    print(y)
        except Exception as e:
            print(e)

    def calculation_aver_score(self, num):
        try:
            sql = 'select sum(score) / sum(proportion) from student_grade where sid = %s'
            data = [num]
            self.cur.execute(sql, data)
            result = self.cur.fetchall()
            return result[0][0]
        except Exception as e:
            print(e)
