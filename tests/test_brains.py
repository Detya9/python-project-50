from gendiff import generate_diff


def test_generate_diff():
    json1_path = 'tests/fixtures/file1.json'
    json2_path = 'tests/fixtures/file2.json'
    yml1_path = 'tests/fixtures/file1.yml'
    yml2_path = 'tests/fixtures/file2.yml'
    ans1_path = 'tests/fixtures/file1_diff_file2.txt'
    ans2_path = 'tests/fixtures/file2_diff_file1.txt'
    with open(ans1_path, encoding='utf-8') as ans1, \
            open(ans2_path, encoding='utf-8') as ans2:
        answer1 = ans1.read().strip()
        answer2 = ans2.read().strip()
        assert generate_diff(json1_path, json2_path) == answer1
        assert generate_diff(json2_path, json1_path) == answer2
        assert generate_diff(yml1_path, yml2_path) == answer1
        assert generate_diff(yml2_path, yml1_path) == answer2
