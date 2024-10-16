def get_plain(tree, array):
    result = []
    for key, value in tree.items():
        array.append(key)
        if value['type'] == 'nested':
            result.append(get_plain(value['value'], array))
        elif value['type'] == 'changed':
            result.append(f"Property \'{'.'.join(array)}\' was updated."
                          f" From {to_str(value['old'])}"
                          f" to {to_str(value['new'])}")
        elif value['type'] == 'removed':
            result.append(f"Property \'{'.'.join(array)}\' was removed")
        elif value['type'] == 'added':
            result.append(f"Property \'{'.'.join(array)}\' was added with "
                          f"value: {to_str(value['value'])}")
        array.pop()
    return '\n'.join(result)


def to_str(item):
    if isinstance(item, dict):
        return '[complex value]'
    elif item is None:
        return 'null'
    elif isinstance(item, bool):
        return str(item).lower()
    elif isinstance(item, int):
        return item
    else:
        return f"'{item}'"
