import pytest


@pytest.fixture
def windy_gridworld():
    import gym
    import gym_gridworlds   
    return gym.make('StochasticWindyGridworld-v0')


def test_windy_gridworld_action_space(windy_gridworld):
    assert windy_gridworld.action_space.n == 8


def test_windy_gridworld_reset(windy_gridworld):
    # reset windy_gridworld
    S = windy_gridworld.reset()
    # check that in start state
    assert S == (3, 0)
    # move right
    S, _, _, _ = windy_gridworld.step(1)
    # check movement to right state
    assert (S == (3, 1)) or (S==(4,1)) or (S==(2,1))
    # reset again
    S = windy_gridworld.reset()
    assert S == (3, 0)
