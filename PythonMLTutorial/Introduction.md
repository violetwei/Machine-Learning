# Introduction

Download [PyCharm](https://www.jetbrains.com/pycharm) and [Anaconda](https://www.anaconda.com/distribution)

Open Terminal/Command prompt

Type `conda` to check if it’s installed

```
conda create -n tensor python=3.6

activate tensor
```

Then install [TensorFlow](https://www.tensorflow.org/) and [Keras](https://keras.io/)

```
pip install tensorflow

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
