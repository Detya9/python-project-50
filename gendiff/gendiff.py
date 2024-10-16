from gendiff.file_parser import get_content
from gendiff.formatter.format_choice import apply_format
from gendiff.diff import get_diff


def generate_diff(file_path1, file_path2, format_name='stylish'):
    file1 = get_content(file_path1)
    file2 = get_content(file_path2)
    diff = get_diff(file1, file2, {})
    return apply_format(diff, format_name)
