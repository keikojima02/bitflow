from .module import Module
from pprint import pprint
import os, pickle

class BatchLearner(Module):
    def __init__(self, filename=None, epochs=2, train_fraction=0.8, test_fraction=0.15, validate_fraction=0.05, **kwargs):
        Module.__init__(self, page_batches=True, **kwargs)

        self.epochs = epochs
        self.validate_fraction = validate_fraction
        self.train_fraction    = train_fraction
        self.test_fraction     = test_fraction

        self.filename = filename
        self.model = None

    def init_model(self):
        self.model = None
    
    def save(self):
        with open(self.filename, 'wb') as outfile:
            pickle.dump(self.model, outfile)
    
    def load(self):
        with open(self.filename, 'rb') as infile:
            self.model = pickle.load(infile)

    def learn(self, batch):
        self.log.log('Learning on ', batch.uuid)

    def test(self, batch):
        self.log.log('Testing on ', batch.uuid)

    def val(self, batch):
        self.log.log('Validating on ', batch.uuid)

    def process(self, node):
        raise RuntimeError('Called process() for Batch Module')

    def process_batch(self, batch):
        if self.model is None:
            self.init_model()
        self.load()
        self.log.log(self.name, ' Processing ', batch.uuid)
        if batch.rand < self.train_fraction:
            gen = self.learn(batch)
        elif batch.rand < self.train_fraction + self.test_fraction:
            gen = self.test(batch)
        else:
            gen = self.val(batch)
        if self.out_label is not None and gen is not None:
            for transaction in gen:
                yield transaction
        self.save()

