# DNA Barcode Classifier using 1D-CNN

This repository contains code for a 1D-CNN to classify species from DNA barcodes. The DNA barcodes are first one-hot encoded, and then processed by the 1D-CNN to predict the species or taxa.

## Requirements

- PyTorch
- Numpy
- Matplotlib (optional, for visualizing results)

## File Structure

- `data`: contains raw DNA barcode data and preprocessing scripts
- `models`: contains the 1D-CNN architecture, training loop, and helper functions
- `experiments`: contains code for conducting experiments with the 1D-CNN
- `results`: contains results of the experiments, including log files, plots, and performance metrics
- `utilities`: contains utility functions and classes used throughout the project
- `main.py`: main script that ties everything together

## Usage

To run the project, simply run the `main.py` script.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details.

## Acknowledgments

- [PyTorch](https://pytorch.org) for providing the deep learning framework.
- [Barcode of Life Data System](https://v4.boldsystems.org/) for providing the DNA barcode data.
