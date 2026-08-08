import mgba
import time

def run():
    print("Current Position before start:", mgba.get_coordinates())
    
    # 1. Move to (3, 3) and face (3, 2)
    mgba.press_buttons(["Left", "sleep 200", "Up", "sleep 200"])
    print("Position after moving to counter:", mgba.get_coordinates())
    
    # 2. Interact with clerk and speed through dialogue
    # We press A, then wait, A, then wait, etc.
    # To be extremely safe, we can do a sequence of buttons with sleep 1000 in between
    buttons = [
        "A", "sleep 800",  # Talk to clerk (Welcome...)
        "A", "sleep 800",  # For just 500...
        "A", "sleep 800",  # Join the hunt? Yes/No prompt.
        "A", "sleep 800",  # Selects Yes. That'll be 500...
        "A", "sleep 800",  # We only use...
        "A", "sleep 800",  # Received 30 Safari Balls!
        "A", "sleep 800",  # We'll call you...
        "A", "sleep 800",  # Best of luck!
        "A", "sleep 2500"  # Fade out and warp into Safari Zone Center (15, 25)
    ]
    mgba.press_buttons(buttons)
    
    print("Position after warp attempt:", mgba.get_coordinates())
    # Take a screenshot to verify
    img_path = mgba.take_screenshot()
    print("Screenshot saved to:", img_path)

if __name__ == "__main__":
    run()
