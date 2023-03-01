import numpy as np
import pandas as pd
import re

def fasta_to_dataframe(file_path):
    # Initialize an empty list to hold the data
    data = []
    # Open the FASTA file and read the data
    with open(file_path) as f:
        lines = f.readlines()
    # Loop over the lines in the file
    i = 0
    while i < len(lines):
        # Check if this is the start of a new sequence
        if lines[i].startswith('>'):
            # Parse the header line to get the metadata fields
            fields = lines[i].strip().split('|')
            # Extract the sample ID and sequence from the header line and sequence line, respectively
            sample_id = fields[0][1:]
            sequence = ""
            # Increment the line counter and collect the sequence lines until a new header is found
            i += 1
            while i < len(lines) and not lines[i].startswith('>'):
                sequence += lines[i].strip().upper()
                # Replace each non-nucleotide character as '-'
                sequence = clean_dna_sequence(sequence)
                i += 1
            # Construct a dictionary of metadata values
            metadata = {f'specimen_data_{str(j+1).zfill(3)}': value for j, value in enumerate(fields[1:], start=1)}
            # Add the sample ID, sequence, and metadata to the data list
            data.append({'Sampleid': sample_id, 'Sequence': sequence, **metadata})
        else:
            # Skip any non-header lines
            i += 1
    # Create a Pandas DataFrame from the data and return it
    columns = [f'specimen_data_{str(i+1).zfill(3)}' for i in range(len(metadata))]
    return pd.DataFrame(data, columns=['Sampleid', 'Sequence', *columns])

def df_to_tensor(df, max_length):
    from utilities.tensor_utils import one_hot_encode_1d
    # Convert sequences to one-hot encoding and pad them to the maximum length
    n = len(df)
    tensor = np.zeros((n, max_length, 5), dtype=np.float32)
    for i, sequence in enumerate(df['Sequence']):
        one_hot_sequence = one_hot_encode_1d(sequence)
        padding = max_length - len(one_hot_sequence)
        if padding < 0:
            padding = 0
        padded_sequence = np.pad(one_hot_sequence, ((padding, 0), (0, 0)))
        tensor[i, :, :] = padded_sequence
    return tensor

def clean_dna_sequence(dna_seq):
    """
    Given a DNA sequence as a string, replaces any characters that are not 'A', 'T', 'G', 'C', 'N', or '-'
    with a blank '-', and returns the cleaned sequence as a string.
    """
    # Define a regular expression to match any characters that are not 'A', 'T', 'G', 'C', 'N', or '-'
    non_dna_regex = '[^ATGCN-]'
    # Use the sub() method to replace any non-DNA characters with a blank '-'
    cleaned_seq = re.sub(non_dna_regex, '-', dna_seq)
    return cleaned_seq
