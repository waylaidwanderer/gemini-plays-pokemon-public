# Route 3, Mt. Moon, and Cerulean City Progression Scratchpad
- Started: Turn 4122, Timestamp: Sunday, May 24, 2026 at 6:18 AM PDT

## Current Status:
- Turn 8183: Standing at (27, 27) on Map 0_61 (Mt. Moon B2F) facing Right. We have definitively tested the southern platform and verified it dead-ends at Column 22 on Rows 21-22, and Column 23 on Row 23, and have documented this constraint in Locations/MtMoon_B2F. We are now backtracking east to the Eastern Corridor at Column 28, then north to Row 17 to reach the Central Platform stairs.

## Systematic Column 19 Passability Test (Started Turn 8011, Timestamp: Monday, May 25, 2026 at 3:00 AM PDT):
- **Objective**: Determine if Column 19 (mislabeled or visually decorated as TYPE_2889) is passable on any row from Row 28 to Row 32.
- **Methodology**:
  1. Return to (24, 28) and move Left to (20, 28).
  2. Attempt to walk Left from (20, 28) into (19, 28) to test Row 28.
  3. If blocked, move Down to (20, 30) and attempt to walk Left into (19, 30).
  4. If blocked, move Down to (20, 31) and attempt to walk Left into (19, 31).
  5. If blocked, move Down to (20, 32) and attempt to walk Left into (19, 32).
- **Results**:
  - Row 28 Test: Solid (Turn 8029 Collision Test - 0 tiles visited)
  - Row 30 Test: Solid (Turn 8036 Collision Test - 0 tiles visited)
  - Row 31 Test: Solid (Turn 8043 Collision Test - 0 tiles visited)
  - Row 32 Test: Solid (Turn 8048 Collision Test - 0 tiles visited)

## Progression Roadmap & Checklist:
- [x] Defeat Pewter Gym Leader Brock (Boulder Badge & TM34 secured!).
- [x] Healed team at Pewter City Pokémon Center at (13, 25).
- [x] Stock up on useful items at Pewter Poké Mart at (23, 17) (Secured 4 Potions, 3 Poké Balls, 3 Antidotes, 1 Paralyze Heal; ¥601 remaining).
- [ ] Explore the Museum of Science (optional, northern part of town).
- [x] Navigate east through Route 3 to Mt. Moon entrance.
- [ ] Traverse Mt. Moon to reach Route 4.
- [ ] Reach Cerulean City.

## Unexplored Paths & West Wall Bypass Hypothesis:
- We are currently exploring Columns 12-13 vertical wall on Mt. Moon 1F. Columns 12 and 13 are solid (TYPE_2889) on rows 2 through 10.
- Columns 10 and 11 are visible on the western side of the rock wall as passable floor (TYPE_3fe2).
- We need to find how to cross from Column 14 to Column 11. We are heading south on Column 14 to see if the rock wall ends.
- Alternatively, check if the rock wall ends at the top (Row 1 or 0) if the southern path is blocked.

## Mt. Moon Team-Training Strategy & Timestamps (Turn 4801):
- Starting Turn for Pewter Restocking: Turn 4801
- Target Level-Ups:
  - **BUGGY (METAPOD)**: Lv 12 achieved! Learned Confusion!
  - **SPARKY (PIKACHU)**: Train to Level 11 to learn Quick Attack.

### SPARKY Training Session Log (Turn 6126):
- Starting Turn for SPARKY training: Turn 6126
- Starting Level: Level 6 (0/117 EXP)
- Target Level: Level 16 (to learn Quick Attack in Red/Blue)
- Timestamp: Sunday, May 24, 2026 at 3:25 PM PDT.
- Grinding Progress:
  - Turn 6149: Reached Level 7 after defeating Rocket Grunt's Level 11 Sandshrew (gained 108 EXP).
  - Turn 6168: Gained 66 EXP after defeating Rocket Grunt's Level 11 Rattata.
  - Turn 6198: Reached Level 8 after defeating Rocket Grunt's Level 11 Zubat (gained 63 EXP).
  - Turn 6263: Gained 69 EXP after defeating wild Level 9 Zubat.
  - Turn 6289: Gained 55 EXP after defeating wild Level 9 Geodude.
  - Turn 6307: Reached Level 9 and learned THUNDER WAVE! (Defeated wild Level 10 Zubat, gained 75 EXP).
  - Turn 6339: Gained 49 EXP after defeating wild Level 8 Geodude. SPARKY is now at Level 9 with 98/148 EXP.
  - Turn 6377: Gained 77 EXP after defeating wild Level 10 Zubat. SPARKY is now at Level 9 with 175/148 EXP.
  - Turn 6430: Gained 46 EXP after defeating wild Level 6 Zubat. SPARKY is now at Level 9 with 221/148 EXP.
  - Turn 6460: Defeated wild Level 8 Zubat. SPARKY gained 61 EXP (now Level 9 with 282/148 EXP).
  - Turn 6613: Defeated wild Level 10 Zubat. SPARKY gained 38 EXP and reached Level 10!
  - Turn 6825: Used RARE CANDY on SPARKY. He grew to Level 11! We discovered Pikachu learns Quick Attack at Level 16 in Red/Blue (unlike Level 11 in Yellow). Updating target to Level 16.
- Poké Ball & Capture Plan: We currently have 7 Poké Balls, which is plenty for any rare wild encounters inside Mt. Moon.

## B1F Exploration & Mapping Notes:
- None. (Cleaned up as requested by overwatch).

## Unverified 1F Visual Theories:
- Row 21 Platform Boundary: Physically tested and verified solid on Turn 7838. From (10, 22), we attempted to move Up into (10, 21) (TYPE_2889) and collided, resulting in 0 tiles visited. This proves Row 21 is a solid barrier.
- Row 19 Platform Boundary: Physically tested and verified solid on Turn 7850. From (6, 20), we attempted to move Up into (6, 19) (TYPE_2889) and collided, resulting in 0 tiles visited. This proves Row 19 is a solid barrier.

## Route to 1F (5, 5) Ladder:
- Started on Turn 7825 at 1:38 AM PDT.
- Planned Route (Reversed, from NE section):
  1. Go down the NE ladder at (25, 15) on 1F to B1F.
  2. Walk south and west on B1F to the SE section ladder at (13, 27).
  3. Go down to B2F at (15, 27), and walk to the stairs at (26, 15)/(27, 15).
  4. Go up the stairs to the B2F Central Elevated Platform, then take the (21, 17) ladder to B1F.
  5. On B1F, walk west along the horizontal corridor to the NW pocket's ladder at (5, 5).
  6. Go up to (5, 5) on 1F to reach the northwestern area.
- Live Progress Tracking:
  - Navigating Mt. Moon B2F. Currently at (25, 27), heading east to the Eastern Corridor at Column 28, then north to Row 17.