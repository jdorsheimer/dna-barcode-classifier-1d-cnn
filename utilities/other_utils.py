
def unique_char_counts(df, col_name):
    """
    Given a pandas DataFrame and the name of a column containing a sequence,
    returns a dictionary containing each unique character in the sequence
    and their total counts.
    """
    # Get the sequence column as a Series.
    seq_series = df[col_name]
    # Concatenate all sequences into a single string
    all_seq_str = ''.join(seq_series)
    # Count the occurrence of each character
    char_counts = {}
    for char in all_seq_str:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def max_length_sequence(sequences):
    return max(len(s) for s in sequences)


