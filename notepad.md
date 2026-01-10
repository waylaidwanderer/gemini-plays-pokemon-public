# Persistence Knowledge
## Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable.
- LADDER: Traversable (triggers floor change).
- WARP_CARPET_DOWN: Traversable (triggers map transition).
- COUNTER: Face and press A to interact.
- WATER: Requires SURF.
- LEDGE: One-way traversal (jump down).
- GRASS: Traversable (wild encounter zone).
- WHIRLPOOL: Requires WHIRLPOOL.
- WATERFALL: Requires WATERFALL.
- ICE: Sliding movement.
- HOLE: Triggers fall to lower floor.

## S.S. Aqua Discoveries
- Fisher at (1, 15) in FastShipCabins_SW_SSW_NW is a trainer (Firebreather Lyle).
- Porthole tiles and pink sprites (e.g., 6, 15 on 15_5) are decorative walls/background tiles, not interactable.
- Sailor at (24, 17) on 1F: "The passengers are all trainers... itching to battle in their cabins."
- My cabin is at (15, 8) on map 15_3.
- Gentleman (2, 17) on 15_6: "She's an energetic child, so she may be bugging someone."

## Active Quests
- **Find the Gentleman's missing granddaughter.**
  - Started Turn: 37715. Timestamp: Friday, January 9, 2026 at 5:17 PM PST.
  - Status: Investigating cabins on 1F and lower deck.
  - Strategy: Check all warps on 1F (Map 15_3) and then the ladder at (6, 12).
  - Map 15_3 Warp Log:
    - (15, 15) -> 15_5 (2, 19) [Checked]
    - (19, 15) -> 15_5 (2, 31) [Checked]
    - (23, 15) -> 15_6 (2, 7) [Checked]
    - (27, 15) -> 15_6 (2, 19) [Checked]
    - (30, 14) -> 15_7 (31, 13) [Current]
- **Collect the 8 Kanto badges.**
  - Strategy: Vermilion City Gym (Lt. Surge) first. Recommended level 44-50.
  - MVP: GNEISS (Graveler) for Ground immunity to Electric.

## Kanto Gym Leaders (Projected Levels)
- Lt. Surge: 44-46 | Brock: 40-45 | Misty: 42-47 | Erika: 46-51 | Janine: 48-53 | Sabrina: 50-55 | Blaine: 52-57 | Blue: 55-60.

## Lessons Learned
- Gengar (Ghost): Immune to Normal moves (Return).
- Dragonite/Charizard: XENON (Haunter) is immune to Normal moves.
- Safeguard: Prevents status/confusion from Outrage.
- Status: Paralysis reduces speed by 75%.
- Lesson: Always verify current map ID and position after movement. Warps can be subtle.

### Map 15_6 (SE/SSE Cabins & Captain's Cabin)
- Cabin 1 (Rows 0-11): Defeated Pokefan Colin (3, 6) and Twins Meg & Peg (2, 4).
- Cabin 2 (Rows 14-23): Met the Gentleman (2, 17) who lost his granddaughter.
- Strategy: Check for a third cabin segment or Captain's Cabin (Rows 24-33).
- Access: Explore east on FastShip 1F (15_3) for more warps.
- Lower Deck (Map 15_7): Met a Sailor at (30, 6) who is looking for his "lazy bum" buddy.
- Hypothesis: The missing granddaughter is with the missing sailor.
- Strategy: Find the missing sailor on the lower deck. Check western corridors (x=26, x=28).
- Pathfinding: Corridor at y=5 is open.
- Target: Super Nerd at (26, 9) in the western corridor.
- Observation: Sailor ID 2 at (31, 6) disappeared and was replaced by Sailor ID 1 at (30, 6).
- Navigation: Move around the sailor at (30, 6) via (31, 6) and (31, 5).