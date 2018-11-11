import pymysql

conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='wanglei666',
    database='cineama',
    charset='utf8'
)

cursor = conn.cursor()
sql = 'INSERT INTO 80scine VALUES(3972, \'低压槽：欲望之城\', \'//t.dyxz.la/upload/img/201802/poster_20180225_4558708_b.jpg\',  \
\'thunder://QUFodHRwOi8vZGwxODAuODBzLmltOjkyMC8xODA0L1vlkI7mnaXnmoTmiJHku6xd6aKE5ZGK54mHL1vlkI7mnaXnmoTmiJHku6xd6aKE5ZGK54mHX2hkLm1wNFpa\')'
try:  
    cur.execute(sql)  
    #提交  
    conn.commit()  
except IntegrityError:  
    #错误回滚  
    conn.rollback()   

cursor.close()
conn.close()
