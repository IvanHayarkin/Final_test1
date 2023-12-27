import requests
import yaml
from BaseApi import BaseAPI

with open('testdata.yaml', encoding='utf-8') as fy:
    testdata = yaml.safe_load(fy)

s = requests.Session()


class OperatorsHelperAPI(BaseAPI):

    def get_title(self, owner=None):
        res = self.get_post(owner=owner)
        if res is None:
            return ''
        data = res['data']
        title = [i['title'] for i in data]
        return title

    def create_new_post(self):
        self.create_post(testdata['title'], testdata["description"], testdata['content'])