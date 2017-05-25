import gym

env = gym.make('CartPole-v0')
env.reset()

def run_episode(env):
	observation=env.reset()
	for t in range(100):
		env.render()
		action=env.action_space.sample()
		observation,reward,done,info=env.step(action)
		print(observation)
		if done:
			print("bakchodi over")
			break

for i_episode in range(20):
	run_episode(env)
	