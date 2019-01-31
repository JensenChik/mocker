def check_count(func):
    def wrapper(*args, **kwargs):
        count = kwargs.get('count')
        if count is None:
            count = args[0]
        assert isinstance(count, int), 'count must be integer'
        assert count > 0, 'count must grater then zero, but now {}'.format(count)
        return func(*args, **kwargs)

    return wrapper


def is_number(val):
    return isinstance(val, int) or isinstance(val, float)


def is_list_of(_type, val):
    assertion = isinstance(val, list)
    for item in val:
        assertion = assertion and isinstance(item, _type)
    return assertion


def len_match(list1, list2):
    return len(list1) == len(list2)


def assert_number_or_list_of_number(val, name):
    assert is_number(val) or is_list_of(int, val) or is_list_of(float, val), \
        '{} must be number or list of number'.format(name)


def check_min_and_max(func):
    def wrapper(*args, **kwargs):
        _min = kwargs.get('min')
        if _min is None:
            _min = args[1]
        assert_number_or_list_of_number(_min, 'min')

        _max = kwargs.get('min')
        if _max is None:
            _max = args[2]
        assert_number_or_list_of_number(_max, 'max')

        if isinstance(_min, list):

            pass
        else:
            if isinstance(_max, list):
                pass
            else:
                assert _max > _min, 'max must grater than min, now max = {}, min = {}'

        assert count > 0, 'count must grater then zero, but now {}'.format(count)
        return func(*args, **kwargs)

    return wrapper
