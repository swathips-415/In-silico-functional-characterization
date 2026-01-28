from Bio import SeqIO

fasta_file = "input_sequence.fasta"
record = SeqIO.read(fasta_file, "fasta")
sequence = record.seq
length = len(sequence)

print("Sequence ID:", record.id)
print("Description:", record.description)
print("Sequence Length:", length)
print("First 50 amino acids:", sequence[:50])

amino_acids = {}
for aa in sequence:
    amino_acids[aa] = amino_acids.get(aa, 0) + 1


print("Amino Acid Composition:")
for aa, count in sorted(amino_acids.items()):
    print(f"{aa}: {count}")
