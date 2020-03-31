from ..utils.module import Module

class MockMLModel(Module):
    def __init__(self, in_label='MLData', out_label=None, connect_labels=None, name='MockMLData'):
        Module.__init__(self, in_label=in_label, out_label=out_label, connect_labels=connect_labels, name=name, page_batches=True)
        self.batch_counts = dict()

    def process(self, node, driver=None):
        pass

    def process_batch(self, batch, driver=None):
        print('*' * 80)
        print('!MockMLModel', flush=True)
        print(batch, flush=True)
        print('*' * 80)
        # yield
