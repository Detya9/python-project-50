from gendiff.file_parser import parser
import gendiff.formatter.stylish as stylish
import gendiff.formatter.plain as plain


def generate_diff(file_path1, file_path2, format_name='stylish'):  # noqa: max-complexity=10
    file1 = parser(file_path1)
    file2 = parser(file_path2)

    def walk(tree1, tree2, dictionary):
        all_keys = sorted({**tree1, **tree2}.keys())
        for key in all_keys:
            if key in tree1 and key in tree2:
                if tree1[key] == tree2[key]:
                    changes = {'type': 'unchanged', 'value': tree1[key]}
                elif isinstance(tree1[key], dict) and isinstance(tree2[key], dict):  # noqa: E501
                    changes = {'type': 'nested', 'value': walk(tree1[key], tree2[key], {})}  # noqa: E501
                else:
                    changes = {'type': 'changed', 'old': tree1[key], 'new': tree2[key]}  # noqa: E501
            elif key in tree1 and key not in tree2:
                changes = {'type': 'removed', 'value': tree1[key]}
            elif key not in tree1 and key in tree2:
                changes = {'type': 'added', 'value': tree2[key]}
            dictionary[key] = changes
        return dictionary

    diff = walk(file1, file2, {})
    match format_name:
        case 'stylish':
            return stylish.get_stylish(diff)
        case 'plain':
            return plain.get_plain(diff, [])
