# UI & Storage Mechanics (Generation 1 Retail)

## Poké Mart & Shop UI Mechanics
- **Quantity Selector Wrap Mechanic:** On the item quantity selection screen in Generation 1 retail, the counter initializes at `x01`. Pressing `Down` at `x01` wraps directly around to `x99` (it does NOT cap at maximum affordable money; wraps strictly to 99) [Empirically verified Turn 29102]. Conversely, pressing `Up` at `x99` wraps symmetrically back to `x01` [Empirically verified Turn 29103], confirming a continuous bidirectional cyclic counter between `x01` and `x99`.

## PC Storage & Menu Mechanics (Generation 1 Retail)
- **PC Pokémon Withdrawal List Vertical Navigation:** In Generation 1 retail, the PC Pokémon storage withdrawal list does NOT wrap vertically from top to bottom (pressing Up at Slot 1 stops at Slot 1 and does not wrap to CANCEL, identical to Bag item list behavior) [Empirically verified Turn 42398].
- **Pokémon Box Storage Indexing:** Empirically confirmed Turn 33419: in Box 1, Krabby (PINCHY, caught Turn 31540) was listed at Slot 1 ahead of Zapdos (THUNDER, caught Turn 29075), disproving strict chronological box index ordering.
- **Item Storage Withdrawal:** When withdrawing items from BLUE's PC, single-quantity items withdraw immediately upon confirmation, while stacked items prompt for quantity (x01..x99). Withdrawn items are placed into the next available Bag slot.
- **PC Menu Navigation:** The PC item storage withdrawal list scrolls vertically. The list does NOT wrap vertically from top to bottom (pressing Up at Item 1 does not wrap to CANCEL).
- **Party Space Prerequisite:** In BILL's PC, selecting WITHDRAW PKMN when the active party is full (6 Pokémon) displays 'Your party is full!' and denies withdrawal. The player must use DEPOSIT PKMN first to free party slots.
- **Batched Operations:** PC sessions can seamlessly transition between BILL's PC and BLUE's PC by pressing B to back out to the main PC menu ('BILL's PC', 'BLUE's PC', 'PROF. OAK's PC', 'LOG OFF') without needing to exit to the overworld between operations.

## PC Deposit Sub-Menu Mechanics (Generation 1 Retail)
- **PC Deposit Menu Loop Mechanics:** In Generation 1 retail, after confirming a deposit and clearing the '[POKéMON] was stored in BOX X' dialogue, the game returns to the main Bill's PC menu with cursor pre-selected on `DEPOSIT PKMN` (it does not remain inside the party deposit list). Selecting `DEPOSIT PKMN` again re-opens the updated party list. [Empirically verified Turns 38057-38058]
- In Generation 1 retail, selecting a Pokémon in the PC DEPOSIT menu does not immediately store it. It opens a secondary sub-menu:
  - `DEPOSIT` (default cursor)
  - `STATS`
  - `CANCEL`
- Pressing A on `DEPOSIT` confirms the deposit and stores the Pokémon into the active box.

## PC Change Box Mechanics & Menu Hierarchy (Generation 1 Retail)
- Selecting `CHANGE BOX` in Bill's PC does NOT immediately open the box list.
- Exact Menu & Dialogue Flow:
  1. Select `CHANGE BOX` (Slot 4 in Bill's PC menu).
  2. Dialogue prints: 'When you change a POKEeMON BOX, data will be saved. Is that OK?'
  3. A `YES / NO` selection prompt appears (cursor defaults to `YES`).
  4. Selecting `NO` (or pressing B) cancels the operation and returns to Bill's PC menu without saving.
  5. Selecting `YES` opens the 'Choose a PKMN BOX' list (`BOX 1` through `BOX 12`), with cursor initializing on the current active box.
  6. Navigating to the desired box and pressing A initiates the save routine ('Saving... DON'T TURN OFF THE POWER.').
  7. Upon save completion, prints '[PLAYER] changed the POKEeMON BOX!' and returns to Bill's PC menu with the newly active box displayed.
## Poké Mart Selling Mechanics & Constraints (Generation 1 Retail)
- **Standard Sell Price Ratio:** Standard purchasable restorative items and vitamins sell for exactly 50% of their retail purchase price (e.g., Max Potion buys for ¥2,500 and sells for ¥1,250 [Empirically verified Turn 34106]; Vitamins buy for ¥9,800 on 5F and sell for ¥4,900).
- **PP UP Sell Price Anomaly:** In Generation 1 retail, PP UP has a base sell price of ¥0 (`x01 ¥0`), yielding zero revenue upon sale [Empirically verified Turn 34100].
- **Unsellable Items ('I can't put a price on that'):**
  - Key Items (Poké Flute, Super Rod, Bicycle, HM02) cannot be sold.
  - Max Elixer cannot be sold ('I can't put a price on that.') [Empirically verified Turn 34101].
  - Technical Machines (TMs) and Hidden Machines (HMs) cannot be sold to Mart clerks in Generation 1 retail; attempting to sell TMs (e.g. TM35) or HMs prompts 'I can't put a price on that.' and denies the transaction [Empirically verified Turn 34107].

## PC Interaction Geometry & Orientation Mechanics [Empirically Verified Turns 34960-34966]
- In Pokémon Centers, the PC terminal monitor is positioned at (13, 3). Tile (13, 4) is the open floor tile directly in front of the terminal.
- The player MUST stand at (13, 4) facing North to boot up the PC terminal.
- Attempting to interact with the PC monitor from the side at (12, 3) facing East produces no effect and does not open dialogue or boot the system.

## Party & Stats Screen UI Navigation (Generation 1 Retail)
- **Stats Screen Page Navigation:** On Page 1 of a Pokémon's STATS screen (displaying HP, stats, types, OT), pressing EITHER 'A' OR 'B' advances to Page 2 (displaying EXP points, Level Up EXP, moves and PP) [Empirically verified: 'B' Turn 39837; 'A' Turn 40083]. On Page 2, pressing 'B' exits the STATS screen back to the Party menu with cursor positioned on the inspected Pokémon [Empirically verified Turn 39838].

## In-Game NPC Trade Party Slot Reorganization Mechanics (Lead Slot Trade, N=1) [Empirically Verified Turns 42344-42358]
- When trading the lead Pokémon (Slot 1) from the active party with an NPC:
  - Removing the lead Pokémon causes all subsequent party Pokémon to shift up by 1 slot (Slot 2 becomes Slot 1, Slot 3 becomes Slot 2, Slot 4 becomes Slot 3).
  - The newly received traded Pokémon is appended directly into the LAST occupied party slot (e.g. 4-member party: Slot 4 became MARC). Behavior for non-lead slot trades (Slots 2..6) remains unverified.
  - Traded Pokémon arrives at the exact same level as the offered Pokémon (Slowbro Lv 37 -> Lickitung Lv 37).