# Gem's Journey in Pokémon Crystal

## Current Strategy
- **Primary Goal:** Buy Flower Mail for Kenya.
  - **Status:** Cherrygrove Mart does not sell it. Going to Violet City.
- **Secondary Goal:** Deliver Kenya to Route 31.
- **Tertiary Goal:** Travel to Mahogany Town (Route 42).
- **Party:** Muscle (41), Garnet (28), Hematite (15), Azurite (13), Lapis (12), Mistral (13).
- **Boxed:** Kenya (10, Box 1), Rocky (21, Box 3).

## Quests
- **Webster:** Deliver mail to Route 31. (Current Mail status: Missing. Need Flower Mail).
- **Jasmine:** Cured. Returned to Gym. (Completed).

## Tile Mechanics
- **FLOOR/WATER:** Traversable (Surf for water).
- **WALL/OBSTACLE:** Impassable.
- **DOOR/WARP:** Transitions map.

## Navigation Log
- **Recent Progress:**
  - Obtained SecretPotion in Cianwood.
  - Cured Amphy in Olivine Lighthouse.
  - Defeated Leader Jasmine (Mineral Badge).
  - Attempted Fly to Violet City, landed in Cherrygrove.

## Gyms & Badges
- **Zephyr, Hive, Plain, Fog, Storm, Mineral.**
- **Next:** Glacier Badge (Mahogany Town).

## Notes
- **Tool Note:** `slow_press` defined for sticky menus.
- **Battle Note:** Muscle's last move was Slot 4.
- **Menu Mechanics:** Observed cursor memory in the Party Menu. It remembered the last position (Mistral, Slot 5) instead of resetting to Slot 1.
- **Navigation Update:** Fly attempt to Violet City failed (landed in Cherrygrove).
- **Hypothesis:** Input timing issue.
- **Plan:** Retrying Fly with a segmented approach. Step 1: Open Fly Map. Step 2: Navigate.
- **Menu Correction:** Accidentally entered Item Use menu instead of Fly.
- **Action:** Backing out to Overworld to retry Fly sequence from scratch.
- **Input Note:** Used `press_sequence` to send 5 B inputs to ensure full menu exit.
- **Fly Map Navigation:** Confirmed cursor memory works (Start->Up->A->A->A got us back to Fly map with Mistral selected).
- **Action:** Attempting `Left` (Cherrygrove) -> `Up` (Violet) -> `A` (Confirm) to Fly.
- **Fly Navigation Plan:** Opening Fly map and navigating `Left` -> `Up`.
- **Validation:** Will NOT press `A` to confirm yet. Checking screen text next turn to ensure "Violet City" is selected.
- **Fly Map Status:** Screen text confirms "Cherrygrove City" is selected.
- **Correction:** The previous `Up` input must have been dropped or timed out.
- **Action:** Pressing `Up` to select Violet City. Will verify text before confirming.