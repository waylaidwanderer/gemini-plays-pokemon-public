<h1><code>Locations/Littleroot_Town</code></h1>

# Littleroot Town — Coordinates & Points of Interest

## Overworld Coordinates
- **Player's House Door (Left House):** `(5, 8)`
- **Rival May's House Door (Right House):** `(14, 8)`
- **Clear East-West Path between Houses:** `y = 9` from `x = 5` to `x = 14`

## Player's House
- **1F Stairs to 2F:** `(8, 2)`
- **1F Exit Mat:** `(8, 8)` / `(9, 8)`
- **2F Stairs to 1F:** `(7, 1)` (arrives at `(7, 2)`)
- **2F Wall Clock:** `(5, 1)` (interact from `(5, 2)` facing Up; confirmation defaults to `NO`, press `Up` then `A` for `YES`)
- **2F Desk PC:** `(0, 1)` (interact from yellow chair at `(0, 2)` facing Up; free Potion x1 withdrawn on Turn 17)

## Rival May's House (Professor Birch's House)
- **1F Entrance Mat:** `(1, 8)` / `(2, 8)` (exiting steps automatically to `(14, 9)` outside)
- **1F Stairs to 2F:** `(2, 2)`
- **2F Stairs to 1F:** `(1, 1)` (arrives at `(1, 2)`)
- **2F May's Poké Ball:** `(5, 4)` (interacting from `(4, 4)` triggers May's entrance and introduction)

## Northern Exit to Route 101
- **North Road:** `x = 10` (or `x = 11`), walking north from `y = 9` to `y = 0` transitions into Route 101.

## Professor Birch's Pokémon Lab
- **Exterior Door:** `(7, 16)` in Littleroot Town (exiting steps to `(7, 17)`)
- **Interior Center Aisle:** `x = 6` from `y = 5` (Professor Birch at `(6, 4)`) straight south to the exit mat at `(6, 12)`.

<hr>

<h1><code>Locations/Route_101_And_Oldale_Town</code></h1>

# Route 101 & Oldale Town — Coordinates & Routing

## Route 101
- **South Entrance (from Littleroot Town):** `(10, 19)` / `(11, 19)`
- **Northbound Path (Littleroot -> Oldale):**
  - From `(10, 19)`, walk `Up` to `(10, 16)`, `Left` 3 to `(7, 16)` (bypasses lower ledge `x=8..11, y=13` and left grass `x=3..5`).
  - Walk `Up` to `(7, 10)`, `Right` 3 to `(10, 10)`, `Right` 5 through grass (`x=11..14, y=10`) to clear road at `(15, 10)`.
  - Walk `Up` 5 along `x=15` to `(15, 5)`, `Left` 5 to `(10, 5)`, and `Up` 6 along `x=10` into Oldale Town `(10, 19)`.
- **Southbound Fast Path (Oldale -> Littleroot via Ledges):**
  - Jump south over upper ledge at `x=6..10, y=6` and lower ledge at `x=8..11, y=13` with zero grass encounters.

## Oldale Town
- **Center Crossroads:** `(10, 10)`
- **Pokémon Center Door:** `(6, 16)`
- **Poké Mart Door:** `(13, 6)` (Mart employee at `(13, 13)` gives a free sample Potion)
- **Straight North-South Corridor:** `x = 10` is completely clear from `y = 19` (Route 101) to `y = 0` (Route 103).

## Route 103 (Southern Section)
- **South Entrance (from Oldale Town):** `(10, 19)`
- **Lower Ledge (`y = 12`):** Spans `x = 6..13, y = 12`. Bypass northbound via `x = 14` (`(10, 13) -> (14, 13) -> (14, 10) -> (10, 10)`).
- **Upper Ledge (`y = 5`):** Spans `x = 6..12, y = 5`. Bypass northbound via `x = 5` (`(10, 6) -> (5, 6) -> (5, 3) -> (9, 3)`).
- **Rival May Position:** `(10, 3)` (interact from clear ground at `(9, 3)` facing Right).
- **Southbound Fast Path (Route 103 -> Oldale Town via Ledges):**
  - From `(9, 3)` / `(10, 4)`, walk straight `Down` along `x = 10` (`y = 4 -> y = 19`), jumping over both ledges (`y = 5` and `y = 12`) with zero tall-grass tiles.
