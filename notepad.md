### Underground Path (Map 3_56) - Turn 51444
### Status
- **Location:** (16, 12) -> Moving to North East Corner (16, 2).
- **Goal:** Investigate (17, 2) which appears to be stairs/door. Access Item Ball from the North.

### Map Analysis
- **East/West Split:** Column 8 is a wall (Row 1-11), separating West (Grunt) from East (Item/Stairs). Connection is at Row 12.
- **Item Room Access:** The item at (13, 9) is enclosed by walls at Row 11 (South) and Column 15 (East). Must enter from the North (Row 1-3).
- **Key Tile:** (17, 2) is TYPE_8564, likely the entrance to the Director's area.

### Plan
1. Go North to (16, 2).
2. Inspect/Enter (17, 2).
3. If not the right way, loop West/South to get Item at (13, 9).
### Secret Room (Map 3_55) - Turn 51461
- **Location:** (13, 1).
- **NPC:** Sprite at (14, 1) / (14, 0).
- **Issue:** The NPC has NO COLLISION. I can walk on top of him (Tile 14, 1). Interaction from South (14, 2) and On Top (14, 1) failed.
- **Hypothesis:** Trying from the side (13, 1) -> Facing Right. If this fails, he might be a glitched sprite or requires a specific trigger (or I already got the key and didn't notice? No, key items list doesn't show it).
- **Inventory Check:** Key Items: BASEMENT KEY, BICYCLE, COIN CASE, OLD ROD, SQUIRTBOTTLE. No CARD KEY.