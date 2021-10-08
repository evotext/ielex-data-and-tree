"""
Builds a NEXUS file form a long-table format CSV.
"""

import csv
from pathlib import Path
from collections import defaultdict

BASE = Path(__file__).parents[1] / "data"


with open(BASE / "ielex.csv", encoding="utf-8") as h:
    data = list(csv.DictReader(h))

taxa = sorted(set([row["LANGUAGE"] for row in data]))

cogs = defaultdict(list)
all_cogs = defaultdict(set)
for row in data:
    cogs[row["LANGUAGE"], row["CONCEPT"]].append(row["COGNATE"])
    all_cogs[row["CONCEPT"]].add(row["COGNATE"])

all_cogs = {key: sorted(value) for key, value in all_cogs.items()}

charstates = []
assumptions = []
cur_idx = 1
for cog in sorted(all_cogs):
    value = all_cogs[cog]
    k = value[0].split("_")[0]

    charstates.append(f"{k}_ascertainment")
    for sub in value:
        charstates.append(sub)

    end_idx = cur_idx + len(value)
    assumptions.append([cog, cur_idx, end_idx])
    cur_idx = end_idx + 1

matrix = {}
for taxon in taxa:
    buf = ""
    for concept in sorted(all_cogs):
        buf += "0"  # ascert
        cogids = all_cogs[concept]

        # if empty
        if len(cogs[taxon, concept]) == 0:
            buf += "?" * len(cogids)
        else:
            vec = [cogid in cogs[taxon, concept] for cogid in cogids]
            buf += "".join([["0", "1"][v] for v in vec])

    matrix[taxon] = buf

############

taxon_len = max([len(taxon) for taxon in taxa])

nexus = ""
nexus += "#NEXUS\n\n"
nexus += "BEGIN DATA;\n"
nexus += "\tDIMENSIONS NTAX=%i NCHAR=%i;\n" % (len(taxa), len(matrix[taxa[0]]))
nexus += '\tFORMAT DATATYPE=STANDARD MISSING=? GAP=- SYMBOLS="01";'
nexus += "\tCHARSTATELABELS\n"
nexus += ",\n".join(["\t\t%i %s" % (idx + 1, cs) for idx, cs in enumerate(charstates)])
nexus += "\n;\n"
nexus += "MATRIX\n"
for taxon, vector in matrix.items():
    label = taxon.ljust(taxon_len + 4)
    nexus += "%s %s\n" % (label, vector)
nexus += ";\n"
nexus += "END;\n\n"

nexus += "begin assumptions;\n"
for assump in assumptions:
    v = all_cogs[assump[0]][0].split("_")[0]
    nexus += "\tcharset %s = %i-%i;\n" % (v, assump[1], assump[2])
nexus += "end;\n\n"
print(nexus)
