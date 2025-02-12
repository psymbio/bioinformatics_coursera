def compute_skew(sequence):
    """Compute the skew at each position in the sequence."""
    skew = [0]  # Initialize skew array with 0
    for nucleotide in sequence:
        if nucleotide == 'G':
            skew.append(skew[-1] + 1)  # Increment for G
        elif nucleotide == 'C':
            skew.append(skew[-1] - 1)  # Decrement for C
        else:
            skew.append(skew[-1])  # No change for A or T
    return skew

def find_max_skew_positions(sequence):
    """Find the position(s) where the skew attains its maximum value."""
    skew = compute_skew(sequence)
    max_skew = max(skew)  # Find the maximum skew value
    max_positions = [i for i, val in enumerate(skew) if val == max_skew]  # Find all positions with max skew
    return max_positions

# Input sequence
sequence = "GCATACACTTCCCAGTAGGTACTG"

# Compute the positions where skew attains its maximum value
max_skew_positions = find_max_skew_positions(sequence)

# Output the result
print(f"Positions where skew attains its maximum value: {max_skew_positions}")