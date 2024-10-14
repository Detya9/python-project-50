from gendiff import generate_diff
import pytest


@pytest.mark.parametrize("file_path1, file_path2, formatter, result", [
    (
        'tests/fixtures/file1.json',
        'tests/fixtures/file2.yml',
        'stylish',
        'tests/fixtures/stylish_f1_f2.txt'
    ),
    (
        'tests/fixtures/file1.json',
        'tests/fixtures/file2.yml',
        'plain',
        'tests/fixtures/plain_f1_f2.txt'
    ),
    (
        'tests/fixtures/file2.json',
        'tests/fixtures/file1.yml',
        'stylish',
        'tests/fixtures/stylish_f2_f1.txt'
    ),
    (
        'tests/fixtures/file1.json',
        'tests/fixtures/file2.yml',
        'json',
        'tests/fixtures/json_f1_f2.txt'
    )
])
def test_generate_diff(file_path1, file_path2, formatter, result):
    with open(result, encoding='utf-8') as res:
        answer = res.read().strip()
        assert generate_diff(file_path1, file_path2, formatter) == answer
