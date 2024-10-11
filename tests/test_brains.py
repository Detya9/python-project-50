from gendiff import generate_diff


def test_generate_diff():
    json1_path = 'tests/fixtures/file1.json'
    json2_path = 'tests/fixtures/file2.json'
    yml1_path = 'tests/fixtures/file1.yml'
    yml2_path = 'tests/fixtures/file2.yml'
    stylish_path1 = 'tests/fixtures/stylish_f1_f2.txt'
    stylish_path2 = 'tests/fixtures/stylish_f2_f1.txt'
    plain_path1 = 'tests/fixtures/plain_f1_f2.txt'
    with open(stylish_path1, encoding='utf-8') as stylish_1, \
            open(stylish_path2, encoding='utf-8') as stylish_2, \
            open(plain_path1, encoding='utf-8') as plain_1 :
        stylish1 = stylish_1.read().strip()
        stylish2 = stylish_2.read().strip()
        plain1 = plain_1.read().strip()
        assert generate_diff(json1_path, yml2_path) == stylish1
        assert generate_diff(json2_path, yml1_path) == stylish2
        assert generate_diff(json1_path, yml2_path, 'plain') == plain1
