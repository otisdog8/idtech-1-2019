#IMPORTS
import tensorflow as tf
import matplotlib.pyplot as plt
#Graph reset
tf.reset_default_graph()
#Input and output
input_data = tf.placeholder(dtype=tf.float32, shape=None)
output_data = tf.placeholder(dtype=tf.float32, shape=None)
#Parameters to change
slope = tf.Variable(100, dtype=tf.float32)
intercept = tf.Variable(100, dtype=tf.float32)
#Equation
model_operation = slope * input_data ** 2 + intercept
#Error and loss calculations
error = model_operation - output_data
squared_error = tf.square(error)
loss = tf.reduce_mean(squared_error)

init = tf.global_variables_initializer()
#GradientDescentOptimizer
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.005)
train = optimizer.minimize(loss)



#generate y_values
def function(xvals):
    yvals = []
    for i in xvals:
        yvals.append(2 * i ** 2 + 5)
    return yvals
x_values = [0,1, 2, 3, 4, 5]
y_values = function(x_values)

with tf.Session() as sess:
    sess.run(init)
    for i in range(10000):
        sess.run(train, feed_dict={input_data:x_values, output_data:y_values})
        if i % 100 == 0:
            print(sess.run([slope, intercept]))
            plt.plot(x_values, sess.run(model_operation, feed_dict={input_data:x_values}))

    print(sess.run(loss, feed_dict={input_data:x_values, output_data:y_values}))
    plt.plot(x_values, y_values, 'ro', 'Training Data')
    plt.plot(x_values, sess.run(model_operation, feed_dict={input_data:x_values}))

    plt.show()
