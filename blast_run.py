import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from Bio.Blast import NCBIWWW
from Bio import SeqIO

record = SeqIO.read("input_sequence.fasta", "fasta")

result_handle = NCBIWWW.qblast(
    program ="blastp",
    database ="swissprot",
    sequence = record.seq,
    expect = 1e-5,
    hitlist_size = 50,
)

with open("blast_result.xml", "w") as out_handle:
    out_handle.write(result_handle.read())

print("BLAST completed successfully")

