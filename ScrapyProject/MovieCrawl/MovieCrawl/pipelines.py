# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class MoviecrawlPipeline(object):
    def process_item(self, item, spider):
        
        conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='wanglei666',
            database='cineama',
            charset='utf8'
        )
        cursor = conn.cursor()

        sql = 'INSERT INTO 80scine VALUES(%d, \'%s\', \'%s\', \'%s\')' % (int(item['iD']), item['cineName'], item['pictureLink'], item['downloadLink'])
        try:
            cursor.execute(sql)
            conn.commit()
        except Exception:
            conn.rollback()
        cursor.close()
        conn.close()
        return item
        
