# UI & Storage Mechanics (Generation 1 Retail)

## Poké Mart & Shop UI Mechanics
- **Quantity Selector Wrap Mechanic:** On the item quantity selection screen in Generation 1 retail, the counter initializes at `x01`. Pressing `Down` at `x01` wraps directly around to `x99` (it does NOT cap at maximum affordable money; wraps strictly to 99) [Empirically verified Turn 29102]. Conversely, pressing `Up` at `x99` wraps symmetrically back to `x01` [Empirically verified Turn 29103], confirming a continuous bidirectional cyclic counter between `x01` and `x99`.

## PC Storage & Menu Mechanics (Generation 1 Retail)
- **Chronological Storage Order:** In Gen 1 retail, items deposited into the player's PC (BLUE's PC) and Pokémon deposited into BILL's PC boxes are appended to the list in strictly chronological order of deposit.
- **Item Storage Withdrawal:** When withdrawing items from BLUE's PC, single-quantity items withdraw immediately upon confirmation, while stacked items prompt for quantity (x01..x99). Withdrawn items are placed into the next available Bag slot.
- **PC Menu Navigation:** The PC item storage withdrawal list scrolls vertically. The list does NOT wrap vertically from top to bottom (pressing Up at Item 1 does not wrap to CANCEL).
- **Party Space Prerequisite:** In BILL's PC, selecting WITHDRAW PKMN when the active party is full (6 Pokémon) displays 'Your party is full!' and denies withdrawal. The player must use DEPOSIT PKMN first to free party slots.
- **Batched Operations:** PC sessions can seamlessly transition between BILL's PC and BLUE's PC by pressing B to back out to the main PC menu ('BILL's PC', 'BLUE's PC', 'PROF. OAK's PC', 'LOG OFF') without needing to exit to the overworld between operations.

## PC Deposit Sub-Menu Mechanics (Generation 1 Retail)
- In Generation 1 retail, selecting a Pokémon in the PC DEPOSIT menu does not immediately store it. It opens a secondary sub-menu:
  - `DEPOSIT` (default cursor)
  - `STATS`
  - `CANCEL`
- Pressing A on `DEPOSIT` confirms the deposit and stores the Pokémon into the active box.
- Pressing B dismisses the sub-menu without depositing [Empirically verified Turn 31307].

## PC Change Box Mechanics & Menu Hierarchy (Generation 1 Retail)
- Selecting `CHANGE BOX` in Bill's PC does NOT immediately open the box list.
- Exact Menu & Dialogue Flow:
  1. Select `CHANGE BOX` (Slot 4 in Bill's PC menu).
  2. Dialogue prints: 'When you change a POK�MON BOX, data will be saved. Is that OK?'
  3. A `YES / NO` selection prompt appears (cursor defaults to `YES`).
  4. Selecting `NO` (or pressing B) cancels the operation and returns to Bill's PC menu without saving.
  5. Selecting `YES` opens the 'Choose a PKMN BOX' list (`BOX 1` through `BOX 12`), with cursor initializing on the current active box.
  6. Navigating to the desired box and pressing A initiates the save routine ('Saving... DON'T TURN OFF THE POWER.').
  7. Upon save completion, prints '[PLAYER] changed the POK�MON BOX!' and returns to Bill's PC menu with the newly active box displayed.