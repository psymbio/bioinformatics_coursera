def count_substring_with_k_mutations(dna, substring, k):
    """
    Count the number of times a substring appears in a DNA sequence with at most k mutations.

    Parameters
    ----------
    dna : str
        A string representing a DNA sequence.
    substring : str
        A string representing a DNA substring.
    k : int
        The maximum number of mutations allowed.

    Returns
    -------
    count : int
        The number of times substring appears in dna with at most k mutations.
    """
    count = 0
    for i in range(len(dna) - len(substring) + 1):
        mutations = 0
        for j in range(len(substring)):
            if dna[i + j] != substring[j]:
                mutations += 1
            if mutations > k:
                break
        if mutations <= k:
            count += 1
    return count

substring_count = count_substring_with_k_mutations("CGTGACAGTGTATGGGCATCTTT", "TGT", 1)
print(substring_count)