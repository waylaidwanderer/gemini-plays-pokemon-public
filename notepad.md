# Suicune Capture Strategy
## Strategy: The Mean Look Pivot
- Train XENON (Gastly) to Lv 13 to learn Mean Look.
- Evolve to Haunter (Lv 25) and train to ~Lv 38-40 (Speed 73-110) to outspeed Suicune.
- Track Suicune using Pokedex AREA map. Cycle between adjacent routes (e.g., 36/37) to force encounter.
- Lead with Haunter: Mean Look (Turn 1) -> Hypnosis -> Ultra Balls.
- Item Goal: Buy Ultra Balls at Goldenrod or Blackthorn Marts.

## Lessons Learned
- Cursor Persistence: The battle move menu remembers the last selected move across turns and battles. Always verify cursor position before confirming.
- Menu Navigation: Start, Party, and Battle menus wrap. Use relative navigation for efficiency.
- Tool Reliability: Custom tools must be verified and refined immediately if they produce incorrect results. Avoid calling complex tools in the same turn as opening a menu to prevent stale state issues.
- Tile Navigability: NPCs, certain trees, and ledges block paths. Verify collision before planning long routes.
- Battle Discipline: Verify cursor position after closing sub-menus or between turns.

## Verified Mechanics & Type Effectiveness
- Hoppip Immunity: Lick (Ghost) fails to affect wild Hoppip (Grass/Flying) in this game. Hypothesis: Hoppip treated as Normal-type or Ghost type-chart changed.
- Ghost Typing: Ghost is immune to Normal (Wrap, Leer) and Fighting moves. Lick (Ghost) is ineffective against Normal types.
- Hypnosis: Fails on targets already affected by a status condition (e.g. Paralyzed, Sleep).
- Sweet Scent: Triggers immediate wild encounter on valid grass tiles.

## Training Log: XENON
- Start: Turn 14423.
- Goal: Lv 13 (1261 Total EXP).
- Status: 20 EXP remaining.
- Strategy: Sweet Scent at (18, 15) Route 32. Lick Gastly/Bellsprout. RUN from Normal-types and Hoppip.
- PP/HP Management: Return to Pokecenter if Lick PP < 5 or HP < 10.

## Tile Mechanics
- TALL_GRASS: Encounter-eligible ground.
- WALL: Impassable boundary.
- LEDGE_HOP: One-way movement (South/East).

## Exploration Plan
- Goal: Reveal 100% of Route 32.
- Targets: West of (13, 10), East of (19, 28), South/West of (11, 37), Perimeter (1, 76-87).

## NPCs & Locations
- Fisher Tully: (15, 13) Route 32. Contact for fishing info.
- Slowpoketail Seller: (11, 67) Route 32. Selling tails for ¥1,000,000.