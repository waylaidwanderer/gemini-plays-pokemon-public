import time
import sys
import bridge

# Set stdout to use utf-8
sys.stdout.reconfigure(encoding='utf-8')

def enter_safari_game():
    print("Enqueuing dialogue buttons to enter Safari Zone...")
    # Send a single comprehensive sequence of A presses and sleeps to talk to clerk and enter!
    bridge.press_buttons([
        "A", "sleep 1000", # Talk to clerk
        "A", "sleep 1000", # Welcome dialogue
        "A", "sleep 1000", # Select YES to join
        "A", "sleep 1000", # Pay ¥500 dialogue
        "A", "sleep 1000", # Receive 30 Safari Balls
        "A", "sleep 1000", # Receive rules explanation
        "A", "sleep 2000"  # Have a great game and warp in!
    ])
    print("Buttons enqueued successfully!")

if __name__ == "__main__":
    enter_safari_game()
