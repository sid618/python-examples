import tensorflow as tf
import numpy as np
import logging

logger = tf.get_logger()
logger.setLevel(logging.ERROR)


celsius_q    = np.array([-40, -10,  0,  8, 15, 22,  38],  dtype=float)
fahrenheit_a = np.array([-40,  14, 32, 46, 59, 72, 100],  dtype=float)

for i,c in enumerate(celsius_q): #The enumerate function is a built-in function that allows you to iterate through a sequence and keep track of the index of each element
  print("{} degrees Celsius = {} degrees Fahrenheit".format(c, fahrenheit_a[i]))

  l0 = tf.keras.layers.Dense(units=1, input_shape=[1])
  model = tf.keras.Sequential([l0])

  model.compile(loss='mean_squared_error', 
              optimizer=tf.keras.optimizers.legacy.Adam(0.9))
  
  history = model.fit(celsius_q, fahrenheit_a, epochs=500, verbose=False)
print("Finished training the model")



print(model.predict([100.0]))
print("These are the layer variables: {}".format(l0.get_weights()))