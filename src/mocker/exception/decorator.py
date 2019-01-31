from assertion import assert_number_or_list_of_number


def first_not_none(*vals):
    for val in vals:
        if val is not None:
            return val


def check_count(func):
    def wrapper(*args, **kwargs):
        count = first_not_none(kwargs.get('count'), args[0])
        assert isinstance(count, int), 'count must be integer'
        assert count > 0, 'count must grater then zero'
        return func(*args, **kwargs)

    return wrapper


def check_min_and_max(func):
    def wrapper(*args, **kwargs):
        _min = first_not_none(kwargs.get('min'), args[1])
        _max = first_not_none(kwargs.get('max'), args[2])

        assert_number_or_list_of_number(_min, 'min')
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
