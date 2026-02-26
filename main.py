# main.py
import asyncio
from environment import Environment
from agent import ModelBasedAgent
from randomizer import randomize
from dashboard import render
from metrics import Metrics

async def main():
    env = Environment()
    metrics = Metrics()
    agent = ModelBasedAgent(env, metrics)

    await asyncio.gather(
        agent.run(),
        randomize(env, agent),
        render(env, agent, metrics)  # pass metrics here
    )

if __name__ == "__main__":
    asyncio.run(main())
    
    

#https://github.com/Jeyo-L/vacuum-cleaner.git