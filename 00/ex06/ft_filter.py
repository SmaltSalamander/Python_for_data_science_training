

def ft_filter(f: callable or None, iter):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    return [obj for obj in iter if f(obj) is True]
