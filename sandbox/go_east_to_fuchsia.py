import mgba
import time

def run():
    print("--- WALKING EAST TO FUCHSIA CITY ---")
    pos = mgba.get_coordinates()
    print("Start position:", pos)
    
    # We are at (40, 9) on Route 18. Walk Right step-by-step.
    # We can walk up to 15 steps Right to find the Fuchsia City map transition!
    for i in range(15):
        mgba.press_buttons(["Right"])
        time.sleep(0.35)
        curr = mgba.get_coordinates()
        print(f"Step {i+1} Right: {curr}")
        if curr['x'] < pos['x']:
            # If our x coordinate became very small (e.g. x=0 or 1), we successfully transitioned into Fuchsia City!
            print(" transitioned to Fuchsia City!")
            break
            
    mgba.take_screenshot()

if __name__ == "__main__":
    run()
