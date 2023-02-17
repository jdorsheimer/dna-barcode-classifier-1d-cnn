from utilities.tensor_utils import one_hot_encode_1d, to_tensor
from utilities.model_utils import dna_barcode_CNN_1d


test_sequence = "ATTTGATGTTCATGAT"
# print(one_hot_encode_2d(test_sequence))
print(to_tensor(one_hot_encode_1d(test_sequence)))
#print(to_tensor(one_hot_encode_1d(test_sequence)))


