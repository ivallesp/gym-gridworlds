import gym
from gym import spaces
import random

class StochasticWindyGridworldEnv(gym.Env):
    # Added oblicuous and stop moves
    def __init__(self):
        self.height = 7
        self.width = 10
        self.action_space = spaces.Discrete(9)
        self.observation_space = spaces.Tuple((
                spaces.Discrete(self.height),
                spaces.Discrete(self.width)
                ))
        self.moves = {
                0: (-1, 0),  # up
                1: (0, 1),   # right
                2: (1, 0),   # down
                3: (0, -1),  # left
                4: (-1, 1),  # up-right
                5: (-1, -1), # up-left
                6: (1, -1), # down-left
                7: (1, 1), # down-right
                8: (0, 0) # stop 
                }

        # begin in start state
        self.reset()

    def step(self, action):
        if self.S[1] in (3, 4, 5, 8):
            self.S = self.S[0] - 1 + random.randint(-1, 1), self.S[1]
        elif self.S[1] in (6, 7):
            self.S = self.S[0] - 2 + random.randint(-1, 1), self.S[1]
        else:
            self.S = self.S[0] + random.randint(-1, 1), self.S[1]

        x, y = self.moves[action]
        self.S = self.S[0] + x, self.S[1] + y

        self.S = max(0, self.S[0]), max(0, self.S[1])
        self.S = (min(self.S[0], self.height - 1),
                  min(self.S[1], self.width - 1))

        if self.S == (3, 7):
            return self.S, -1, True, {}
        return self.S, -1, False, {}

    def reset(self):
        self.S = (3, 0)
        return self.S
