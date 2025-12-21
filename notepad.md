# Tile Mechanics
- **FLOOR**: Standard traversable tile.
- **WALL**: Impassable barrier.
- **LADDER**: Warp point between floors.
- **WARP_PANEL**: Transport tile (often one-way).
- **BOOKSHELF**: Impassable background object.
- **COUNTER**: Impassable. Interact with NPCs/Items from an adjacent tile.
- **SECURITY_CAMERA / Persian Statue**: Triggers alarms and battles until disabled.
- **NPC/Item Sprites**: All sprites have collision and act as walls.

# Team Rocket Base Investigation (Mahogany Town)
- **Start Turn:** 7917 (Mahogany Mart), 8051 (B2F), 8222 (Switch Phase)
- **Status:** Passwords 'RATICATE TAIL' and 'SLOWPOKETAIL' obtained.

## Map: Team Rocket Base B1F (3_49)
- **Security:** Persian statues act as security cameras. Proximity triggers intruder alerts.
- **Warps:**
  - (27, 2): Ladder to B2F East.
  - (3, 14): Ladder to B2F West.
  - (5, 15): Warp panel (shortcut) to (25, 2).
- **Objects:**
  - (18, 12): Scientist Jed (Defeated).
  - (19, 11): Secret Switch (Disables Statues). Interact from (19, 12).
  - (21, 12): Item Ball.
  - (14, 15): Item Ball.

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
  - Rocket Grunt (7, 14): Raticate (Lv19). Reward: ¥760. Password 1: RATICATE TAIL.
  - Rocket Girl (21, 7): Ekans (Lv18), Gloom (Lv18). Reward: ¥720. Password 2: SLOWPOKETAIL.

# Strategy (HOW)
1. **Disable Alarms:** Interact with the Secret Switch at (19, 11) from (19, 12).
2. **Loot B1F:** Collect items at (21, 12) and (14, 15).
3. **Advance to B2F:** Use the western ladder at (3, 14).
4. **Navigate B2F:** Move through the Voltorb traps to reach the western section.
5. **Infiltrate B3F:** Use passwords to unlock the Boss door at (10, 9) on B3F.
6. **Final Objective:** Shut down the transmitter on B2F.

# Lessons Learned
- Item sprites and COUNTER tiles have collision; interact from adjacent FLOOR.
- Map sections can be completely isolated; look for alternative floor transitions.
- Persian statues on B1F trigger alarms until switch at (19, 11) is flipped.