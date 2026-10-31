<h1><code>Locations/Encounters</code></h1>

# Nuzlocke Encounters (Attempt #1)

| Location | Pokemon | Nickname | Status | Notes |
| :--- | :--- | :--- | :--- | :--- |
| Starter (Route 101) | Mudkip (M, Lv 10) | TRITON | Active | Bashful, Torrent; Held: `Oran Berry`; Moves: `Tackle`, `Bubble`, `Mud Sport`, `Water Gun`; Stats: 30/19/15/17/17/15 |
| Littleroot Town | TBD | TBD | Deferred | Custom pond at `(17, 13..14)` — deferred to catch grass encounters first |
| Route 101 | Butterfree (M, Lv 12) | MORPHEUS | Active | Naughty, Compound Eyes; Held: `Oran Berry`; Moves: `Tackle`, `String Shot`, `Harden`, `Confusion`; Stats: 40/20/17/28/22/22 |
| Route 103 | Hoppip (M, Lv 11) | ZEPHYR | Active | Calm, Chlorophyll; Held: `Oran Berry`; Moves: `Confusion`, `PoisonPowder`, `Mega Drain`, `Gust`; Stats: 31/13/15/14/20/18 |
| Route 102 | Meowth (M, Lv 10) | MIDAS | Active | Naughty, Limber; Held: `Oran Berry`; Moves: `Pay Day`, `Faint Attack`; Stats: 28/16/12/13/11/23 |
| Petalburg City | Azurill (F, Lv 10) | CALYPSO | Active | Bashful, Huge Power; Held: `Oran Berry`; Moves: `Water Gun`, `Charm`, `Secret Power`, `BubbleBeam`; Stats: 32/9/14/9/14/10 |
| Route 104 | Jigglypuff (F, Lv 10) | LYRA | Active | Quiet, Cute Charm; Held: `Oran Berry`; Moves: `Sing`, `Pound`, `Disable`; Stats: 45/16/11/15/12/10 |

<hr>

<h1><code>Main</code></h1>

# Nuzlocke Dashboard — Attempt #1

## Active Rules & Status
- **Attempt**: #1
- **Current Level Cap**: Lv 16 (Roxanne - Rustboro Gym)
- **Battle Style**: `Set` (Configured & verified Turn 13; Text Speed `Fast`)
- **Unlimited Items**: Rare Candies & any acquired Berries (`Oran Berry` +10 HP, `Pecha Berry` cures Poison — picked at `(24..25, 2)` on Route 102) auto-refill to 99 in the overworld.
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
  - Switching through an empty pocket (`TMs & HMs` or `BERRIES`) clamps the item cursor onto `>CLOSE BAG`; since `Up` never wraps past index 0 inside a Bag pocket or Poke Mart list, pressing `Up` multiple times deterministically clamps to index 0 (and `Up, Up, Down` deterministically selects index 1).
  - Giving a held item (`GIVE`) to a Pokemon already holding an item prompts `"Would you like to switch the two items? [>YES / NO]"`; press `A` to swap the items, and allow `~1200ms` for the Party screen to fade back to the Bag.
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
- **Battle Menu Action Cursor**: At the start of every new battle turn (`What will [POKEMON] do?`), the action cursor always resets to `>FIGHT` (top-left, index 0). It only remains on `>BAG` or `>POKEMON` if you cancel out of the Bag or Party screen with `B` during the same turn, or after a failed Poke Ball throw (`>BAG`).
- **Berry Tree Harvesting**: Interacting with a Berry Tree takes **3 `A` presses** (`Interact -> "You found N [X] BERRIES!" -> "Do you want to pick the [X] BERRIES? [>YES]"`), followed by `sleep 3500` for the fanfare and **3 `B` presses** (`sleep 1500` apart) to dismiss the put-away and loamy-soil messages without replanting.
  - **Loamy Soil `USE` Trap**: Selecting `USE` on a Berry in the `BERRIES` pocket while facing a soft, loamy soil patch in the overworld automatically plants the Berry into the soil and exits the Bag/Start menu to the overworld instead of opening the Party menu. Always turn away or step off the loamy soil before selecting `USE` on a Berry.

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
- **Eastern Entrance**: Enters from Oldale Town at `(48, 11)`. Caught `Meowth` (Lv 6, `MIDAS`) at `(39, 6)`.
- **Trainers**:
  - **Defeated**: Youngster Calvin `(33, 14)`, Bug Catcher Rick `(25, 15)`, Lass Tiana `(15, 5)`, Bug Catcher Allen `(13, 2)`.
  - **Remaining**: Trainer in tall grass at `(18, 12)`.
