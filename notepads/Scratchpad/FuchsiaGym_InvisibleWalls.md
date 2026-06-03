# Fuchsia Gym Invisible Walls Mapping (Scratchpad)
- **Start Turn**: 43409
- **Objective**: Map the invisible walls of Fuchsia Gym (Map 0_157) step-by-step through direct empirical testing.

## Recent Exploration History
- **Turn 43717**: Player at (7, 9). Planned to return to the column 8 corridor to test access to the green-haired trainer at (8, 13).
- **Turn 43718**: Moved Right to (8, 9).
- **Turn 43721**: Moved Down to (8, 10).
- **Turn 43726**: Moved Down to (8, 11).
- **Turn 43728**: Moved Down to (8, 12). No battle was triggered by the green-haired trainer standing at (8, 13) facing Up, suggesting a boundary block.
- **Turn 43730**: Tested moving Down from (8, 12). Bumped into an invisible wall! This confirms there is an invisible wall between (8, 12) and (8, 13).
- **Turn 43733**: Moved Right to (9, 12).
- **Turn 43735**: Moved Down to (9, 13).
- **Turn 43738**: Turned Left facing (8, 13). Bumped into the Juggler NPC, confirming (9, 13) to (8, 13) is physically passable (except for the NPC collision).
- **Turn 43741**: Pressed A facing Left from (9, 13). Successfully initiated and won the battle with Juggler (Hypno Lv38)!

## Current Status & Next Steps
- **Current Position**: (9, 13) facing Left.
- **Current Team Status**: GEMMY (BLASTOISE) is level 58 with 174/190 HP. Moves: DIG (1/10 PP), HYDRO PUMP (5/5 PP), BITE (7/15 PP), WATER GUN (22/25 PP).
- **Plan**:
  1. We need to find the remaining gym trainers and Gym Leader Koga.
  2. Koga is located in the center area.
  3. Let's trace our current verified routes to see how to explore the western/central parts of the gym.
- **Gym Statues Verification**:
  - Estimated at (3, 14)-(3, 15) and (6, 14)-(6, 15). These coordinates are unverified by direct collision or on-foot interaction, so they are stored here in the scratchpad until empirically proven.
- **Turn 43790 Plan**:
  - Current Position: (3, 13) facing Down.
  - Target: Trainer at (1, 12) facing Down.
  - Expected Path: Left to (2, 13), then Left to (1, 13).
  - Standing at (1, 13) will put us directly in the trainer's line of sight, triggering a battle.
  - Action: Move Left to (2, 13).
- **Turn 43793 Battle Start**:
  - Current Position: (1, 13) facing Up.
  - Battle started with Juggler standing at (1, 12) (roster unverified yet, we will log it as the battle proceeds).
  - Action: Press A to advance text and enter battle.