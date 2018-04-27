from gym.envs.registration import register

register(
    id='connect4rl-v0',
    entry_point='gym_connect4rl.envs:connect4rlEnv',
)
