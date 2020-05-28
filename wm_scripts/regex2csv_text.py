import re
import argparse
import csv
import operator

def main(args):
    words = {}
    with open(args.input, 'r') as f:
        for line in f:
            matchesiter = re.finditer('\((.*?)\)', line)
            for matchobj in matchesiter:
                try:
                    words[matchobj[0]] += 1
                except KeyError:
                    words[matchobj[0]] = 1

    sortedwords = dict(sorted(words.items(), key=operator.itemgetter(1), reverse=True))

    with open(args.output, 'w', newline='') as csvfile:
        w = csv.DictWriter(csvfile, sortedwords.keys())
        w.writeheader()
        w.writerow(sortedwords)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get path of text to process')
    parser.add_argument('input', help='input text file path')
    parser.add_argument('output', help='output text file path')
    args = parser.parse_args()
    main(args)
