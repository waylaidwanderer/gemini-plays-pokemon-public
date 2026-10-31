<h1><code>Locations/Encounters</code></h1>

# Nuzlocke Encounters (Attempt #1)

| Location | Pokemon | Nickname | Status | Notes |
| :--- | :--- | :--- | :--- | :--- |
| Starter (Route 101) | Mudkip (M, Lv 10) | TRITON | Active | Bashful, Torrent; Moves: `Tackle`, `Bubble`, `Mud Sport`, `Water Gun`; Stats: 30/19/15/17/17/15 |
| Littleroot Town | TBD | TBD | Deferred | Custom pond at `(17, 13..14)` — deferred to catch grass encounters first |
| Route 101 | Butterfree (M, Lv 10) | MORPHEUS | Active | Naughty, Compound Eyes; Moves: `Tackle`, `String Shot`, `Harden`, `Confusion`; Stats: 35/18/15/24/19/19 |
| Route 103 | Hoppip (M, Lv 11) | ZEPHYR | Active | Calm, Chlorophyll; Moves: `Confusion`, `PoisonPowder`, `Mega Drain`, `Gust`; Stats: 31/13/15/14/20/18 |
| Route 102 | Meowth (M, Lv 10) | MIDAS | Active | Naughty, Limber; Moves: `Pay Day`, `Faint Attack`; Stats: 28/16/12/13/11/23 |

<hr>

<h1><code>Main</code></h1>

# Nuzlocke Dashboard — Attempt #1

## Active Rules & Status
- **Attempt**: #1
- **Current Level Cap**: Lv 16 (Roxanne - Rustboro Gym)
- **Battle Style**: `Set` (Configured & verified Turn 13; Text Speed `Fast`)
- **Unlimited Items**: Rare Candies & any acquired Berries auto-refill to 99 in the overworld.
- **Key Items Obtained**: `Pokedex`, `Running Shoes`, `Old Rod` (from Fisherman on Route 103 at `(20, 12)`).

## Level Cap Schedule
1. **Roxanne (Rustboro Gym)**: Lv 16
2. **Brawly (Dewford Gym)**: Lv 20
3. **Wattson (Mauville Gym)**: Lv 29
4. **Flannery (Lavaridge Gym)**: Lv 42
5. **Norman (Petalburg Gym)**: Lv 48
6. **Winona (Fortree Gym)**: Lv 55
7. **Tate & Liza (Mossdeep Gym)**: Lv 70
8. **Wallace / Juan (Sootopolis Gym)**: Lv 77
9. **Champion (Pokemon League)**: Lv 100

## Notepad Index
- `Locations/Encounters`: Route-by-route Nuzlocke encounter tracking & status
- `Mechanics/UI_And_Tools`: Verified menu, Bag, fishing, and overworld mechanics
- `Scratchpad/Routing`: Active early-game notes and routing

<hr>

<h1><code>Mechanics/UI_And_Tools</code></h1>

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

<hr>

<h1><code>Scratchpad/Routing</code></h1>

# Early Game Routing & Notes (Attempt #1)

## Littleroot Town
- **Landmarks**: Player's House (East): `(14, 8)`; Rival's House (West): `(5, 8)`; Birch's Lab: `(7, 16)`.
- **Custom Pond**: Located on the east side at `(18, 12..14)`; stand at `(17, 13)` facing `Right` to fish with the Old Rod.
- **Navigation Note**: Central vertical road runs along `x=10..11` from `y=17` north to `y=0` (Route 101). Use `x=12` (`y=10..17`) to bypass the wandering NPC near `(10..11, 12..14)`.

## Route 101
- **Observed Wild Species**: `Togepi` (Lv 2), `Caterpie` (Lv 2), `Igglybuff` (Lv 3).
- **Grass-Free Path (Northbound)**: `(11, 19)` -> `Up x5` to `(11, 14)` -> `Left x4` to `(7, 14)` -> `Up x4` to `(7, 10)` -> `Right x6` to `(13, 10)` -> `Up` to `(13, 9)` -> `Right x2` to `(15, 9)` -> `Up` to `(15, 8)`, then through `(15, 7..5)` (3 grass tiles) to `(15, 4)` -> `Left x3` (2 grass tiles) to `(12, 4)` -> `Left x2` to `(10, 4)` -> `Up` into Oldale Town.
- **Grass-Free Path (Southbound)**: From `(10, 0)`, step `Left` to `(9, 0)`, walk straight `Down` along `x=9` (jumping ledges at `y=6` and `y=13`) to `(9, 14)`, then `Right x2` to `(11, 14)` and `Down x6` into Littleroot Town `(11, 0)`.

## Oldale Town & Route 103
- **Oldale Central Road**: `x=10` (`y=0..19`) is a straight vertical road between Route 101 and Route 103.
- **Route 103 Grass-Free Path (Northbound)**: From `(10, 21)`, walk `Up x8` to `(10, 13)`, `Right x4` to `(14, 13)`, `Up x3` to `(14, 10)` (east to `(20, 11)` for the Old Rod Fisherman, or north to `(13, 7)` -> `Left x7` to `(6, 7)` -> `(5, 6)` -> `Up x3` to `(5, 3)` for the upper plateau).
- **Route 103 Grass-Free Path (Southbound)**: From `(10, 3)`, walk straight `Down` along `x=10` (jumping ledges at `y=5` and `y=12`) into Oldale Town `(10, 0)`.
- **Oldale West Exit (to Route 102)**: From `(10, 9)`, step `Down x2` to `(10, 11)` (passing south of the scientist at `(8, 9)`) and walk `Left x11` onto Route 102.
## Route 102
- **Eastern Entrance**: Enters from Oldale Town at `(48, 11)`.
- **First Tall Grass Patch**: Located at `(38..39, 5..6)` just west of the pond bank at `(40, 6)`. Caught `Meowth` (Lv 6, `MIDAS`) at `(39, 6)`.
- **Trainers**:
  1. **Youngster Calvin** at `(33, 14)` facing `Down` (approached from `(36, 11) -> (36, 14) -> (34, 14)`):
     - Team (3 Pokemon): `Sentret` (Lv 6, `Quick Attack`), `Zigzagoon` (Lv 6, `Sand-Attack`), `Poochyena` (Lv 6, `Super Fang`).
  2. **Bug Catcher Rick** at `(25, 15)` (rotates/spots `(25, 14)`):
     - Team (4 Pokemon): `Caterpie` (Lv 5), `Wurmple` (Lv 5), `Cascoon` (Lv 5, `Poison Sting`, `Iron Defense`, holds `Berry Juice`), + 1 more Bug-type.

<hr>