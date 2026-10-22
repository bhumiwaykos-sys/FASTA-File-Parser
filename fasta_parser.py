
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

fasta_file = "sequences.fasta"

for record in SeqIO.parse(fasta_file, "fasta"):
    sequence_id = record.id
    sequence = str(record.seq).upper()
    length = len(sequence)

    if length > 0:
        gc_content = gc_fraction(sequence) * 100
    else:
        gc_content = 0

    print("Sequence ID:", sequence_id)
    print("Sequence Length:", length)
    print("GC Content:", round(gc_content, 2), "%")
    print("--------------------")
