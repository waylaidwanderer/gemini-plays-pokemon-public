# Suicune Capture Strategy
## Strategy: The Mean Look Pivot
- Train XENON (Gastly) to Lv 13 to learn Mean Look.
- Evolve to Haunter (Lv 25) and train to ~Lv 38-40 (Speed 73-110) to outspeed Suicune.
- Lead with Haunter: Mean Look (Turn 1) -> Hypnosis -> Ultra Balls.
- Track Suicune using Pokedex AREA map. Cycle between adjacent routes to force encounter.
- Item Goal: Buy Ultra Balls at Goldenrod or Blackthorn Marts.

## Lessons Learned
- Cursor Persistence: Battle move menu remembers selection. Always verify cursor position before confirming.
- Menu Navigation: Start, Party, and Battle menus wrap. Use relative navigation for efficiency.
- Tool Hygiene: Refine custom tools immediately if they produce incorrect results. Use manual button presses to progress if a tool fails in battle.
- Tile Navigability: NPCs, trees, and ledges block paths. Use 'run_code' to verify tile navigability before planning long routes.
- Battle Discipline: Always check the move index before pressing A in battle.

## Verified Mechanics & Type Effectiveness
- Ghost Immunity: Ghost-type Pokemon are immune to Normal (e.g., Wrap, Leer) and Fighting-type moves.
- Ghost Ineffectiveness: Ghost moves (Lick) do not affect Normal-type Pokemon.
- Hoppip Immunity: Lick (Ghost) fails to affect wild Hoppip (Grass/Flying) in this game. Verified immunity.
- Hypnosis: Fails on targets already affected by a status condition (e.g., Paralyzed, Sleep).
- Sweet Scent: Triggers immediate wild encounter on valid grass tiles.
- Floor Up Wall: Impassable when moving south (down). Hypothesis: Traversable when moving north (up).

## Training Log: XENON
- Status: Lv 13 reached. Mean Look learned.
- Goal 1: Lv 13 (Mean Look) - COMPLETE.
- Goal 2: Lv 25 (Evolution to Haunter).
- Strategy: Use Sweet Scent at (18, 15) grass patch. Lick Gastly/Bellsprout. RUN from Normal-types and Hoppip.

## Tile Mechanics
- TALL_GRASS: Encounter-eligible ground.
- WALL: Impassable boundary.
- LEDGE_HOP: One-way movement (South/East).
- FLOOR_UP_WALL: Impassable when moving South. Hypothesis: Traversable when moving North (acting as a one-way ledge).

## Exploration Plan
- Goal: Reveal 100% of Route 32.
- Targets: West of (13, 10), East of (19, 28), South/West of (11, 37), Perimeter (1, 76-87).

## NPCs & Locations
- Fisher Tully: (15, 13) Route 32. Contact for fishing info.
- Slowpoketail Seller: (11, 67) Route 32. Selling tails for ¥1,000,000.