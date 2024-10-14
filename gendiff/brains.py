from gendiff.file_parser import get_python_dict
from gendiff.formatter.format_choice import choose_format
from gendiff.diff import get_diff


def generate_diff(file_path1, file_path2, format_name='stylish'):
    file1 = get_python_dict(file_path1)
    file2 = get_python_dict(file_path2)
    diff = get_diff(file1, file2, {})
    return choose_format(diff, format_name)
