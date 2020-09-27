import argparse


def give_args():
    parser = argparse.ArgumentParser(description='Ping script')
    parser.add_argument("--query", action="store", dest="query")
    args = parser.parse_args()
    query = args.query

    return query



def divide_to_batches(data: list, count):
    batches = []
    for n in range(0, len(data), count):
        batches.append(data[n : n + count])

    return batches

