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
- **Start Turn:** 7917 (Mahogany Mart), 8051 (B2F), 8256 (B2F Exploration)
- **Status:** Passwords 'RATICATE TAIL' and 'SLOWPOKETAIL' obtained. Alarms disabled on B1F.

## Map: Team Rocket Base B2F (3_50)
- **Navigation:** The central column (Col 23) is a wall. The only passage is at (23, 16).
- **Security:** Voltorb sprites (e.g., (7, 9), (22, 7-15)) are hidden traps. Approaching them triggers a Voltorb battle.
- **Objects:**
  - (14, 12), (15, 12): Locked Doors to Transmitter Room.
  - (3, 10): Item Ball.
  - (5, 13): Lance (Heals party).
  - (21, 14), (25, 13): Rocket Grunts.
- **Warps:**
  - (3, 14): Ladder to B1F West.
  - (27, 14): Ladder to B3F East.

# Strategy (HOW)
1. **Loot B2F West:** Pick up item at (3, 10).
2. **Heal:** Talk to Lance at (5, 13) if needed.
3. **Traverse Voltorb Traps:** Move east through the corridor (Rows 7-11) toward the barrier at Col 23.
4. **Bypass Barrier:** Navigate south to (23, 16) to enter the eastern section.
5. **Clear B2F East:** Defeat Grunts and reach the ladder at (27, 14).
6. **Infiltrate B3F:** Use passwords to unlock the Boss door at (10, 9) on B3F.
7. **Final Objective:** Shut down the transmitter on B2F.

# Lessons Learned
- Item sprites and COUNTER tiles have collision; interact from adjacent FLOOR.
- Map sections can be completely isolated; look for alternative floor transitions.
- Persian statues on B1F trigger alarms until switch at (19, 11) is flipped.
- Voltorb sprites on B2F are stationary traps; expect battles when adjacent.