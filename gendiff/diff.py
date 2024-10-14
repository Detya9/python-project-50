def get_diff(tree1, tree2, dictionary):
    all_keys = sorted({**tree1, **tree2}.keys())
    for key in all_keys:
        if key not in tree2:
            changes = {'type': 'removed', 'value': tree1[key]}
        elif key not in tree1:
            changes = {'type': 'added', 'value': tree2[key]}
        elif tree1[key] == tree2[key]:
            changes = {'type': 'unchanged', 'value': tree1[key]}
        elif isinstance(tree1[key], dict) and isinstance(tree2[key], dict):  # noqa: E501
            changes = {'type': 'nested', 'value': get_diff(tree1[key], tree2[key], {})}  # noqa: E501
        else:
            changes = {'type': 'changed', 'old': tree1[key], 'new': tree2[key]}  # noqa: E501
        dictionary[key] = changes
    return dictionary
