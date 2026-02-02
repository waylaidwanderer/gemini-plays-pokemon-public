# Team Rocket HQ (Mahogany Town)
## Objectives
- Find Shutter Switch on B1F.
- Get Murkrow (requires Shutter open).
- Open Boss Door on B2F (requires Murkrow).

## Status
- **Passwords Obtained**:
  1. "Hail Giovanni" (Scientist Jed/Computer).
  2. "SLOWPOKETAIL" (Grunt at 20, 7).
- **Grunt Hint**: "But it's useless unless you have..." (Text looped). Likely implies need for 2nd password or Boss interactions.
- **Plan**: Head to B2F Boss Door immediately.
- **Murkrow**: Likely irrelevant now that I have the password.
- **Path**: Exit computer area via Col 19 gap, then to stairs at (27, 14).
- **Oath Text**: "Exploit POKéMON for profit!" (Both machines).

## Exploration Log (Map 3_51)
- **Tile Mechanics**:
  - `TYPE_1fdc`: Solid (Machine/Oath?).
  - `TYPE_2889`/`TYPE_63e2`: Solid (Walls/Desks/Plants).
  - `TYPE_3fe2`: Walkable Floor.
  - **Barriers**:
    - Row 4 (East): Solid Wall from Col 18 to 27. Gap at Col 16-17.
    - Row 11 (West): Blocked by desks (Cols 1-13). No gap at Col 10 (Correction).
    - Row 12 (West): Blocked by plants at Col 2.
- **Cleared Areas (Nothing Found)**:
  - East Wing (Rows 6, 10), North Wall (Row 0), West Wing (Row 11).
  - Computers: Row 11 (Cols 1, 8-13), Row 10 (Cols 20-25).
  - Specifics: (4-7, 13) Oath (Text only), (1, 11) Wall/Dead End.
  - West Strip (Col 1): Fully explored. Dead End.
- **Findings**:
  - Items: X Special (3, 13), Protein (1, 12).
  - Oath Carpet: Row 13 (Cols 4-7).
- Target: NE Area (Murkrow Search). SE Computers (Re-verify).
- Suspect: Hidden switch might be in the SE area or on a computer I missed in the East.
- (15, 16): Inspected (Solid/No Interaction) - Confirmed Shutter/Wall.
- (15, 11): Suspected Shutter/Wall (Type 63e2).
- (14, 11): Locked Shutter (Verified non-interactive/Locked).
- (15, 16): Suspected Shutter.
- Note: Displaced Murkrow at (28, 9). It fled. Tracking it down (likely North/West).
- **Grunt Info**: Grunt at (5, 14) is useless (gives bad password "Raticate Tail").
- (1, 11): Wall (Dead End).
- Plan: Investigate "Oath" area (Row 13, Cols 4-7) and objects at Row 12.
- Check West Room for Murkrow.
- **Map Update**: Continuous barrier of plants/walls at Column 2 (Rows 11-15). Access to West Strip is only via Row 16 or Row 10 (if gap exists, but Row 10 seemed blocked earlier).
- Note: Confirmed no stairs at (3, 14). Summary error.
- West Strip (Col 1): Confirmed Dead End. Blocked at (1, 11).
- Plan: Search South-East Area (Rows 12-16, Cols 20-29) for Murkrow.
- Location: Moving to SE Area.
- (4, 13): Oath (Text only).
- (5, 13): Inaccessible (Blocked by Grunt at 5, 14 and walls).
- (6, 13): Oath (Text only).
- (7, 13): Oath (Text only).
- (15, 10): Wall/Shutter (Solid).
- (16, 0): Checked (Wall/Terminal?).
- (18, 12-13): Wall (Solid). Passage to East Wing at Row 13 (Gap at Col 15).
- (27, 14): Stairs to B2F (Confirmed).
- (28, 16): Checked (Empty).
- (20-28, 16): Checked (Empty).
- Hypothesis: Murkrow might be trapped behind the shutter in the NW area. To get it, I must find the switch first.
- Hypothesis: Check the Statues/machines at (12, 1) again?
- **Tool Status**: `bfs_navigate` confirmed unreliable in this area (Turn 24369-24372). Using manual pathing.
- **Search Plan**:
  1. Check West Murkrow Spawn at (3, 12).
  2. If empty, return to NE Spawn at (28, 9).
  3. Investigate "Sealed Area" hypothesis (NW Room seems inaccessible except via Shutter).

- **Current Hypothesis**: Murkrow location cycles between NE (28,9) and West (3,12). Interaction physics unclear.
- (15, 10): Checking potential Shutter/Door.
- **Interaction Attempt**: Stepped OFF Murkrow at (28, 11) to (28, 12), facing UP, pressing A.
- **Interaction Attempt**: Moving Left to (27, 11), facing Right to interact.
- **Ghost Bird Conclusion**: Murkrow at (28, 11) is non-interactive/non-solid. Abandoning interaction attempts. Focusing on finding Shutter Switch or "Real" Murkrow elsewhere.
- **Strategy Shift**: Testing "Raticate Tail" password on B2F Boss Door. Grunt at (5, 14) provided it. Hypothesis: Murkrow hunt might be skippable if this password works.
- **Observation**: Rival Silver spotted at (24, 13) and Grunt at (25, 13) on B2F. They appear static.
- **Action**: Attempting to open Boss Door at (23, 14) with "Raticate Tail" (Player Hypothesis).
- **Anomaly**: Rival Silver at (24, 13) disappeared when player stepped onto the tile. Possible glitch or cutscene skip?
- **Action**: Talking to Grunt at (25, 13) to see if he triggers the door or battle.
- **Result**: "Raticate Tail" password FAILED. Boss Door remains locked.
- **Next Step**: Returning to B1F to investigate Persian Statues at (12, 1) and (13, 1).
- **Oath Machine**: Investigating text at (6, 13).
- **Oath Text 1**: "Exploit POKéMON for profit!" (Machine at 6, 13).
- **Computer Sweep**: Computers at 20-22 checked (no result).
- **Plan**: Exploring area behind computers (Rows 7-9).
- **Oath Text**: "Exploit POKéMON for profit!" (Both machines).
- **Murkrow Anomaly**: Murkrow at (3, 12) is non-solid/non-interactive (Ghost).
- **Door Status**: Locked. Password "SLOWPOKETAIL" alone didn't work.
- **Silver**: Standing at (24, 12). Attempting to talk to him.
- **Grunt**: Standing at (25, 13).
- **Hypothesis**: "Useless unless you have..." likely refers to the Boss's Voice, which Murkrow mimics.
- **Plan**: If Silver/Grunt don't open the door, I MUST solve the Ghost Murkrow puzzle.