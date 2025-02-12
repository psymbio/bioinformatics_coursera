def hamming_distance(u, v):
    """
    Compute the Hamming distance between two strings of equal length.

    Parameters
    ----------
    u : str
        A string.
    v : str
        A string.
    
    Returns
    -------
    distance : int
        The Hamming distance between u and v.
    """
    distance = 0
    for i in range(min(len(u), len(v))):
        if u[i] != v[i]:
            distance += 1
    return distance

distance = hamming_distance("CTACAGCAATACGATCATATGCGGATCCGCAGTGGCCGGTAGACACACGT", 
                            "CTACCCCGCTGCTCAATGACCGGGACTAAAGAGGCGAAGATTATGGTGTG")
print(distance)