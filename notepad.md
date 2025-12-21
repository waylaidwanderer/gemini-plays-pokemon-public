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
  - (27, 2): Entrance Ladder.
  - (3, 14): Ladder to B2F West (South section).
  - (5, 15): Warp panel (shortcut) to (25, 2).
  - (18, 12): Scientist Jed (Defeated).
  - (19, 11): Secret Switch (Disables Statues). Interact from (19, 12).
- **B2F (3_50):**
  - (3, 14): Ladder to B1F West (South section).
  - (3, 2): Ladder to B1F North-West (Entry Point 1).
  - (27, 14): Ladder to B3F East.
  - (14, 12), (15, 12): Locked Doors to Transmitter Room.
  - (14, 9): Radio Transmitter.
  - (23, 16): Passage between East and West sections.
  - (7-22, 7-15): Voltorb traps.
- **B3F (3_51):**
  - (27, 14): Ladder to B2F East.
  - (24, 14): Rocket Grunt (Talked to).
  - (23, 11): Scientist Ross (Defeated).
  - (10, 9): Boss Room Door (Locked). Requires 2 passwords. Hypothesis: Western section is isolated from the east; reach via B2F North.

# Strategy (HOW)
1. **Access B2F North:** Use the ladder at (27, 2) on B3F to reach the isolated northern corridor on B2F.
2. **Explore B2F North:** Follow the corridor west to find the ladder to B3F West.
3. **Confront Boss:** Unlock the door at (10, 9) on B3F and defeat the Executive.
4. **Shut Down Transmitter:** Use the final password to disable the signal on B2F.

# Lessons Learned
- Map sections can be completely isolated; look for alternative floor transitions.
- Voltorb sprites on B2F are stationary traps; expect battles when adjacent.
- Persian statues on B1F trigger alarms until switch at (19, 11) is flipped.
- Always check if an NPC or Item sprite is at the target coordinate before pathing.
- **Path to Boss:** The western section of B3F (Boss Room) is reached by taking the ladder at (27, 14) on B2F to B3F East, then the ladder at (27, 2) on B3F to reach B2F North, which leads to B3F West.
- **B2F Exploration:**
  - (3, 6): Ladder (Unmarked). Hypothesis: Leads to B3F West (Boss Room).
  - (3, 10): Item Ball.
  - (1, 8) to (19, 8): Unseen tiles.
  - (10, 4), (18, 4), (19, 4): Gaps in the central wall allowing North/South movement.
  - (19, 10): Gap between East and West sections.
- **B2F Map Structure:**
  - The floor is divided into isolated sections.
  - **North-West Corridor (x=1-5, y=1-3):** Contains ladder (3, 2) to B1F North-West.
  - **Central Section (x=7-22, y=4-11):** Accessible via gaps in Row 4 at (10, 4), (11, 4), (18, 4), (19, 4).
  - **South-West Room (x=1-5, y=5-11):** Contains ladder (3, 6) and item (3, 10). Enclosed by walls at x=0, x=6, Row 4, and Row 12. Hypothesis: Enter via B1F or B3F.
  - **Passage (x=24, y=1-16):** Connects North-East and South-East sections.
  - **Southern Corridor (y=13-16):** Split into West (x=1-22) and East (x=24-28). Connected by a gap at (23, 16).