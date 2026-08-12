import bridge
import time

def main():
    print("Opening Start Menu...")
    bridge.press_buttons(["Start", "sleep 500"])
    
    print("Moving cursor to ITEM and opening Bag...")
    # Since cursor might be on POKEDEX or ITEM, let's press Down twice and A
    # Wait, in the Start Menu, POKEDEX is at top. ITEM is 2 Down.
    # To be safe, we can press Up 5 times to wrap to bottom (EXIT/OPTION), then Down to POKEDEX, then Down 2 times to ITEM.
    # Actually, when Start Menu opens, cursor is usually on the last selected option (which was ITEM).
    # Let's just press A. If it opens Bag, great. If not, let's close and do it reliably.
    # Actually, let's use a very reliable way:
    # Press B to make sure Start menu is closed.
    bridge.press_buttons(["B", "sleep 300", "Start", "sleep 500"])
    # Now cursor is definitely at the top (POKEDEX) or last selected.
    # In Gen 1, Start menu cursor memory resets when you close and reopen!
    # Yes! Cursor resets to the top (POKEDEX) when you reopen the Start menu!
    # So we press Down twice, then A.
    bridge.press_buttons(["Down", "sleep 200", "Down", "sleep 200", "A", "sleep 800"])
    
    print("Bag opened. We are at the top.")
    # Now we press Down 10 times, pausing after each, and printing coordinates/taking screenshot if we could
    # Since we can't see the screenshots directly, we will just press Down one-by-one to let the harness log the screen!
    for i in range(15):
        print(f"Scrolling down step {i}...")
        bridge.press_buttons(["Down", "sleep 400"])
        
    print("Closing Bag...")
    bridge.press_buttons(["B", "sleep 300", "B", "sleep 300"])
    print("Audit finished.")

if __name__ == "__main__":
    main()
