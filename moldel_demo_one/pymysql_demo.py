from pymysql import connect


# def insert_data():
#     """
#     在mysql中新增一条数据
#     """
#     # 1.创建连接
#     conn = connect(
#         host="localhost",
#         port=3306,
#         user="pymysql",
#         password="mysql",
#         database="pymysql_demo",
#         charset="utf8"
#     )
#     # 2.创建游标
#     cursor = conn.cursor()
#     # 3.执行语句
#     sql = '''insert into test_table values(0, now(), 'Hello MySQL！');'''
#     try:
#         cursor.execute(sql)
#         conn.commit()
#     except Exception as e:
#         print(e)
#     # 4.关闭游标
#     cursor.close()
#     # 5.关闭连接
#     conn.close()
#
#
# insert_data()


# def select_data():
#     """
#     从mysql中查询数据
#     """
#     conn = connect(
#         host="localhost",
#         port=3306,
#         user="pymysql",
#         password="mysql",
#         database="pymysql_demo",
#         charset="utf8"
#     )
#     cursor = conn.cursor()
#     row_one = None
#     sql = '''select * from test_table;'''
#     try:
#         cursor.execute(sql)
#         row_one = cursor.fetchone()
#     except Exception as e:
#         print(e)
#     cursor.close()
#     conn.close()
#     print(row_one)
#
#
# select_data()


def delete_data():
    """
    从mysql中删除数据
    """
    conn = connect(
        host="localhost",
        port=3306,
        user="pymysql",
        password="mysql",
        database="pymysql_demo",
        charset="utf8"
    )
    cursor = conn.cursor()
    sql = '''delete from test_table;'''
    try:
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)
    cursor.close()
    conn.close()


delete_data()


"""
准备事项:
1.创建数据库pymysql_demo
create database pymysql_demo charset utf8;
2.使用数据库pymysql_demo
use pymysql_demo;
3.创建表test_table
create table test_table(id int unsigned primary key auto_increment not null,create_time TIMESTAMP not null DEFAULT 
CURRENT_TIMESTAMP,test_data LONGTEXT not null);
4.创建数据库用户pymysql
# 用户名 pymysql, 密码 mysql 只能对pymysql_demo数据库进行操作,可以进行所有操作
grant all privileges on pymysql_demo.* to 'pymysql'@'localhost' identified by 'mysql';
"""






