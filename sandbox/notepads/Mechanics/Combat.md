# Combat Mechanics (Generation 1 Retail)

## Battle UI & Controls
- **Start Menu Cursor Memory:** In Generation 1 retail, the overworld Start menu remembers the last selected menu item across overworld sessions (empirically confirmed Turns 3985-3986: hovering on POKéMON causes the Start menu to re-open on POKéMON on the next press).
- **Move Cursor Memory:** Within the same battle, the move selection menu remembers the last selected move slot across turns and across enemy Pokémon faintings (empirically confirmed Turn 3049 vs Rival RED: Slot 3 Bubblebeam remained selected after Pidgeotto fainted). At the start of each new battle, the move cursor always re-initializes to Slot 1 (empirically confirmed Turns 3144, 3160, 3175).
- **Shift Style Prompt:** When an opposing Pokémon faints in trainer battles, the game asks "Will BLUE change POKéMON?". Default cursor is YES. Pressing B automatically selects NO and retains current Pokémon.
- **Top Battle Menu:** Pressing B on the main battle menu (`FIGHT`, `ITEM`, `PKMN`, `RUN`) does nothing and cannot accidentally trigger unwanted actions.
- **Trainer Battles:** Fleeing (`RUN`) is impossible in trainer battles.
- **Bag Menu Navigation:** The Item Bag scrolling list does NOT wrap vertically from top to bottom (pressing Up at Item 1 stops at Item 1 and does not wrap to CANCEL, empirically confirmed Turn 3069).
- **Battle Bag Cursor Memory:** Within the same battle, the in-battle Item Bag menu remembers the last selected item slot across combat turns (empirically confirmed Turn 29002 vs Zapdos: selecting ITEM re-opened directly on Slot 11 ULTRA BALL x36 without resetting to Slot 1).
- **Party Menu Cursor Memory:** In Generation 1 retail, the overworld Party Pokémon menu remembers the last selected party member across overworld sessions (empirically confirmed Turn 8260).
- **Battle Reset of Menu Cursor Memory:** Entering and exiting any battle (wild or trainer) immediately re-initializes both the overworld Start menu cursor to Slot 1 (POKéDEX) and the Bag menu cursor to Slot 1. Menu cursor persistence only applies across consecutive overworld menu sessions without intervening battles [Empirically confirmed Turns 12354-12357].

## Stat & Damage Mechanics
- **Special Stat:** Gen 1 combines Special Attack and Special Defense into a single Special stat.
- **Physical Types:** Normal, Fighting, Flying, Poison, Ground, Rock, Bug, Ghost.
- **Special Types:** Water, Grass, Fire, Ice, Electric, Psychic, Dragon.
- **STAB:** Same-Type Attack Bonus provides a 1.5x multiplier to damage.
- **Priority:** Quick Attack has +1 priority.

## Obedience
- **Original Trainer Pokémon:** Starter Pokémon and Pokémon caught by the player never disobey, regardless of level or badge count. Badge obedience limits (e.g. Cascadebadge Lv 30) only apply to traded / outsider Pokémon.



## Poké Mart & Shop UI Mechanics
- **Quantity Selector Wrap Mechanic:** On the item quantity selection screen in Generation 1 retail, the counter initializes at `x01`. Pressing `Down` at `x01` wraps directly around to `x99` (it does NOT cap at maximum affordable money; wraps strictly to 99) [Empirically verified Turn 29102]. Conversely, pressing `Up` at `x99` wraps symmetrically back to `x01` [Empirically verified Turn 29103], confirming a continuous bidirectional cyclic counter between `x01` and `x99`.

## PC Storage & Menu Mechanics (Generation 1 Retail)
- **Chronological Storage Order:** In Gen 1 retail, items deposited into the player's PC (BLUE's PC) and Pokémon deposited into BILL's PC boxes are appended to the list in strictly chronological order of deposit.
- **Item Storage Withdrawal:** When withdrawing items from BLUE's PC, single-quantity items withdraw immediately upon confirmation, while stacked items prompt for quantity (x01..x99). Withdrawn items are placed into the next available Bag slot.
- **PC Menu Navigation:** The PC item storage withdrawal list scrolls vertically. The list does NOT wrap vertically from top to bottom (pressing Up at Item 1 does not wrap to CANCEL).
- **Party Space Prerequisite:** In BILL's PC, selecting WITHDRAW PKMN when the active party is full (6 Pokémon) displays 'Your party is full!' and denies withdrawal. The player must use DEPOSIT PKMN first to free party slots.
- **Batched Operations:** PC sessions can seamlessly transition between BILL's PC and BLUE's PC by pressing B to back out to the main PC menu ('BILL's PC', 'BLUE's PC', 'PROF. OAK's PC', 'LOG OFF') without needing to exit to the overworld between operations.
