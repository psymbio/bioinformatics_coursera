def most_freq_kmer_polymer(dna, k):
    """
    Find the most frequent k-mer in a DNA sequence.

    Parameters
    ----------
    dna : str
        A string representing a DNA sequence.
    k : int
        The length of kmer to search for.
    
    Returns
    -------
    most_freq_kmer : list
        A list of the most frequent k-mers in dna.
    """
    kmer_dict = {}
    for i in range(len(dna) - k + 1):
        kmer = dna[i : i + k]
        if kmer in kmer_dict:
            kmer_dict[kmer] += 1
        else:
            kmer_dict[kmer] = 1
    max_count = max(kmer_dict.values())
    return [kmer for kmer, count in kmer_dict.items() if count == max_count]

most_freq_3mer_polymer = most_freq_kmer_polymer("CGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA", 3)
print(most_freq_3mer_polymer)