import bridge

def enter_safari():
    print("Turning UP and enqueuing safari entry dialogue...")
    bridge.press_buttons([
        "Up", "sleep 500",
        "A", "sleep 1000", # Talk to clerk
        "A", "sleep 1000", # Welcome dialogue
        "A", "sleep 1000", # Select YES to join
        "A", "sleep 1000", # Pay ¥500 dialogue
        "A", "sleep 1000", # Receive 30 Safari Balls
        "A", "sleep 1000", # Receive rules explanation
        "A", "sleep 2000"  # Have a great game and warp in!
    ])
    print("Dialogue buttons enqueued successfully!")

if __name__ == "__main__":
    enter_safari()
