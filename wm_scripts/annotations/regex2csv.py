import re
import argparse
import csv
import operator


class UnknownLangException(Exception):
    pass

def main(args):
    words = {}
    try:
        if args.input.split('.')[-1] == 'en':
            annotations = ('\((.*?)\)', '[A-Z]{2,4}:', 'Narrator:', 'Interviewer:', 'Audience:', 'Man:', 'Woman:', 'Video:', 'Child:')
            regex = "|".join(annotations)
        elif args.input.split('.')[-1] == 'es':
            annotations = ('\((.*?)\)', '[A-Z]{2,4}:', 'Narrador:', 'Audiencia:', 'Público:', 'Hombre:', 'Mujer:', 'Video:', 'Niño:')
            regex = "|".join(annotations)
        else:
            raise UnknownLangException('Unknown input language.')
    except UnknownLangException as e:
        print(e)

    with open(args.input, 'r') as f:
        for line in f:
            matchesiter = re.finditer(regex, line)
            for matchobj in matchesiter:
                try:
                    words[matchobj[0]] += 1
                except KeyError:
                    words[matchobj[0]] = 1

    sortedwords = dict(sorted(words.items(), key=operator.itemgetter(1), reverse=True))
    wordslist = [{'Annotation': k, 'Count': v} for k,v in sortedwords.items()]

    with open(args.output, 'w', newline='') as csvfile:
        w = csv.DictWriter(csvfile, wordslist[0].keys())
        w.writeheader()
        for wdict in wordslist:
            w.writerow(wdict)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get path of text to process')
    parser.add_argument('input', help='input text file path (MUST end with .lang)')
    parser.add_argument('output', help='output text file path (MUST end with .lang)')
    args = parser.parse_args()
    main(args)
