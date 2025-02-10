def pattern_matching_indexes(dna, substring):
    """
    Find the indexes of all occurrences of substring in dna.
    
    Parameters
    ----------
    dna : str
        A string representing a DNA sequence.
    substring : str
        A string representing a DNA sequence.
    
    Returns
    -------
    indexes : list
        A list of the indexes of all occurrences of substring in dna.
    """
    indexes = []
    for i in range(len(dna) - len(substring) + 1):
        if dna[i : i + len(substring)] == substring:
            indexes.append(i)
    return indexes

indexes = pattern_matching_indexes("GACGATATACGACGATA", "ATA")
for i, index in enumerate(indexes):
    if i < len(indexes) - 1:
        print(index, end=" ")
    else:
        print(index, end="")