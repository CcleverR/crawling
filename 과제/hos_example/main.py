import pymysql

conn=pymysql.connect(host="localhost", port=3333, user='root', password='root', db="hospital", charset='utf8')

curs=conn.cursor()

query = 'insert into doctor (hospital,name,major,specialization, contacts) value("souel","이국종2","정형외과2","외과궁2","010-1243-3422")'
curs.execute(query)
conn.commit()

#sql="select * from doctor"
#curs.execute(sql)
#rows= curs.fetchall()
#print(rows)

conn.close()