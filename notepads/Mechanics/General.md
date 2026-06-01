# General Mechanics & Controls
- Verified basic game mechanics, controls, and UI behaviors.

## Battle Mechanics:
- Turn-based combat. First starter battle triggers immediately after selecting starter and rival picking theirs.
- Lead Pokémon (first slot) is automatically sent out first.
- HP (Hit Points) represents health. Our starter SQUIRTLE (GEMMY) starts with 20 max HP.
- Moves have PP (Power Points) representing usage limits. SQUIRTLE's Tackle has 35 PP, Tail Whip has 30 PP.
- Benched Healing: Benched healing is 100% functional and allowed in Generation 1 battles. A Potion or other healing item can be used from the bag on a benched (inactive) Pokémon during battle. (Verified on Turn 29275)

## Overworld Navigation:
- PC in player's room can store items. Potion withdrawn on Turn 62 successfully.
- Warps (stairs, doors) transition between maps and are activated by walking onto them.

## Ledge Mechanics:
- Ledges (TYPE_44f6) are one-way drop-offs.
- Verified on Turn 262: Moving South (Down) from (10, 4) to (10, 6) over a ledge at (10, 5) successfully jumps over the ledge.
- Moving North (Up) against a ledge is impassable.
- **Ledge Blockage Mechanic (Verified Turn 6981)**:
  - **Verified Fact**: A ledge jump (such as jumping south from (3, 17) over the (3, 18) ledge to (3, 19) on Mt. Moon 1F) is completely blocked and impassable in both directions if its landing tile (Row 19) is occupied by a solid, impassable obstacle (such as the rock wall at (3, 19)). Ledges cannot be jumped if the landing tile is solid rock/wall.

## Pokémon Center Counter Mechanics:
- Test 4: Left Counter Tile Interaction Check
  - **Hypothesis**: The player can interact with Nurse Joy from (3, 3) facing Up (the left counter tile) to heal their Pokémon, bypassing the blocking NPC at (4, 3).
  - **Methodology**:
    - Turn 1679: Standing at (3, 3) facing Up.
    - Action: Press 'A' to interact with the counter directly above us at (3, 2).
    - Verification: Check if Turn 1687 state shows the Pokémon Center healing dialogue on screen.
  - **Results**:
    - Turn 1687: Successfully verified! The screen shows "Shall we heal your POKéMON?" and the interactive menu `▶HEAL / CANCEL` is open, with the cursor pointing at `▶HEAL`.
    - **Conclusion**: Confirmed! In Generation 1, you can talk to Nurse Joy and heal your Pokémon from the left counter tile (3, 3) facing Up. You do not need to stand in the center (4, 3). This is an incredibly useful mechanic to bypass any NPC blocking the center counter spot.

## Verified Route 2 Mechanics:
### Test 1: Red Flower Tile Collision Check
- **Hypothesis**: Red flower tiles (visually red flowers, system tile type `TYPE_3fe2`) are passable and do not block player movement.
- **Results**: Verified on Turn 1042. Player successfully moved from (4, 66) to (5, 66) (a red flower tile). Red flower tiles are passable.

### Test 2: Route 2 Southern Tall Grass Patch Wild Encounters Check
- **Hypothesis**: Tall grass tiles (TYPE_3fe2) in the southern portion of Route 2 (Columns 8 & 9, Rows 61-67) contain wild Pokémon encounters.
- **Results**: Completed on Turn 1411. Player took 42 cumulative steps on these tiles between Turn 1052 and Turn 1411 without triggering a single wild encounter. Consistently negative. Encounters on this specific grass patch are either disabled or extremely rare.

### Test 3: Route 2 Northern Tall Grass Patch Wild Encounters Check
- **Hypothesis**: The TYPE_fed7 tall grass patch (starting at Y=51, Columns X=4 to X=9) contains active wild encounters.
- **Results**: Completed on Turn 1554. On Turn 1537, at 13 cumulative steps, we triggered a wild Level 4 PIDGEY encounter (captured as BIRBIE). The northern tall grass patch contains active wild encounters.
## Gen 1 Battle Move Menu Structure Insight (Turn 4492 Verification):
- In Pokémon Red/Blue, the battle moves menu is a single vertical column of 4 moves, NOT a 2x2 grid.
  - Position 1 (top): Move 1 (TACKLE)
  - Position 2: Move 2 (TAIL WHIP)
  - Position 3: Move 3 (BUBBLE)
  - Position 4 (bottom): Move 4 (WATER GUN)
