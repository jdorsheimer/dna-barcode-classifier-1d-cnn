import torch

# one-hot encoding of DNA barcode
def one_hot_encode(barcode):
    alphabet = 'ACGT'
    encoding = [alphabet.index(base) for base in barcode]
    return torch.eye(4)[encoding].T.flatten().float()

# create tensor from one-hot encoding
def to_tensor(barcode_list):
    encoded_list = [one_hot_encode(barcode) for barcode in barcode_list]
    return torch.stack(encoded_list)

#barcode_list = ['AGCT', 'CGTA', ...]
#barcode_tensor = to_tensor(barcode_list)
