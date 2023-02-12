
class dna_barcode_CNN_1d(nn.Module):
    import torch
    import torch.nn as nn
    def __init__(self, input_size, num_layers, num_filters):
        super(dna_barcode_CNN_1d, self).__init__()
        self.layers = nn.ModuleList()
        self.layers.append(nn.Conv1d(in_channels=1, out_channels=num_filters, kernel_size=3, padding=1))
        for i in range(1, num_layers):
            self.layers.append(nn.Conv1d(in_channels=num_filters, out_channels=num_filters, kernel_size=3, padding=1))
        self.layers.append(nn.Linear(input_size - (num_layers * 2), 1))
        self.relu = nn.ReLU()

    def forward(self, x):
        x = x.view(x.size(0), 1, -1)
        for layer in self.layers[:-1]:
            x = self.relu(layer(x))
        x = self.layers[-1](x.view(x.size(0), -1))
        return x

