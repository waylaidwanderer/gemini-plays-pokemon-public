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
  - `Left` 6 to `(22, 71)` -> `Up` 8 to `(22, 63)` -> `Left` 3 to `(19, 63)` -> `Up` 4 to `(19, 59)` -> `Left` 2 to `(17, 59)` -> `Up` 6 via west beach steps `(17, 54)` to `(17, 53)` (in front of **Mr. Briney's Cottage** door at `(17, 51)`).
  - From `(17, 53)`, walk `Right` 5 to `(22, 53)` and `Up` 10 along `x = 22` to `(22, 43)` (Oran Berry tree at `(22, 41)`, Pecha Berry tree at `(24, 41)`).
  - From `(22, 43)`, walk `Left` 11 along `y = 43` to `(11, 43)` (Lady Cindy at `(11, 44)` — Zigzagoon Lv. 7 [Defeated]), then `Up` 5 along `x = 11` into **Petalburg Woods** at `(11, 38)`.

## Petalburg Woods
- **South Entrance (from Route 104 South `(11, 38)`):** `(17, 38)`
- **Path to Western Corridor & Devon Researcher:**
  - From `(17, 38)`, walk `Up` 4 tiles to `(17, 34)` and `Left` 10 tiles along `y = 34` (clear ground below grass `x = 10..14, y = 32..33`) to `(7, 34)` (Bug Catcher Lyle at `(7, 33)` — Wurmple Lv. 3 x4 [Defeated]).
  - From `(7, 34)`, step `Left` 1 to `(6, 34)` and walk `Up` 10 tiles along `x = 6` through tall grass `(6, 32..26)` onto clear ground at `(6, 24)`.
  - From `(6, 24)`, follow the clear footpath: `Right` 8 to `(14, 24)` -> `Down` 3 to `(14, 27)` -> `Right` 12 along `y = 27` to `(26, 27)` -> `Up` 4 along `x = 26` to `(26, 23)` (triggers the Devon Researcher & Team Aqua Grunt cutscene; Team Aqua Grunt — Poochyena Lv. 9 [Defeated]; received Great Ball x1 from Researcher).
  - From `(26, 23)`, walk `Up` 7 along `x = 26` to `(26, 16)`, `Left` 18 along `y = 16` (`x = 10..8` is tall grass) to `(8, 16)`, then `Left, Up, Left, Up` through `(7, 16)` and `(7, 15)` onto clear ground at `(6, 14)` (Bug Catcher James at `(4, 14)` — Nincada Lv. 6 x2 [Defeated]).
  - From `(6, 14)`, walk `Up` 4 to `(6, 10)` (Ether item ball is at `(4, 8)`), `Right` 8 (`x = 7..10` is tall grass) to `(14, 10)`, and `Up` 5 to the **North Exit** at `(14, 5)` (step `Up` from `(14, 5)` to exit onto Route 104 North).
- **Petalburg Woods Southbound Center Ledges (Zero Tall Grass):** From the North Exit `(14, 5)`, walk `Down` 16 along `x = 14` (jumps the ledges at `(14, 14)` and `(14, 22)`) to `(14, 26)`, `Right` 3 to `(17, 26)`, and `Down` 12 along `x = 17` (jumps the ledge at `(17, 30)`) out the South Exit at `(17, 38)` onto Route 104 South `(11, 38)`.

<hr>

<h1><code>Locations/Route_104_And_Rustboro_City</code></h1>

# Route 104 North & Rustboro City — Coordinates & Routing

## Route 104 North
- **South Entrance (from Petalburg Woods `(14, 5)`):** `(10, 29)`
- **Eastbound Path to Wooden Bridge:**
  - From `(10, 29)`, walk `Up` 4 to `(10, 25)`, `Right` 7 to `(17, 25)`, `Up` 1 to `(17, 24)` (Rich Boy Winston at `(20, 25)` — Zigzagoon Lv. 7 [Defeated]), and `Right` 7 to `(24, 24)` (Lass Haley at `(28, 24)` — Lotad Lv. 6, Shroomish Lv. 6 [Defeated]).
  - From `(24, 24)`, step `Down` 1 to `(24, 25)`, `Right` 4 to `(28, 25)`, `Up` 3 to `(28, 22)`, and `Right` 2 onto the wooden bridge at `(30, 22)`.
- **Wooden Bridge & Northbound Path to Rustboro City:**
  - Walk `Up` 6 along the eastern bridge (`(30, 22)` -> `(30, 16)`), `Left` 5 across the horizontal bridge section (`(30, 16)` -> `(25, 16)`, passing Twins Gina & Mia at `(27, 15)` and `(28, 15)` — Seedot Lv. 6, Lotad Lv. 6 [Defeated]), and `Up` 12 (`(25, 16)` -> `(25, 4)`).
  - From `(25, 4)`, walk `Left` 9 along `y = 4` to `(16, 4)` and `Up` across `y = 0` into **Rustboro City** at `(16, 59)`.

## Rustboro City
- **South Entrance (from Route 104 North `(16, 0)`):** `(16, 59)` (central white stone avenue `x = 15..16`). After receiving the PokéNav, Rival May stands at `(16, 50)` and triggers a Match Call registration cutscene along `y = 53` (`[YES / NO]` optional battle prompt can be declined with `B`) [Registered].
- **Poké Mart Door:** `(16, 45)` (exiting steps to `(16, 46)`). To continue north past the Poké Mart toward the Pokémon Center `(16, 38)`, walk around the Poké Mart via `x = 13` (west side) or `x = 20` (east avenue).
- **Pokémon Center Door:** `(16, 38)` (exiting steps to `(16, 39)`). From `(16, 39)`, walk `Right` 5 to `(21, 39)` to join the main northbound avenue (`x = 21..22`) leading to Rustboro Gym.
- **Rustboro Gym Door:** `(27, 19)` (exiting steps to `(27, 20)`). Reachable from `(21, 39)` by walking `Up` 19 along `x = 21` to `(21, 20)`, `Right` 6 along `y = 20` to `(27, 20)`, and `Up` 1 into `(27, 19)`.
## Rustboro Gym
- **Interior Entrance Mat:** `(5, 19)`
- **Western Bypass Route:**
  - From `(5, 19)`, walk `Up` 2 to `(5, 17)`, `Left` 4 to `(1, 17)`, and `Up` 8 along `x = 1` to `(1, 9)` (bypasses Youngster Josh at `(5, 13)`).
  - Stepping onto `(1, 9)` triggers a Double Battle (if 2+ conscious party Pokémon) with **Hiker Marc** at `(1, 6)` (Geodude Lv. 8 x2 [Defeated]) and **Youngster Tommy** at `(3, 9)` (Geodude Lv. 8 x2 [Defeated]).
  - After the Double Battle at `(1, 9)`, loop around Hiker Marc `(1, 8)` and Youngster Tommy `(2, 9)` via: `Down` 3 to `(1, 12)`, `Right` 4 behind Youngster Josh `(5, 13)` to `(5, 12)`, `Up` 4 to `(5, 8)`, `Left` 3 to `(2, 8)`, `Up` 4 to `(2, 4)`, `Right` 3 to `(5, 4)`, and `Up` 1 to `(5, 3)` in front of **Gym Leader Roxanne** at `(5, 2)` (Geodude Lv. 12 x2, Nosepass Lv. 15 [Defeated — Stone Badge & TM39 Rock Tomb obtained]).
  - **Exit Route from `(5, 3)` (once Marc & Tommy have reset to `(1, 6)` and `(3, 9)`):** `Down` 1 to `(5, 4)` -> `Left` 3 to `(2, 4)` -> `Down` 4 to `(2, 8)` -> `Left` 1 to `(1, 8)` -> `Down` 9 to `(1, 17)` -> `Right` 4 to `(5, 17)` -> `Down` 3 onto `(5, 19)` and out the door to `(27, 20)`.
- **Devon Goods Theft Cutscene & Route 116 Exit:**
  - After defeating Roxanne, exiting Rustboro Gym to `(27, 20)` and walking `Left` 4 to `(23, 20)` triggers the Team Aqua Grunt & Devon Researcher chase cutscene.
  - From `(23, 20)`, walk `Left` 2 to `(21, 20)`, `Up` 10 along `x = 21` to `(21, 10)`, and `Right` 8 along `y = 10` to `(29, 10)` to trigger the Devon Researcher at `(30, 10)`.
  - After clearing the Researcher's dialogue with `B`, step `Down` 1 to `(29, 11)` and walk `Right` across `x = 39` onto **Route 116**.
## Route 116
- **West Entrance (from Rustboro City `(39, 11)`):** `(0, 11)`
- **Eastbound Path toward Rusturf Tunnel:**
  - From `(1, 11)`, walk `Right` 3 to `(4, 11)`, `Up` 4 to `(4, 7)`, `Right` 4 along `y = 7` to `(8, 7)`, `Up` 3 to `(8, 4)`, and `Right` 4 along `y = 4` to `(12, 4)` (Youngster Joey at `(12, 7)` — Machop Lv. 9 [Defeated]).
  - From `(12, 4)`, walk `Right` 2 to `(14, 4)`, `Down` 5 to `(14, 9)`, `Right` 6 along `y = 9` to `(20, 9)`, `Down` 4 to `(20, 13)`, and `Right` 2 to `(22, 13)` (School Kid Karen at `(22, 16)` — Shroomish Lv. 9 [Defeated]).
  - From `(22, 13)`, walk `Right` 8 along `y = 13` to `(30, 13)`, `Down` 1 to `(30, 14)`, `Right` 4 to `(34, 14)`, `Up` 1 to `(34, 13)`, and `Right` 1 to `(35, 13)` (Youngster Johnson at `(36, 13)` — Shroomish Lv. 8, Lotad Lv. 8 [Defeated]).
  - From `(35, 13)`, step `Down` 1 to `(35, 14)` and `Right` 1 to `(36, 14)` (Hiker Clark at `(36, 17)` — Geodude Lv. 8 [Defeated]), then walk `Right` 1 to `(37, 14)` and `Up` 1 to `(37, 13)` (Hiker Devan at `(42, 13)` — Geodude Lv. 8 x2 [Defeated]).
  - From `(37, 13)`, walk `Up` 3 to `(37, 10)` in front of the Tunnelers' Rest House `(38, 8)` (an item ball at `(32, 7)` west of the Rest House requires HM01 Cut at `(31, 10)` or `(33, 10)`), then walk `Right` 10 along `y = 10` to `(47, 10)` and `Up` 2 into **Rusturf Tunnel** at `(47, 8)` (Mr. Briney is at `(46, 9)`).
## Rusturf Tunnel
- **West Entrance (from Route 116 `(47, 8)`):** `(4, 10)`
- **Path to Team Aqua Grunt:**
  - From `(4, 10)`, walk `Up` 5 to `(4, 5)` (an item ball is at `(3, 1)` up the northern stairs at `(8, 3)`) and `Right` 9 along `y = 5` to `(13, 5)` (Team Aqua Grunt at `(14, 5)` — Poochyena Lv. 11 [Defeated — Devon Goods recovered & Peeko rescued]).
  - **Exit Route from `(13, 5)`:** Walk `Left` 9 to `(4, 5)` and `Down` 6 onto `(4, 10)` to exit onto Route 116 at `(47, 9)`.
- **Westbound Return Route (Rusturf Tunnel -> Rustboro City):**
  - From `(47, 9)`, walk `Down` 1 to `(47, 10)`, `Left` 9 to `(38, 10)`, `Down` 4 to `(38, 14)`, `Left` 3 to `(35, 14)`, `Up` 1 to `(35, 13)`, `Left` 15 along `y = 13` to `(20, 13)`, `Up` 4 to `(20, 9)`, `Left` 6 to `(14, 9)`, `Up` 5 to `(14, 4)`, `Left` 6 to `(8, 4)`, `Down` 3 to `(8, 7)`, `Left` 4 to `(4, 7)`, `Down` 4 to `(4, 11)`, and `Left` 14 into **Rustboro City** at `(30, 11)`.
  - Stepping onto `(30, 11)` with the recovered Devon Goods triggers the Researcher at `(30, 10)` (awards Great Ball x1 and escorts the player to Devon Corporation 3F to receive Steven's Letter and the PokéNav from President Stone).
- **Devon Corporation Exit Route (3F -> 2F -> 1F -> Rustboro City):**
  - **3F (from `(14, 5)`):** Walk `Up` 2 to `(14, 3)`, `Left` 11 along `y = 3` (above the conference table) to `(3, 3)`, `Up` 1 to `(3, 2)`, `Left` 1 to `(2, 2)`, and `Up` 1 into `(2, 1)` to warp to 2F `(2, 2)`.
  - **2F (from `(2, 2)`):** Walk `Right` 12 along `y = 2` to `(14, 2)` and `Up` 1 into `(14, 1)` to warp to 1F `(14, 2)`.
  - **1F (from `(14, 2)`):** Walk `Left` 1 to `(13, 2)`, `Down` 4 to `(13, 6)`, `Left` 8 along `y = 6` to `(5, 6)`, and `Down` 3 onto `(5, 8)` to exit to Rustboro City.
  - **Devon Corporation Exterior Door:** `(11, 15)` (exiting steps to `(11, 16)`; exiting after receiving the PokéNav triggers the Devon Researcher's Match Call tutorial, ending at `(11, 17)`). To return south to the Pokémon Center from `(11, 17)`, walk `Down` 4 to `(11, 21)`, `Right` 10 to `(21, 21)`, `Down` 18 along `x = 21` to `(21, 39)`, and `Left` 5 to `(16, 39)`.
- **Cutter's House Door:** `(9, 38)` (exiting steps to `(9, 39)`), 7 tiles west of the Pokémon Center door `(16, 38)`. Interior entrance mat is `(5, 8)..(6, 8)`; the Cutter sits at `(7, 5)` (reachable at `(7, 6)`) and awards **HM01 (Cut)** [Obtained].

<hr>

<h1><code>Main</code></h1>

# Main Notepad — Pokémon Emerald Version

## Trainer & Party Info
- **Name:** ORION (Boy / Brendan sprite) | **Money:** $7,220 | **Badges:** 1 (Stone Badge)
- **Key Features Unlocked:** Pokédex, Running Shoes, PokéNav
- **Text Speed:** FAST
- **Inventory:** Devon Goods, Letter, Great Ball x2, Poké Ball x2, HM01 (Cut), TM39 (Rock Tomb)
- **Party:**
  1. ATRITON (Marshtomp, Male, Lv. 17 — Mud Shot, Growl, Mud-Slap, Water Gun)
  2. OBERON (Silcoon, Male, Lv. 8 — Tackle, String Shot, Poison Sting, Harden)
  3. GAIA (Nincada, Female, Lv. 7 — Scratch, Harden, Leech Life)

## Notepad Index
- `Locations/Littleroot_Town`: Coordinates and interaction details for Player's House, Rival May's House, Professor Birch's Lab, and Northern Exit.
- `Locations/Route_101_And_Oldale_Town`: Coordinates and routing for Route 101, Oldale Town, and Route 103 (including fast southbound ledge paths).
- `Locations/Route_102_And_Petalburg_City`: Coordinates, trainer statuses, and routing for Route 102, Petalburg City, Route 104 South, and Petalburg Woods.
- `Locations/Route_104_And_Rustboro_City`: Coordinates, trainer statuses, and routing for Route 104 North and Rustboro City.

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
- **Trainer Mid-Battle Faint Sequence (With 2+ Party Pokémon):** Use **5 `B` presses** with generous EXP wait (`B, sleep 3000, B, sleep 1800, B, sleep 1800, B, sleep 1800, B, sleep 4500`) to clear fainted text, full EXP bar animation, trainer's next Pokémon announcement, and `"Will ORION change POKéMON?"` (`No`).
- **Berry Tree Harvesting Sequence:** Requires **3 `A` presses** (`A` #1: found berries, `A` #2: opens `[YES / NO]` prompt, `A` #3: confirms `YES` to pick berries), followed by `sleep 3500` and `B` x 3.
- **Overworld Bag & Party Cursor Persistence:** Both the Start menu and Party menu remember their last cursor index across the session (`slotId` in the Party menu can start on Slot 2 `OBERON` after catching/viewing a Pokémon; press `Left` in the Party menu to move from the right column back to Lead Slot 1 `ATRITON`).
- **Double Battle Single-Mon Bypass:** Overworld Double Battle trainers (such as Twins Gina & Mia on the Route 104 North bridge) cannot initiate a battle if the player has only 1 conscious Pokémon (`GetMonsStateToDoubles() != PLAYER_HAS_TWO_USABLE_MONS`).
- **Evolution Screen Safety:** Never press `B` when a Pokémon is about to evolve after battle (`B` cancels evolution); use `A` to advance post-battle victory text when a level-up triggers evolution.
- **Side-Talking Trainers to Avoid Double Battles:** When two Single Battle trainers have overlapping lines of sight (such as Youngster Johnson at `(36, 13)` and Hiker Clark at `(36, 17)` on Route 116), walking up to the side of one trainer and pressing `A` initiates a 1v1 Single Battle instead of stepping into their shared line of sight for a 2v2 Double Battle.
- **Double Battle Target Selection:** Single-target moves (such as `Mud Shot` or `Tackle`) require **3 `A` presses** per Pokémon in a Double Battle (`A` for `FIGHT`, `A` for the move slot, and `A` to confirm the target).
- **Post-Battle Match Call Registration:** After obtaining the PokéNav, defeating a Match Call-eligible trainer triggers an automatic overworld dialogue box immediately after the post-battle fade-in (including a ~3s registration fanfare) that must be cleared with `B` before overworld movement can resume.

<hr>