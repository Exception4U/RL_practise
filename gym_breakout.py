import gym
import pygame

env = gym.make('Breakout-v0')

cumulatesRewards = []

pygame.init()
pygame.display.set_mode()

for episode in range(10):
    env.reset()
    env.render() # only call this once
    for _ in range(10000):
        env.render() # just update the data
        action = env.action_space.sample()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                action = 2
            elif event.key == pygame.K_RIGHT:
                action = 3
            elif event.key == pygame.K_DOWN:
                action = 1
            else:
                action = 0
        observation, reward, done, info = env.step(action)


        if reward>0:
            cumulatesRewards.append(reward)
        if done:
            break
