# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector


class DadosPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='python'
        )
        self.curr = self.conn.cursor()
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS `2022`""")
        self.curr.execute("""CREATE TABLE `2022` (
					            id int NOT NULL AUTO_INCREMENT,                                   
                                question text,                                                      
                                answers text,
                                comments text,                                
                                votes int, 
                                amount_comments int,                               
					            primary key(id)                                 
                                                                                        
                               ) """)


    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):

        self.curr.execute("""INSERT ignore INTO `2022`(question,answers,comments,votes,amount_comments) values (%s,%s,%s,%s,%s)""", (
            item['question'],
            item['answer'],
            item['comments'],
            item['votes'],
            item['amount_comments']

        ))

        self.conn.commit()

