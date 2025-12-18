# Gem's Journey in Pokémon Crystal

## Current Strategy
- **Primary Goal:** Defeat Whitney (Goldenrod Gym).
- **Strategy:**
    1. **Train to Lv 20:** Grind in National Park (Left Side).
       - *Status:* Lv 18 (Target: Lv 20). HP: 47/58.
       - *Session Start:* Turn 5358.
       - *Method:* Wild Encounters (Muscle as Lead).
    2. **Gym Battle:** Use MUSCLE (Low Kick) and ROCKY (High Defense) vs Miltank.
- **Notes:**
    - MUSCLE (Machop) has Low Kick (Fighting, STAB, 50 BP fixed in Gen 2).
    - MUSCLE Item: **GOLD BERRY** (Consumed Turn 5464).
    - AZURITE (Heracross) lacks Fighting moves (Level 13).

## Key Items & Progress
- **Badges:** Zephyr, Hive (2/8).
- **Key Items:** Coin Case, Bicycle, Old Rod.
- **HM/TM:** Cut (Belladonna), Headbutt (Tutor).

## Tile Mechanics
- **FLOOR:** Traversable.
- **WALL:** Impassable.
- **COUNTER:** Interact from adjacent tile.
- **TALL_GRASS:** Traversable, wild encounters.
- **WATER:** Impassable without Surf.
- **HEADBUTT_TREE:** Impassable. Can be Headbutted for encounters.
- **CUT_TREE:** Impassable. Can be removed with Cut (respawns).
- **WARP_CARPET_DOWN:** Traversable. Triggers warp when moving off-map.

## Important Locations
- **Game Corner:** (14, 21) Goldenrod.
- **Dept Store:** (24, 27) Goldenrod.
- **Pokemon Center:** (15, 27) Goldenrod.

## Knowledge Base
- **Move Menu:** Vertical list (1-4). Wraps. **Resets to Slot 1 at start of battle.** Remembers last move *within* battle.
- **Game Corner:** 50 Coins = 1000 Yen. TMs: 5500. Abra: 100.
- **Dept Store B1F:** Solved puzzle by resetting floor (Elevator). Loot paused.
- **Party Management:** MUSCLE is Lead for switch training.
- **Radio Hint:** Fisher Ivan on Route 35 mentions 'The Pokémon March' on radio lures wild Pokémon.
- **Fisher Ivan:** Did not battle (Turn 5318).
- **Route 35 Encounters:** Growlithe (Morning).
- **Route 36 Encounters:** Ledyba (Morning).
- **Pokefan William:** Raichu Lv 14 (Quick Attack, Tail Whip). Holds Berry.
, Ditto (Morning).
, Pidgey (Morning).
- **Mom's Savings:** Mom bought a "useful item" (Turn 5455). Check PC.
- **Caught:** Nidoran♂ (COBALT) Lv 12 in National Park.
- **Pokefan Beverly:** Snubbull Lv 14.
- **Item:** Quick Claw (Held item, chance to strike first) obtained from Teacher at (27, 40) National Park.
- **Menu Navigation:** Start Menu cursor remembers the last position in Gen 2. `use_item_sequence` tool assumes it starts at the top (Pokedex). Must manually reset cursor to top or account for position.
- **Current Cursor:** At 'GEM' (Index 5). Needs to go UP to 'PACK' (Index 3) or Top.
- **Menu Correction:** 'use_item_sequence' failed due to cursor memory (Started at 'GEM' -> moved to 'OPTION').
- **Fix:** Manually exiting Option menu, navigating to Pack, resetting pocket cursor (Right/Left), and selecting Super Potion.
- **Learned:** Always account for Start Menu cursor memory or manually reset it before relying on blind sequences.
- **Battle:** Fighting moves (Karate Chop) are Not Very Effective against Poison types (Nidoran).
- **Navigation Strategy:** Explored West Side. Now exploring East Side.
    - **Status:** Found Item at (35, 12) inside a fenced nook.
    - **Pathfinding:** Access requires a long detour.
        - **Route:** Backtrack to (27, 5), then navigate the "Snake Path" East/South through the northern rows to reach the item.
    - **Plan:** Navigate to (27, 5) to start the approach.
- **Current Action:** Backtracking to (27, 5).
- **Battle:** Low Kick is weight-dependent. Nidoran is light -> Low damage. Use Karate Chop (Fixed 50 BP) instead.
- **Tool Issue:** `smart_battle_move` with `target_slot=4` selected Slot 1 (Low Kick) via `Up`. Likely due to Grid layout (1 2 / 3 4) vs List assumption. Manual navigation (Down, Right) recommended for Slot 4.
- **Move Menu:** Vertical List (1-2-3-4). Down moves 1->2->3->4. Cursor remembers position within battle.
- **Current Cursor:** Slot 3 (Focus Energy). Target: Slot 4 (Karate Chop).
- **Action:** A (Fight) -> Down (3->4) -> A (Select).