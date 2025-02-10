def count_substring(dna, substring):
    """
    Count the number of times that substring appears in dna.
    
    Parameters
    ----------
    dna : str
        A string representing a DNA sequence.
    substring : str
        A string representing a DNA sequence.
    
    Returns
    -------
    count : int
        The number of times that substring appears in dna.
    """
    count = 0
    for i in range(len(dna) - len(substring) + 1):
        if dna[i : i + len(substring)] == substring:
            count += 1
    return count

substring_count = count_substring("CGCGATACGTTACATACATGATAGACCGCGCGCGATCATATCGCGATTATC", "CGCG")
print(substring_count)