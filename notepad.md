# Suicune Quest (Crystal)
- Milestone 1: Burned Tower (Seen).
- Milestone 2: Cianwood City (Seen). Defeated Eusine.
- Milestone 3: Route 42 (In Progress). Current attempt started turn 17600.
- Milestone 4: Route 36 (Next). Requirement: Complete Route 42 sighting.
- Milestone 5: Tin Tower (Final). Requirement: Clear Bell (OBTAINED) + all overworld sightings.

## Suicune Hunt Strategy
- Route 42: Approach the three fruit trees in the island center.
- Route 36: Enter from the Violet City side (East) after Route 42 is completed.
- Pokedex 'Area' confirms the next overworld sighting location.

## Suicune Trigger Hypothesis Testing (Route 42)
- Tested 20 tiles around the fruit trees at (27, 16)-(29, 16) with no trigger. Hypotheses 1-20 failed. [Turn 17641]
- Strategic Pivot: Explore the rest of Route 42 (North/South paths) to find Suicune, as it is not on the island center. [Turn 17641]

# Tile Mechanics (Global)
- FLOOR: Traversable collision type.
- WALL / FRUIT_TREE / COUNTER / HEADBUTT_TREE: Impassable collision types.
- TALL_GRASS: Traversable, triggers wild encounters.
- WATER: Impassable without Surf.
- LEDGE: One-way movement (verified South-only for standard ledges).
- WARP / DOOR / WARP_CARPET: Map transition.
- CUT_TREE: Impassable until CUT is used.
- ROCK: Impassable. Requires ROCK SMASH.
- VOID: Impassable map boundary.
- CAVE: Warp tile leading to an interior area.
- FLOOR_UP_WALL: Impassable wall tile that appears as a floor edge.

# PC Storage (Box 1)
- VORTEX (Poliwag 22), INTERCEPT (Yanma 12), ROCKY (Onix 6), EGG (CleFFA 5), XFDW (Meowth 16), FRITTATA (Togepi 5), SHUCKIE (Shuckle 15), Blarney (Sudowoodo 20).

# Key Observations
- Pokedex 'Area' tracks the current active overworld sighting location.
- Sightings are triggered by entering specific overworld zones.
- Ecruteak History: Two towers (Bell Tower/Tin Tower and Brass Tower/Burned Tower). Three Pokemon born of water, lightning, fire ran off.

# Items & Contacts
- Fire Stone: Route 36 (Alan).
- Rock Smash (Info): Route 36 (Fisher at 44, 9).
- Fisher Tully: Route 42. Gives items.
- Bug Catcher Arnie: Route 35. Reports Yanma swarms.
## Route 42 Suicune Sweep Plan
- Goal: Visit all reachable FLOOR tiles on the island to trigger the event.
- Coordinates to visit: 
  - Y=10: X(20-33)
  - Y=11: X(20-33)
  - Y=12: X(22-28)
  - Y=13: X(24)
  - Y=14: X(24-27)
  - Y=15: X(25-30)
  - Y=16: X(26-30)
  - Y=17: X(26-30)
- Note: Already tested tiles near fruit trees (27-29, 16).
- Progress: Systematic search initiated. Y=10 and Y=11 completed. Currently at (20, 11). Moving to Y=12.