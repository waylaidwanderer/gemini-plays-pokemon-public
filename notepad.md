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
  - (5, 15): Warp panel shortcut to (25, 2).
  - (19, 11): Secret Switch (Disables Statues). Interact from (19, 12).
- **B2F (3_50):**
  - **Structure:** Divided into isolated sections.
  - **North-West Corridor:** Ladder (3, 2) to B1F North-West.
  - **Central Section:** Gaps in Row 4 at (10, 4), (18, 4), (19, 4). Contains Voltorb traps.
  - **South-West Room:** Ladder (3, 6) and item (3, 10). Reachable via B3F West.
  - **Southern Corridor:** Gap at (23, 16) connects East and West.
- **B3F (3_51):**
  - (27, 14): Ladder to B2F East.
  - (10, 9): Boss Room Door. **HOW:** Face (10, 9) or (11, 9) and press A to use passwords.
  - (3, 2): Ladder to B2F North-West.
  - (3, 6): Ladder to B2F South-West (Isolated Room).
- **Key Encounters:**
  - **Malice:** Met on B3F West (7, 10). He complained about losing to a "cape guy with dragon Pokemon" (Lance) and mentioned Lance's lecture on loving Pokemon. He left to find stronger Pokemon.

# Strategy (HOW)
1. **Confront Boss:** Open the door at (10, 9) on B3F and defeat the Executive.
2. **Shut Down Transmitter:** Use the final password (obtained from the boss) to disable the signal on B2F.

# Lessons Learned
- Map sections can be completely isolated; look for alternative floor transitions.
- Voltorb sprites on B2F are stationary traps; expect battles when adjacent.
- Persian statues on B1F trigger alarms until switch at (19, 11) is flipped.
- **Path to Boss:** B2F East -> B3F East -> B2F North -> B3F West.