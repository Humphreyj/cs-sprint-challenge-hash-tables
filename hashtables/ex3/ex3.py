def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    table = {}
    result = []
    for i in arrays:
        for k in i:
            if k not in table:
                table[k] = None
            elif k not in result:
                result.append(k)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
