from .transaction import Transaction
from .log import Log

class Module:
    def __init__(self, in_label=None, out_label=None, connect_labels=None, name='Default', page_batches=False):
        self.in_label      = in_label
        self.out_label     = out_label
        self.connect_labels = connect_labels
        self.name = name
        self.page_batches = page_batches
        self.log = Log(name, directory='modules')

    def default_transaction(self, data, uuid=None, from_uuid=None):
        return Transaction(in_label=self.in_label, out_label=self.out_label, connect_labels=self.connect_labels, data=data, uuid=uuid, from_uuid=from_uuid)
    
    def query_transaction(self, query):
        return Transaction(query=query)

    def custom_transaction(self, *args, **kwargs):
        return Transaction(*args, **kwargs)

    def process(self, node, driver=None):
        pass

    def process_batch(self, batch, driver=None):
        for item in batch.items:
            for transaction in self.process(item, driver=driver):
                yield transaction

    def __str__(self):
        if self.in_label is None:
            return '{}: ({})'.format(self.name, self.out_label)
        else:
            return '{}: ({}) -> ({})'.format(self.name, self.in_label, self.out_label)
