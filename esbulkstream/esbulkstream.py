
import os
import elasticsearch
import elasticsearch.helpers
from elasticsearch import Elasticsearch

class Documents:

    def __init__(self, index, update_frequency=1000):

        if 'ESURL' not in os.environ:
            es_url = "http://localhost:9200"
        else:
            es_url = os.environ['ESURL']

        self.es = Elasticsearch([es_url])
        self.index = index
        self.frequency = update_frequency
        self.docs = []

    def add(self, document_data, document_id):

        new_data = {
            '_op_type': 'update',
            '_index': self.index,
            '_id': document_id,
            'doc_as_upsert': True,
            'doc': document_data
        }

        self.docs.append(new_data)

        return self.__maybe_update__()

    def __maybe_update__(self, force = False):

        if len(self.docs) < self.frequency and force != True:
            return

        errors = []

        for ok, item in elasticsearch.helpers.streaming_bulk(self.es, self.docs, max_retries=2):
            if not ok:
                errors.append(item)

        self.docs = []

        return errors

    def done(self):
        return self.__maybe_update__(True)
