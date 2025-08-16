
class VacuumCleaner:
    def __init__(self, dust_type, shape, advantage):
        self.dust_type = dust_type
        self.shape = shape
        self.advantage = advantage
        self.running = False

    def start(self):
        if not self.running:
            self.running = True
            print(f"[START] The {self.shape}-shaped vacuum starts cleaning {self.dust_type}.")
        else:
            print("[INFO] Vacuum is already running.")

    def stop(self):
        if self.running:
            self.running = False
            print(f"[STOP] The {self.shape}-shaped vacuum has stopped.")
        else:
            print("[INFO] Vacuum is already stopped.")

    def left(self):
        print(f"[MOVE] Turning LEFT to cover more {self.dust_type}.")

    def right(self):
        print(f"[MOVE] Turning RIGHT to cover more {self.dust_type}.")

    def dock(self):
        print(f"[DOCK] Returning to docking station. Battery recharging...")

    def description(self):
        print(f" Shape: {self.shape}")
        print(f" Best for: {self.dust_type}")
        print(f" Advantage: {self.advantage}")
        print("-" * 40)

vacuum_options = {
    1: ("Fine Dust", "Circular", "Easily maneuvers around furniture and covers open spaces efficiently."),
    2: ("Pet Hair", "Oval", "Longer coverage path per sweep, great for carpets with pet hair."),
    3: ("Large Debris", "Square", "Can align with walls and corners for maximum debris pickup."),
    4: ("Liquid Spills", "Triangle", "Sharp tip reaches tight corners while absorbing liquid effectively.")
}
print("Select Dust Type for Vacuum Cleaner:")
for key, (dust, shape, adv) in vacuum_options.items():
    print(f"{key}. {dust} → Shape: {shape}")

choice = int(input("Enter choice (1-4): "))
if choice not in vacuum_options:
    print("Invalid choice. Exiting.")
    exit()

dust, shape, adv = vacuum_options[choice]
vacuum = VacuumCleaner(dust, shape, adv)

vacuum.description()


print("Available commands: start, stop, left, right, dock, exit")
while True:
    cmd = input("Enter command: ").strip().lower()
    if cmd == "start":
        vacuum.start()
    elif cmd == "stop":
        vacuum.stop()
    elif cmd == "left":
        vacuum.left()
    elif cmd == "right":
        vacuum.right()
    elif cmd == "dock":
        vacuum.dock()
    elif cmd == "exit":
        print("Exiting vacuum control...")
        break
    else:
        print("[ERROR] Unknown command.")