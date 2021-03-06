from __future__ import print_function
import gym_TAIL
import numpy as np
from mlfromscratch.utils import to_categorical
from mlfromscratch.deep_learning.optimizers import Adam
from mlfromscratch.deep_learning.loss_functions import SquareLoss
from mlfromscratch.deep_learning.layers import Dense, Dropout, Flatten, Activation, Reshape, BatchNormalization
from mlfromscratch.deep_learning import NeuralNetwork
from mlfromscratch.reinforcement_learning import DeepQNetwork

"""
The script originates from https://github.com/CoderJolly/ML-From-Scratch/blob/master/mlfromscratch/examples/deep_q_network.py

This file is used to verify learning occurs when using another
Python library calls the Python environment. Other popular library
that follows a similar design is TensorFlow.

This script does not appear to solve for an optimal policy and should
only be used for testing purposes until more research is done. Please
refer to this repo for documentation. https://github.com/CoderJolly/ML-From-Scratch
"""

def main():
    dqn = DeepQNetwork(env_name='TAIL-v1',
                       epsilon=0.9,
                       gamma=0.8,
                       decay_rate=0.005,
                       min_epsilon=0.1)

    # Model builder
    def model(n_inputs, n_outputs):
        clf = NeuralNetwork(optimizer=Adam(), loss=SquareLoss)
        clf.add(Dense(64, input_shape=(n_inputs,)))
        clf.add(Activation('relu'))
        clf.add(Dense(n_outputs))
        return clf

    dqn.set_model(model)

    print()
    dqn.model.summary(name="Deep Q-Network")

    dqn.train(n_epochs=500)
    dqn.play(n_epochs=100)


if __name__ == "__main__":
    main()
