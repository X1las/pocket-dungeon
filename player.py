import threading
import time

# Player class
class Player:
    def __init__(self, name, pockets = 2, population = 10, x = 0.0, y = 0.0, speed = 1):
        self.x = x
        self.y = y
        self.name = name
        self.pockets = pockets
        self.population = population
        self.speed = speed
        self.move_distance = 1
        self.move_orders = 0
        self.inventory = []
    
    def move(self, dx, dy, times):
        self.move_orders += 1
        for i in range(times):
            self.x += dx/self.move_orders
            self.y += dy/self.move_orders
            time.sleep(self.speed)
        self.move_orders -= 1

    def move_order(self, targx, targy):
        dx = targx - self.x
        dy = targy - self.y
        distance = (dx**2 + dy**2)**0.5
        times = int(distance // self.move_distance)
        dx = (dx / distance) * self.move_distance
        dy = (dy / distance) * self.move_distance
        threading.Thread(target=self.move, args=(dx, dy, times)).start()
        print(f"{self.name} moved to {self.x}, {self.y}.")
    