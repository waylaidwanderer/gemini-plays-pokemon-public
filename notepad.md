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
### Secret Room (Map 3_55) - Turn 51466
- **Location:** (13, 3).
- **Status:** The "Director" at (14, 1) is a TILE, not an NPC. `stun_npc` confirmed no NPC exists there. I was trying to talk to the floor.
- **Plan:**
    1. Check the rest of this room (crates, corners).
    2. If nothing, return to Map 3_56 (Underground Path).
    3. The path split at Map 3_56 (x=8 wall). I might need to access the *other* side of that wall (the Item Ball side) to find the true entrance or the key.
- **Inventory Check:** Still no Card Key.