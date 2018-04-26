from gym.envs.registration import register

register(
    id='connect4-rl-v0',
    entry_point='gym_connect4-rl.envs:connect4-rlEnv',
)
register(
    id='connect4-rl-extrahard-v0',
    entry_point='gym_connect4-rl.envs:connect4-rlExtraHardEnv',
)