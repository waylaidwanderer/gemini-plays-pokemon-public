import mgba
import time

def heal():
    print("Talking to Nurse Joy...")
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    
    print("Advancing: Welcome to our...")
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    
    print("Advancing: We heal your POKéMON...")
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    
    print("Selecting YES on the heal menu...")
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    
    print("Advancing: OK, I'll take your...")
    mgba.press_buttons(["A"])
    time.sleep(5.5)  # Wait for the healing animation and music
    
    print("Advancing: Thank you for waiting...")
    mgba.press_buttons(["A"])
    time.sleep(1.5)
    
    print("Advancing: We hope to see you again...")
    mgba.press_buttons(["A"])
    time.sleep(1.0)
    
    print("Done!")

heal()
