# Scratchpad: Wild Captures and Leveling Goals

## High-Level Strategy:
- Goal: Capture additional wild Pokémon (Pidgey, Rattata, Nidoran, etc.) to build our team.
- Goal: Level up SQUIRTLE (GEMMY) and new team members to prepare for Pewter City Gym.
- Goal: Travel north through Route 2 towards Viridian Forest.

## Live Status:
- Turn 843: Currently inside Poké Mart (Map 0_42) at (2, 5) facing Left.
- Money: ¥1075.
- Inventory: 10 Poké Balls, 1 Antidote, 1 Town Map.
- Squirtle HP: 21/24 (Level 7).

## Next Navigation Step:
- Select "QUIT" from Mart menu.
- Move: Right 1 to (3, 5), Down 2 to (3, 7) to warp outside to Viridian City at (29, 20).
- Go to Route 2 (north exit of Viridian City).

## Testing Methodology:
- Execute `["Down", "Down", "A"]` to select QUIT.
- Verify that the overworld screen is active and the menu is closed on Turn 844.
- Turn 847: SQUIRTLE is at 21/24 HP. Player is at (2, 5) facing Left inside Poké Mart (Map 0_42).
  - Observation: The BUY/SELL/QUIT menu shows the cursor on QUIT, and the textbox displays "Thank you!".
  - Immediate Plan: Press A to dismiss the dialogue and close the shop menu.
  - Testing Methodology: Execute `["A"]` and verify that the overworld is active with no menu or dialogue on Turn 848.
- Turn 851: SQUIRTLE is at 21/24 HP. Player is at (3, 7) facing Down inside Poké Mart (Map 0_42) standing on the exit warp mat.
  - Observation: The shop menu is fully closed, and we are standing on the red mat.
  - Immediate Plan: Press Down once to trigger the exit warp.
  - Testing Methodology: Execute `["Down"]` and verify that we warp outside to Viridian City (Map 0_1) at (29, 20) on Turn 852.
- Turn 857: SQUIRTLE is at 21/24 HP. Player successfully exited the Poké Mart and is standing at (29, 20) facing Down in Viridian City (Map 0_1).
  - Verification: `<CurrentScreen turn="857">` shows that the path Left along Row 20 is clear (TYPE_3fe2).
  - Movement Plan: Move Left 9 steps along Row 20 to reach the main central street at (20, 20).
  - Testing Methodology: Execute `["Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left", "Left"]` and verify that the player's coordinate becomes (20, 20) in the next turn's game state.
- Turn 863: SQUIRTLE is at 21/24 HP. Player is at (20, 20) facing Left on Map 0_1.
  - Visual Verification: `<CurrentScreen turn="863">` shows that we are at (20, 20). The Trainer School wall blocks Column 20 at Row 17, but Column 19 is completely open going north.
  - Navigation Plan: Move Left 1 step to (19, 20), then Up 4 steps to (19, 16) to bypass the school building.
  - Testing Methodology: Execute `["Left", "Up", "Up", "Up", "Up"]` and verify that the player's coordinate becomes (19, 16) on the next turn.
- Turn 867: SQUIRTLE is at 21/24 HP. Player is at (19, 16) facing Up in Viridian City (Map 0_1).
  - Visual Verification: `<CurrentScreen turn="867">` shows Column 19 from Row 16 to Row 12 is completely clear (TYPE_3fe2).
  - Movement Plan: Move Up 4 steps to (19, 12).
  - Testing Methodology: Execute `["Up", "Up", "Up", "Up"]` and verify that the player's coordinate becomes (19, 12) on Turn 868.
- Turn 869: SQUIRTLE is at 21/24 HP. Player is at (19, 16) facing Up.
  - Visual Verification: `<CurrentScreen turn="869">` shows Column 19 is clear of obstacles up to Row 12 (all TYPE_3fe2).
  - Movement Plan: Move Up 4 steps to (19, 12).
  - Testing Methodology: Execute `["Up", "Up", "Up", "Up"]` and verify that the player is at (19, 12) on Turn 870.