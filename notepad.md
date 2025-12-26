# Strategy: Suicune Hunt (Johto)
- Status: Suicune confirmed on Route 42 via Pokedex (Turn 21433).
- Strategy: Complete methodical sweep of the island floor (Y=10-17) after map reset to trigger Sighting 3 flee event.
- Lessons Learned:
    - Pokedex: Alphabetical order places SUICUNE between SUDOWOODO and SUNKERN.
    - Scripted: Sighting sequence is fixed. Pokedex AREA map tracks current scripted location.
    - Map Reset: Performed map reset by entering Mount Mortar (Turn 21550).
    - Trigger: Suicune on Route 42 is a tile trigger on the southern Apricorn island floor.

# Primary Goal Strategy: Catch Suicune at Tin Tower 1F
1. Complete scripted Johto sightings (Burned Tower, Cianwood, Route 42).
2. Defeat/interact with Eusine as required (Cianwood complete).
3. Obtain the Clear Bell (Complete - In inventory as of Turn 21577).
4. Trigger Route 42 sighting (Current).
5. Head to Tin Tower in Ecruteak City.
6. Battle and catch Suicune at the 1F altar.

# Milestone Audit
- Sighting 1: Burned Tower (Complete).
- Sighting 2: Cianwood (Complete).
- Eusine: Defeated in Cianwood (Complete).
- Sighting 3: Route 42 (Current).

# Repetitive Task: Suicune Island Sweep
- Start Turn: 21556
- Status: In progress. Target area: southern island floor near Apricorn trees (Y:15-17).
- Trigger Insight: Walking toward the three Apricorn trees at (27, 16), (28, 16), (29, 16) triggers Suicune flee.

# Tile Mechanics
- FLOOR: Traversable. Standard ground. [Verified]
- WALL: Impassable. [Verified]
- WATER: Traversable via Surf. [Verified]
- HEADBUTT_TREE/CUT_TREE/FRUIT_TREE: Impassable. Interaction only. [Verified]
- TALL_GRASS: Traversable. Wild encounters. [Verified]
- WARP: CAVE, WARP_CARPET, LADDER. [Verified]
- FLOOR_UP_WALL: Impassable ledge (one-way down). [Verified]

# Contingency Plan
- If sweep fails to trigger Suicune, I will:
    1. Re-verify Pokedex AREA map for exact location.
    2. Check Route 36 (Sighting 4) to see if sequence advanced.
    3. Visit Tin Tower (Sighting 5) if others are skipped.
    4. Fly to Ecruteak to reset the map and return.