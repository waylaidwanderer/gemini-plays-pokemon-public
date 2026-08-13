# Script to scroll down 5 more times to check the rest of the PC inventory
import time
import sys
import bridge

sys.stdout.reconfigure(encoding='utf-8')

def main():
    print("=== PC AUDIT: SCROLLING FURTHER DOWN ===")
    
    # Press Down 5 times to scroll the PC list down further
    for i in range(5):
        bridge.press_buttons(["Down", "sleep 400"])
        
    print("Done! Check the screen next turn.")

if __name__ == "__main__":
    main()
