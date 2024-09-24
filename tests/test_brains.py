from gendiff import generate_diff


def test_generate_diff():
    file1_path = 'gendiff/file1.json'
    file2_path = 'gendiff/file2.json'
    ans1_path = 'tests/fixtures/file1_diff_file2.txt'
    ans2_path = 'tests/fixtures/file2_diff_file1.txt'
    with open(ans1_path, encoding='utf-8') as ans1, \
            open(ans2_path, encoding='utf-8') as ans2:
        answer1 = ans1.read().strip()
        answer2 = ans2.read().strip()
        assert generate_diff(file1_path, file2_path) == answer1
        assert generate_diff(file2_path, file1_path) == answer2
