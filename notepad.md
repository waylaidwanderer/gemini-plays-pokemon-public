# Verified Game Systems
- Start Menu: 1.POKEDEX, 2.POKEMON, 3.PACK, 4.POKEGEAR, 5.GEM, 6.SAVE, 7.OPTION, 8.EXIT.
- Fly Map Cursor: Starts at current location? (Hypothesis: Starts at New Bark Town (5, 4) in some cases). Verification needed.
- Johto Fly Grid (Absolute):
  - (3, 3) Ecruteak, (4, 3) Violet, (5, 3) Mahogany
  - (3, 4) Goldenrod, (4, 4) Cherrygrove, (5, 4) New Bark
  - (3, 5) Azalea
  - (5, 2) Indigo Plateau
  - (2, 4) Olivine, (1, 4) Cianwood

# Roamer Hunt Strategy
- Session 4 Start: Turn 45281.
- Method: Ecruteak Shuffle (Route 37 South Gate).
- Current Status: Arrived in Ecruteak City.
- Repel: Active (Applied Turn 45439, 0 steps). Resetting count for fresh hunt.

# Quest Log
- Dana's Gift: Route 38 (Waiting).
- Yanma Swarm: Route 35 (Active).

# Fly Verification Log
- Attempt 1 (Turn 45533): Exited Option menu. Cursor now on OPTION.
- Attempt 3 (Turn 45535): Cursor moved New Bark -> Cherrygrove (Left). Up and Left from Cherrygrove failed. Hypothesis: Fly map requires multiple presses or specific paths.
- Attempt 4 (Turn 45536): From Cherrygrove, Up x3 then Right -> GOLDENROD CITY. Verified: Goldenrod is reachable from Cherrygrove via this sequence.
- Attempt 5 (Turn 45537): Cursor at Goldenrod. Moving Up to reach Ecruteak.
- Verified Fly Map Grid (Partial):
  - New Bark -> (Left) -> Cherrygrove.
  - Cherrygrove -> (Up x3, Right) -> Goldenrod.
  - Goldenrod -> (Up) -> ECRUTEAK CITY (Target).
- Verified Fly Map Grid (Relative to New Bark):
  - Left: Cherrygrove City.
  - Up from Cherrygrove: VIOLET CITY (To be verified).
  - Right from Violet: MAHOGANY TOWN (To be verified).