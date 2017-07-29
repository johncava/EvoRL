import gym
import numpy as np
from itertools import count

# Create the environment
env = gym.make('CartPole-v0')
env.reset()

# Create a Neural Network 
class NN_Agent():
    
    def __init__(self):
        self.W1 = np.random.rand(4,5)
        self.W2 = np.random.rand(5,5)
        self.W3 = np.random.rand(5,2)

    def forward(self, x):
        hidden_layer_1 = x.dot(self.W1)
        hidden_layer_2 = hidden_layer_1.dot(self.W2)
        output = hidden_layer_2.dot(self.W3)
        print output
        return np.argmax(output)

# Create agent
agent = NN_Agent()

# Parameters
max_epochs = 10 

# Start Environment
while True:
    #env.render()
    env.reset()
    # Initial observation
    state, reward, done, _ = env.step(0)
    print "New Entity"
    print "XXXXXXXXXXXXXXXXXXXX"
    while True:
        env.render()
        # Retrieve next action
        print state
        action = env.action_space.sample()
        print action
        # Emulate the chosen action 
        next_state, reward, done, _ = env.step(action)
        if done:
            break

print('Complete')
env.render(close=True)