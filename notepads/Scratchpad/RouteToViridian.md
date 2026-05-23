# Scratchpad: Journey back to Viridian City
Started: Turn 521
Goal: Go from Pallet Town (13, 6) to Viridian City Poké Mart to buy Poké Balls.

## Live Route Planning:
- Successfully returned to Viridian City and entered the Poké Mart on Turn 809.

## Turn Log:
- Turns 521-808: Successfully traveled from Pallet Town through Route 1, bypassing all ledge obstacles (using Column 14 to bypass the Row 5 ledge), and entered Viridian City.
- Turn 809: Arrived at the Poké Mart (Map 0_42) door at (29, 19) and successfully entered the building.
- Turn 814: SQUIRTLE is at 21/24 HP. Inside the Poké Mart at (3, 7) facing Up, preparing to talk to the clerk.
- Turn 817: SQUIRTLE is at 21/24 HP. Player is at (3, 7) facing Up inside Viridian City Poké Mart (Map 0_42).
  - Visual Verification: `<CurrentScreen turn="817">` shows the path is clear: (3, 6) is TYPE_3fe2, (3, 5) is TYPE_3fe2, and (2, 5) is TYPE_3fe2. The clerk is at (0, 5) behind the counter at (1, 5).
  - Interaction Plan: Move Up 2 steps to (3, 5), Left 1 step to (2, 5) (facing Left), then press A to initiate conversation with the clerk.
  - Testing Methodology: Execute `["Up", "Up", "Left", "A"]` and verify that the dialogue/shopping menu is active in the next turn's game state.
- Turn 829: SQUIRTLE is at 21/24 HP. Player is at (2, 5) facing Left in Poké Mart.
  - Observation: The BUY menu is open, showing only POKE BALL, ANTIDOTE, PARLYZ HEAL, and BURN HEAL, with no down arrow visible.
  - Hypothesized Behavior: Potions might not be in the inventory, or we need to scroll.
  - Plan: Press Down once to point to ANTIDOTE. We will check the cursor position next turn to verify. Then we will check if any further scrolling is possible.
  - Testing Methodology: Execute `["Down"]` and verify that the cursor points to ANTIDOTE on Turn 830.
- Turn 830: SQUIRTLE is at 21/24 HP. Player is at (2, 5) facing Left in Poké Mart.
  - Verification: `<CurrentScreen turn="830">` clearly shows a down arrow (▼) next to BURN HEAL ¥250, proving that POTION is indeed in the shop inventory list below!
  - Next Step: Press Down 4 times to select POTION, select quantity 3, and confirm the purchase for ¥750. Then buy 1 Antidote for ¥100.
  - Testing Methodology: Move cursor Down 4 times by executing `["Down", "Down", "Down", "Down"]` and verify that the cursor points to POTION on the next turn.
- Turn 837: SQUIRTLE is at 21/24 HP. Player is at (2, 5) facing Left in Poké Mart.
  - Visual Verification: `<CurrentScreen turn="837">` shows the quantity selection menu active for ANTIDOTE, with the default quantity `x01` and total price `¥100` selected.
  - Action Plan: Press A to confirm the quantity and open the YES/NO confirmation prompt.
  - Testing Methodology: Execute `["A"]` and verify that the YES/NO confirmation menu appears on Turn 838.