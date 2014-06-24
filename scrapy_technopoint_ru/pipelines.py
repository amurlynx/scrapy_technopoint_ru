# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import sqlite3
from os import path

from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher

class ScrapyTechnopointRuPipeline(object):
    def process_item(self, item, spider):
        return item



class SQLiteStorePipeline(object):
    filename='mydb.db'

    def __init__(self):
        self.conn=None
        dispatcher.connect(self.initialize,signals.engine_started)
        dispatcher.connect(self.finalize,signals.engine_stopped)

    def initialize(self):
        if path.exists(self.filename):
            self.conn=sqlite3.connect(self.filename)
        else:
            self.conn=self.create_table(self.filename)

    def finalize(self):
        if self.conn is not None:
            self.conn.commit()
            self.conn.close()
            self.conn=None

    def create_table(self,filename):
        conn=sqlite3.connect(filename)
        conn.execute("create table if not exists pars (cnt text, name text)")
        conn.commit()
        return conn

    def process_item(self,item,spider):
        self.conn.execute("insert into pars(cnt, name) values (?, ?)", (item['Count'], item['Name']))
        self.conn.commit()
        #self.conn.execute("insert into pars(name) values (?)", (item['Name']))
        #self.conn.commit()
        return item