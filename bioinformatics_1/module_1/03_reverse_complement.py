def reverse_complement(dna):
    """
    Find the reverse complement of a DNA sequence.

    Parameters
    ----------
    dna : str
        A string representing a DNA sequence.
    
    Returns
    -------
    reverse_complement : str
        The reverse complement of dna.
    """
    reverse_complement_dna = ""
    for i in range(len(dna)):
        if dna[i] == "A":
            reverse_complement_dna += "T"
        elif dna[i] == "T":
             reverse_complement_dna += "A"
        elif dna[i] == "C":
             reverse_complement_dna += "G"
        elif dna[i] == "G":
             reverse_complement_dna += "C"
    return reverse_complement_dna[::-1]

reverse_complement_dna = reverse_complement("GCTAGCT")
print(reverse_complement_dna)