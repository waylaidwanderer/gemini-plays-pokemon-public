# Gem's Journey in Pokémon Crystal

## Current Strategy
- **Primary Goal:** Stop Team Rocket.
- **Secondary Goal:** Investigate Radio Tower (Team Rocket takeover).
- **Navigation:** Operating PC at (9, 1).
- **Status:** In Bill's PC (Retrying Deposit).
- **Reason:** Previous attempt failed; backed out of the context menu instead of confirming.
- **Plan:**
    1. Open Context Menu for Kenya (A).
    2. Select DEPOSIT (A).
    3. Return to Main PC Menu (B, B).
    4. Select "WITHDRAW PKMN".
    5. Withdraw Togepi.
    6. Exit and Fly.

# Reflection (Turn 11588)
- **Execution:** No deferred tasks. Addressed PC confusion immediately.
- **Hygiene:** Notepad is up to date. Map markers are good.
- **Automation:** Tools are functioning, though `navigate_to_coords` had a pathfinding issue earlier (likely distance/door related).
- **Goals:** Clear.
- **Errors:** Menu navigation failed (ended in Pack). Lesson: Assume menu cursor memory or verify state before long sequences.
- **Quest Info:** Rocket Uniform NOT needed (Crystal specific). Fight the Grunt at Radio Tower 2F.
- **Quest Info:** Showing Togepi to Elm awards Everstone (Side Quest).
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