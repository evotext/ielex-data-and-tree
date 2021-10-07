#!/usr/bin/env python3
import argparse
import sys
import re

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("infile", type=open, help="File in")
    parser.add_argument("outfile", type=argparse.FileType("w"),
            default=sys.stdout, help="File out")
    args = parser.parse_args()

    lookup = list()
    #languages = list()
    with open("lookup.tsv") as fo:
        header = next(fo).strip().split("\t")
        for line in  fo:
            row = dict(zip(header, line.strip().split("\t")))
            lookup.append((row["language"], row["glottocode"]))
            #languages.append(lang)

    # check glottocodes are unique
    assert len(set(e[1] for e in lookup)) == len(lookup)

    text = args.infile.read()
    args.infile.close()
    for lang, glotto in lookup:
        # use word boundaries because some language names are subsets of other language names
        #assert len(set(l for l in languages if lang in l)) == 1
        text = re.sub(r"\b{}\b".format(lang), glotto, text)

    print(text, file=args.outfile)
    args.outfile.close()
    return

if __name__ == "__main__":
    main()
