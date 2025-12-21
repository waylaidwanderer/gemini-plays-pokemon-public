# Tile Mechanics
- **FLOOR**: Standard traversable. Stops sliding movement.
- **WALL**: Impassable. Stops sliding movement.
- **ICE**: Sliding movement. Entering an ICE tile causes the player to slide in that direction until they hit a WALL, an Object, or a non-ICE tile.
- **LADDER**: Warp point.
- **SECURITY_CAMERA / Persian Statue**: Triggers alarms until switch at (19, 11) is flipped.
- **NPC/Item Sprites**: All sprites act as walls and stop sliding movement.

# Movesets
- **Dewgong**: Growl.
- **Swinub**: Endure.
- **Jynx**: Doubleslap.
- **Seel**: (In battle).

# Team Rocket Base Investigation (Mahogany Town) - COMPLETED
- **Status:** Transmitter shut down. HM06 Whirlpool obtained from Lance.
- **B1F (3_49):**
  - (27, 2): Entrance/Exit Ladder to Mahogany Mart.
  - (19, 11): Secret Switch (Disabled Alarms).
- **B2F (3_50):**
  - (14, 9): Radio Transmitter (Signal Stopped).
  - (3, 14): Ladder to B1F (3, 14).
- **B3F (3_51):**
  - (10, 9): Boss Room. Executive defeated.

# Strategy (HOW)
- **Earn Glacier Badge:**
  1. Challenge Gym Leader Pryce. Calcifer (Typhlosion) is lead for Ice-type advantage.
  2. Navigate the ice puzzle by using walls and trainers as anchors.

# Floor Connectivity
- B1F (27, 2) <-> Mahogany Mart (7, 3) [Entrance/Exit]
- B1F (3, 14) <-> B2F (3, 14)
- B2F (27, 14) <-> B3F (27, 14)
- B3F (27, 2) <-> B2F (27, 2)
- B2F (3, 2) <-> B3F (3, 2)
- B3F (3, 6) <-> B2F (3, 6) [Access to TM46]

# Lessons Learned
- Map sections are isolated; use specific ladders to cross.
- Whirlpool requires Glacier Badge to use out of battle.
- B3F West and East sections are connected via a gap in the central wall at (18, 16).
- `switch_pokemon_v1` and `battle_move_selector` are designed for specific menu states (PKMN menu and Move menu respectively). Do not use in overworld menus.

# Mahogany Gym (2_2) - Glacier Badge
- **Leader:** Pryce (Ice-type).
- **Strategy:** Lead with Calcifer (Typhlosion) for Flame Wheel/Ember.
- **Trainer Data:**
  - Skier Clarissa (2_2, 9, 17): Dewgong Lv28.
  - Boarder Brad (2_2, 5, 9): Swinub Lv26.
  - Skier Roxanne (2_2, 4, 6): Jynx Lv28.
  - Boarder Ronald (2_2, 2, 17): Seel Lv24.
  - Rocker (2_2, 2, 4): Unseen.

# Mahogany Gym Navigation Plan (Updated Turn 8516)
- Current Position: (1, 17) [In battle with Ronald at (2, 17)].
- Goal 1: Defeat Boarder Ronald.
- Goal 2: Defeat Rocker at (2, 4).
  1. From (2, 17), move Up to (2, 16) [FLOOR].
  2. Move Up to (2, 14) [FLOOR].
  3. Move Up to (2, 5) [ICE, stops at Rocker].
  4. Talk to Rocker at (2, 4).
- Goal 3: Defeat Gym Leader Pryce at (5, 3).
  1. From (2, 5), move Right to (6, 5) [FLOOR].
  2. Move Up to (6, 2) [FLOOR].
  3. Move Left to (5, 2) [ICE, stops at Pryce or WALL at (4, 2)].
  4. Move Down to talk to Pryce at (5, 3).