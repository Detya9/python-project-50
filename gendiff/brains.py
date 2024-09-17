import json


def generate_diff(file_path1, file_path2):
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))
    all_keys = sorted({**file1, **file2}.keys())
    res = ['{']
    for key in all_keys:
        if key in file1 and key in file2:
            if file1[key] == file2[key]:
                res.append(f'    {key}: {file1[key]}')
            else:
                res.append(f'  - {key}: {file1[key]}')
                res.append(f'  + {key}: {file2[key]}')
        elif key in file1 and key not in file2:
            res.append(f'  - {key}: {file1[key]}')
        elif key not in file1 and key in file2:
            res.append(f'  + {key}: {file2[key]}')
    res.append('}')
    return '\n'.join(res)
