import re
import argparse
import csv
import operator


def main(args):
    try:
        assert args.input.split('.')[-1] == args.annotations.split('.')[-1], \
        (
            f"Language missmatch between input ({args.input.split('.')[-1]}) "
            f"and annotation ({args.annotations.split('.')[-1]})files."
        )
    except AssertionError as e:
        raise

    annotations = []
    with open(args.annotations) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            annotations.append(row['Annotation'])

    print(annotations)

    regex = "|".join(map(re.escape, annotations))

    with open(args.input, 'r') as infile, open(args.output, 'w') as outfile:
        for line in infile:
            goodline = re.sub(regex, '', line)
            outline = ' '.join(goodline.split()).strip()
            outfile.write(outline + '\n')
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get path of text to process')
    parser.add_argument('-i', '--input', help='input text file path')
    parser.add_argument('-o', '--output', help='output text file path')
    parser.add_argument('-a',   '--annotations', help='annotations csv file path')
    args = parser.parse_args()
    main(args)
