
def divide_to_batches(data: list, count):
    batches = []
    for n in range(0, len(data), count):
        batches.append(data[n : n + count])

    return batches