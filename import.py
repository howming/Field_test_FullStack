# -*- coding:utf-8 -*-
import pandas as pd
import pymysql
import time

def get_data(file_name):
    data = pd.read_csv(file_name,error_bad_lines=False)
    data['Date'] = data['frame.time_epoch'].apply(lambda n: time.strftime('%Y-%m-%d', time.localtime(int(str(n).split('.')[0]))))
    data['Time'] = data['frame.time_epoch'].apply(lambda n: time.strftime('%H:%M:%S', time.localtime(int(str(n).split('.')[0]))))
    data['usec'] = data['frame.time_epoch'].apply(lambda n: (int((n - int(n)) * 1000000000) - (int((n - int(n)) * 1000000000) % 1000)))
    data = data.drop('frame.time_epoch', axis=1)
    data = data.fillna(0)
    val = data.values.tolist()

    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='p9tc1OTJ65:w',
        db='testdb',
        charset='utf8'
    )
    cursor = conn.cursor()
    sql = 'insert into testdate (SourceIP,SourcePort,DestinationIP,DestinationPort,FQDN,Date,Time,usec) values (%s,%s,%s,%s,%s,%s,%s,%s)'

    try:
        cursor.executemany(sql, val)

    except Exception as e:
        print(e)
        conn.rollback()

    finally:
        cursor.close()
        conn.commit()
        conn.close()


def main():
    get_data('./dns_sample.csv')


if __name__ == '__main__':
    main()
