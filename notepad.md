<h1><code>Main</code></h1>

# Pokémon Blue Version — Main Dashboard

## Run Overview
- **Game:** Pokémon Blue Version (Generation I)
- **Trainer Name:** COBALT
- **Rival Name:** GARNET
- **Starter Plan:** Squirtle (Nickname: `NAUTILUS`)

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
1. **NAUTILUS** (Squirtle) — Lv. 13 | Moves: Bubble, Tail Whip, Tackle
2. **AMETHYST** (Nidoran♀) — Lv. 4 | Moves: Growl, Tackle

## Inventory & Money
- Money: ¥531
- Key Items: Pokédex, Town Map
- Bag: Antidote x2, Poké Ball x7, TM34 (Bide), Potion x5

## Notepad Index
- `notepads/Main.md` — High-level dashboard & party summary
- `notepads/Scratchpad/Routing.md` — Active route planning & immediate checklists
- `notepads/Mechanics/Harness.md` — Verified harness timing & input behavior


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
- **Evolution `B`-Cancel Warning**:
  - Pressing `B` during a post-battle evolution animation (`"What? <POKEMON> is evolving!"`) **cancels the evolution** in Gen 1! When a Pokémon is at `Lv 15` (`NAUTILUS` -> Wartortle at Lv 16, `AMETHYST` -> Nidorina at Lv 16), use **`A`** (or wait ~12s without `B`) after winning a battle that crosses the Level 16 threshold!
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
- **Pokémon Center Nurse Joy (`(3, 3)` facing `Up` — Requires FIVE `A`s!)**:
  - `["A", "sleep 900", "A", "sleep 900", "A", "sleep 900", "A", "sleep 900", "A", "sleep 8000", "B", "sleep 700", "B", "sleep 700", "B", "sleep 500"]` (plus bounded `for _ in range(5): if y > 3: break; press(["B", "sleep 600", "Down"])` for larger parties, as each additional party Poké Ball adds ~0.4s to the healing machine animation).
  - *(Verified Turn 103: `"We heal your POKéMON..."` has TWO `▼` prompts before `"Shall we heal..."`, so 4 `A`s only opens `►HEAL / CANCEL` and `B` cancels it! The 5th `A` confirms `►HEAL`.)*

## Navigation Scripting Guardrails (Verified Turns 53, 60)
- Always use bounded `for _ in range(N):` loops rather than unbounded `while` loops so an unexpected wall/NPC cannot trip the 150-button script abort limit.
- Never dodge `Down` when walking directly above a south-facing ledge (e.g., Viridian `y = 26`).





<hr>

<h1><code>Scratchpad/Routing</code></h1>

# Active Routing & Immediate Checklist

## Early Game — Pallet Town to Pewter City
1. Complete Professor Oak's introduction:
   - Name player `COBALT` (Done).
   - Name rival `GARNET`.
2. Red's Bedroom (2F):
   - Open `Start` -> `OPTION`: set `TEXT SPEED` = `FAST`, `BATTLE ANIMATION` = `OFF`.
   - Interact with Bedroom PC (top-left corner) -> `COBALT's PC` -> `WITHDRAW ITEM` -> `POTION` (quantity 1).
   - Walk to stairs (top-right) -> 1F -> exit house (bottom door mat).
3. Pallet Town:
   - Step into north grass exit to trigger Professor Oak cutscene.
   - Follow Oak into Lab; choose middle-ish Poké Ball for **Squirtle** (verify prompt says water Pokémon Squirtle before confirming!).
   - Nickname Squirtle `NAUTILUS`.
   - Defeat Rival's Bulbasaur on the way out (Tail Whip once + Tackle spam; use Potion if needed, though winning is optional, winning gives Lv 6 + money!).
4. Oak's Parcel Delivery:
   - Travel north up Route 1 (grab free Potion sample from Mart clerk on Route 1!).
   - Enter Viridian City Poké Mart -> receive `OAK'S PARCEL`.
   - Return south down Route 1 (hopping ledges!) -> Pallet Town -> Oak's Lab -> deliver Parcel -> receive `POKéDEX`.
   - Optional: Visit Rival's sister (house northeast in Pallet Town) to pick up `TOWN MAP`.
5. Viridian City -> Viridian Forest -> Pewter City:
   - Buy Poké Balls at Viridian Mart once Pokédex is obtained.
   - Catch early teammates (e.g., Nidoran♂ on Route 22, Pidgey/Caterpie/Pikachu if encountered) and nickname every catch.
   - Clear Viridian Forest (pick up hidden/visible Potions & Antidote) -> reach Pewter City -> challenge Brock!


<hr>