- **Post-Battle Oldale Trigger:** After defeating May on Route 103, stepping onto `(10, 19)` in Oldale Town triggers a brief 2-box cutscene where May says `"Let's hurry home!"` and walks south into Route 101.

<hr>

<h1><code>Locations/Route_102_And_Petalburg_City</code></h1>

# Route 102 & Petalburg City — Coordinates & Routing

## Route 102
- **East Entrance (from Oldale Town):** `(49, 10)`
- **West Exit (to Petalburg City):** `(0, 8)` -> enters Petalburg City at `(29, 18)`
- **Westbound Path (Oldale -> Petalburg):**
  - `(49, 10)` -> `Left` to `(36, 10)` -> `Down` 5 to `(36, 15)` -> `Left` along `y = 15` past Youngster Calvin at `(33, 14)` to `(24, 13)`.
  - From `(24, 13)`, walk `Up` 3 to `(24, 10)`, `Left` 6 to `(18, 10)`, `Up` 6 through the ledge gap at `(18, 6)` to `(18, 4)`.
  - From `(18, 4)`, walk `Left` 7 along `y = 4` (bypasses Youngster Allen at `(19, 4)`) to `(11, 4)`.
  - From `(11, 4)`, walk `Down` 4 to `(11, 8)` and `Left` 11 along `y = 8` (bypasses grass `x = 4..10, y = 4..7`) into Petalburg City `(29, 18)`.
- **Trainers Defeated:**
  - Youngster Calvin `(33, 14)` — Poochyena Lv. 5 [Defeated]
  - Bug Catcher Rick `(25, 15)` — Wurmple Lv. 4 x2 [Defeated]
  - Lass Tiana `(8, 7)` — Zigzagoon Lv. 4, Shroomish Lv. 4 [Defeated]

