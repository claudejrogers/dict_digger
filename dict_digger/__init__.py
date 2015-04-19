import functools


def dig(collection, *keys, fail=False):
    """
    Digs into an collection. If anything along the way is not in the collection,
    then simply return None.

    Set fail=True if you want to raise an Error instead of returing None.

    """
    class DiggerException(Exception):
        pass

    def get_item(collection, key):
        try:
            return collection[key]
        except (KeyError, IndexError, TypeError):
            if fail:
                if isinstance(collection, dict):
                    raise KeyError
                else:
                    raise IndexError
            raise DiggerException
    try:
        return functools.reduce(get_item, keys, collection)
    except DiggerException:
        return None
