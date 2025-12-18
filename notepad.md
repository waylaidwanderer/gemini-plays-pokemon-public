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
- **Navigation Strategy:** East Side Exploration.
    - **Status:** At SE Corner (26, 31).
    - **Position Correction:** Verified at (26, 31).
    - **Plan:** Read Battle Notice Sign at (27, 31). Then continue South to (27, 40) to explore.
    - **Note:** Quick Claw already obtained from Teacher at (27, 40).
- **Current Action:** Read Sign (Face Right + A).
- **Reflection (Turn 5668):**
    - **Hygiene:** Condensed maze logs.
    - **Lesson:** Always verify coordinates. Hallucinated position (23,2) vs (27,5) due to mental shortcut.
    - **Goals:** Clear. Catch Pidgey -> Explore SE Corner.