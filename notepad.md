# Tile Mechanics
- **FLOOR**: Standard traversable.
- **WALL**: Impassable.
- **LADDER**: Warp point.
- **SECURITY_CAMERA / Persian Statue**: Triggers alarms until switch at (19, 11) is flipped.
- **NPC/Item Sprites**: All sprites act as walls.

# Team Rocket Base Investigation (Mahogany Town)
- **Status:** All passwords obtained. Executive defeated. Currently in B2F Transmitter Room with Lance.
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
- **Verify Current Map ID and Coordinates via Game State before executing navigation.**
1. **Defeat Grunts:** Win the battle against the grunts in the transmitter room.
2. **Shut Down Transmitter:** Neutralize the three Electrode (Lv30) powering the signal.
3. **Reward:** Speak with Lance to receive HM06 (Whirlpool).

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
- B3F West and East sections are connected via gaps in the central walls at (15, 12), (15, 13) and (18, 14), (18, 15).
- Ladders trigger warps automatically; do not press A.