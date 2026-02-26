# randomizer.py
import asyncio
import random

async def randomize(env, agent):
    while True:
        await asyncio.sleep(2)

        other = env.other_room(agent.current_room)

        if agent.phase == "CLEANING":
            p_dirty = 0.6
        else:
            p_dirty = 0.3

        new_state = "dirty" if random.random() < p_dirty else "clean"
        await env.set_state(other, new_state)