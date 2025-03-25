import time
import random

def artistic_hello_world():
    """Prints 'Hello World' in an artistic, animated way."""

    hello_world = "Hello World"
    colors = ["\033[31m", "\033[33m", "\033[32m", "\033[36m", "\033[34m", "\033[35m"]  # ANSI color codes
    reset = "\033[0m"

    for _ in range(3):  # Repeat the animation a few times
        for char in hello_world:
            color = random.choice(colors)
            print(f"{color}{char}{reset}", end="", flush=True)  # Print with random color and flush
            time.sleep(0.1 + random.uniform(-0.05, 0.05))  # Add slight random delay

        print("\n") #newline
        time.sleep(0.5)

    # Adding a final flourish
    for _ in range(2):
        for char in reversed(hello_world):
            color = random.choice(colors)
            print(f"{color}{char}{reset}", end="", flush=True)
            time.sleep(0.05 + random.uniform(-0.025, 0.025))
        print("\n")
        time.sleep(0.25)

    print("\n")
    print("\033[38;5;208m" + "✨ Finished! ✨" + reset) #orange color

if __name__ == "__main__":
    artistic_hello_world()