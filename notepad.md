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
- Fisher at (1, 15) in FastShipCabins_SW_SSW_NW is a trainer (Firebreather Lyle).
- Porthole tiles (e.g., 0, 12 on 15_5) and pink sprites at (6, 15), (6, 17) on 15_5 are decorative walls/background tiles, not interactable.
- Sailor at (24, 17) on 1F: "The passengers are all trainers... itching to battle in their cabins."
- My cabin is at (15, 8) on map 15_3.

### Lessons Learned
- Gengar (Ghost): Immune to Normal moves (Return).
- Dragonite/Charizard (Ghost interaction): XENON is immune to Normal moves (Hyper Beam/Slash).
- Safeguard: Prevents status conditions and confusion from Outrage.
- Outrage: User is locked for 2-3 turns.
- Status Management: Paralysis reduces speed by 75%.

## Post-Game Strategy
- Start Turn: 37664 (Return to New Bark Town).
- Strategy: Use Fly to Olivine, board S.S. Aqua.
- Kanto Gym 1: Lt. Surge (Vermilion City). Lv 44-46. MVP: GNEISS (Lv 51) for Ground immunity.

## Kanto Gym Leaders (Projected/Verified Levels)
- Lt. Surge: 44-46 (Confirmed) | Brock: 40-45 | Misty: 42-47 | Erika: 46-51 | Janine: 48-53 | Sabrina: 50-55 | Blaine: 52-57 | Blue: 55-60.

## Active Quests
- Find the Gentleman's missing granddaughter. Started Turn: 37715.
- Strategy: Check all cabins on 1F and explore lower deck areas via all staircases/ladder.
- Map 15_3 Staircases: (15, 15) -> 15_5 (2, 19) [Checked], (19, 15) -> 15_5 (2, 31) [Checked], (23, 15) -> 15_6 (2, 7) [Current], (27, 15) [Next].
- Map 15_3 Ladder: (6, 12).
- FastShip 15_6: Found two Twins at (2, 4) and (3, 4). Defeated them. One might be the granddaughter.
- Kanto Gym 1: Lt. Surge (Vermilion City). Lv 44-46. MVP: GNEISS (Lv 51).

### Battle Observations (S.S. Aqua)
- Hiker Noland: Sandslash (Lv 31), Golem (Lv 33).
- Firebreather Lyle: Koffing (Lv 28), Flareon (Lv 31).
- Type Effectiveness: Rock resists Normal and Fire. Ground is immune to Electric.
- Lesson: Always verify current map ID and position in Game State Information after movement, even if no warp animation is seen. Warps can be subtle.
### Map 15_6 (SE/SSE Cabins & Captain's Cabin)
- Cabin 1 (Rows 0-11): Defeated Pokefan Colin (3, 6) and Twins Meg & Peg (2, 4), (3, 4).
- Mystery: Observed a pink sprite that moved between (5, 5) and (5, 7). Attempted interaction at (5, 6) facing up, but no text appeared. The sprite is NOT in the Map Objects list. It may be decorative or require a trigger (like talking to the Captain).
- Strategy: Exit this cabin and check the next warp in FastShip 1F (15_3) at (27, 15) to find the Captain's Cabin.
- Access: Use other warps in FastShip 1F (15_3) to reach other segments of Map 15_6. Segment 1 (checked) is rows 0-11.