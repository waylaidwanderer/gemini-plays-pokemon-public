<h1><code>Main</code></h1>

# Pokémon Blue Version — Main Dashboard

## Run Overview
- **Game:** Pokémon Blue Version (Generation I)
- **Trainer Name:** COBALT
- **Rival Name:** GARNET
- **Starter:** Squirtle (Nickname: `NAUTILUS`)

## Badges & Milestones
- [x] Starter Pokémon & Pokédex (Pallet Town / Viridian City)
- [x] Boulder Badge — Brock (Pewter City)
- [ ] Cascade Badge — Misty (Cerulean City)
- [ ] Thunder Badge — Lt. Surge (Vermilion City)
- [ ] Rainbow Badge — Erika (Celadon City)
- [ ] Soul Badge — Koga (Fuchsia City)
- [ ] Marsh Badge — Sabrina (Saffron City)
- [ ] Volcano Badge — Blaine (Cinnabar Island)
- [ ] Earth Badge — Giovanni (Viridian City)
- [ ] Indigo Plateau — Elite Four & Champion

## Active Party
1. **AMETHYST** (Nidoran♀) — Lv. 9 | Moves: Scratch, Growl, Tackle
2. **NAUTILUS** (Wartortle) — Lv. 17 | Moves: Water Gun, Tail Whip, Tackle, Bubble
3. **CELESTE** (Clefairy) — Lv. 8 | Caught on Mt. Moon 1F (1% encounter!)

## Inventory & Money
- Money: ~¥1,700
- Key Items: Pokédex, Town Map
- Bag: Potion x2, Antidote x1, Poké Ball x3, TM34 (Bide), TM12 (Water Gun — save for Nidoqueen!)

## Notepad Index
- `notepads/Main.md` — High-level dashboard & party summary
- `notepads/Scratchpad/Routing.md` — Active route planning & immediate checklists
- `notepads/Mechanics/Harness.md` — Verified harness timing & input behavior
- `notepads/Locations/` — Verified town, route, and dungeon notes


<hr>

<h1><code>Locations/PalletTown</code></h1>

# Pallet Town — Verified Coordinates & Landmarks

## Red / Cobalt's House
- **2F (Bedroom)**:
  - Initial spawn: `(3, 6)`
  - Bedroom PC: `(0, 1)` — interact from `(0, 2)` facing `Up` (contains 1 free `POTION` at start).
  - Stairs to 1F: `(7, 1)`
- **1F (Living Room)**:
  - Stairs arrival from 2F: `(7, 1)`
  - Clear route to exit: `(7, 1) -> (6, 1..6) -> (3, 6..7) -> Down`
  - Exits to Pallet Town at `(5, 6)`.

## Pallet Town Overworld
- Cobalt's House door: `(5, 5)` (exits to `(5, 6)`).
- North tall-grass Route 1 entrance: `(10, 1)` and `(11, 1)`.
- Professor Oak's Lab door: `(12, 11)` (exits to `(12, 12)`).
- Rival's House (Daisy / Town Map): Northeast house (`x = 12..15, y = 3..5`, door at `(13, 5)`).

## Professor Oak's Lab
- Starter Poké Ball table: `(6, 3)` Charmander, `(7, 3)` Squirtle, `(8, 3)` Bulbasaur.
- Table front apron `(6..8, 4)` is walkable floor; interact facing `Up` from `(x, 4)`.
- Central aisle: `x = 4..5`; Rival first battle triggers at `y = 6` (`(4, 6)` or `(5, 6)`).
- Exit mat: `(4, 11)` and `(5, 11)` (`Down` exits to Pallet Town).


<hr>

<h1><code>Locations/PewterCity</code></h1>

# Pewter City — Verified Coordinates & Landmarks

