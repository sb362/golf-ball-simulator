# Golf ball simulator
Updated version of
https://github.com/s-ballantyne/gdp
with a UI

## To-do
- Implement `BallView` which will contain golfball model type, initial conditions, etc.
- Rework `BallController` to accommodate `BallView`
- Implement all golfball models
- Ballistic trajectory plot
- Carry distance against loft angle plot

## Dependencies
- [Python 3](https://www.python.org/)
- [Qt for Python (PySide2)](https://www.qt.io/qt-for-python) for the UI
- [NumPy](https://numpy.org/) for number crunching
- [SciPy](https://scipy.org/) for integration/solving ODEs
- [Matplotlib](https://matplotlib.org/) for plotting results

`pip3 install pyside2 numpy scipy matplotlib`

## Usage
`./main.py` or `python3 main.py`

## License
See [LICENSE](LICENSE)
