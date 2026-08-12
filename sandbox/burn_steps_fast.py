import bridge

def burn_fast():
    # Start at (20, 24)
    # 1. Walk Right to (21, 24) (2 actions)
    # 2. Walk Left to (17, 24) (8 actions)
    # 3. Walk Right to (21, 24) (8 actions)
    # We can repeat the Left-Right sequence 5 times.
    # Total actions: 2 + 5 * 16 = 82 actions.
    # Total steps: 1 + 5 * 8 = 41 steps.
    
    buttons = ["Right", "sleep 150"]
    for _ in range(5):
        # 4 steps Left
        buttons.extend(["Left", "sleep 150"] * 4)
        # 4 steps Right
        buttons.extend(["Right", "sleep 150"] * 4)
        
    print(f"Sending sequence of {len(buttons)} button actions to burn {1 + 5*8} steps...")
    res = bridge.press_buttons(buttons)
    print(f"Response: {res}")
    print(f"New coordinates: {bridge.get_coordinates()}")

if __name__ == "__main__":
    burn_fast()
