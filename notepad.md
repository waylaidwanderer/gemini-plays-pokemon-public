# Strategy: Suicune Hunt (Johto)
- Status: Suicune confirmed on Route 42 via Pokedex (Turn 21433).
- Strategy: Complete methodical sweep of the island floor after map reset.
- Lessons Learned:
    - Pokedex: Alphabetical order places SUICUNE between SUDOWOODO and SUNKERN.
    - Scripted: Sighting sequence is fixed. Pokedex AREA map tracks current scripted location.
    - Map Reset: Performed map reset by entering Mount Mortar (Turn 21550).
    - Trigger: Suicune on Route 42 is a tile trigger on the southern Apricorn island floor.
- Unmarked Floor Tiles (Turn 21535): (22, 12), (23, 12), (24, 12), (25, 12), (26, 12), (27, 12), (28, 12), (27, 15).

# Tile Mechanics
- FLOOR: Traversable. Standard ground. [Verified]
- WALL: Impassable. [Verified]
- WATER: Traversable via Surf. [Verified]
- HEADBUTT_TREE: Impassable. Interaction triggers Headbutt. [Verified]
- CUT_TREE: Impassable. Interaction triggers Cut. [Verified]
- FRUIT_TREE: Impassable. Interaction gives Apricorn/Berry. [Verified]
- TALL_GRASS: Traversable. Wild encounters. [Verified]
- CAVE: Warp. [Verified]
- WARP_CARPET_LEFT/DOWN: Warp. [Verified]
- LADDER: Warp. [Verified]
- FLOOR_UP_WALL: Impassable. Ledge that can be jumped over from above. [Verified]

# Milestone Audit
- Current Milestone: Sighting 3 (Route 42).
- Previous Milestones: Sighting 1 (Burned Tower), Sighting 2 (Cianwood).
- Eusine: Defeated in Cianwood.

# Island Sweep Plan
1. Re-verify Suicune AREA box in Pokedex.
2. Step on all unmarked floor tiles: (22, 12), (23, 12), (24, 12), (25, 12), (26, 12), (27, 12), (28, 12), (27, 15).
3. If trigger fails, Fly to Ecruteak and return to re-verify.