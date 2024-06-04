import pytest

from src.utils import emp_info
from src.utils import vacancy_info


@pytest.fixture
def test_info():
    test_information = [
        {"id": 1, "name": "a", "area": {"name": "a1"}, "salary": {"from": 100, "to": 200, "currency": "RUR"},
         "published_at": 11, "alternate_url": "a2", "snippet": {"requirement": "'a3", "responsibility": "a4'"},
         "employer": {"id": 1, "name": "PiP", "url": "htpps:www.ry"}},
        {"id": 2, "name": "b", "area": {"name": "b1"}, "salary": {"from": 300, "to": 400, "currency": "RUR"},
         "published_at": 12, "alternate_url": "b2", "snippet": {"requirement": "'b3", "responsibility": "b4'"},
         "employer": {"id": 2, "name": "PaP", "url": "htpps:ww.ra"}}]
    return test_information


def test_emp_info(test_info):
    assert emp_info(test_info) == ["(1, 'PiP', 'htpps:www.ry')", "(2, 'PaP', 'htpps:ww.ra')"]


def test_vacancy_info(test_info):
    assert vacancy_info(test_info) == ["(1, 'a', 'a1', 100, 200, 'RUR', '11', 'a2', ' a3', 'a4 ', 1)",
                                       "(2, 'b', 'b1', 300, 400, 'RUR', '12', 'b2', ' b3', 'b4 ', 2)"]
