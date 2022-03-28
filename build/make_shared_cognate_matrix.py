"""
Builds a matrix of shared cognates for the doculects.
"""

import csv
import itertools
from collections import defaultdict
# Import Python standard libraries
from pathlib import Path

BASE_PATH = Path(__file__).parents[1] / "data"


def main():
    """
    Script entry point.
    """

    # Load data
    with open(BASE_PATH / "ielex.csv", encoding="utf-8") as h:
        data = list(csv.DictReader(h))

    # Collect information for the matrix with a dumb iteration
    cognates = defaultdict(set)
    languages = set()
    concepts = set()
    for entry in data:
        cognates[entry["LANGUAGE"], entry["CONCEPT"]].add(entry["COGNATE"])
        languages.add(entry["LANGUAGE"])
        concepts.add(entry["CONCEPT"])

    # collect per language
    matrix = {}
    for lang1, lang2 in itertools.combinations(sorted(languages), 2):
        # select concepts found in both languages
        concept_subset = [concept for concept in concepts if
                          cognates.get((lang1, concept))
                          and cognates.get((lang2, concept))

                          ]

        # collect the number of cognates in common for all concepts
        total_cognates = 0
        common_cognates = 0
        for concept in concept_subset:
            all_cognates = cognates[lang1, concept].union(cognates[lang2, concept])
            in_common = [cognate for cognate in all_cognates
                         if cognate in cognates[lang1, concept]
                         and cognate in cognates[lang2, concept]]

            total_cognates += len(all_cognates)
            common_cognates += len(in_common)

        # Add to matrix
        matrix[lang1, lang2] = common_cognates / total_cognates

    # build output results
    rows = []
    for lang1 in sorted(languages):
        row = [lang1]
        for lang2 in sorted(languages):
            if lang1 == lang2:
                val = 1.0
            else:
                val = matrix.get((lang1, lang2)) or matrix[lang2, lang1]

            row.append("%.4f" % val)

        rows.append(row)

    # output results
    with open(BASE_PATH / "shared_cognates.tsv", "w", encoding="utf-8") as handler:
        header = [""] + sorted(languages)
        handler.write("\t".join(header))
        handler.write("\n")

        for row in rows:
            handler.write("\t".join(row))
            handler.write("\n")


if __name__ == "__main__":
    main()
