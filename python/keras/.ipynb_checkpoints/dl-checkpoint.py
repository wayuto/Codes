from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 50)
n = np.random.normal(0, 1.5, x.shape)
y = 2 * x + n
print(x, y, n)

model = keras.Sequential()
model.add(layers.Dense(1, input_dim=1))
model.compile(
    optimizer='adam',
    loss='mse'
)
model.summary()

from time import time
s = time()
model.fit(x, y, epochs=1000)
print(time()-s)
