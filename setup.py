try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

description = "Tilitools is basically a collection of (non-mainstream) machine learning model and tools with a special focus on" \
              "anomaly detection, one-class learning, and structured data. Furthermore, we emphasize" \
              "simplicity and ease-of-use *not* runtime performance (although we put some effort into optimization)." \
              "Descriptive examples can be found in the notebooks/ and scripts/ sub-directories. "

config = {
    'name': 'tilitools --- tiny little machine learning toolbox',
    'description': description,
    'url': 'https://github.com/nicococo/tilitools',
    'author': 'Nico Goernitz',
    'author_email': 'nico.goernitz@tu-berlin.de',
    'version': '2017.03',
    'install_requires': ['nose','scikit-learn','numpy', 'scipy', 'matplotlib', 'cvxopt', 'numba'],
    'packages': ['tilitools'],
    'package_dir' : {'tilitools': 'tilitools'},
    'classifiers':['Intended Audience :: Science/Research',
                   'Programming Language :: Python',
                   'Topic :: Scientific/Engineering',
                   'Operating System :: POSIX',
                   'Operating System :: Unix',
                   'Operating System :: MacOS',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.7']
}

setup(**config)
