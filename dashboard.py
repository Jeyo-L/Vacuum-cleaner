# dashboard.py
import asyncio
import os

async def render(env, agent, metrics):
    while True:
        await asyncio.sleep(1)

        rooms = await env.snapshot()
        os.system("clear")

        print("========= VACUUM WORLD DASHBOARD =========\n")

        for r in ["A", "B"]:
            marker = "🤖" if agent.current_room == r else " "
            state = "🟢 CLEAN" if rooms[r] == "clean" else "🔴 DIRTY"
            print(f"Room {r}: {state} {marker}")

        print("\n-------------- AGENT STATUS --------------")
        print(f"Phase        : {agent.phase}")
        print(f"Belief State : {agent.internal_model}")

        print("\n-------------- METRICS -------------------")
        print(f"Cleans       : {metrics.clean_count}")
        print(f"Goals        : {metrics.goal_count}")
        print(f"Total Reward : {metrics.total_reward}")

        print("\n==========================================\n")