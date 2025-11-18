def flatten(items):
    """Return a fully flattened list with all None values removed."""
    result = []

    def _walk(value):
        if value is None:
            return
        if isinstance(value, list):
            for v in value:
                _walk(v)
        else:
            result.append(value)

    _walk(items)
    return result
