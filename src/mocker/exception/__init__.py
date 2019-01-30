def count_must_grater_than_zero(func):
    def wrapper(*args, **kwargs):
        count = kwargs.get('count') or args[0]
        assert count > 0, 'count must grater then zero, but now {}'.format(count)
        return func(*args, **kwargs)

    return wrapper
