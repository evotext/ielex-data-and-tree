#!/usr/bin/env python3
"""
Take data from ielex-130421-ag-cc.txt and transform it into beastling
compatible format with column marking for ascertainment correction. Meanings
from EXCLUDE_MEANINGS are excluded, as are meanings which are missing in more
than 30% of the languages.

Make sure to use the option binarised=True in the beastling configuration.
"""
import argparse
import sys

EXCLUDE_MEANINGS = {"mother", "father", "blow"}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-g", "--glottocode", action="store_true")
    args = parser.parse_args()

    subst = dict() # ielex names to names used in analysis
    lang_names = list() # ordered list of analysis names according to lookup.tsv
    with open("lookup.tsv") as fo:
        next(fo) # header
        for line in fo:
            lang_name, glottocode, ielex_name = line.strip().split("\t")
            if args.glottocode:
                subst[ielex_name] = glottocode
                lang_names.append(glottocode)
            else:
                subst[ielex_name] = lang_name
                lang_names.append(lang_name)

    data = dict() 
    ascertainment = dict() # languages which have at least one observed value for a meaning
    count_attestation = dict() # number of languages with data for each meaning
    with open("ielex-130421-ag-cc.txt") as fo:
        next(fo) # header
        for line in fo:
            row = line.rstrip().split("\t")
            cc, ielex_name = row[0], row[2]
            meaning = cc.split("-")[0]
            data.setdefault(meaning, dict())
            ascertainment.setdefault(meaning, set())
            try:
                lang_name = subst[ielex_name]
                data[meaning].setdefault(cc, set()).add(lang_name)
                ascertainment[meaning].add(lang_name)
                count_attestation.setdefault(meaning, set())
                count_attestation[meaning].add(lang_name)
            except KeyError:
                pass # ignore rows which are not in lookup.tsv

    threshold = len(lang_names) * 0.7
    for meaning, languages in count_attestation.items():
        if len(languages) < threshold:
            EXCLUDE_MEANINGS.add(meaning)

    # print header
    if args.glottocode:
        header = ["glottocode"]
    else:
        header = ["language"]
    for meaning in sorted(data):
        header.append("{}-asc".format(meaning))
        for cc in sorted(data[meaning]):
            header.append(cc)
    print(*header, sep=",")

    # print data
    for lang_name in lang_names:
        row = [lang_name]
        for meaning in sorted(data):
            unobserved = lang_name not in ascertainment[meaning]

            # ascertainment column
            if unobserved:
                row.append("?")
            else:
                row.append("0")

            # data columns
            for cc in sorted(data[meaning]):
                if unobserved:
                    row.append("?")
                else:
                    if lang_name in data[meaning][cc]:
                        row.append("1")
                    else:
                        row.append("0")
        print(*row, sep=",")

    print("EXCLUDED:", *sorted(EXCLUDE_MEANINGS), file=sys.stderr)
    return

if __name__ == "__main__":
    main()
