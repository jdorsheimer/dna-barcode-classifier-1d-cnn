# one-hot encoding of DNA barcode into a 2D matrix
def one_hot_encode_2d(sequence):
    import numpy as np
    mapping = {'A': [1,0,0,0], 'T': [0,1,0,0], 'G': [0,0,1,0], 'C': [0,0,0,1]}
    encoding = np.array([mapping[letter] for letter in sequence])
    return encoding

# one-hot encoding of DNA barcode into a 1D vector
def one_hot_encode_1d(sequence):
    import numpy as np
    mapping = {'A': [1,0,0,0], 'T': [0,1,0,0], 'G': [0,0,1,0], 'C': [0,0,0,1]}
    encoding = np.array([mapping[letter] for letter in sequence])
    return encoding.flatten().tolist()

# create tensor from one-hot encoding
def to_tensor(barcode_list):
    import torch
    encoded_list = [one_hot_encode(barcode) for barcode in barcode_list]
    return torch.stack(encoded_list)

#barcode_list = ['AGCT', 'CGTA', ...]
#barcode_tensor = to_tensor(barcode_list)
