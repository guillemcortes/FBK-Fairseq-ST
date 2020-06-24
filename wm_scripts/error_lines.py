import argparse
import csv
import operator
import pickle

def main(args):
    error_ids = []
    error_count = 0
    fin_line_count = 0
    with open(args.input, 'r') as fin, open(args.output, 'w') as fout:
        for line in fin:
            fin_line_count += 1
            if 'Error in' in line:
                error_ids.append(int(line.split()[-1]))
                error_count += 1
                continue
            fout.write(line)
    
    percent = round(100*(error_count/fin_line_count),2)
    print(f"({percent}%) {error_count} Error lines out of {fin_line_count} input lines.")

    if args.errorids:
        with open(args.errorids + ".txt", 'w') as ferror:
            ferror.write(f"Error lines:\t{error_count}\n")
            ferror.write(f"Total lines:\t{fin_line_count}\n")
            ferror.write(f"% error lines:\t{percent}%\n")
            ferror.write(f"Error ids:\t{error_ids}\n")
        
        with open(args.errorids + ".pickle", "wb") as fids:
            pickle.dump(error_ids, fids)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Count nad/or delete error lines')
    parser.add_argument('input', help='input text file path', type=str)
    parser.add_argument('output', help='output text file path', type=str)
    parser.add_argument('--errorids', help='error ids file path', type=str)
    args = parser.parse_args()
    main(args)
