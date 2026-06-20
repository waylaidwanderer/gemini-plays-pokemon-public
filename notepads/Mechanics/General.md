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

## Wandering NPC Bottleneck Clearance Protocol (Markov-Verified)
- **Problem**: Friendly wandering NPCs blocking a 1-tile bottleneck (e.g. column 14 leading to row 9 on 10F).
- **Mathematical Analysis of Random Walk (Markov Chain)**:
  - From State 9 (Y=9), the NPC chooses one of 4 cardinal directions (25% each).
  - Since North and East are blocked by walls, and West (13, 9) is the exit, their only passable paths are West (exit) and South (Y=10).
  - If we stand at Y=K (blocking the corridor at K), the available states are 9, 10, ..., K-1.
  - Using absorption Markov analysis, the expected steps to exit starting from State 9 is exactly 4 * (K - 9).
    - Player at Y=10 (Corridor length 1): Expected steps to exit = 4.00
    - Player at Y=11 (Corridor length 2): Expected steps to exit = 8.00
    - Player at Y=12 (Corridor length 3): Expected steps to exit = 12.00
    - Player at Y=13 (Corridor length 4): Expected steps to exit = 16.00
    - Player at Y=14 (Corridor length 5): Expected steps to exit = 20.00
    - Player at Y=15 (Corridor length 6): Expected steps to exit = 24.00
  - **Counter-Intuitive Truth**: Walking further south actually *increases* the expected steps for the NPC to exit, because it opens up more vertical dead-end states (Y=10..K-1) where they can waste steps wandering back and forth instead of stepping West.
- **Optimal Protocol**:
  1. Stand as close as possible to the NPC (Y=10 or Y=11) to block the dead-end states and maximize exit probability.
  2. Actively step back and forth (e.g., between Y=10 and Y=11) to force the overworld update loop to run.
  3. Once the NPC steps West to (13, 9), immediately run past them.

## Cut Bush Respawning Mechanic (Verified Turn 45601)
- **Verified Fact**: In Generation 1, cuttable bushes (TYPE_5519) are not permanently cleared. Whenever the player transitions maps, warps, uses DIG/FLY, or reloads the game, all cut bushes in the overworld respawn and must be cut again using the CUT move to be passable. This was verified on Turn 45601 when returning to Fuchsia City and finding the (18, 19) bush respawned.

## Gym Badge Mechanics (Verified Records)
- **Boulder Badge**: Obtained from Brock (Pewter City).
  - **Overworld Ability**: Unlocks the use of **HM05 FLASH** outside of battle.
  - **Stat Boost**: Increases Pokémon's Attack in battle.
- **Cascade Badge**: Obtained from Misty (Cerulean City).
  - **Overworld Ability**: Unlocks the use of **HM01 CUT** outside of battle.
  - **Obedience Level**: Traded Pokémon up to **Level 30** will obey the player.
- **Thunder Badge**: Obtained from Lt. Surge (Vermilion City).
  - **Overworld Ability**: Unlocks the use of **HM02 FLY** outside of battle.
  - **Stat Boost**: Increases Pokémon's Speed in battle. (Vanilla Theory - Pending ROM-specific empirical stat audit)
