# Johto Journey - Final Phase

## Strategy: Preparing for the Elite Four
- Training: Level all active members (especially XENON and Ouroboros) to 45+ at Route 45 or Route 27.
- Coverage: Dragonite (Ouroboros) is the primary candidate for Ice-type coverage (TM33) against Lance.
- Route: Surf east from New Bark Town to Route 27 once preparations are complete.
- Fast Travel: Swap Ravioli (KRABBY) for ICARUS (PIDGEY) to use Fly. [Completed Turn 35719]

## Strategy: Navigate Tohjo Falls
- Start Turn: 35972
- Objective: Traverse Tohjo Falls to reach the eastern exit leading to the rest of Route 27.
- Requirements: SURF and WATERFALL (Rising Badge allows use).
- Steps:
  1. Use Surf to cross the water. [Done]
  2. Search for HM07 Waterfall on land patches. [Current]
  3. Use Waterfall to climb the falls.
  4. Locate the eastern exit.

## Tile Mechanics (Tohjo Falls specific)
- Ledge (FLOOR_UP_WALL): Impassable from North at (10, 16) and (11, 16). Attempted jump 5 times.

## Strategy: Search for HM07 Waterfall
- Hypothesis: HM07 is located on one of the land patches in Tohjo Falls.
- Current Plan:
  1. Explore the eastern water and land patches. [Current]
  2. If blocked, check if (15, 14) or (16, 14) allow jumping east/south.
  3. Investigate the warp at (13, 15).
- Observation: Western strip (Column 0) and southern floor (Row 17) are blocked by ledge collision at (10, 16) and (11, 16).
- Observation: Moon Stone found at (2, 6). [Turn 35981]

## Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable.
- PC: Impassable; interactable from front.
- COUNTER: Impassable; interactable from front.
- WARP_CARPET_DOWN: Warps to another map.
- LADDER: Warps to another map.
- GRASS: Traversable; triggers encounters.
- WATER: Traversable (requires SURF).
- WHIRLPOOL: Impassable (requires WHIRLPOOL to clear).
- WATERFALL: Impassable (requires WATERFALL to climb; Rising Badge required).
- LEDGE/LEDGE_HOP_DOWN (FLOOR_UP_WALL): One-way jump (South).

## Pokemon Info
- Party: XENON (Lv37 Haunter), GNEISS (Lv48 Graveler), Calcifer (Lv49 Typhlosion), Ouroboros (Lv15 Dratini), ICARUS (Lv16 Pidgey), LAPIS (Lv12 Poliwag).
- PC (Box 1): GLAIVE (Scyther), SELKIE (Seel), DELTA (Mantine), RANGOON (Krabby), NOMURA (Tentacool), Ravioli (Krabby), KIMCHI (Gloom).

## Lessons Learned
- Dragon Shrine Entrance: South side (19, 29).
- Fly: Use 'Down' to cycle cities.
- **Move Compatibility (CRITICAL):**
  - XENON (Haunter), Calcifer (Typhlosion), Ouroboros (Dratini) CANNOT learn TM33 Ice Punch.
- **Elm's Lab PC (3, 5):** Research notes only; no storage access.
- **Menu Verification:** Always cross-reference "Current Screen Text" and "Text History".
- **Rising Badge:** Allows use of HM07 Waterfall outside battle (Johto Badge 8).

## Contest Scoring Criteria
- Formula: Level + (Remaining HP / Max HP) * 100 + Base Stat Total factor.
- Tiers: Scyther and Pinsir are top tier. Higher level and full HP are best.
- Winning: 1st place typically requires 300-350+ points.

## Battle Strategies
- Wild Battles: Running is prioritized for efficiency.
- Bug-Catching Contest: Use Hypnosis. Avoid damaging low-level targets with Night Shade. Catching at full HP is prioritized.
## Strategy: Search for HM07 Waterfall (Updated)
- Accessing Western Strip: The strip at Column 0 is blocked by a wall of WALL tiles at Column 1 from Row 2-15. It must be accessed from the southern floor by jumping the ledge at (10, 16) and walking west to (1, 16) or (1, 17).
## Strategy: Search for HM07 Waterfall (Update 2)
- Attempted to jump ledge at (10, 16) from (10, 15) but failed [Turns 36025-36027].
- Plan: Move east to (11, 15) or (12, 15) and try jumping the ledge there to reach Row 17.
- Goal: Reach Column 0 via Row 17 and (1, 16).