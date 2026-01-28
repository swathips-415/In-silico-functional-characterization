
# STEP 1: Read XML file & Count Hits

from Bio.Blast import NCBIXML

with open("blast_result.xml") as b:
    blast_record = NCBIXML.read(b)

print("Total BLAST hits:", len(blast_record.alignments))

print("__"*78)

# STEP 2: List All Hits in Order of Similarity

for i, alignment in enumerate(blast_record.alignments):
    print(i, alignment.title)

print("__"*78)

# STEP 3: Identify the best HIT among top three BLAST hits

best_alignment = None
best_evalue = None

print("Checking top three hits to identify the closest hit")

for i in range(3):
    alignment = blast_record.alignments[i]
    hsp = alignment.hsps[0]

    print("Hit number")
    print(i)
    print(alignment.title)
    print("Score")
    print(hsp.score)
    print("E value")
    print(hsp.expect)

    if best_alignment is None:
        best_alignment = alignment
        best_evalue = hsp.expect
    elif hsp.expect < best_evalue:
        best_alignment = alignment
        best_evalue = hsp.expect

print("Selected closest hit")
print(best_alignment.title)
print("Protein length")
print(best_alignment.length)

print("__"*78)

# STEP 4: Select the best HSP from the closest hit

best_hsp = best_alignment.hsps[0]

print("Best HSP from the closest hit")
print("Score")
print(best_hsp.score)
print("E value")
print(best_hsp.expect)

print("__"*78)

# STEP 5: Alignment Interpretation

print("Query Sequence")
print(best_hsp.query)

print("Matched Sequence")
print(best_hsp.sbjct)

print("Alignment Match")
print(best_hsp.match)

if " " in best_hsp.query or " " in best_hsp.sbjct:
    print("Gaps are present in the alignment")

if "+" in best_hsp.match:
    print("Conservative substitutions are present")
else:
    print("No conservative substitutions detected")

print("__"*78)

# STEP 6: Functional Region Mapping

print("Query range:", best_hsp.query_start, "-", best_hsp.query_end)
print("Subject range:", best_hsp.sbjct_start, "-", best_hsp.sbjct_end)

print("__"*78)