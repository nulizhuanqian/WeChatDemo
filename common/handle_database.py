# coding:utf-8
import pymysql
import time
import logging
logger = logging.getLogger(__name__)

class DataOper():

    mysqlDict={
        "host":"10.0.5.107",
        "db":"mall",
        "user":"mall_rw",
        "password":"123456"
    }

    def open(self):
        try:
            self.datebase = pymysql.Connect(host=self.mysqlDict['host'], db=self.mysqlDict['db'], port=31307,
                                            user=self.mysqlDict['user'], password=self.mysqlDict['password'])
        except pymysql.err.OperationalError as e:
            logger.exception("数据库连接失败！")
            if "Errno 10060" in str(e) or "2003" in str(e):
                logger.error("数据库连接失败！")
            raise
        self.currentConn = self.datebase  # 数据库连接完成
        self.cursor = self.currentConn.cursor()  # 游标，用来执行数据库


    #把多条sql拆分成单条，放进sqlList中
    def splitesql(self,sql):
        sqllist = sql.split(';')
        return sqllist[0:-1]



    def select_sql(self,sql):
        '''
        查询单个字段
        :param sql:
        :return:
        '''
        self.open()
        cur=self.datebase.cursor()
        try:
            cur.execute(sql)
            result=cur.fetchall()
            return result
        except:
            # 发生错误时回滚
            self.datebase.rollback()
        self.datebase.close()


    # 删除数据
    def del_updata_sql(self,sql:str,closeConn =True) -> list:
        self.open()
        sqllist = self.splitesql(sql)
        logger.info(f"开始执行sql语句")
        try:
            with self.cursor as my_cursor:
                for i in sqllist:
                    my_cursor.execute(i)
                    self.datebase.commit()
        except:
            self.datebase.rollback()

        #关闭数据库
        my_cursor.close()
        self.currentConn.close()



    #查询数据库条数
    def db_count(self,sql):
        self.open()
        db=self.datebase.cursor()
        db.execute(sql)
        self.datebase.commit()
        count_sql=db.fetchall()
        if len(count_sql)>0:
            return len(count_sql)
        else:
            print("查询数据库数据为空")





if __name__ == '__main__':

    # sql='DELETE from bs_group where group_code="999998";'"delete from bs_address where relation_no='999998';"
    # DataOper().del_updata_sql(sql)
    sql="SELECT integration_goods_code FROM ums_integration_goods ORDER BY create_time DESC LIMIT 1  "
    sql=DataOper().select_sql(sql)
    print(sql)



