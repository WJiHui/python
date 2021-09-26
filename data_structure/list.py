def reverse(sequence):
    """
    sequence can be list or tuple
    list return <class 'list_reverseiterator'>
    tuple return <class 'reversed'>
    """

    print(reversed(sequence))
    print(type(reversed(sequence)))

    for i in reversed(sequence):
        print(i)


if __name__ == '__main__':
    reverse([1, 2, 3, 4])
    reverse(('a', 'b', 'v', 'd'))
