import yaml
from pagetest_api import OperatorsHelperAPI

with open('testdata.yaml', encoding='utf-8') as fy:
    testdata = yaml.safe_load(fy)


def test_get_post_in_title():
    test_api = OperatorsHelperAPI()
    res_title = test_api.get_title(owner='notMe')

    assert testdata['search_title'] in res_title


def test_create_new_post():
    test_api = OperatorsHelperAPI()
    test_api.create_new_post()
    res_title = test_api.get_title()

    assert testdata['title'] in res_title