## Map Connections
- **South Entrance (from Route 2 North)**: Enters at `(18, 35)`.
- **East Exit (to Route 3)**: Walk East from `(23, 18)` along `y = 18..19` to `x = 39 -> Right` warps to Route 3 `(0, 10)`.
  - **Route 3 Early Landmarks**: Lass #1 triggers at `(14, 9)` (`2x Pidgey Lv 9`); Bug Catcher #1 triggers at `(11, 6)` (`Caterpie Lv 10, Weedle Lv 10, Caterpie Lv 10`).

## Key Buildings
- **Pokémon Center**: Door at `(13, 25)` (approached via `(18, 35) -> (18, 26) -> (13, 26)`).
- **Poké Mart**: Door at `(23, 17)` (east of central `x = 19` road).
- **Pewter City Gym**: Door at `(16, 17)`.
  - Verified loop from `(13, 26)` PokéCenter: `(13, 26) -> (19, 26) -> (19, 12) -> (11, 12) -> (11, 16) -> (10, 16) -> (10, 18) -> (16, 18) -> Up` into `(16, 17)` (reverse to exit).
  - Interior: Spawn at `(4, 13)`, Jr. Trainer♂ triggers at `(4, 6)`, Brock stands at `(4, 1)` (talk from `(4, 2)`).


<hr>

<h1><code>Locations/Route1</code></h1>

# Route 1 — Verified Coordinates & Navigation

## Map Connections
- **South Exit (to Pallet Town)**: `x = 10..11, y = 35` -> `Down` warps to Pallet Town `(10..11, 0)`.
- **North Exit (to Viridian City)**: `x = 10..11, y = 0` -> `Up` warps to Viridian City `(20..21, 35)`.

## Key NPCs
- **Poké Mart Sample Clerk (Free Potion)**: Wanders around `(5, 24..25)` in the west-central clearing.

## Verified Northbound Path (Pallet -> Viridian)
1. Enter at `(10, 35)` -> `Up` x 7 to `(10, 28)`.
2. `Left` x 2 to `(8, 28)` -> `Up` x 2 to `(8, 26)` -> `Right` x 5 to `(13, 26)` -> `Up` x 6 to `(13, 20)`.
3. `Left` x 8 to `(5, 20)` -> `Up` x 6 to `(5, 14)`.
4. `Right` x 10 to `(15, 14)` (avoids Boy NPC at `(14, 13)`) -> `Up` x 3 to `(15, 11)`.
5. `Left` x 4 to `(11, 11)` -> `Up` x 5 to `(11, 6)` -> `Right` x 3 to `(14, 6)` -> `Up` x 2 to `(14, 4)` -> `Left` x 3 to `(11, 4)` -> `Up` x 5 into Viridian City.

## Verified Southbound Ledge Chain (Viridian -> Pallet, Minimal Grass)
1. Enter at `(10, 0)` -> `Down` x 3 to `(10, 3)` -> `Left` x 2 to `(8, 3)`.
2. `Down` along column `x = 8` down to `(8, 18)` (hops 3 ledges at `y = 5, 9, 13` with ZERO tall grass tiles!).
3. `Right` x 5 to `(13, 18)` -> `Down` to `(13, 26)` (hops `y = 19` ledge; 4 grass tiles `y = 22..25`).
4. `Left` x 3 to `(10, 26)` -> `Down` to `(10, 35)` -> `Down` into Pallet Town `(10, 0)` (hops `y = 27` ledge; 4 grass tiles `y = 32..35`).



<hr>

<h1><code>Locations/Route2_ViridianForest</code></h1>

# Route 2 & Viridian Forest — Verified Coordinates

## Route 2 (South Half)
- **South Entrance (from Viridian City)**: Enters at `(8, 71)`.
- **Verified Path to Viridian Forest South Gate**:
  - `(8, 71) -> (8, 63) -> (7, 63) -> (7, 59)` (crosses `(7, 61)` bridge).
  - `(7, 59) -> (3, 59) -> (3, 48) -> (8, 48) -> (8, 46) -> (3, 46) -> (3, 43)` (South Gate door).
- **Viridian Forest South Gate (`10x8`)**:
  - South entrance arrives at `(4, 7)`.
  - North exit door to Viridian Forest is at `(5, 0)`.

