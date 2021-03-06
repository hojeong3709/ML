'''
아이리스(붓꽃) 데이터에 대한 데이터이다:
1. Sepal Length: 꽃받침의 길이 정보이다.
2. Sepal Width: 꽃받침의 너비 정보이다.
3. Petal Length: 꽃잎의 길이 정보이다.
4. Petal Width: 꽃잎의 너비 정보이다.
Species 꽃의 종류 정보이다.
setosa / versicolor / virginica 의 3종류로 구분된다.
'''

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
import warnings

warnings.filterwarnings('ignore')

iris = datasets.load_iris()
data = iris["data"]

print(data)
x_data = data[:, 1:]
y_data = data[:, :1]

print(x_data.shape)
print(y_data.shape)

features = 3
classes = 1

w = tf.Variable(tf.random_uniform([features, classes]), dtype=tf.float32)
b = tf.Variable(tf.random_uniform([classes]), dtype=tf.float32)

X = tf.placeholder(dtype=tf.float32, shape=[None, features])
Y = tf.constant(y_data, dtype=tf.float32)
# Y = tf.placeholder(dtype=tf.flocat32, shape=[None, 1])

hx = tf.matmul(X, w) + b
cost = tf.reduce_mean(tf.square(hx - Y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

for i in range(1000):
    sess.run(train, feed_dict={X: x_data})
    if not i % 100:
        print(i, sess.run(cost, feed_dict={X: x_data}))

print(sess.run(w))
print(sess.run(b))

# 예측
# Sepal Width, Petal Length, Petal Width
# 3.5 1.4 0.2
predict = sess.run(hx, feed_dict={X: [[3.5, 1.4, 0.2]]})
print(predict)

# 실제값
plt.plot(y_data, 'b--')

# 예측값
plt.plot(sess.run(hx, feed_dict={X: x_data}), "r--")
plt.show()
