# Suicune Capture Strategy
## Strategy: The Mean Look Pivot
- Train XENON (Gastly) to Lv 13 to learn Mean Look. (COMPLETE)
- Evolve to Haunter (Lv 25) and train to ~Lv 38-40 (Speed 73-110) to outspeed Suicune.
- Lead with Haunter: Mean Look (Turn 1) -> Hypnosis -> Ultra Balls.
- Track Suicune using Pokedex AREA map. Cycle between adjacent routes to force movement.
- Item Goal: Buy Ultra Balls at Goldenrod or Blackthorn Marts.

## Training Progress: XENON
- Start Turn: 14500
- Status: Lv 13 reached. Mean Look learned.
- Next Goal: Lv 25 (Evolution).
- Method: Sweet Scent at (18, 15) Route 32. RUN from Normal-types and Hoppip.

## Exploration Plan
- Goal: Reveal 100% of Route 32.
- Current Task: Explore southern land via the western corridor (Column 1).
- Target: Bottom-left perimeter (1, 87).
- Future Targets: West of (13, 10), East of (19, 28).

## Lessons Learned & Corrections
- **Type Matchups:** Ghost is immune to Normal/Fighting. Lick (Ghost) is ineffective against Normal. Hoppip is Grass/Flying and is NOT immune to Ghost moves (confused with Hoothoot).
- **Tile Mechanics:**
    - `FLOOR_UP_WALL`: One-way pathing (North only). Blocks southward progression at y=6, 14, 24, 26, 34, 36, 72, 76, 86.
    - `LEDGE_HOP_DOWN`: One-way pathing (South only).
    - `LEDGE_HOP_RIGHT`: One-way pathing (East only).
- **Menu Navigation:** Start, Party, and Battle menus wrap. Always verify cursor position.
- **Tool Hygiene:** Refine custom tools immediately if they produce incorrect results.

## NPCs & Locations
- Fisher Tully: (15, 13) Route 32. Contact for fishing info.
- Slowpoketail Seller: (11, 67) Route 32. Selling tails for ¥1,000,000.
- Arnie (Bug Catcher): Mentions Growlithe sightings (likely Route 31).
- Youngster Gordon: (4, 63) Route 32. Defeated.
## Exploration Strategy: Western Bypass
- Observation: Southward movement is blocked at y=72 and y=86 in the eastern corridors.
- Hypothesis: The western land (Column 1-4) is reachable by surfing across the lake at y=40-50.
- Test: Reach (11, 40), use SURF to cross to the west, and follow the corridor south.
- Goal: Reach (1, 87) to complete Route 32 exploration.