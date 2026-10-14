# Main Notepad — Pokémon Emerald Version

## Trainer & Party Info
- **Name:** ORION (Boy / Brendan sprite) | **Money:** $3,444
- **Key Features Unlocked:** Pokédex, Running Shoes
- **Text Speed:** FAST
- **Inventory:** Potion x1, Poké Ball x3
- **Party:**
  1. ATRITON (Mudkip, Male, Lv. 9 — Tackle, Growl, Mud-Slap)
  2. OBERON (Wurmple, Male, Lv. 2 — Tackle, String Shot)

## Notepad Index
- `Locations/Littleroot_Town`: Coordinates and interaction details for Player's House, Rival May's House, Professor Birch's Lab, and Northern Exit.
- `Locations/Route_101_And_Oldale_Town`: Coordinates and routing for Route 101, Oldale Town, and Route 103 (including fast southbound ledge paths).

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