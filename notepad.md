# Tile Mechanics
- **FLOOR**: Standard traversable.
- **WALL**: Impassable.
- **LADDER**: Warp point.
- **SECURITY_CAMERA / Persian Statue**: Triggers alarms until switch at (19, 11) is flipped.
- **NPC/Item Sprites**: All sprites act as walls.

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
  1. Exit base via B1F (27, 2).
  2. Heal at Pokemon Center.
  3. Challenge Gym Leader Pryce. Calcifer (Typhlosion) is lead for Ice-type advantage.

# Floor Connectivity (Mahogany Base)
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

# Mahogany Gym (2_2) - Glacier Badge
- **Leader:** Pryce (Ice-type).
- **Strategy:** Lead with Calcifer (Typhlosion) for Flame Wheel/Ember. GNEISS (Graveler) has Rock Throw/Rollout but is weak to Water (if any) and potentially Ice (though Ground/Rock is weak to Ice).
- **Puzzle Mechanics:**
  - ICE tiles: Sliding movement. You slide until you hit a wall or obstacle.
  - FLOOR tiles: Normal movement.
- **Gym Guide Advice:** Talk to Guide at (7, 15) for hints.

# Progress Log
- Turn 8460: Entered Gym. Position (4, 17). Heading to Gym Guide.

# Reflection (Turn 8465)
- Immediate Execution: Completing the Pokémon switch started on turn 8464.
- Notepad Hygiene: Added Gym strategy and progress log. Cleaned up base connectivity notes.
- Map Hygiene: Marked Gym Guide and trainers. Will mark more as discovered.
- Automation: Using manual buttons for the overworld party menu as custom tools are battle-focused.
- Goal Clarity: Goals are focused on the Glacier Badge.
- Error Analysis: Corrected turn number mismatch. Being cautious with menu navigation to avoid mixing button types.
- Root Hypothesis: The ice puzzle requires finding a path to Pryce. Simple hypothesis: sliding to walls will eventually lead there.

# Mahogany Gym Navigation
- Starting from (7, 16).
- Unseen tiles at Y=11 suggest a large area North.
- Ice tiles (🧊) at (1, 12), (0, 12), etc.
- Goal: Reach Pryce at the back of the gym.

# Progress Log
- Turn 8466: Switching Calcifer to lead position in party menu.

# Trainer Data
- Skier Clarissa (2_2, 9, 17): Dewgong Lv28.

# Progress Log
- Turn 8480: Defeated Skier Clarissa. Calcifer grew to level 37.

# Mahogany Gym Navigation Analysis
- Current Position: (9, 16)
- Obstacles:
  - BEAUTY (Clarissa) at (9, 17) - defeated.
  - WALLS at (8, 12-15), (6, 12-15), (3, 14-15), (1, 12-15).
- Observation: The ice floor starts at Y=13 and continues north.
- Hypothesis 1: To reach the back of the gym, I need to navigate the ice sliding puzzle by using walls and NPCs as stopping points.
- Test 1: Move West from (9, 16) onto the ice at (8, 16) to see where I stop.

# Trainer Data
- Rocker (2_2, 5, 9): Unseen.
- Rocker (2_2, 0, 17): Unseen.

# Progress Log
- Turn 8483: Moving to (5, 10) to challenge the Rocker at (5, 9).

# Trainer Data
- Boarder Brad (2_2, 5, 9): Swinub Lv26.

# Trainer Data
- Boarder Brad (2_2, 5, 9): Swinub Lv26 (Knows Endure).