# UI & Storage Mechanics (Generation 1 Retail)

## Poké Mart & Shop UI Mechanics
- **Quantity Selector Wrap Mechanic:** On the item quantity selection screen in Generation 1 retail, the counter initializes at `x01`. Pressing `Down` at `x01` wraps directly around to `x99` (it does NOT cap at maximum affordable money; wraps strictly to 99) [Empirically verified Turn 29102]. Conversely, pressing `Up` at `x99` wraps symmetrically back to `x01` [Empirically verified Turn 29103], confirming a continuous bidirectional cyclic counter between `x01` and `x99`.

## PC Storage & Menu Mechanics (Generation 1 Retail)
- **Chronological Storage Order:** In Gen 1 retail, items deposited into the player's PC (BLUE's PC) and Pokémon deposited into BILL's PC boxes are appended to the list in strictly chronological order of deposit.
- **Item Storage Withdrawal:** When withdrawing items from BLUE's PC, single-quantity items withdraw immediately upon confirmation, while stacked items prompt for quantity (x01..x99). Withdrawn items are placed into the next available Bag slot.
- **PC Menu Navigation:** The PC item storage withdrawal list scrolls vertically. The list does NOT wrap vertically from top to bottom (pressing Up at Item 1 does not wrap to CANCEL).
- **Party Space Prerequisite:** In BILL's PC, selecting WITHDRAW PKMN when the active party is full (6 Pokémon) displays 'Your party is full!' and denies withdrawal. The player must use DEPOSIT PKMN first to free party slots.
- **Batched Operations:** PC sessions can seamlessly transition between BILL's PC and BLUE's PC by pressing B to back out to the main PC menu ('BILL's PC', 'BLUE's PC', 'PROF. OAK's PC', 'LOG OFF') without needing to exit to the overworld between operations.
