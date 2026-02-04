# Team Rocket HQ (Mahogany Town)
## Objectives
- **Primary**: Open Boss Door on B2F (Need "Raticate Tail" + Murkrow Voice).
- **Secondary**: Find Hidden Switch (Likely B1F) to disable alarms/open paths.
- **Tertiary**: Catch Murkrow (Location unknown, last seen B2F North?).

## Map Structure (Verified)
- **B1F**: 
  - **West Side**: Traps (Cols 1-5). Stairs to B2F at (3, 14). Exit at (27, 2).
  - **East Side**: NE Room (Computers/Statue), SE Room (Crates).
  - **Connections**: Row 2 (North Corridor), Row 16 (South Corridor).
  - **Fake/Solid Objects**: Warp at (22, 14), Stairs at (3, 2), Stairs at (27, 14).
- **B2F**: 
  - **South Section**: Accessed via B1F (3, 14). Blocked by Wall at Row 12.
  - **North Section**: Inaccessible from South. Contains Sprite (Murkrow/Grunt?).

## Confirmed Secrets & Mechanics
- **Secret Passage**: Found at (9, 4)! Connects NE Room to North Corridor (Row 1).
- **Hidden Stairs**: Stairs at (3, 2) and (3, 6) are currently HIDDEN/FLOOR. Need a switch to reveal them.
- **Traps**: Warp at (22, 14) is a trap. Floor traps warp to entrance.
- **Alarms**: Switch at (19, 11) is OFF (Alarms disabled).
- **B1F Layout**: Row 1 (North Corridor) connects West and East sides.

## Current Strategy
1. **Navigate to NE Room**: Go West to Col 11/12, then North to Row 4, then East to (19, 8).
2. **Systematic Search**: Interact with EVERY computer in the NE Room (Rows 4, 5, 8).
3. **If NE Room fails**: Go to SE Room and check crates.
4. **Goal**: Find hidden switch for B2F North stairs.

## Current Status
- **Location**: B2F SW Corner (3, 14).
- **Action**: Investigating B2F West Wall (Row 12).
- **Goal**: Find a gap in the wall to access the North Section.
- **Hypothesis**: Access to Murkrow is via a gap in Cols 1-3.
- **Next**: Move North to check (1-3, 12). If blocked, reconsider B1F options.
## Verified Map Features
- **B1F West**: (3, 2) and (3, 6) are floors. (3, 16) is safe.
- **B1F East**: (19, 8) Fake Computer (Passage). (22, 14) Solid Fake Warp.
- **Traps**: Floor traps warp to entrance.
- **Hidden Corridor**: Connects Row 2 (NE) to Row 16 (South).
- **South Corridor**: Warp at (5, 15) -> B1F East (25, 2).
- **B2F**: Row 12 Wall is solid. Boss Door at (23, 14) requires Password + Murkrow.

## Current Strategy
1. **Search B1F NE Room**: Inspect all computers for a hidden switch to reveal stairs (likely at 3,2).
    - Current Location: (13, 3).
    - Plan: Sweep Row 4 computers (West to East).
2. **Search B1F SE Room**: Check Crates if NE Room fails.
3. **Locate Murkrow**: B2F North (accessible via hidden stairs).

## Past Accomplishments (Context)
- Disabled Persian Alarms at (19, 11).
- Obtained "Hail Giovanni" and "Raticate Tail".
- Confirmed switch at (19, 11) says "The switch is turned off." This likely means the alarms are disabled.
- Path to NE Room: Blocked by wall at Row 10/11 near (19, 12). Must detour West to Col 8, then North, then East to (19, 8).
- **Discovery**: Computers at (9, 4) and (5, 4) are marked as WALKABLE (TYPE_3fe2) in memory, unlike others (TYPE_2889). Likely secret passages!
- **Correction**: (5, 4) is blocked by wall at Col 6.
- **Plan**: Entering secret passage at (9, 4) (Walkable Computer).
- **Discovery**: Column 9 (Rows 1-4) appears to be a secret corridor connecting the computer room to the North.
- **Hypothesis**: The hidden stairs at (3, 2) and (3, 6) only appear when the Switch at (19, 11) is ON (or in the other state).
- **Plan**: Toggle the switch at (19, 11) and check (3, 2) again.