# Team Rocket Base Investigation (Mahogany Town)
## Map: Team Rocket Base B1F (3_49)
- **Security:** Persian statues (e.g., (24, 1), (6, 1), (8, 15), (24, 5)) act as security cameras. Passing them triggers an intruder alert and a Grunt battle.
- **Warps:**
  - (27, 2): Ladder to B2F East.
  - (3, 14): Ladder to B2F West.
  - (5, 15): Warp panel to [Unknown].
- **Current Task:** Explore the warp panel at (5, 15) to find a route to B3F West.

## Map: Team Rocket Base B2F (3_50)
- **Path to West:** Column 23 is a barrier. Bypass via Row 16 (FLOOR) at (23, 16).
- **Objects:**
  - (14, 12), (15, 12): Locked Doors to Transmitter Room.
  - (21, 14), (25, 13): Rocket Grunts (Defeated).
  - (22, 7-15): Voltorb traps.

## Map: Team Rocket Base B3F (3_51)
- **Observations:** Boss Room (10, 9) is isolated by a wall at Row 11. Eastern ladder (27, 14) is a dead end for the Boss.
- **Trainer Roster:**
  - Scientist Mitch (11, 15): Ditto (Lv24). Reward: ¥2400.
  - Rocket Grunt (7, 14): Raticate (Lv19). Password 1: RATICATE TAIL.
  - Rocket Girl (21, 7): Ekans (Lv18), Gloom (Lv18). Password 2: SLOWPOKETAIL.

# Global Tile Mechanics
- FLOOR: Traversable.
- WALL / BOOKSHELF / TABLE / MART_SHELF: Impassable.
- WATER: Traversable (Surf + HM Badge).
- COUNTER: Impassable. Interact with NPCs/Items from an adjacent tile.
- WARP: Map transition.

# Strategy (HOW)
1. Defeat the current Grunt on B1F.
2. Enter the warp panel at (5, 15) on B1F.
3. Search for a ladder leading to the western (isolated) section of B3F.
4. Use passwords 'RATICATE TAIL' and 'SLOWPOKETAIL' to unlock the Boss door at (10, 9).
5. Defeat the Executive to shut down the transmitter.

# Lessons Learned
- Item sprites and COUNTER tiles have collision; interact from adjacent FLOOR.
- Map sections can be completely isolated; look for alternative floor transitions.
- Alarms are triggered by proximity to Persian statues on B1F.