## Petalburg City
- **East Entrance (from Route 102):** `(29, 18)`
- **Pokémon Center Door:** `(20, 16)` (exiting steps to `(20, 17)`)
- **Petalburg Gym Door:** `(15, 8)` (exiting steps to `(15, 9)`; interior entrance mat is `(4, 111)`, Norman is 4 tiles north at `(4, 107)`).
- **Wally Tutorial Event:** Completed on Turn 107–108, unlocking the western exit of Petalburg City into Route 104 South.
- **West Exit (to Route 104 South):** `(0, 12)` (Scott's cutscene at `(4, 12)` completed on Turn 110).

## Route 104 South
- **East Entrance (from Petalburg City):** `(34, 62)`
- **Beach Bypass Route (Zero Tall Grass):**
  - `(34, 62)` -> `Left` 6 to `(28, 62)` -> `Down` 9 via east beach steps `(28, 70)` to `(28, 71)`.
  - `Left` 6 to `(22, 71)` -> `Up` 8 to `(22, 63)` -> `Left` 3 to `(19, 63)` -> `Up` 4 to `(19, 59)` -> `Left` 2 to `(17, 59)` -> `Up` 6 via west beach steps `(17, 54)` to `(17, 53)` (in front of Mr. Briney's Cottage).
  - From `(17, 53)`, walk `Right` 5 to `(22, 53)` and `Up` 10 along `x = 22` to `(22, 43)` (Oran Berry tree at `(22, 41)`, Pecha Berry tree at `(24, 41)`).
  - From `(22, 43)`, walk `Left` 11 along `y = 43` to `(11, 43)` (Lady Cindy at `(11, 44)` — Zigzagoon Lv. 7 [Defeated]), then `Up` 5 along `x = 11` into **Petalburg Woods** at `(11, 38)`.

## Petalburg Woods
- **South Entrance (from Route 104 South `(11, 38)`):** `(17, 38)`
- **Path to Western Corridor & Devon Researcher:**
  - From `(17, 38)`, walk `Up` 4 tiles to `(17, 34)` and `Left` 10 tiles along `y = 34` (clear ground below grass `x = 10..14, y = 32..33`) to `(7, 34)` (Bug Catcher Lyle at `(7, 33)` — Wurmple Lv. 3 x4 [Defeated]).
  - From `(7, 34)`, step `Left` 1 to `(6, 34)` and walk `Up` 10 tiles along `x = 6` through tall grass `(6, 32..26)` onto clear ground at `(6, 24)`.
  - From `(6, 24)`, follow the clear footpath: `Right` 8 to `(14, 24)` -> `Down` 3 to `(14, 27)` -> `Right` 12 along `y = 27` to `(26, 27)` -> `Up` 4 along `x = 26` to `(26, 23)` (triggers the Devon Researcher & Team Aqua Grunt cutscene; Team Aqua Grunt — Poochyena Lv. 9 [Defeated]; received Great Ball x1 from Researcher).
  - From `(26, 23)`, walk `Up` 7 along `x = 26` to `(26, 16)`, `Left` 18 along `y = 16` (`x = 10..8` is tall grass) to `(8, 16)`, then `Left, Up, Left, Up` through `(7, 16)` and `(7, 15)` onto clear ground at `(6, 14)` (Bug Catcher James at `(4, 14)` — Nincada Lv. 6 x2 [Defeated]).

<hr>

<h1><code>Main</code></h1>

# Main Notepad — Pokémon Emerald Version

## Trainer & Party Info
- **Name:** ORION (Boy / Brendan sprite) | **Money:** $5,184
- **Key Features Unlocked:** Pokédex, Running Shoes
- **Text Speed:** FAST
- **Inventory:** Potion x1, Great Ball x1, Poké Ball x3
- **Party:**
  1. ATRITON (Mudkip, Male, Lv. 12 — Tackle, Growl, Mud-Slap, Water Gun)
  2. OBERON (Wurmple, Male, Lv. 3 — Tackle, String Shot)

## Notepad Index
- `Locations/Littleroot_Town`: Coordinates and interaction details for Player's House, Rival May's House, Professor Birch's Lab, and Northern Exit.
- `Locations/Route_101_And_Oldale_Town`: Coordinates and routing for Route 101, Oldale Town, and Route 103 (including fast southbound ledge paths).
- `Locations/Route_102_And_Petalburg_City`: Coordinates, trainer statuses, and routing for Route 102 and Petalburg City.

## Mechanics & Harness Notes
- **Naming Screen Grid (7 cols x 4 rows, Select = toggle case, Start = jump to OK):**
  - Row 0: `A B C D E F .` (cols 0..6)
  - Row 1: `G H I J K L ,` (cols 0..6)
  - Row 2: `M N O P Q R S` (cols 0..6)
  - Row 3: `T U V W X Y Z` (cols 0..6)
- **Pokémon Fanfare Auto-Advance:** The `"received/caught [POKéMON]!"` fanfare text box automatically advances to the `"give a nickname?" [YES / NO]` prompt once the jingle finishes; press `A` only ONCE to enter the naming screen.
- **Overworld Warp Transitions:** Stepping onto a warp/door aborts remaining `press_buttons` inputs and leaves the next turn at the start of the fade-in; prepend `sleep 1000` when chaining actions immediately after a warp. Exiting an exterior building door automatically steps the player 1 tile `Down`.
- **Clearing NPC Dialogue Safely:** When facing an NPC, use `B` (not `A`) to advance and close the final text box so extra presses cannot accidentally re-initiate dialogue.
- **Pokémon Center Healing Sequence:** Nurse Joy has 3 opening lines before `[YES / NO]` appears; press `A` **4 times** (`A, sleep 1000, A, sleep 1000, A, sleep 1000, A, sleep 6500`), then press `B` 4 times (`B, sleep 1000` x4) to clear her closing dialogue safely.
- **Trainer Mid-Battle Faint Sequence (With 2+ Party Pokémon):** Requires **4 `B` presses** (`B` #1: fainted, `B` #2: EXP gain, `B` #3: trainer about to use next Pokémon, `B` #4: selects `No` on `"Will ORION change POKéMON?"`), followed by `sleep 4500` for the next Pokémon send-out.
- **Berry Tree Harvesting Sequence:** Requires **3 `A` presses** (`A` #1: found berries, `A` #2: opens `[YES / NO]` prompt, `A` #3: confirms `YES` to pick berries), followed by `sleep 3500` and `B` x 3.
- **Overworld Bag & Party Cursor Persistence:** Both the Start menu and Party menu remember their last cursor index across the session (`slotId` in the Party menu can start on Slot 2 `OBERON` after catching/viewing a Pokémon; press `Left` in the Party menu to move from the right column back to Lead Slot 1 `ATRITON`).

<hr>