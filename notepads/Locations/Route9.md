# Route 9 Geographical Records (Map 0_20)

## Map Transitions & Connections:
- **West Exit**: Connects back to Cerulean City (Map 0_3) at Column 0, Row 8 (spawns at (39, 16) on Map 0_3). Fully verified on Turn 19934.
- **East Exit**: Leads towards Route 10 and Rock Tunnel.

## Structural Layout & Obstacles:
- **Corridor entrance**: A narrow east-west pathway between Row 7 and Row 10 (which are bounded by solid rock walls, TYPE_2889).
- **Cuttable Bush**: Located at (5, 8) (TYPE_5519). This bush completely blocks the pathway to the east. We must use CUT on (5, 8) to proceed.
- **Signpost/Rock**: Located at (4, 9) (TYPE_2889), which blocks Row 9, forcing the player to use CUT at (5, 8).

## Wild Encounters Database & SPARKY Training Log:
- **SPARKY Grinding Goal**: Train SPARKY (Pikachu) to Lv 24.
- **Active Grinding Log**:
  - Starting Level: 22 (Turn 20126)
  - Current Level: 23 (Turn 20588)
  - EXP gained on Route 9: 0 EXP
  - Grinding Sessions:
    - Session 1 (Start Turn 20215): Grinding on Row 12 (Columns 10-16) grass patch. Lead: SPARKY (PIKACHU) Lv 22, HP 52/52.
    - Session 2 (Start Turn 20282): Grinded on Row 14 (Columns 29-43) grass patch. Met and defeated Hiker trainer at (45, 15) on Turn 20334.
    - Session 3 (Start Turn 20424): Defeated Bug Catcher at (40, 8) on Turn 20415 and Hiker at (43, 3) on Turn 20459.
    - Encounters Tracked: none yet.

| Species | Levels | Encounter Count | Matchup Strategy | Notes & Verification |
|---------|--------|-----------------|------------------|----------------------|
| Rattata | -      | 0               | Neutral EXP      | Not encountered yet  |
| Spearow | -      | 0               | Super-effective  | Not encountered yet  |
| Ekans   | -      | 0               | Neutral EXP      | Not encountered yet  |
| Sandshrew | -    | 0               | Avoid with Sparky| Not encountered yet  |

## Trainer Matchups & Battle History:
- **Trainer 1**: Jr. Trainer ♀ at (13, 10)
  - Team: ODDISH Lv 18, BELLSPROUT Lv 18, ODDISH Lv 18, BELLSPROUT Lv 18
  - Matchup: SPARKY (PIKACHU) Lv 22 vs. ODDISH Lv 18 (Won), SPARKY (PIKACHU) Lv 22 vs. BELLSPROUT Lv 18 (Slept Sparky), BIRBIE vs. BELLSPROUT Lv 18 (Slept Birbie), GEMMY Lv 30 vs. BELLSPROUT Lv 18 (Won), GEMMY Lv 30 vs. ODDISH Lv 18 (Won), GEMMY Lv 30 vs. BELLSPROUT Lv 18 (Won)
  - Battle Status: Defeated on Turn 20048
- **Verified Corridor: Column 19, Row 13 (Verified on Turn 20238)**:
  - This tile is a completely flat, bidirectional passage connecting the upper grass strip (Row 12) and the lower pathway (Row 14).
  - Test proof: We successfully walked Down from (15, 12) to (19, 14) through (19, 13) on Turn 20227, and successfully walked back Up from (19, 14) to (19, 12) through (19, 13) on Turn 20233. This proves there are no invisible colliders or one-way triggers blocking movement in either direction.
- **Trainer 2**: Bug Catcher at (40, 8)
  - Team: CATERPIE Lv 20, WEEDLE Lv 20, VENONAT Lv 20
  - Battle Status: Defeated on Turn 20415
- **Trainer 3**: Hiker at (43, 3)
  - Team: GEODUDE Lv 20, MACHOP Lv 20, GEODUDE Lv 20
  - Battle Status: Defeated on Turn 20459