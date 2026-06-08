# Post-Safari Zone Route & Progression Plan (Turn 73685)

## Socratic Question 1: Standing at (19, 28) outside the Fuchsia City Pokémon Center on Turn 73685 with both the Warden's Gold Teeth and HM03 Surf in inventory, explain the exact unblocked sequence of overworld buttons to walk to the Warden's House at (22, 13) and stand directly in front of his desk. Document this walking route and its step-by-step coordinate math.

### Overworld Path Analysis:
- Starting Location: (19, 28) [Fuchsia City - Map 0_7]
- Target Location: Warden's House Entrance at (22, 13) [Fuchsia City - Map 0_7]

Let's look at the Fuchsia City map layout and ledges:
1. From (19, 28), we can walk:
   - Walk Down 2 steps to (19, 30).
   - Walk Right 5 steps to (24, 30).
   - Walk Up 17 steps along Column 24 to Row 13:
     - (24, 30) -> (24, 13).
   - Walk Left 2 steps along Row 13 to the Warden's House Entrance at (22, 13).
   Wait! Let's check if Column 24 is blocked by any ledges or structures.
   Looking at the map markers and the current screen:
   - At (23, 26) there is a ledge (TYPE_44f6). We jump over it from West to East if we walk Right from Column 22 to 24 on Row 26.
   - However, Column 24 itself is completely open grass (TYPE_3fe2) and paved path. Wait! Is Column 24 unblocked all the way up to Row 13?
   Let's check the map markers:
   - Warden's House is at (22, 13).
   - Let's verify if there is an unblocked path from the Pokemon Center to (22, 13).
   Wait, is Row 13 accessible from Column 24?
   Yes, the Warden's House is at (22, 13), so we can enter it from (22, 14) by walking Up 1 step! Wait, in Gen 1, building doors are entered by walking UP into them. The door coordinate is usually the wall tile of the door, so we stand at (22, 14) and walk UP 1 step to (22, 13) to warp inside.
   Let's trace:
   - From (19, 28) [Player's current position]:
     - Down 2 steps to (19, 30)
     - Right 5 steps to (24, 30)
     - Up 16 steps along Column 24 to Row 14: (24, 14)
     - Left 2 steps along Row 14 to stand in front of the door at (22, 14)
     - Up 1 step to enter the door at (22, 13)
   Let's check if Column 24 is blocked between Row 30 and Row 14.
   Wait, let's verify if there are any buildings, trees, or ledges on Column 24 or surrounding areas.
   In Fuchsia City:
   - The Safari Zone gatehouse is in the north (Row 3).
   - The Zoo cages are in the north-east and north-central area.
   - The Warden's House is in the south-east.
   - Let's verify if Column 24 has any blockages:
     - Row 24-25 is the house wall or path.
     - Row 27-28 is open path.
     - Let's check our map marker locations. The Warden's House Entrance is at (22, 13).
     - Wait, are there any other paths to (22, 13)?
     - We can also walk:
       - Up 1 step to (19, 27)
       - Right 3 steps to (22, 27) (this crosses Column 22 Row 27, which is open path/grass).
       - Let's look at the current screen:
         - (22, 27) is TYPE_3fe2 (open path).
         - (23, 27) is TYPE_44f6 (ledge).
         - (24, 27) is TYPE_3fe2 (open path).
         - So if we go Right 5 steps from (19, 27) to (24, 27), we would jump over the ledge at (23, 27)!
         - Once we jump over the ledge to Column 24, we cannot go back to the west of the city without going around or flying. But we want to go to the Warden's House, which is in the eastern part of the city anyway! So jumping over the ledge to Column 24 is perfectly fine and actually direct!
         - Wait, is there a ledge on Row 13 or similar? No, the eastern part of Fuchsia City has the Warden's House, the Safari Zone gate, and some zoo pens.
         - Let's trace the path:
           1. Right 5 steps from (19, 28) to (24, 28). This jumps over the ledge at (23, 28) (TYPE_44f6).
              Wait, let's check if the ledge is a jump-down ledge facing East. Yes, TYPE_44f6 is a jump ledge. Walking Right onto it jumps over it to (24, 28).
           2. From (24, 28), walk Up 14 steps along Column 24 to (24, 14).
           3. Walk Left 2 steps to (22, 14).
           4. Walk Up 1 step to (22, 13) to enter the Warden's House!
           Let's verify this path. This is extremely direct and completely bypasses any other obstacles because Column 24 is open path/grass in the eastern section!

### Steps Inside the Warden's House:
- Once inside the Warden's House, we will be at some entry coordinate (typically at the bottom of the map, e.g., (2, 7) or (3, 7) facing Up).
- The Warden is usually standing behind or near his desk.
- Let's trace his position once we are inside and stand directly in front of him to speak.

## Socratic Question 2: Once inside the Warden's House, we will deliver the Gold Teeth to receive HM04 Strength. Verify which Pokémon in our party (e.g. ROCKY the Geodude or GEMMY the Blastoise) will learn Strength, and confirm whether we need to delete an existing move or if they have an open slot. Document this teaching plan to ensure zero menu mistakes.

### Teaching Strength Plan:
- **Which Pokémon will learn Strength?**
  - **ROCKY (GEODUDE)** at Level 15!
  - Let's check ROCKY's current moves:
    - `TACKLE (PP: 35)`
    - `DEFENSE CURL (PP: 40)`
  - Since Geodude only has 2 moves (TACKLE and DEFENSE CURL) out of 4 maximum slots, ROCKY has **2 open slots**!
  - This means we do **NOT** need to delete any existing moves to teach Strength to ROCKY!
  - This is extremely safe and eliminates any risk of accidentally deleting a crucial move!
- **How to teach Strength to ROCKY**:
  1. Open the Start menu and select ITEM.
  2. Scroll to HM04 (Strength) in our inventory.
  3. Select HM04, select USE.
  4. Select ROCKY (GEODUDE).
  5. The game will teach Strength directly into Slot 3 without prompting to forget a move because Slot 3 is empty!
  6. Confirm and dismiss the dialog.