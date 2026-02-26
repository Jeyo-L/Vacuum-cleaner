# agent.py
import asyncio

class ModelBasedAgent:
    def __init__(self, env, metrics):
        self.env = env
        self.metrics = metrics
        self.current_room = "A"
        self.phase = "CLEANING"
        self.internal_model = {"A": None, "B": None}

    async def perceive(self):
        state = await self.env.get_state(self.current_room)
        self.internal_model[self.current_room] = state
        return state

    def update_model(self, room, state):
        self.internal_model[room] = state

    async def clean(self):
        await asyncio.sleep(1)
        await self.env.set_state(self.current_room, "clean")
        self.update_model(self.current_room, "clean")
        self.metrics.reward_clean()

    async def move(self):
        self.metrics.reward_move()
        self.current_room = self.env.other_room(self.current_room)

    async def act(self):
        percept = await self.perceive()

        if percept == "dirty":
            await self.clean()
        else:
            await self.move()

    async def run(self):
        while True:
            self.phase = "CLEANING"
            self.metrics.start_cycle()
            start = asyncio.get_event_loop().time()

            while asyncio.get_event_loop().time() - start < 10:
                if await self.env.both_clean():
                    self.metrics.reward_goal()
                    break
                await self.act()
                await asyncio.sleep(1)

            self.phase = "RESTING"
            self.metrics.time_penalty()
            await asyncio.sleep(5)
            self.metrics.report()