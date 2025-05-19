# Python Graph Visualizer

## Overview

Python Graph Visualizer is a desktop application for creating, visualizing, and analyzing graphs. It supports various types of graphs (directed/undirected) and provides interactive features such as exporting graph metrics to a text file and displaying a condensation graph.

## Features

- Generate directed and undirected graphs
- Export graph metrics: degree, connectivity, components
- Display a condensation graph
- User-friendly GUI built with Tkinter

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/python-graph-visualizer.git
   cd graph-visualizer
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. Enjoy

## Usage

1. Run the main application:

   ```bash
       python main.py
   ```

2. Use the GUI to generate and analyze graphs. Export the metrics if needed.

3. A graph generates within next rules:

   - The seed should contain 4 numbers (`n1, n2, n3, n4`)

   - The formula may contain some of this variables and should return an int/float (e.g. `1.0-n3\*0.01-n4\*0.005-0.15`)

   - Amount of the vertices depends on `n3` and is equal to `n3+10`

4. New analysis text files are exported to a `./logs` directory

## Dependencies

- Python 3.7 or higher

- Tkinter (usually bundled with Python)

## Contributing

Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License.
