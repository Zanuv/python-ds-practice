def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    s = ''.join(reversed(phrase))
    return s

    # or use slicing
    # return phrase[::-1], slicing is faster
