import torch
import numpy as np

# one-hot encoding of DNA barcode into a 2D matrix
def one_hot_encode_2d(sequence):
    import numpy as np
    mapping = {'A': [1,0,0,0,0], 'T': [0,1,0,0,0], 'G': [0,0,1,0,0], 'C': [0,0,0,1,0], 'N': [0,0,0,0,1], '-':[0,0,0,0,0]}
    encoding = np.array([mapping[letter] for letter in sequence])
    return encoding

# one-hot encoding of DNA barcode into a 1D vector
def one_hot_encode_1d(sequence):
    import numpy as np
    mapping = {'A': [1,0,0,0,0], 'T': [0,1,0,0,0], 'G': [0,0,1,0,0], 'C': [0,0,0,1,0], 'N': [0,0,0,0,1], '-':[0,0,0,0,0]}
    encoding = np.array([mapping[letter] for letter in sequence])
    return encoding.flatten()

# create tensor from one-hot encoding
def one_hot_to_1d_tensor(one_hot_list):
    tensor = torch.from_numpy(np.array(one_hot_list)).float()
    return tensor

def symmetric_padding(tensor, desired_length):
    current_length = tensor.size(0)
    if current_length >= desired_length:
        return tensor
    padding_needed = desired_length - current_length
    padding_left = padding_needed // 2
    padding_right = padding_needed - padding_left
    return torch.nn.functional.pad(tensor, (padding_left, padding_right), mode='constant', value=0)

def stacked_one_hot_1d_tensors(sequence_list):
    from utilities.other_utils import max_length_sequence
    # Calculates the maximum sequence length to pad every sequence to be this length
    stacked_tensor = None  # initialize the stacked tensor to None
    max_length = max_length_sequence(sequence_list)
    # Sets num_chars equal to an integer representing the one-hot encoding mapping, i.e. len([0,0,0,0,0])
    num_chars = 5
    sp_list = []
    for sequence in sequence_list:
        ohe = one_hot_encode_1d(sequence)
        ts = one_hot_to_1d_tensor(ohe)
        sp = symmetric_padding(ts, max_length * num_chars)
        sp_list.append(sp)
    stacked_tensor = torch.stack(sp_list)
    return stacked_tensor
