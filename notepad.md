## Persistence Knowledge
### Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable.
- LADDER: Traversable.
- WARP_CARPET: Traversable (triggers map transition).
- COUNTER: Face and press A to interact.
- WATER: Requires SURF.
- LEDGE: One-way traversal (jump down).
- GRASS: Traversable (wild encounter zone).
- WHIRLPOOL: Requires WHIRLPOOL.
- WATERFALL: Requires WATERFALL.
- ICE: Sliding movement.
- HOLE: Triggers fall to lower floor.

### Tile Mechanics (S.S. Aqua)
- FLOOR: Traversable.
- WALL: Impassable.
- WARP_CARPET: Traversable.
- LADDER: Traversable.

### S.S. Aqua Discoveries
- My cabin is at (15, 8) on map 15_3. Nap in the bed to heal Pokemon.
- Explore all cabins to find the missing girl.
- Gentleman at (25, 6) in FastShip 1F is looking for his granddaughter.
- Sailor at (14, 7) in FastShip 1F guards/points to the player's cabin.
- Fisher at (1, 15) in FastShipCabins_SW_SSW_NW is a trainer (Firebreather Lyle).

### Lessons Learned
- Gengar (Ghost): Immune to Normal moves (Return).
- Dragonite/Charizard (Ghost interaction): XENON is immune to Normal moves (Hyper Beam/Slash).
- Safeguard: Prevents status conditions and confusion from Outrage.
- Outrage: User is locked for 2-3 turns.
- Status Management: Paralysis reduces speed by 75%.
- S.S. Aqua: Granddaughter lead - check all cabins and hallways.

## Post-Game Strategy
- Start Turn: 37664 (Return to New Bark Town).
- Objective: Travel to Olivine City to board the S.S. Aqua to Kanto.
- Objective: Collect the 8 Kanto Badges.
- Strategy: Use Fly to Olivine, enter the Port Passage south of the city, and follow the path to the S.S. Aqua.

## Kanto Gym Leaders
- Brock (Pewter City): Rock-type. Recommended level: 40-45.
- Misty (Cerulean City): Water-type. Recommended level: 42-47.
- Lt. Surge (Vermilion City): Electric-type. Recommended level: 44-49.
- Erika (Celadon City): Grass-type. Recommended level: 46-51.
- Janine (Fuchsia City): Poison-type. Recommended level: 48-53.
- Sabrina (Saffron City): Psychic-type. Recommended level: 50-55.
- Blaine (Cinnabar Island): Fire-type. Recommended level: 52-57.
- Blue (Viridian City): Multi-type. Recommended level: 55-60.
- Kanto Strategy (from analyst): Head to Vermilion City Gym first. Lt. Surge uses Electric-types (Lv 44-46). GNEISS (Lv 51) is the MVP.
- Need to train XENON, Ouroboros, and LAPIS or find stronger replacements.
- S.S. Aqua 15_5: Cabin doors at (0, 12), (2, 12), (4, 12), (6, 12).
- S.S. Aqua 15_5: Pink sprites at (1, 17) and (6, 17) appear to be background tiles, not NPCs.
- S.S. Aqua 15_5: Testing door at (0, 12).
- Hypothesis: The porthole tile at (0, 12) is a door that can be entered by walking into it.
- Test 1: Press Up at (0, 13) facing up. Result: FAILED (Tile is a WALL).
- Conclusion: Porthole tile at (0, 12) is NOT a door.
- Hypothesis 2: Maybe one of the other porthole tiles is a door.
- Test 2: Press Up at (2, 13) facing (2, 12). Result: FAILED (Tile is a WALL).
- Conclusion: Porthole tiles at (0, 12) and (2, 12) are NOT doors.
- Hypothesis 3: Porthole tiles might require pressing 'A'.
- Test 3: Press A at (4, 13) facing (4, 12). Result: [Pending]
- Observation: Pink sprites at (1, 17) and (6, 17) are not in the object list; likely background tiles.
- Strategy: If (0, 12) is a wall, check all other porthole tiles (2, 12), (4, 12), (6, 12) and then explore 1F cabins.