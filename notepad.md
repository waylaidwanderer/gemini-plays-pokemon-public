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
- Current Status: Verifying Fly Map cursor behavior.
- Repel: Active (Applied Turn 45439, 10 steps).

# Quest Log
- Dana's Gift: Route 38 (Waiting).
- Yanma Swarm: Route 35 (Active).

# Fly Verification Log
- Attempt 1 (Turn 45533): Exited Option menu. Cursor now on OPTION.
- Attempt 2 (Turn 45534): Map opened successfully. Verified: Cursor starts at New Bark Town (red arrow at easternmost dot).
- Attempt 3 (Turn 45535): Moving cursor to verify grid. Target: Ecruteak City.
- Verified Fly Map Grid (Relative to New Bark):
  - Left: Cherrygrove City.
  - Left, Up: Violet City.
  - Left, Up, Left: Ecruteak City.