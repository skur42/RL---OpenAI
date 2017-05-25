import gym
import numpy as np

def run_episode(env,parameters):
	observation=env.reset()
	totalreward=0

	for _ in range(200):
		env.render()
		action=0 if np.matmul(parameters,observation)<0 else 1
		observation,reward,done,info=env.step(action)

		totalreward+=reward

		if done:
			break
	return totalreward

def train(submit):
	env=gym.make('CartPole-v0')

	noise_scaling=0.1

	parameters=np.random.rand(4)*2 - 1 #initialize weights b/w -1 and 1

	bestreward=0

	for _ in range(10000):
		newparams=parameters+(np.random.rand(4)*2 - 1)*noise_scaling
		reward=run_episode(env,newparams)
		
		print(reward)

		if reward>bestreward:
			bestreward=reward
			parameters=newparams
			if reward==200:
				break

r=train(submit=False)
print(r)