- The moves menu remembers its last selected position. If you used Move 2 last round, the cursor starts on Move 2.
- The menu allows wrapping. Pressing Up on the 1st move wraps down to the 4th move. Pressing Down on the 4th move wraps up to the 1st move. Verified on Turn 4492!

## Item Pickup Collision Mechanic:
- **Hypothesis**: Poké Ball items on the floor in Gen 1 are solid sprites that block player movement. To collect them, the player must stand adjacent, face them, and press 'A' to interact, rather than walking onto them.
- **Verification**: On Turn 6803, standing at (28, 5) facing Right towards the Poké Ball item at (29, 5), pressing 'A' successfully collected the item (TM01 - Mega Punch), and the item sprite disappeared, proving that items on the floor are solid sprites in Generation 1.
- **Conclusion**: Floor item sprites are indeed solid and impassable. They must be collected by standing adjacent, facing them, and pressing 'A'.
## Gen 1 Confusion Move PP Consumption (Turn 12533 Verification):
- **Verified Fact**: In Generation 1, if a Pokémon selects a move but hurts itself in confusion instead of attacking, 1 PP is still consumed from the selected move. Verified on Turn 12532/12533: GEMMY selected BITE (starting at 22 PP), hurt itself in confusion, and BITE's PP was successfully reduced to 21 despite the move not executing.

## S.S. Anne Sprite Wrapping and rendering duplicate protocol
- When exploring upper floors on a horizontal edge boundary (such as Column 13 of Map 0_100), Gen 1's engine edge-wraps and duplicates the sprite slots of the adjacent loaded map.
- These rendering artifacts can execute the dialogue script of the underlying RAM sprite slots (e.g., interacting with Bug Catcher at (11, 13) on Map 0_100 executed the Kitchen Sailor's script).
- **Verification Rule:** If an NPC is positioned at the extreme boundary column of an indoor map section, confirm its physical collision and speech script. If it mimics an NPC from another floor, document it as a mirrored duplicate and skip combat/grinding assumptions for that duplicate.

## Randomized ROM Mechanics (Verified Turn 17672):
- **Hidden Items Rule**: In this randomized ROM, standard hidden item locations (such as the S.S. Anne Kitchen trash cans or similar spots) are completely scrambled or empty. To prevent wasting turns, do not systematically search vanilla hidden item spots (including the Vermilion Gym trash cans for items, except when mathematically/mechanically necessary for puzzle progression).

### Gen 1 Inventory Space & Item Collection Mechanics (Verified Turn 40330)
- **Bag Limit**: The inventory bag is capped at exactly 20 unique item slots.
- **Stacking Rule**: Multi-quantity items (like Great Balls, Potions, or Parlyz Heals) occupy a single slot regardless of quantity. Reducing the count of a stack (e.g. from 5 to 4) does NOT free up a bag slot. Only completely depleting or tossing the entire stack frees the slot.
- **Overworld Item Solid Collision**: Overworld item Pokéballs are solid physical objects. Trying to step directly onto them results in a collision. To collect an overworld item, the player must stand on an adjacent floor tile, face the item, and press 'A'.
- **Verification Proof of Work**: Checked on Turn 40321 and 40330 on Silph Co. 4F. Step-by-step adjacent interactions were verified to successfully collect items without colliding.

## Wandering NPC Bottleneck Clearance Protocol
- **Problem**: In Gen 1, friendly wandering NPCs can block 1-tile bottlenecks (such as doorways or narrow corridors), stopping the player from proceeding.
- **Protocol**:
  1. Do NOT repeatedly press blocked directional buttons in place, as this does not effectively clear the way and can waste turns.
  2. **Step Backwards**: Take 1-2 step(s) backwards (away from the NPC) to open up adjacent tiles.
  3. **Provide Space**: By opening up more adjacent empty tiles, the NPC is given the physical space to select a different direction and wander out of the bottleneck.
  4. **Pass through**: Once they step aside, immediately traverse past the bottleneck.