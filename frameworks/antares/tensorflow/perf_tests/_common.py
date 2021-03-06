# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

import tensorflow as tf
import os, time
import numpy as np

def compare_ops(left, right):
  config = tf.ConfigProto()
  config.gpu_options.allow_growth = True
  with tf.Session(config=config) as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(tf.reshape(left, [-1])))
    print(sess.run(tf.reshape(right,[-1])))
    t_start = time.time()
    sess.run([left, right])
    t_end = time.time()
    eval_time = t_end - t_start
    runs = int(10 / eval_time + 1)

    for i in range(runs):
      sess.run([left, right])
  print('\nRunning finished, please use nvprof/rocprof to evaluate the kernel performance.')

increment_uid = 0

def create_variable(shape, dtype=tf.float32, value=1):
  global increment_uid
  increment_uid += 1
  return tf.get_variable('input%d' % increment_uid, shape, dtype, initializer=tf.constant_initializer(value))

