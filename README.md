# Crazy Hot Matrix Plotter
Everything a young man needs to navigate the dating world. 

Source Material: https://youtu.be/pInk1rV2VEg?feature=shared

This repository contains a Python function to plot the Crazy Hot Matrix, a humorous concept popularized by a viral video. The function allows you to visualize data points on a matrix defined by "Hot" and "Crazy" axes, and it categorizes different zones based on these values.

## Features

- **Plotting**: Visualizes data points on the Crazy Hot Matrix with labeled zones.
- **Zone Identification**: Determines the zone where the center of the data points is located using KMeans clustering.
- **Customizable Transparency**: Adjust the transparency of data points.
- **Optional Plotting**: Choose whether to display the plot or just return the zone information.

## Zones

The matrix includes several zones:

- **No Go Zone**: x < 5
- **Danger Zone**: Above the diagonal line for x >= 5
- **Fun Zone**: Below the diagonal line for 5 <= x < 8
- **Girlfriend Zone**: Below the diagonal line for x >= 8 and y >= 7
- **Wife Zone**: x >= 8 and 5 <= y < 7
- **Unicorn Zone**: x >= 8 and y < 5
- **Trany Zone**: y < 4

## Usage

To use the function, import it and pass your data:

```python
from crazyHot import plot_crazy_hot_matrix

hot_vector = [8, 9, 7, 6, 10]
crazy_vector = [5, 6, 4, 7, 8]
area = plot_crazy_hot_matrix(hot_vector, crazy_vector, return_area=True)
print("Center is located in:", area)
```

## Parameters

- `hot_values`: List or array of hot values.
- `crazy_values`: List or array of crazy values.
- `alpha`: Transparency level for the data points (default is 0.5).
- `return_area`: If True, returns the area where the cluster center is located (default is False).
- `plot`: If True, displays the plot (default is True).

## Installation

Clone the repository and install the necessary dependencies:

```bash
git clone https://github.com/alex-m-parvu/crazy-hot-matrix.git
cd crazy-hot-matrix
pip install -r requirements.txt
```

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## Contact

For questions or feedback, please open an issue in the repository.


email: alex_parvu@proton.me

---

This project is intended for educational and entertainment purposes only. It is based on a humorous concept and should not be taken seriously.
