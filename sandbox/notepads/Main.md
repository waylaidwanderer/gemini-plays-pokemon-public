# Main Notepad — Pokémon Emerald Version

## Trainer & Party Info
- **Name:** ORION (Boy / Brendan sprite) | **Money:** $5,728
- **Key Features Unlocked:** Pokédex, Running Shoes
- **Text Speed:** FAST
- **Inventory:** Great Ball x1, Poké Ball x3
- **Party:**
  1. ATRITON (Mudkip, Male, Lv. 13 — Tackle, Growl, Mud-Slap, Water Gun)
  2. OBERON (Silcoon, Male, Lv. 7 — Tackle, String Shot, Poison Sting, Harden)

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