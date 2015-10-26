# geometry-quoting

## Installation Instructions
In order to install this software, create a virtual environment and then, with it activated do:

```
pip install -r requirements.txt
python setup.py develop
```

And you should be ready to go.


## Usage Instructions
Given a profile in a JSON file: profile.json, to use the calculator to get a quote type the following:

```
python calculate.py quote -f /path/to/profile.json
```

In order to get a quote in which the dimensions of the optimal bounding rectangle have been used type:
```
python calculate.py quote -f /path/tp/profile.json --optimize-rectangle
```

In both cases, the quote is echoed to the command line and is the dollar value estimated for cutting
the profile out of a rectangle of stock.


## Future Improvements

Possible future improvements include:
1. Improving the serializer so that the whole file does not have to be loaded into memory before it is parsed.
2. Identifying areas in the profile which may be problematic to execute in practice.
3. Drawing an image of the profile as it would appear when contained within the optimal bounding box.


## References
1. Numpy Arctan2 [Numpy Arctan2 Documentation](http://docs.scipy.org/doc/numpy/reference/generated/numpy.arctan2.html)
2. Datagenetics Blog Post on Bounding Boxes [Datagenetics](http://www.datagenetics.com/blog/march12014/index.html)
3. Scipy Spatial Convex Hull [Scipy Spatial Documentation on Convex Hull](http://scipy.github.io/devdocs/generated/scipy.spatial.ConvexHull.html)
4. Rotation Matrices [Wikipedia Entry on Rotation Matrices](https://en.wikipedia.org/wiki/Rotation_matrix)
