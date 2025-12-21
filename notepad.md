# Team Rocket Base Investigation (Mahogany Town)
- Status: Passwords 'RATICATE TAIL' and 'SLOWPOKETAIL' obtained.

## Map: Team Rocket Base B1F (3_49)
- **Traps:** Persian statues (e.g., at (24, 1), (6, 1)) trigger intruder alerts and Grunt battles. Alarms are at col 24 and col 6.
- **Warps:**
  - (27, 2): Ladder to B2F.
  - (3, 14): Ladder to B2F (West).
  - (5, 15): Warp panel.

## Map: Team Rocket Base B2F (3_50)
- **Path to West:** Column 23 wall is bypassed via Row 16 (FLOOR).
- **Warps:**
  - (3, 14): Ladder to B1F.
  - (27, 14): Ladder to B3F (Eastern section).
- **Objects:**
  - (14, 12), (15, 12): Locked Doors to Transmitter Room.
  - (14, 9): Radio Transmitter.
  - (21, 14): Rocket Grunt (Defeated).
  - (25, 13): Rocket Grunt (Defeated).
  - (22, 7), (22, 9), (22, 11), (22, 13), (22, 15): Voltorbs (Statues/Traps).
- **B2F Strategy:** Traverse Row 16 to bypass the Column 23 wall and access the western section of the base.

## Map: Team Rocket Base B3F (3_51)
- **Observations:**
  - Row 11: WALL from (1, 11) to (13, 11) isolates the Boss Room (10, 9).
  - Eastern section (reachable via ladder at 27, 14) is a dead end for reaching the Boss.
  - Western section items: X Special (3, 12), Protein (1, 12). Both collected.
- **Trainer Roster:**
  - Scientist Mitch (11, 15): Ditto (Lv24). Reward: ¥2400.
  - Rocket Grunt (7, 14): Raticate (Lv19). Reward: ¥760. Password 1: RATICATE TAIL.
  - Scientist Ross (23, 11): Koffing (Lv22), Koffing (Lv22). Reward: ¥2200.
  - Rocket Girl (21, 7): Ekans (Lv18), Gloom (Lv18). Reward: ¥720. Password 2: SLOWPOKETAIL.

# Global Tile Mechanics
- FLOOR: Verified traversable.
- WALL / BOOKSHELF / TABLE / MART_SHELF: Verified impassable.
- WATER: Verified traversable (Surf + HM Badge).
- TALL_GRASS: Verified traversable.
- COUNTER: Verified impassable (interact from adjacent).
- WARP: Map transition.

# Party Training Status
- GNEISS (GRAVELER): Lv38 (106/106 HP). Primary carry. Magnitude, Defense Curl, Strength, Rollout.
- Calcifer (TYPHLOSION): Lv36 (113/114 HP). Primary carry. Flame Wheel, Headbutt, Smokescreen, Ember.
- ICARUS (PIDGEY): Lv16 (43/43 HP).
- KIMCHI (GLOOM): Lv21 (57/57 HP).
- Ravioli (KRABBY): Lv10 (27/27 HP).
- Blarney (SUDOWOODO): Lv20 (60/60 HP).

# Lessons Learned
- Item sprites and COUNTER tiles have collision; interact from adjacent FLOOR.
- Map sections can be completely isolated; look for alternative floor transitions.
- Alarms trigger battles at specific columns/tiles on B1F.