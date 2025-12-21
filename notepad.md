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
- **Status:** Passwords 'RATICATE TAIL', 'SLOWPOKETAIL', and 'HAIL GIOVANNI' obtained. Executive defeated.
- **B1F (3_49):**
  - (19, 11): Secret Switch (Disables Statues).
- **B2F (3_50):**
  - **Structure:** Isolated sections. Row 1 is the only path between NW and East.
  - **Central Section:** Contains Electrode transmitter powering the radio signal.
  - **South-West Room:** Ladder (3, 6) and item (3, 10). Reachable via B3F West.
- **B3F (3_51):**
  - (10, 9): Boss Room Door (Opened).
  - (8, 3): Boss Office. Executive defeated.
  - (7, 2): Murkrow location (gives final password).
- **Key Encounters:**
  - **Malice:** Met on B3F West (7, 10). Left to find stronger Pokemon.
  - **Rocket Executive:** Defeated on B3F West.

# Strategy (HOW)
- **Verify Current Map ID and Coordinates via Game State before executing any multi-turn navigation plan.**
1. Shut Down Transmitter: Return to B2F South, open the locked doors at (14, 12) or (15, 12) using 'HAIL GIOVANNI', and neutralize the three Electrode.
2. Reward: Speak with Lance to receive HM06 (Whirlpool).

# Floor Connectivity (Mahogany Base)
- B1F (3, 14) < Indoors > B2F (3, 14) [Main Path]
- B2F (27, 14) < Indoors > B3F (27, 14) [East-South]
- B3F (27, 2) < Indoors > B2F (27, 2) [East-North]
- B2F (3, 2) < Indoors > B3F (3, 2) [NW <-> B3F West North]
- B3F (3, 6) < Indoors > B2F (3, 6) [B3F West South <-> Isolated SW Room (TM46)]

# Lessons Learned
- Map sections are isolated; use specific ladders to cross.
- Voltorb sprites on B2F are traps.
- Boss door requires two passwords from grunts on B3F.
- **Path to Transmitter Room:** B2F NW (3, 2) -> (27, 2) via Row 1 -> B3F East -> (27, 14) -> B2F South -> (14, 12).
- B3F West and East sections are connected via gaps in the central walls at (15, 12), (15, 13) and (18, 14), (18, 15).