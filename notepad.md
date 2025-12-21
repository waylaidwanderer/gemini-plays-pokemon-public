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
- B1F (27, 2) <&lt;-> Mahogany Mart (7, 3) [Entrance/Exit]
- B1F (3, 14) <&lt;-> B2F (3, 14)
- B2F (27, 14) <&lt;-> B3F (27, 14)
- B3F (27, 2) <&lt;-> B2F (27, 2)
- B2F (3, 2) <&lt;-> B3F (3, 2)
- B3F (3, 6) <&lt;-> B2F (3, 6) [Access to TM46]

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

# Mahogany Gym Navigation Analysis
- Current Position: (2, 10).
- Goal: Reach Beauty at (4, 6).
- Path: (2, 10) -> Right -> (5, 10) -> Right -> (9, 10) -> Up -> (9, 7) -> Left -> (4, 7).
- Hypothesis: Sliding into FLOOR tiles is the key to course-correcting in this gym.