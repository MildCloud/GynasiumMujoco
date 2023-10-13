import gymnasium as gym
import time
env = gym.make('InvertedPendulum-v4', render_mode="human")

observation, info = env.reset(seed=42)
env.render()
print(env.action_space.low[0], env.action_space.high[0])
while(1):
    action = env.action_space.sample()
    # print(action.shape)
    observation, reward, terminated, truncated, info = env.step(action)
    # time.sleep(0.5)

    if terminated or truncated:
        observation, info = env.reset()
env.close()