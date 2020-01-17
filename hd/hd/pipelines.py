# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import  json

class HdPipeline(object):
    def process_item(self, item, spider):

        a=json.dumps(dict(item), ensure_ascii=False, indent=4)
        with  open ('C:\\Users\\Administrator\\PycharmProjects\\hd\\hd\\j.json','a') as f:
            f.write(a)
        #print(type(item))
        return item
