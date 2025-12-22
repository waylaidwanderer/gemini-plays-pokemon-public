# Gem's Journey in Pokémon Crystal

## Current Strategy
- **Primary Goal:** Stop Team Rocket.
- **Secondary Goal:** Investigate Radio Tower (Team Rocket takeover).
- **Navigation:** Operating PC at (9, 1).
- **Status:** At PC in Goldenrod Pokemon Center.
- **Reason:** Accessing Bill's PC to swap Kenya for Togepi.
- **Plan:**
    1. Open PC (Up, A).
    2. Select "Bill's PC".
    3. Select "Deposit PKMN".
    4. Deposit Kenya.
    5. Select "Withdraw PKMN".
    6. Withdraw Togepi.
    7. Exit and Fly.

# Reflection (Turn 11588)
- **Execution:** No deferred tasks. Addressed PC confusion immediately.
- **Hygiene:** Notepad is up to date. Map markers are good.
- **Automation:** Tools are functioning, though `navigate_to_coords` had a pathfinding issue earlier (likely distance/door related).
- **Goals:** Clear.
- **Errors:** Menu navigation failed (ended in Pack). Lesson: Assume menu cursor memory or verify state before long sequences.
- **Quest Info:** No Rocket Uniform needed. Just force/battle through.
- **Locked Door:** Underground (18, 6) needs a key. Remember this for later.

## Map Data
- **Goldenrod City:**
  - Gym: (24, 7)
  - Name Rater: (15, 7)
  - Underground Entrances: (9, 5) and (11, 29)
  - Dept Store: (24, 27)
  - PokeCenter: (15, 27)
  - Game Corner: (14, 21)
  - Flower Shop: (29, 5)
  - Bike Shop: (29, 29)
  - **Radio Tower:** Location unknown (Likely North/West).

## Tile Mechanics
- **LADDER:** Traversable (Warps to another map).
- **WARP_CARPET_DOWN:** Traversable (Exits map).
- **FLOOR:** Traversable.
- **WALL:** Impassable.
- **COUNTER:** Impassable. Interact from adjacent tile facing it.
- **ICE:** Sliding tiles (Mahogany Gym).
- **Trap Tiles:** Rocket Hideout B1F.