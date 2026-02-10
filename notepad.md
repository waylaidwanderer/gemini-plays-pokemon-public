# Team Rocket HQ - Murkrow Puzzle

## STATUS: CHECKING SHUTTER
**Goal**: Verify Shutter state at (15, 10).
**Prediction**: Shutter is likely CLOSED (`TYPE_2889` Wall).
**Correction**: Path from (19, 9) to Switch is blocked by Wall at (19, 10). Must enter from West (Row 11).

## Plan
1. **Check Shutter**: Move Down from (15, 9).
2. **If Blocked (Closed)**:
   - Move Left to Col 7 or 8 (Gaps in Row 10).
   - Enter Trap Zone (Row 11).
   - Navigate East to Switch at (19, 11).
   - Toggle Switch.
3. **Reset**:
   - Exit via (27, 2) to reset Murkrow.
4. **Execute**: "Jed Sandwich" Strategy.