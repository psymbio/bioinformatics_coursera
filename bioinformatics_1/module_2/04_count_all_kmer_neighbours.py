from itertools import product

def hamming_distance(s1, s2):
    """Calculate the Hamming distance between two strings."""
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

def d_neighborhood_size(pattern, d):
    """Calculate the number of k-mers in the d-neighborhood of a given pattern."""
    k = len(pattern)
    alphabet = "ACGT"
    neighborhood = set()
    
    # Generate all possible k-mers
    for positions in product(range(k), repeat=d):  # Positions to mutate
        for mutations in product(alphabet, repeat=d):  # Nucleotides to substitute
            neighbor = list(pattern)
            for i, pos in enumerate(positions):
                neighbor[pos] = mutations[i]
            neighbor = ''.join(neighbor)
            neighborhood.add(neighbor)
    
    # Include the original pattern
    neighborhood.add(pattern)
    
    return len(neighborhood)

# Input
pattern = "CCAGTCAATG"
d = 1

# Calculate the size of the 2-neighborhood
neighborhood_size = d_neighborhood_size(pattern, d)
print(f"Number of 5-mers in the {d}-neighborhood of {pattern}: {neighborhood_size}")