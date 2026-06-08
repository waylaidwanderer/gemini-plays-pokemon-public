# Post-Safari Zone Route & Progression Plan (Turn 73728)

## Socratic Question 1: Standing at (4, 2) inside the Warden's House (Map 0_158) on Turn 73728, explain why the Gold Teeth remain in your inventory after pressing A multiple times. Since the Warden stands at (4, 1) in the overworld, and your present coordinate is (4, 2), could you be facing the wrong direction, making interaction impossible? How will you test walking Down 1 step to (4, 3), facing UP, and pressing A to talk to him?

### Empirical Analysis:
- On Turn 73728, we are standing at (4, 2) inside the Warden's House (Map 0_158).
- The Warden is standing at (4, 1) directly above us.
- Our Gold Teeth remain in our inventory after pressing A because the player character is currently facing LEFT, not UP!
- In Gen 1, pressing A to talk to an NPC only checks the tile directly in front of the player's facing direction. Because we are facing LEFT, pressing A checks (3, 2) (which is empty), resulting in no interaction with the Warden at (4, 1).
- To resolve this and trigger the dialogue successfully, we must face UP toward (4, 1).
- Testing Method:
  1. We will press 'Up' once from our current position (4, 2). Since (4, 1) is blocked by the Warden, this movement will fail to step forward but WILL successfully turn our player character to face UP and trigger a bump sound.
  2. We will then press 'A' to talk to him while facing UP.
  3. If this still fails, we will test stepping Down 1 step to (4, 3), pressing 'Up' to face UP, and pressing 'A' to initiate dialogue from a distance of one tile.

## Socratic Question 2: Once the Warden gives you HM04 Strength, verify your menu navigation steps to teach it to ROCKY (GEODUDE). Since ROCKY has two open move slots, confirm that no moves will be deleted, and document this seamless process in your scratchpad.

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

- Turn 73790: Currently standing at (5, 1) facing LEFT inside Warden's House. We are directly adjacent to the Warden at (4, 1). We will press A to talk to him. Hypothesis: Since we have the GOLD TEETH in our inventory and are facing him, he will recognize the teeth, thank us, take them, and then reward us with HM04 Strength. Let's execute.

- Turn 73796: Visual analysis of the screen reveals that the old man sprite (the WARDEN) is actually standing at (10, 1) on the right side of the room, while the sprite at (4, 1) is a Youngster. That explains why talking to (4, 1) yielded the youngster's line about the Warden looking vacant!
- To talk to the Warden, we need to stand at (9, 1) facing RIGHT.
- Plan:
  1. Walk Right 4 steps from our current position at (5, 1) to (9, 1).
  2. Verify we are at (9, 1) facing RIGHT.
  3. Press A to talk to the Warden, hand over the Gold Teeth, and get HM04.
Let's execute the 4 steps Right first.

- Turn 73818: Visual breakthrough! The Warden's sprite in Gen 1 is actually the bald man (safari outfit with green pants) who is standing at (0, 2) on the far left side of the room.
- The NPC at (10, 1) is the Warden's grandson (youngster), which is why he spoke in normal English about his grandpa having a speech problem!
- The NPC at (4, 1) is actually the Warden's pet Slowpoke, which is why interacting with him displayed the Slowpoke text!
- Therefore, the real Warden is at (0, 2).
- Currently, we are at (1, 2) facing UP, with a textbox open saying "Crammed full of POKeMON books!".
- Plan:
  1. Press B to dismiss the bookshelf text.
  2. Press Left to face the Warden at (0, 2).
  3. Press A to talk to him, hand over the Gold Teeth, and receive HM04 Strength.
Let's dismiss the text first.