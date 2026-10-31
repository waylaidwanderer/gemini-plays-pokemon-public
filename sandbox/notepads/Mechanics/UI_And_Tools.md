# UI, Menu, and Tool Mechanics

## Menu & Cursor Mechanics
- **Start Menu Cursor Memory**: The Start menu preserves its last-used index across openings. When `POKEMON` or `POKEDEX` is added at index 0, the stored index shifts relative to older items.
- **Pokemon Summary Exit**: Takes 3 `B` presses to return from Summary to the Start menu (`Summary -> Party submenu -> Party slot list -> Start menu`) and a 4th `B` to close the Start menu.
- **PC Item Withdrawal Exit**: Takes 4 `B` presses after withdrawing an item to return to the overworld (`Dismiss text -> Item list -> Item Storage submenu -> Top-level PC menu`).
- **Bag Pocket Navigation & Cursor Clamping**:
  - Bag pockets (`1: ITEMS`, `2: POKE BALLS`, `3: TMs & HMs`, `4: BERRIES`, `5: KEY ITEMS`) wrap around between `ITEMS` and `KEY ITEMS`.
  - Switching through an empty pocket (`TMs & HMs` or `BERRIES`) clamps the item cursor onto `>CLOSE BAG`; always press `Up` before `A` when arriving at a target pocket if you passed through an empty pocket.
  - In `KEY ITEMS`, the `USE / REGISTER / CANCEL` submenu is arranged in 2 columns (`>USE` on left, `REGISTER` on right); press `A, Right, A` to register a Key Item to `Select`.
  - In `BERRIES`, the submenu is a 2-column grid (`Row 0: >CHECK TAG`; `Row 1: USE | GIVE`; `Row 2: TOSS | CANCEL`); press `A, Down, A` to `USE` a Berry or `A, Down, Right, A` to `GIVE` a Berry.
- **Rare Candy Chaining**: From the Bag (`>RARE CANDY` at index 0), pressing `A` repeatedly (`sleep 900`) automatically chains Rare Candies onto Party Slot 1 as long as that Pokemon has `< 4` moves.
- **Naming Screen Helper (`naming.py`)**: Use `naming.get_naming_buttons(name, confirm=True, start_pos=(0, 0))` to generate exact button inputs for uppercase nicknames. Never use `B` when approaching a gift or capture nickname `YES / NO` prompt, as `B` selects `NO`. After a Poke Ball capture (`"Gotcha!"` after `"sleep 7500", "B"`), exactly **4 `A` presses** (`["A", "sleep 2000", "A", "sleep 1500", "A", "sleep 2500", "A"]`) open the naming screen with 0 stray characters typed.

## Overworld & Fishing Mechanics
- **NPC Sprite Coordinates**: Gen 3 NPC sprites are 32px tall (2 vertical tiles); their true collision/interaction tile is always the bottom half (feet/shadow), while their head overlaps `y - 1`.
- **Turn-in-Place Delay**: When turning to face an adjacent obstacle/NPC without stepping onto a new tile, include `"sleep 300"` between the directional input and `"A"`, otherwise `"A"` fires during the 8-frame turn animation and is ignored.
- **Old Rod Timing (`Task_Fishing`)**:
  - Cast animation before the 1st dot takes ~1.5s, and each of the 3..10 dots takes ~0.33s (`3 dots = 2.5s` .. `10 dots = 4.8s`), with a ~0.55s `"Oh! A bite!"` window.
  - **Battle-Safe Multi-Cast Loop**: Chaining `Select, sleep <3300..4800>, A, sleep 1200, B, sleep 1000` across multiple casts in a single `press_buttons` call is 100% battle-safe: once a cast hooks a fish (`"A"` -> `"A POKEMON's on the hook!"` -> `"B"` starts the battle), any remaining `A` + `B` pairs harmlessly open and close the `FIGHT` menu without using a move (verified Turn 182 when hooking Lv 5 Azurill at `4500ms`).
- **Poke Mart Purchasing**: Poke Balls cost only `$10` each (`$100` for 10 + 1 bonus Premier Ball). After confirming a 10+ ball purchase, it takes **6 `B` presses** (`Thank you -> Premier Ball -> BUY list -> Anything else -> QUIT -> Please come again!`) to return to overworld control.
- **Party Menu Fade-In & Navigation**:
  - Opening the Party menu (`Start -> POKEMON` or `BAG -> USE`) takes ~800ms to fade in; directional inputs sent within 300ms of opening are ignored during the fade-in.
  - `BAG -> USE` remembers the last active Party `slotId` (including slots selected during a prior `GIVE`), whereas `Start -> POKEMON` and `BAG -> GIVE` always open at `slotId = 0` (Slot 1).
  - `Down` steps sequentially (`Slot 1 -> Slot 2 -> ... -> Last Slot -> CANCEL -> Slot 1`), `Up` steps in reverse (`Slot 1 -> CANCEL -> Last Slot`), and `Left` from any slot (`Slots 1..6`) deterministically clamps the cursor onto `Slot 1` (`slotId = 0`).
- **Battle Menu Cursor Memory**: After selecting `POKEMON` (bottom-left) to switch in battle, the battle action cursor remains on `>POKEMON` on the next turn; press `Up` before `A` to select `>FIGHT` (top-left).
- **Berry Tree Harvesting**: Interacting with a Berry Tree takes **3 `A` presses** (`Interact -> "You found N [X] BERRIES!" -> "Do you want to pick the [X] BERRIES? [>YES]"`), followed by `sleep 3500` for the fanfare and **3 `B` presses** (`sleep 1500` apart) to dismiss the put-away and loamy-soil messages without replanting.
  - **Loamy Soil `USE` Trap**: Selecting `USE` on a Berry in the `BERRIES` pocket while facing a soft, loamy soil patch in the overworld automatically plants the Berry into the soil and exits the Bag/Start menu to the overworld instead of opening the Party menu. Always turn away or step off the loamy soil before selecting `USE` on a Berry.