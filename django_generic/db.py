def pks_from_iterable(iterable, unique_output=False):
    """
    Return pks list based on iterable
    :param iterable: list of django model objects OR django queryset
    :param unique_output: if True returned list will be unique
    :return: list of int
    """
    pks = list()
    for obj in iterable:
        try:
            pks.append(int(getattr(obj, 'pk', obj)))
        except (TypeError, ValueError):
            raise TypeError("Iterable %s is not any of Queryset, list with django Model objects or ints" % iterable)
    return list(set(pks)) if unique_output else pks