## Viridian Forest (`34x48`)
- **South Entrance**: Arrives at `(17, 47)`.
- **Verified Low-Grass S-Curve Route**:
  1. `(17, 47) -> (17, 43) -> (27, 43) -> (27, 41) -> (26, 41) -> (26, 33)` (Bug Catcher #1 at `(27, 33)`).
  2. `(26, 33) -> (26, 32) -> (31, 32) -> (31, 8)` (100% grass-free east lane!).
  3. `(31, 8) -> (16, 8) -> (16, 19) -> (12, 19) -> (12, 4) -> (11, 4) -> (11, 2) -> (6, 2) -> (6, 25) -> (1, 25)`.
  4. `(1, 25) -> (1, 18)` (Bug Catcher Sammy: `Weedle Lv 9`) -> `(1, 0)` (North Gate warp).
- **Viridian Forest North Gate (`10x8`)**:
  - South entrance arrives at `(4, 7)`; North exit door at `(5, 0)` -> Route 2 North `(3, 11)`.
- **Route 2 (North Exit to Pewter City)**:
  - `(3, 11) -> (8, 2) -> (8, 0) -> Up` warps to Pewter City `(18, 35)`.



<hr>

<h1><code>Locations/Route3_MtMoon</code></h1>

# Route 3 & Route 4 West — Verified Coordinates & Landmarks

## Route 3 (`x = 0..59`)
- **West Entrance (from Pewter City `(39, 18)`)**: Enters at `(0, 10)`.
- **Verified Trainers & Obstacles**:
  - **Lass #1**: `(14, 9)` (`2x Pidgey Lv 9`) — Defeated.
  - **Bug Catcher #1**: `(11, 6)` (`Caterpie Lv 10, Weedle Lv 10, Caterpie Lv 10`) — Defeated.
  - **Youngster #1**: `(14, 6)` (`Rattata Lv 11, Ekans Lv 11`) — Defeated.
  - **Bug Catcher #2**: `(19, 5)` facing Left/Down, triggered at `(19, 6)` (`Weedle Lv 9, Kakuna Lv 9, Caterpie Lv 9, Metapod Lv 9`) — Defeated (Turn 141).
  - **Lass #2**: Starts at `(23, 4)` facing Left, spots player at `(20, 4)` and walks to `(21, 4)` (`Rattata Lv 10, Nidoran♂ Lv 10`) — Defeated (Turn 146; `NAUTILUS` reached Lv 16).
  - **Tree Wall & Ledges around `x = 17..24`**:
    - Vertical bush barriers at `(17, 6)..(17, 10)` and `(23, 6)..(23, 10)`.
    - South-facing ledge along `y = 7` (`(15, 7)..(16, 7)`, `(18, 7)..(22, 7)`, `(24, 7)`).
    - Open eastward gap between rock wall (`y = 3`) and bush column (`x = 23, y >= 6`) runs along `y = 4..5` (`(20, 5) -> (24, 5)` bypasses `(21, 4)` Lass #2).
    - **Bug Catcher #3**: Stands at `(24, 6)` facing Right; spots player at `(27, 6)` (`Caterpie Lv 11, Metapod Lv 11`) — Defeated (Turn 152). Wooden stairs across the `y = 7` ledge are at `(27, 7)`.
    - **Youngster #2**: Visible at `(22, 9)` facing Left (south of `y = 7` ledge).
    - **Lass #3**: Triggers at `(33, 8)` (`Jigglypuff Lv 14`) — Defeated (Turn 155; `NAUTILUS` reached Lv 17).
  - **East Exit to Route 4**:
    - From `(33, 8)` -> `(37, 8)` -> stairs at `(37, 7)` -> `(37, 4)` -> East along `y = 4` to `(49, 4)` -> South down stairs `(49, 7)` to `(49, 10)` -> East to `(56, 10)` -> `(56, 8)` -> `(59, 8)` -> North up stairs `(59, 7)` along `x = 59` to `(59, 0) -> Up`, which connects to **Route 4 `(9, 17)`**.

## Route 4 West (Outside Mt. Moon)
- **South Connection (from Route 3 `(59, 0)`)**: Enters at `(9, 17)` (dodge south ledges `(6, 15)..(9, 15)` via `x = 10..11` and `(7, 11)..(11, 11)` via `x = 12..13`).
- **Mt. Moon Pokémon Center**: Door at `(11, 5)` (settles last-visited heal checkpoint right outside Mt. Moon!).
- **Mt. Moon 1F Entrance**: Walk East along `y = 6` from `(11, 6)` to `(18, 6) -> Up` into `(18, 5)`.

## Mt. Moon 1F (`40 x 36`)
- **Entrance / Exit Mat**: `(14, 35)..(15, 35)` (warps back to Route 4 `(18, 6)`).
- **Southwest Corridor (`TM12 Water Gun`)**:
  - From `(14, 35)` walk `Up * 7` to `(14, 28)` -> `Left * 9` to `(5, 28)`.
  - Item ball at **`(5, 32)`** (`TM12 Water Gun` — visible 4 tiles south of `(5, 28)` in Turn 166 `filmstrip_2.png`).


<hr>

<h1><code>Locations/ViridianCity</code></h1>

# Viridian City — Verified Coordinates & Landmarks

## Map Connections
- **South Exit (to Route 1)**: `x = 20..21, y = 35` -> `Down` warps to Route 1 `(10..11, 0)`.
- **West Exit (to Route 22)**: `y = 17, x = 0` (reached via `(19, 18) -> (4, 18) -> (4, 17) -> (0, 17)`) -> `Left` warps to Route 22 `(39, 9)`.
  - **Route 22 Safe East Grass**: `(39, 9) -> (35, 9) -> (35, 12) -> (33, 12) -> (33, 8..11)` (safely east of `x = 29` Rival 2 trigger; contains Spearow, Nidoran♀/♂, Rattata).
- **North Exit (to Route 2)**: Straight `Up` along `x = 18..19` from `(19, 18)` to `y = 0`.
- **South Entrance Ledge**: Row `y = 27`; northbound wooden bridge gap at `(19, 27)`; southbound hop available along `x = 20` (`(20, 26) -> (20, 28)`, completely unobstructed down column `x = 20` to `y = 35`).

## Key Buildings
- **Pokémon Center**: Door at `(23, 25)` (south road along `y = 26`).
- **Poké Mart**: Door at `(29, 19)` (reached via `(29, 26) -> (29, 20)` or `(27, 26) -> (27, 20) -> (29, 20)`).
  - Interior (`8x8`): Exit mat at `(3, 7)` and `(4, 7)` (Parcel cutscene leaves player at `(2, 5)`, requiring `Right` to `x = 3` before exiting `Down`).



<hr>

<h1><code>Mechanics/Harness</code></h1>

# Harness & Emulator Mechanics (Verified)

## Tool Sequencing (Verified Turns 2–4)
- Top-level tool calls execute sequentially in the order emitted.
- Calling `mcp_game_press_buttons` followed by `read_file` on `screenshots/latest.png` in the same turn reliably reads the newly settled screen produced at the end of `press_buttons`.

## Real-Time Emulation Clock (Verified Turn 3 `filmstrip_1.png`)
- The emulator runs continuously in real time during `[THINKING]` (observed `#01 +0.00s` -> `#03 +28.53s` in Turn 3).
- Implications:
  - Keep deliberation concise to avoid unnecessary real-time drift in areas with wandering NPCs.
  - Static menus, dialogue prompts, and battle command menus safely wait for input regardless of elapsed thinking time.

## Gen 1 Dialogue Safety
- Pressing `B` advances standard `▼` text boxes and accelerates text scrolling without accidentally confirming `YES/NO` prompts (defaults to `NO`/cancel) or list menus like `YOUR NAME?` that disallow `B` cancellation.

## Gen 1 Naming Screen Grid (Verified Turn 6)
9 columns (`0..8`) x 5 character rows (`0..4`), cursor starts at `(0, 0)` (`A`):
- Row 0: `A B C D E F G H I`
- Row 1: `J K L M N O P Q R`
- Row 2: `S T U V W X Y Z [space]`
- Row 3: `× ( ) : ; [ ] PK MN`
- Row 4: `- ? ! ♂ ♀ / . , ED` (where `(8, 4)` is `ED` = End/Confirm; Note: filling max length auto-jumps cursor to `ED`!)
- Row 5: `lower case` toggle across bottom row.
- Reusable Python generator (for names shorter than max length: <7 for trainer/rival, <10 for Pokémon):
```python
ROWS = ["ABCDEFGHI", "JKLMNOPQR", "STUVWXYZ "]
def name_buttons(word):
    cx, cy, seq = 0, 0, []
    for ch in word:
        for ry, r in enumerate(ROWS):
            if ch in r: tx, ty = r.index(ch), ry; break
        seq += (["Right"]*(tx-cx) if tx>cx else ["Left"]*(cx-tx))
        seq += (["Down"]*(ty-cy) if ty>cy else ["Up"]*(cy-ty)) + ["A"]
        cx, cy = tx, ty
    return seq + ["Right"]*(8-cx) + ["Down"]*(4-cy) + ["A"]
```

## Event & Fanfare Timings (Verified Turns 2–41)
- **ROM Variant**: Colorized Pokémon Blue enhancement with GBC palettes and a live blue EXP bar under player HP in battle (verified Turn 27). Maps, items, and encounters match Pokémon Blue.
- **Battle Move Cursor Memory**:
  - **New Battle (Turn 1)**: BOTH the top-level command menu (`►FIGHT`) AND the `FIGHT` move submenu (`►Slot 1`) **reset to Slot 1** at the start of every new battle (verified Turn 97 `filmstrip_1.png` — earlier assumption that `FIGHT` remembered across battles was false!).
  - **Same Battle (Turn 2+)**: Within the same battle, the top-level command menu, `FIGHT` submenu, and `ITEM` submenu all remember their last selected positions (verified Turns 21, 67, 73).
  - *(Tip — Verified `Select` Swap Mechanics, Turns 110, 121, 125)*:
    - In the **`FIGHT` move menu**, `Select -> Down * k -> Select` swaps Slot `k` into Slot 0 and **automatically resets the cursor onto Slot 0** (and note: `FIGHT` wraps vertically, so pressing `Up` from Slot 0 wraps to the bottom move!).
    - In the **`ITEM` bag menu**, `Select -> Down * k -> Select` leaves the cursor at Slot `k`; always verify the highlighted item before pressing `A` after reordering items.
  - In `SHIFT` trainer battles, `B`-clearing between attack rounds safely declines `"Will COBALT change POKéMON?"` (`NO`). Use 8–10 `B` presses (`"sleep 650"`) per round when stat-drop or poison ticks occur (Turns 83, 95).
- **Catching & Nickname Safety (Verified Turns 66–75)**:
  - Never spam `B` after throwing a Poké Ball (`B` cancels `"give a nickname?"` as `NO`). Wait `"sleep 9500"` after throwing a Ball to inspect catch outcome, then advance Pokédex Page 1 & Page 2 with `A` up to the `►YES / NO` nickname prompt.
- **Evolution `B`-Cancel Warning & Verified Safe Evolution Recipe (Verified Turn 146)**:
  - Pressing `B` during a post-battle evolution animation (`"What? <POKEMON> is evolving!"`) **cancels the evolution** in Gen 1!
  - Evolution ONLY triggers **after the entire battle ends** (never mid-battle when KOing an earlier trainer Pokémon, and never if the evolving Pokémon faints before the battle ends).
  - Verified recipe when KOing the final opposing Pokémon on an evolution battle: execute the attack (`["A", "sleep 400", "A", "sleep 3500"]`), then use **ONLY `A`** (`["A", "sleep 1100"] * 6 + ["A", "sleep 10000", "A", "sleep 6000", "A", "sleep 1500", "A", "sleep 1500"]`) — `A` advances victory dialogue without ever cancelling evolution.
- **Gen 1 Battle Quirks (Verified Turns 137–139)**:
  - `Bubble` is 20 BP (half of `Water Gun`'s 40 BP), and 100%-accurate moves in Gen 1 still have a `1/256` miss chance (observed on `Water Gun` in Turn 139 `filmstrip_1.png` `#18`). Always verify KO outcomes before assuming fixed hit counts.
- **Coordinate Behavior in Battles & Warps**:
  - `mgba.get_coordinates()` continues returning the underlying overworld `(x, y)` during battles (`<GameState>` omits `<Position>` when in battle).
  - Step-by-step `before == after` comparison reliably detects wild encounters in tall grass; following a blocked grass step with `["sleep 800", "B"] * 8` (~6.4s) lands cleanly on `►FIGHT`.
  - Door warps have a ~0.5s white fade; ending a script immediately on a door step can capture the white transition frame before indoor coordinates update (Turn 41). Call `tools.observe()` or include a short post-warp settle when inspecting a new room.
- **Title Screen**: Pressing `Start` during a starter sprite swap is ignored; wait or append `"sleep 1500"` for the starter cry to finish before Main Menu input.
- **Pokémon Obtained Fanfare**: Lasts ~4.5 seconds before `"received a <POKEMON>!"` accepts `A`/`B` dismissal (`"sleep 3500"` was slightly early in Turn 18).
- **Cutscene Clearing**: Spacing `B` presses with `"sleep 700"`–`"sleep 900"` safely clears multi-box dialogues and lands cleanly on `►FIGHT` (in battles) or `YOUR NAME?` without triggering unwanted `YES` confirmations or attacks.

## Poké Mart & Pokémon Center Recipes (Verified Turns 52–62)
- **Poké Mart Buying (Requires THREE `A`s after Quantity!)**:
  1. Select item with `A`, `"sleep 900"` -> opens `×01` (`Up` increments quantity).
  2. `A` #1 (`"sleep 900"`) -> `"<ITEM>? ▼"`
  3. `A` #2 (`"sleep 900"`) -> `"That will be ¥<PRICE>. OK?"` `►YES / NO`
  4. `A` #3 (`"sleep 900"`) -> `"Here you are! Thank you! ▼"` (always verify `MONEY` box decreased before pressing `B`!).
  *(Misstep fixed in Turn 62: pressing only two `A`s before `B` cancels `YES/NO` as `NO`.)*
- **Pokémon Center Nurse Joy (`(3, 3)` facing `Up` — Requires FIVE `A`s & FOUR `B`s!)**:
  - `["A", "sleep 900"] * 4 + ["A", "sleep 8500"] + ["B", "sleep 700"] * 4` before stepping `Down` (verified Turn 162: only 3 `B`s left `"We hope to see you again!"` open during the `Down` loop).

## Navigation Scripting Guardrails & Cave Primitives (Verified Turns 53, 60, 152, 165–166)
- Always use bounded `for _ in range(N):` loops rather than unbounded `while` loops so an unexpected wall/NPC cannot trip the 150-button script abort limit.
- Never dodge `Down` when walking directly above a south-facing ledge (e.g., Viridian `y = 26`).
- **Gen 1 Menu Wrapping Summary (Verified Turns 124, 155, 184)**:
  - `Start` menu (`POKéDEX .. EXIT`) **wraps** vertically (`Up` from `POKéDEX` jumps to `EXIT`, `Down` from `EXIT` jumps to `POKéDEX`), and catching a new Pokémon resets `Start` to `POKéDEX`.
  - Battle `FIGHT` move menu **wraps** vertically.
  - `ITEM` bag menu **clamps** (does NOT wrap) at Slot 0 (`Up` at top stays on Slot 0).
  - Battle 2x2 command menu (`FIGHT / PKMN / ITEM / RUN`) **clamps** (`Left, Up` always lands on `►FIGHT`).
  - The 2x2 battle command menu (`FIGHT / PKMN / ITEM / RUN`) does **not** wrap, so `["Left", "sleep 150", "Up", "sleep 150"]` deterministically resets the cursor to `►FIGHT` from any quadrant, and pressing `Left` or `Up` while already on `►FIGHT` is a pure no-op in battle.
  - When a step `d` from `b` fails (`after == b`), clearing potential battle intro (`["sleep 1200"] + ["B", "sleep 700"] * 8`) and probing `back_d` (the known-open tile you just came from) cleanly distinguishes a **wall** (`pos != b`) from an active **battle** (`pos == b`), and in Gen 1 `PlayerSpeed >= EnemySpeed` guarantees 100% first-try escape via `RUN`.





<hr>

<h1><code>Scratchpad/Routing</code></h1>

# Active Routing & Immediate Checklist

## Route 3 -> Mt. Moon -> Cerulean City (Cascade Badge)
1. **Route 3 (`y = 0..17, x = 0..59`)**:
   - Defeat Bug Catcher #2 at `(19, 6)` -> `NAUTILUS` reaches Level 15 (`Water Gun`) and approaches Level 16 (`Wartortle` — do NOT press `B` during evolution!).
   - Navigate east across Route 3 (`x = 19 -> 54`) and north (`y = 0`) onto Route 4.
   - Heal at the **Mt. Moon Pokémon Center** on Route 4 West before entering Mt. Moon.
2. **Mt. Moon (`1F -> B1F -> B2F`)**:
   - **1F Items**:
     - Pick up `TM12 (Water Gun)` at `(5, 32)` (Done — verified Turn 178 `filmstrip_1.png` `#16` that `Nidoran♀` is `NOT ABLE` to learn `TM12`, so keep `TM12` in Bag and teach it to `AMETHYST` right after she evolves into **Nidoqueen** at Level 16!).
     - Pick up `Potion` at `(2, 20)`, `Moon Stone` (top-left corner of 1F), `Rare Candy` (bottom-right of 1F), and `Escape Rope`.
   - **Training & Nidoqueen Power Spike**:
     - Switch-train **`AMETHYST`** (lead Slot 0 -> switch to `NAUTILUS` Lv. 17 Wartortle on trainers, plus finish safe low-level targets) through Mt. Moon trainers until **Level 16** -> evolves into **Nidorina** (use `A` after KOs at Lv 15 so evolution isn't `B`-cancelled!).
     - Immediately use the **`Moon Stone`** on `AMETHYST` (`Nidorina`) -> evolves into **Nidoqueen** at Level 16, then teach her **`TM12 (Water Gun)`**! (Nidoqueen also learns **Body Slam** at Level 23 in Pokémon Blue!).
   - **B2F Finale**:
     - Pick up `TM01 (Mega Punch)` (via the B2F side ladder) and consider teaching to `AMETHYST` or `NAUTILUS` for neutral physical power against Misty's Starmie.
     - Defeat Team Rocket Grunts & Super Nerd Miguel -> claim a Fossil (`Dome` or `Helix`) -> exit via B1F corridor to Route 4 East -> hop ledge east into **Cerulean City**.
3. **Cerulean City & Route 24/25**:
   - Heal at Cerulean Pokémon Center.
   - Defeat Rival **`GARNET`** at Nugget Bridge (`Pidgeotto Lv 18, Abra Lv 15, Rattata Lv 15, Bulbasaur Lv 17`).
   - Clear Nugget Bridge (5 trainers + Rocket Grunt for `Nugget`) -> cross Route 25 -> rescue **Bill** at Sea Cottage for the **`S.S. TICKET`**.
   - Challenge **Cerulean Gym** -> defeat **Misty** (`Staryu Lv 18, Starmie Lv 21`) -> earn **Cascade Badge** + `TM11 (BubbleBeam)`.
   - Defeat backyard Team Rocket Grunt -> obtain **`TM28 (Dig)`** -> head south down Route 5 Underground Path to Vermilion City.


<hr>