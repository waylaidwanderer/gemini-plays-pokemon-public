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
- **Status:** Passwords 'RATICATE TAIL' and 'SLOWPOKETAIL' obtained. Alarms disabled on B1F.
- **B1F (3_49):**
  - (27, 2): Entrance Ladder (from Mart).
  - (3, 14): Ladder to B2F West (South section).
  - (5, 15): Warp panel (shortcut) to (25, 2).
  - (18, 12): Scientist Jed (Defeated).
  - (19, 11): Secret Switch (Disables Statues). Interact from (19, 12).
- **B2F (3_50):**
  - (3, 14): Ladder to B1F West (South section).
  - (27, 14): Ladder to B3F East.
  - (14, 12), (15, 12): Locked Doors to Transmitter Room.
  - (14, 9): Radio Transmitter.
  - (23, 16): Passage between East and West sections.
  - (7-22, 7-15): Voltorb traps.
- **B3F (3_51):**
  - (27, 14): Ladder to B2F East.
  - (24, 14): Rocket Grunt (Talked to).
  - (23, 11): Scientist Ross (Defeated).
  - (10, 9): Boss Room Door (Locked). Requires 2 passwords.

# Strategy (HOW)
1. **Find B2F North:** Search B1F for a ladder leading to the isolated northern section of B2F.
2. **Loot B2F North:** Reach the item at (3, 10) on B2F.
3. **Find B3F West:** Locate the ladder in B2F North that leads to the western section of B3F.
4. **Confront Boss:** Use passwords to unlock the door at (10, 9) on B3F and defeat the Executive.
5. **Shut Down Transmitter:** Use the final password to enter the transmitter room on B2F and disable the signal.

# Lessons Learned
- Map sections (like B2F and B3F) can be completely isolated; look for alternative floor transitions.
- Voltorb sprites on B2F are stationary traps; expect battles when adjacent.
- Persian statues on B1F trigger alarms until switch at (19, 11) is flipped.
- Always check if an NPC or Item sprite is at the target coordinate before pathing.