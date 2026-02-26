# metrics.py
import time

class Metrics:
    def __init__(self):
        self.total_reward = 0
        self.clean_count = 0
        self.goal_count = 0
        self.start_time = None

    def start_cycle(self):
        self.start_time = time.time()

    def reward_clean(self):
        self.total_reward += 10
        self.clean_count += 1

    def reward_move(self):
        self.total_reward -= 1

    def reward_goal(self):
        self.total_reward += 50
        self.goal_count += 1

    def time_penalty(self):
        self.total_reward -= 5

    def report(self):
        print("\n===== METRICS =====")
        print(f"Cleans: {self.clean_count}")
        print(f"Goals: {self.goal_count}")
        print(f"Total Reward: {self.total_reward}")
        print("===================\n")