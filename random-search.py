import gym
import numpy as np

def run_episode(env,parameters):
	observation=env.reset()
	total_reward=0

	for _ in range(200):
		env.render()
		action =0 if np.matmul(observation,parameters)<0 else 1
		observation,reward,done,info=env.step(action)
		total_reward+=reward

		if done:
			break

	return total_reward

def random(submit):
	best_params=None
	best_reward=0
	env=gym.make('CartPole-v0')

	for _ in range(10000):
		parameters=2*np.random.random(4)-1
		reward=run_episode(env,parameters)

		print(reward)

		if reward>best_reward:
			best_reward=reward
			best_params=parameters

			if reward==200:
				break

r=random(submit=False)
print(r)