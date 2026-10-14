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

<hr>

<h1><code>Main</code></h1>

# Main Notepad — Pokémon Emerald Version

## Trainer & Party Info
- **Name:** ORION (Boy / Brendan sprite)
- **Text Speed:** FAST
- **Inventory:** Potion x1 (withdrawn from bedroom PC)
- **Party:** ATRITON (Mudkip, Male, Lv. 6 — Tackle, Growl, Mud-Slap)

## Notepad Index
- `Locations/Littleroot_Town`: Coordinates and interaction details for Player's House, Rival May's House, Professor Birch's Lab, and Northern Exit.

## Mechanics & Harness Notes
- **Naming Screen Grid (7 cols x 4 rows, Select = toggle case, Start = jump to OK):**
  - Row 0: `A B C D E F .` (cols 0..6)
  - Row 1: `G H I J K L ,` (cols 0..6)
  - Row 2: `M N O P Q R S` (cols 0..6)
  - Row 3: `T U V W X Y Z` (cols 0..6)
- **Pokémon Fanfare Auto-Advance:** The `"received/caught [POKéMON]!"` fanfare text box automatically advances to the `"give a nickname?" [YES / NO]` prompt once the jingle finishes; press `A` only ONCE to enter the naming screen.
- **Overworld Warp Transitions:** Stepping onto a warp/door aborts remaining `press_buttons` inputs and leaves the next turn at the start of the fade-in; prepend `sleep 1000` when chaining actions immediately after a warp. Exiting an exterior building door automatically steps the player 1 tile `Down`.
- **Clearing NPC Dialogue Safely:** When facing an NPC, use `B` (not `A`) to advance and close the final text box so extra presses cannot accidentally re-initiate dialogue.

<hr>