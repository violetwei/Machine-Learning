# Introduction

Installing an IDE: [PyCharm](https://www.jetbrains.com/pycharm) 

Installing Anaconda, we are going to setup our virtual environment using [Anaconda](https://www.anaconda.com/distribution), 

Open Terminal/Command prompt

Type `conda` to check if it’s installed

### Creating a new virtual environment using anaconda and python 3.6

```
conda create -n tensor python=3.6

# tensor is the name of the new virtual environment created

activate tensor
```

Then install [TensorFlow](https://www.tensorflow.org/) and [Keras](https://keras.io/)

```
pip install tensorflow

pip install sklearn

pip install pickle

pip install numpy

pip install keras
```

Open PyCharm

Create a new Python project called **tensorEnv**

Create *test.py* and add these two lines

```
import tensorflow

import keras
```

Add Project Interpreter

Add Configurations for test.py
