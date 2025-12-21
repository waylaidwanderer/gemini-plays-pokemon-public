# Tile Mechanics
- **FLOOR**: Standard traversable.
- **WALL**: Impassable.
- **LADDER**: Warp point.
- **SECURITY_CAMERA / Persian Statue**: Triggers alarms until switch at (19, 11) is flipped.
- **NPC/Item Sprites**: All sprites act as walls.

# Team Rocket Base Investigation (Mahogany Town)
- **B1F (3_49):**
  - (19, 11): Secret Switch (Disables Statues).
- **B2F (3_50):**
  - **Structure:** Divided into isolated sections. Row 1 connects NW and East.
  - **Central Section:** Transmitter room (locked door 14, 12). Contains three Electrode (Lv30).
- **B3F (3_51):**
  - (10, 9): Boss Room Door (Opened).
  - (8, 3): Boss Office. Executive defeated.
  - (7, 2): Murkrow location (gave password 'HAIL GIOVANNI').

# Strategy (HOW)
- **Neutralize Electrodes:** Interact with tiles (7, 5), (7, 7), and (7, 9) from column 8 or 6.
- **Exit Base:** Speak with Lance after clearing Electrodes for HM06 (Whirlpool).
- **Navigation:** Verify Map ID and Coordinates via Game State before multi-turn movement.

# Floor Connectivity (Mahogany Base)
- B1F (3, 14) <-> B2F (3, 14) [Main Path]
- B2F (27, 14) <-> B3F (27, 14) [East-South]
- B3F (27, 2) <-> B2F (27, 2) [East-North]
- B2F (3, 2) <-> B3F (3, 2) [NW <-> B3F West North]
- B3F (3, 6) <-> B2F (3, 6) [B3F West South <-> SW Secret Room]

# Lessons Learned
- Map sections are isolated; use specific ladders to cross.
- Voltorb sprites on B2F are traps.
- Boss door requires two passwords from grunts on B3F.
- B3F West and East sections are connected via a gap in the central wall at (18, 16).
- Ladders trigger warps automatically; do not press A.