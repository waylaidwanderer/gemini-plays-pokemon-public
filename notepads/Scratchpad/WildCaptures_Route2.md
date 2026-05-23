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