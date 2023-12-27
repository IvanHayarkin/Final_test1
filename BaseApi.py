import logging
import requests
import yaml

with open('testdata.yaml', encoding='utf-8') as fy:
    testdata = yaml.safe_load(fy)


class BaseAPI:

    def __init__(self):
        try:
            data = {'username': testdata['login'], 'password': testdata['password']}
            self.session = requests.Session()
            post = self.session.post(url=testdata['url_auto'], data=data)
            if post.status_code == 200:
                self.token = post.json()['token']
                logging.debug(f'initializing session and getting token for {testdata["login"]}')
                return
            logging.debug(f'toke getting failed: {testdata["login"]}, status code {post.status_code}')
        except Exception as e:
            logging.exception(f'failed to get token for {testdata["login"]} or open session: {e}')

    def get_post(self, owner='notMe'):
        try:
            path = testdata['url_post']
            get = requests.get(url=path, params={'owner': owner}, headers={'X-Auth-Token': self.token})
            if get.status_code == 200:
                logging.info(f'posts received with user: {testdata["login"]}, author: {owner}')
                return get.json()
            logging.info(f'posts not found with user: {testdata["login"]}, author: {owner}, status code {get.status_code}')
        except Exception as e:
            logging.exception(f'failed to get posts: {e}')
            return None

    def create_post(self, title, description, content):
        try:
            self.session.post(url=testdata['url_post'], headers={'X-Auth-Token': self.token},
                              params={"title": title, 'description': description, 'content': content})
            logging.info(f"post created on {testdata['login']}'s page")
        except:
            logging.exception(f"failed to create post on {testdata['login']}'s page")