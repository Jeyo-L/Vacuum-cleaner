# actions.py
import time

def remove_dirty(env, room):
    print(f"[ACTION] Cleaning Room {room}")
    time.sleep(1)
    env.set_state(room, "clean")

def move(env, current_room):
    next_room = env.other_room(current_room)
    print(f"[ACTION] Moving to Room {next_room}")
    return next_room

def rest(seconds):
    print(f"[REST] Agent resting for {seconds} seconds\n")
    time.sleep(seconds)