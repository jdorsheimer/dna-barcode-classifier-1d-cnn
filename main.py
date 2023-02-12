from utilities.tensor_utils import one_hot_encode_2d, one_hot_encode_1d

test_sequence = "ATTTGATGTTCATGAT"
print(one_hot_encode_2d(test_sequence))
print(one_hot_encode_1d(test_sequence))