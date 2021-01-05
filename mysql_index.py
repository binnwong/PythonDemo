# coding=utf-8
from pymysql import connect


def insert_data():
    """
    在Phone_table中新增100000条数据
    """
    conn = connect(
        host="localhost",
        port=3306,
        user="root",
        password="mysql",
        database="MyDB_one",
        charset="utf8"
    )
    cursor = conn.cursor()
    for i in range(100000):
        sql = "insert into Phone_table values({id}, 'Phone{i}', 'black');".format(id=i, i=i)
        try:
            cursor.execute(sql)
            conn.commit()
        except Exception as e:
            print(e)
    cursor.close()
    conn.close()


if __name__ == '__main__':
    insert_data()
