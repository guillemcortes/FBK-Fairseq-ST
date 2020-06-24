import argparse
import csv
import operator
import pickle

def main(args):
    with open(args.pickle, "rb") as fpickle:
        errorids = pickle.load(fpickle)

    with open(args.input, "r") as fin, open(args.output, "w") as fout:
        errorid = errorids.pop(0)
        for index, line in enumerate(fin):
            if index == errorid and errorid is not None:
                try:
                    errorid = errorids.pop(0)
                except IndexError as e:
                    errorid = None
                continue
            fout.write(line)
            


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Count nad/or delete error lines')
    parser.add_argument('input', help='input text file path', type=str)
    parser.add_argument('output', help='output text file path', type=str)
    parser.add_argument('--pickle', help='pickle with rows to be removed file path', type=str)
    args = parser.parse_args()
    main(args)
