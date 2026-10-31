# UI, Menu, and Tool Mechanics

## Menu & Cursor Mechanics
- **Start Menu Cursor Memory**: The Start menu preserves its last-used index across openings. When `POKEMON` or `POKEDEX` is added at index 0, the stored index shifts relative to older items.
- **Pokemon Summary Exit**: Takes 3 `B` presses to return from Summary to the Start menu (`Summary -> Party submenu -> Party slot list -> Start menu`) and a 4th `B` to close the Start menu.
- **PC Item Withdrawal Exit**: Takes 4 `B` presses after withdrawing an item to return to the overworld (`Dismiss text -> Item list -> Item Storage submenu -> Top-level PC menu`).
- **Bag Pocket Navigation & Cursor Clamping**:
  - Bag pockets (`1: ITEMS`, `2: POKE BALLS`, `3: TMs & HMs`, `4: BERRIES`, `5: KEY ITEMS`) wrap around between `ITEMS` and `KEY ITEMS`.
  - Switching through an empty pocket (`TMs & HMs` or `BERRIES`) clamps the item cursor onto `>CLOSE BAG`; always press `Up` before `A` when arriving at a target pocket if you passed through an empty pocket.
  - In `KEY ITEMS`, the `USE / REGISTER / CANCEL` submenu is arranged in 2 columns (`>USE` on left, `REGISTER` on right); press `A, Right, A` to register a Key Item to `Select`.
- **Rare Candy Chaining**: From the Bag (`>RARE CANDY` at index 0), pressing `A` repeatedly (`sleep 900`) automatically chains Rare Candies onto Party Slot 1 as long as that Pokemon has `< 4` moves.
- **Naming Screen Helper (`naming.py`)**: Use `naming.get_naming_buttons(name, confirm=True, start_pos=(0, 0))` to generate exact button inputs for uppercase nicknames. Never use `B` when approaching a gift or capture nickname `YES / NO` prompt, as `B` selects `NO`. After a Poke Ball capture (`"Gotcha!"` after `"sleep 7500", "B"`), exactly **4 `A` presses** (`["A", "sleep 2000", "A", "sleep 1500", "A", "sleep 2500", "A"]`) open the naming screen with 0 stray characters typed.

## Overworld & Fishing Mechanics
- **NPC Sprite Coordinates**: Gen 3 NPC sprites are 32px tall (2 vertical tiles); their true collision/interaction tile is always the bottom half (feet/shadow), while their head overlaps `y - 1`.
- **Turn-in-Place Delay**: When turning to face an adjacent obstacle/NPC without stepping onto a new tile, include `"sleep 300"` between the directional input and `"A"`, otherwise `"A"` fires during the 8-frame turn animation and is ignored.
- **Old Rod Timing (`Task_Fishing`)**:
  - Pressing `A` or `B` while the initial dots (`. . .`) are still printing cancels the cast into `"Not even a nibble..."`.
  - When the bite timer expires without `A`, the player sprite pulls the rod out of the water (~0.3s) while `"Oh! A bite!"` remains displayed before `"It got away..."` prints.
  - Active rod-in-water `"Oh! A bite!"` frames were observed at `+3.66s` into the post-`Select` sleep for 8 dots (Turn 84 `#46`) and `+4.29s` into the sleep for 9 dots (Turn 85 `#47`).
- **Poke Mart Purchasing**: Poke Balls cost only `$10` each (`$100` for 10 + 1 bonus Premier Ball). After confirming a 10+ ball purchase, it takes **6 `B` presses** (`Thank you -> Premier Ball -> BUY list -> Anything else -> QUIT -> Please come again!`) to return to overworld control.
- **Party Menu Fade-In & Navigation**:
  - Opening the Party menu (`Start -> POKEMON` or `BAG -> USE`) takes ~800ms to fade in; directional inputs sent within 300ms of opening are ignored during the fade-in.
  - `BAG -> USE` remembers the last active Party `slotId`, whereas `Start -> POKEMON` opens at `slotId = 0` (Slot 1).
  - `Down` steps sequentially (`Slot 1 -> Slot 2 -> ... -> Last Slot -> CANCEL -> Slot 1`), `Up` steps in reverse (`Slot 1 -> CANCEL -> Last Slot`), and `Left` from any right-column slot (`Slots 2..6`) jumps directly to `Slot 1`.
- **Berry Tree Harvesting**: Interacting with a Berry Tree takes **3 `A` presses** (`Interact -> "You found N [X] BERRIES!" -> "Do you want to pick the [X] BERRIES? [>YES]"`), followed by `sleep 3500` for the fanfare and **3 `B` presses** (`sleep 1500` apart) to dismiss the put-away and loamy-soil messages without replanting.