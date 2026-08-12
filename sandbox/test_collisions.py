import time
import bridge

def get_pos():
    pos = bridge.get_coordinates()
    if pos is None:
        return None
    return pos[0], pos[1]

def walk_and_return(direction, opposite):
    pos = get_pos()
    print(f"Current pos before walking {direction}: {pos}")
    bridge.press_buttons([direction, "sleep 400"])
    pos2 = get_pos()
    print(f"Result after walking {direction}: {pos2}")
    
    # If we successfully moved, walk back to the starting tile
    if pos2 != pos:
        print(f"Walked successfully! Returning with {opposite}...")
        bridge.press_buttons([opposite, "sleep 400"])
        return True
    return False

def test_all():
    print("Testing all directions from (27, 24)...")
    # Test LEFT
    test_left = walk_and_return("Left", "Right")
    # Test RIGHT
    test_right = walk_and_return("Right", "Left")
    # Test UP
    test_up = walk_and_return("Up", "Down")
    # Test DOWN
    test_down = walk_and_return("Down", "Up")
    
    print(f"LEFT is {'OPEN' if test_left else 'BLOCKED'}")
    print(f"RIGHT is {'OPEN' if test_right else 'BLOCKED'}")
    print(f"UP is {'OPEN' if test_up else 'BLOCKED'}")
    print(f"DOWN is {'OPEN' if test_down else 'BLOCKED'}")

if __name__ == "__main__":
    test_all()
