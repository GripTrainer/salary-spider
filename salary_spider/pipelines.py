import dataset

class DatabasePipeline(object):
    def __init__(self, connection_string):
        self.db = dataset.connect(connection_string)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            connection_string=crawler.settings.get("CONNECTION_STRING"),
        )

    def open_spider(self, spider):
        self.table = self.db[spider.name]
        

    def process_item(self, item, spider):
        self.table.insert(item)

        return item
        
