def _is_number(val):
    return isinstance(val, int) or isinstance(val, float)


def _is_list_of(_type, val):
    assertion = isinstance(val, list)
    for item in val:
        if _type == 'number':
            assertion = assertion and (isinstance(item, int) or isinstance(item, float))
        else:
            assertion = assertion and isinstance(item, _type)
    return assertion


def _len_match(list1, list2):
    return len(list1) == len(list2)


def assert_number_or_list_of_number(val, name):
    assert _is_number(val) or _is_list_of('number', val), \
        '{} must be number or list of number'.format(name)


def assert_len_match(**kwargs):
    for name, val in kwargs.items():
