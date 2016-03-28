#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb
import datetime 
import os
from DBUtil import *
class Do_insert_work:

    @staticmethod
    def read_line_file(file_name):
        file = open(file_name)
        while 1:
            lines = file.readlines(10000)
            if not lines:
                break
            for line in lines:
                if ("\n" != line):
                    Do_insert_work.parse_one_line(line,os.path.basename(file_name)) 
        file.close()

    @staticmethod
    def parse_one_line(line,filename):
        lastIndex = int(len(line)-1)
        fieldarr = line[0:lastIndex].split("\t")
        Do_insert_work.do_insert(fieldarr,filename)

    @staticmethod
    def do_insert(fieldarr,serviceName):
        conn = get_mysql_conn("ctrade")
        cur = conn.cursor()
        now =  datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
        insert_sql ="insert into usermanage_count (phone,count_number,service_name,ua,count_date)     values('%s','%s','%s','%s','%s')" %(fieldarr[1],fieldarr[2],serviceName,fieldarr[0],now)
        cur.execute(insert_sql)
        conn.commit()
        conn.close()

if __name__ == '__main__':
    create_default_db("ctrade")
    Do_insert_work.read_line_file("./tmp/appLogin")
    Do_insert_work.read_line_file("./tmp/appRelated")
    Do_insert_work.read_line_file("./tmp/openAndSign")
    Do_insert_work.read_line_file("./tmp/reg.do")
