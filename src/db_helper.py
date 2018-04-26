import pymysql


class DbExeu(object):

    def get_start(self, command):
        try:
            con = pymysql.connect(host="localhost", user="user", password="P@ssw0rd", db="db_lianjia", port=3307)
            cur = con.cursor()
            if not command == None:
                cur.execute(command)
        except Exception as e:
            print(e)
            raise e
        finally:
            cur.close()
            con.close()


    def return_many(self, sql, para):
        try:
            con = pymysql.connect(host="localhost", user="user", password="P@ssw0rd", db="db_lianjia", port=3307)
            cur = con.cursor()
            cur.execute(sql,para)
            list = cur.fetchall()
            return list
        except Exception as e:
            print(e)
            raise e
        finally:
            cur.close()
            con.close()

    def trans(self, sql, paras):
        try:
            con = pymysql.connect(host="localhost", user="user", password="P@ssw0rd", db="db_lianjia", port=3307)
            cur = con.cursor()
            cur.executemany(sql,paras)
        except Exception as e:
            con.rollback()
            print(e)
            raise e
        finally:
            cur.close()
            con.close()


if __name__ == '__main__':