- **Rainbow Badge**: Obtained from Erika (Celadon City).
  - **Overworld Ability**: Unlocks the use of **HM04 STRENGTH** outside of battle (to be verified immediately upon receipt in Warden's House).
  - **Obedience Level**: Traded Pokémon up to **Level 50** will obey the player.
- **Soul Badge**: Obtained from Koga (Fuchsia City).
  - **Overworld Ability**: Unlocks the use of **HM03 SURF** outside of battle.
  - **Stat Boost**: Increases Pokémon's Defense in battle. (Vanilla Theory - Pending ROM-specific empirical stat audit)
- **Marsh Badge**: Obtained from Sabrina (Saffron City).
  - **Obedience Level**: Traded Pokémon up to **Level 70** will obey the player.
- **Volcano Badge**: Obtained from Blaine (Cinnabar Island).
  - **Stat Boost**: Increases Pokémon's Special in battle.
- **Earth Badge**: Obtained from Giovanni (Viridian City).
  - **Obedience Level**: All traded Pokémon will obey the player regardless of level.

## Permanent Strength & Boulder Mechanics (Verified Turns 74245-74267)
- **Activating STRENGTH**: Can be selected from the POKéMON party options for a Pokémon that knows STRENGTH (e.g., ROCKY/GEODUDE).
  - *Confirming Textbox*: The game displays: `[Name] used STRENGTH.` followed by `[Name] can move boulders.`
- **Pushing Boulders**: Once STRENGTH is active, the player can push boulders (e.g., at (8, 4)) by walking directly into them from an adjacent tile (e.g., standing at (7, 4) facing Right and pressing Right).
  - *Movement*: The boulder slides exactly 1 tile in the direction pushed.
  - *Player Positioning (Gen 1 Engine Quirk - Verified Turn 99508)*: When you push a boulder, the player **does not** automatically step forward onto the tile the boulder just occupied. Instead, the player remains on their original tile, and the tile between the player and the boulder becomes empty. To push the boulder a second time in a straight line, the player must press the direction button once to step forward into the empty tile, and then press the direction button again to push the boulder. Thus, pushing a boulder $N$ tiles in a straight line requires exactly $2N - 1$ direction presses.
- **Deactivation & Reset Rules**:
  - *Map Transition Reset*: Exiting and re-entering the map (e.g., leaving the Warden's House to Fuchsia City and immediately re-entering) **fully resets** all boulders to their default starting coordinates (e.g., back to (8, 4)).
  - *Strength State Reset*: Map transition **fully deactivates** the overworld STRENGTH state. If the player re-enters the map, they must manually reactivate STRENGTH from the POKéMON menu to push any boulders again, even if they have already activated it during that play session.

## Badge-Boost Multiplier Empirical Audit Protocol
- **Objective**: Audit whether the 12.5% speed boost from the Thunder Badge (and 12.5% defense boost from the Soul Badge) is active and functioning in this ROM's combat engine.
- **Speed Boost (Thunder Badge) Audit Methodology**:
  1. **Identify SPARKY's Stat Speed**: View SPARKY's Speed stat $S$ in the Pokémon Stats menu (e.g., $S = 54$).
  2. **Calculate Boosted Speed**: The boosted speed should be $S_{boosted} = \lfloor 1.125 \times S \rfloor$ (e.g., $\lfloor 1.125 \times 54 \rfloor = 60$).
  3. **Target Opponent selection**: Find a wild Pokémon or trainer Pokémon whose Speed $O$ lies in the critical window: $S \le O < S_{boosted}$.
     - Example: If $S = 54$ and $S_{boosted} = 60$, we find an opponent with Speed $O = 57$.
  4. **Perform Battle Tests**:
     - Engage in battle with the target opponent.
     - Avoid using priority moves (like Quick Attack) and avoid status conditions that affect speed (like Paralysis, which reduces Speed by 75% in Gen 1).
     - Observe who moves first on Turn 1.
     - Repeat multiple times to eliminate coin-flip variance (if $S = O$, turn order is 50/50).
     - If SPARKY consistently moves first (100% over $\ge 10$ trials), the boosted speed $S_{boosted} > O$ is active, confirming the 12.5% Thunder Badge boost is functioning.
     - If turn order is randomized or the opponent consistently moves first, the boost is inactive.
- **Defense Boost (Soul Badge) Audit Methodology**:
  1. **Identify Defender's Defense**: View our active Pokémon's Defense stat $D$ (e.g., ROCKY's Defense is 36).
  2. **Calculate Boosted Defense**: The boosted Defense should be $D_{boosted} = \lfloor 1.125 \times D \rfloor$ (e.g., $\lfloor 1.125 \times 36 \rfloor = 40$).
  3. **Establish Attacker's Stats & Move**: Select a wild Pokémon (e.g., a Level 20 Rattata) whose Level $L$ and Attack stat $A$ are known, and that uses a physical move (like Tackle, base power 35) with no stat modifiers.
  4. **Calculate Damage Ranges**:
     - Compute the expected damage range received with unboosted Defense $D$:
       $Damage = \lfloor \frac{\lfloor \frac{2 \times L}{5} + 2 \rfloor \times Power \times \frac{A}{D}}{50} \rfloor + 2 \times \text{Random Factor}$
     - Compute the expected damage range received with boosted Defense $D_{boosted}$.
     - Find a scenario where the two ranges have distinct, non-overlapping minimums (e.g., unboosted range is 12-14, boosted range is 10-12).
  5. **Perform Battle Tests**:
     - Let the wild Pokémon hit us with the physical move.
     - Record the exact HP lost.
     - If we record damage values that are only possible under the boosted Defense calculation (such as 10 or 11 damage in the above example), we empirically prove that Koga's 12.5% Soul Badge Defense boost is active and functioning.

## Overworld HM Execution without Bag Items (Verified Turn 74893)
- **Verified Fact**: HM moves (specifically HM03 SURF and HM04 STRENGTH) can be executed in the overworld from the Pokémon party menu even if the physical HM item is stored in the PC, provided a Pokémon in the party knows the move.
- **Proof of Work**: On Turn 74872, we deposited HM03 and HM04 in GEM's PC. On Turn 74893, standing at (11, 13) facing Down towards water, we successfully selected GEMMY (BLASTOISE) from the party menu and executed SURF.
- **Conclusion**: Carrying physical HM items in the Bag is completely unnecessary once taught, freeing up vital inventory slots.

## Virtual Notepad Datastore Search Rule (Turn 90152 Verification)
- **Verified Fact**: Standard Python filesystem utilities (such as `os.walk`, `os.path`, and the standard `open()` command) executed within the `run_code` tool are completely blind to the game's virtual pseudo-filesystem. 
- **Rule**: The virtual persistent notepads (including `Main`, `Locations/*`, `Scratchpad/*`, etc.) are managed in a separate sandboxed datastore. To search, read, or list notepads programmatically, you MUST exclusively use the built-in `search_notepads`, `read_notepad`, and `load_notepads` tools. Standard OS commands will return empty results.

## Virtual Notepad Datastore Search Rule (Turn 90781 Verification)
- **Verified Fact**: Standard Python filesystem utilities (such as `os.walk`, `os.path`, and the standard `open()` command) executed within the `run_code` tool are completely blind to the game's virtual pseudo-filesystem. 
- **Rule**: The virtual persistent notepads (including `Main`, `Locations/*`, `Scratchpad/*`, etc.) are managed in a separate sandboxed datastore. To search, read, or list notepads programmatically, you MUST exclusively use the built-in `search_notepads`, `read_notepad`, and `load_notepads` tools. Standard OS commands will return empty results. This ensures no compute or time is wasted on blind filesystem searches.

## Fly Map Navigation (Verified Turn 111416)
- On the FLY map, pressing Left or Right is a no-op. The map locations are scrolled linearly as a list strictly using UP and DOWN, as indicated by the ▲ and ▼ icons on the top-right of the screen.