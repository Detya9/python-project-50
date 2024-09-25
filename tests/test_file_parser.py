from gendiff import parser


def test_parser():
    file_path1 = 'tests/fixtures/file1.json'
    file_path2 = 'tests/fixtures/file2.yml'
    dict1 = {'host': 'hexlet.io', 'timeout': 50,
             'proxy': '123.234.53.22', 'follow': False}
    dict2 = {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}
    assert parser(file_path1) == dict1
    assert parser(file_path2) == dict2
