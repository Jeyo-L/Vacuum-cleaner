# environment.py
import asyncio

class Environment:
    def __init__(self):
        self.rooms = {"A": "dirty", "B": "dirty"}
        self.lock = asyncio.Lock()

    async def get_state(self, room):
        async with self.lock:
            return self.rooms[room]

    async def set_state(self, room, state):
        async with self.lock:
            self.rooms[room] = state

    async def snapshot(self):
        async with self.lock:
            return dict(self.rooms)

    def other_room(self, current):
        return "B" if current == "A" else "A"

    async def both_clean(self):
        async with self.lock:
            return all(v == "clean" for v in self.rooms.values())