- **Northern Berry Patch & Grass-Free Routes**:
  - **Grass-Free Path North**: `(25, 14)` -> `Up x4` to `(25, 10)` -> `Left x4` to `(21, 10)` -> `Up x2` to `(21, 8)` -> `Left x2` to `(19, 8)` -> `Up x3` to `(19, 5)`.
  - **Berry Trees**: Located at `(24, 2)` (`Oran Berry`) and `(25, 2)` (`Pecha Berry`); harvested on Turn 144 (auto-refill to 99 in the overworld).
  - **Grass-Free Path to Petalburg City**: From `(13, 3)`, step `Left` to `(12, 3)`, `Down x4` to `(12, 7)`, `Left` to `(11, 7)`, `Down` to `(11, 8)`, and `Left x12` along `y=8` straight into Petalburg City.

## Petalburg City
- **Eastern Entrance**: Enters from Route 102 onto `y=18` (`x=29`).
- **Landmarks**:
  - **Pokemon Center**: Door at `(20, 16)`.
  - **Poke Mart**: Door at `(25, 12)` (`Poke Ball` $10, `Potion` $300, `Antidote` $100, `Parlyz Heal` $200, `Awakening` $250, `Escape Rope` $550, `Repel` $350, `X Speed` $350, `X Attack` $500, `X Defend` $550, `Orange Mail` $50).
  - **Petalburg Gym**: Door at `(15, 8)`; Norman at `(4, 107)` inside — **Norman & Wally tutorial event COMPLETED (Turns 207-208)**.
  - **Wally's House**: Door at `(12, 19)`.
  - **Southern Pond**: Located at `x=6..11, y=22..25`; stand at `(12, 23)` facing `Left` at `(11, 23)` to fish (caught `Azurill` Lv 5, `CALYPSO`).
  - **Western Exit (to Route 104)**: Straight west along `y=12..13` past `(8, 12)` to `x=0` (triggers Scott cutscene near `x=4`).
## Route 104 (South)
- **Eastern Entrance**: Enters from Petalburg City at `(36, 62)`.
- **Tall Grass Patch**: Located at `(22..24, 56..61)`; caught `Jigglypuff` (Lv 7, `LYRA`) at `(23, 60)`.
- **Beach Staircase**: Located at `(28..29, 70)` (the northern ledges at `y=57..59` are one-way southbound).
- **Trainers & NPCs**:
  - **Friendly Boy** at `(28, 74)` on the shoreline (not a trainer).
  - **Bird Keeper Billy** at `(23, 66)` facing `Left` — **DEFEATED**:
    - Team (3 Pokemon): `Pidgey` (Lv 7, holds `Berry Juice`), `Wingull` (Lv 7, `Supersonic`, `Water Gun`, `Gust`), `Taillow` (Lv 7).
  - **Friendly Fisherman** at `(15, 60)` facing `Right` (not a trainer).
  - **Fisherman Darian** at `(15, 59)` facing `Right` — **DEFEATED**:
    - Team (4 Pokemon): `Magikarp` (Lv 9, `Bounce`), `Feebas` (Lv 8, `Icy Wind`, `Facade`, holds `Sitrus Berry`), `Goldeen` (Lv 7, `Swift Swim`; `Rain Dance`, `Peck`, `Horn Attack`, `Dive`), `Luvdisc` (Lv 7, `Attract`).
- **Mr. Briney's Cottage & Northern Berry Patch**:
  - Cottage door at `(17, 51)`; northern beach stairs at `(17..18, 55)`.
  - **Berry Trees**: Located at `(22, 41)` (`Oran Berry`) and `(24, 41)` (`Pecha Berry`) — harvested Turn 267.

<hr>