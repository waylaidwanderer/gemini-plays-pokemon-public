# Victory Road Puzzle Mechanics & Master Log

## Floor 1F Puzzle System (SOLVED)
- Boulder at (5, 15) pushed via lower highway (row 16) to eastern corridor (14, 14) -> (16, 12) -> (17, 12) -> onto Switch (17, 13).
- Lowers shutters at (5, 13) and (7, 7), unlocking access to 2F Ladder at (1, 1).

## Floor 2F Master Solution (SOLVED & VERIFIED)

### Master Progression Route:
1. **Phase 1 (Boulder 2 -> Switch 1 @ (1, 16)) [SOLVED & VERIFIED Turn 23674-23676]**:
   - Initial position: Boulder 2 at (4, 14).
   - Verified Push Sequence: (4, 14) -> (3, 14) -> (3, 15) -> (3, 16) -> (2, 16) -> (1, 16) [Switch Plate 1].
   - **Result**: Shutter 1 at (5, 10) AND Shutter 3 at (21, 15) are OPEN!

2. **Phase 2 (Traverse Shutter 3 to SE Ladder @ (25, 14)) [SOLVED & VERIFIED Turn 23736]**:
   - Route: From (5, 8) in Central Corridor -> (13, 8) -> (13, 12) -> (20, 12) -> (20, 14) -> (21, 14) -> stepped South into Shutter 3 at (21, 15)!
   - Walk along row 16: (21, 16) -> (25, 16) -> (25, 14) to ascend SE Ladder to Victory Road 3F!

## Battle Escape Protocol (Standardized)
- Turn 1: Dismiss intro text with `['A', 'B']`.
- Turn 2: Select RUN from battle menu with `['Down', 'Right', 'A']`.
- Turn 3: Clear "Got away safely!" textbox with `['A']` or `['B']`.

## Verified Collision Truths (2F)
- (19, 11) is a solid south-facing cliff wall / ledge; northward passage from (19, 12) into (19, 11) is blocked.
- (5, 2) is a solid rock obstacle blocking northward boulder movement from (5, 3).
- (21, 13) is occupied by a defeated Juggler NPC (solid obstacle; bypass via column 20).
- (23, 14) is a west-facing ledge (one-way descent from SE platform).

## Floor 3F Master Solution & Testing Plan (Active Exploration)
- **Sector Survey Status**:
  - Upper Terrace (rows 0-1, cols 6-25): Fully surveyed. Connects NW Ladder (4, 1), Western Bridge (cols 6-7), and NE Plateau (cols 21-25).
  - Western Bridge & SW Sector: Bridge reaches (6, 6). Switch Plate at (3, 5) and Item Ball at (7, 7) identified.
  - North Central Chamber: Cooltrainer♂ at (13, 3), Shutter at (17, 5).
  - Southeast & South Sectors: Survey in progress from Ladder (23, 7) southwards.
- **Active Hypotheses**:
  1. Switch Plate at (3, 5) or another local switch lowers Shutter at (17, 5).
  2. Southern chamber contains a boulder and pit leading down to 2F to unlock the exit shutter.
- **Next Testing Steps**:
  1. Survey SE and Southern sector from (23, 7) south to locate all boulders, pits, and switches.
  2. Document exact coordinates of any pits and boulders before pushing.
## Floor 3F Topology & Progression Route (Verified Turn 23847)
- 3F Section A (Terrace & Hallways): Connected via NW Ladder (4, 1) to 2F (1, 1).
- 3F Section B (Pit Chamber): Connected via SE Ladder (26, 8) to 2F SE Ladder (25, 14).
- Master Navigation Route:
  1. From 3F (23, 7), traverse North to (23, 0) and West to (4, 1).
  2. Take NW Ladder (4, 1) down to 2F (1, 1).
  3. On 2F (where Shutters 1 and 3 are open), walk: (1, 1) -> (5, 8) -> (5, 10) [Open Shutter 1] -> (13, 12) -> (21, 14) -> (21, 15) [Open Shutter 3] -> (25, 16) -> (25, 14).
  4. Ascend ladder at (25, 14) to 3F (26, 8) inside Pit Chamber.
  5. Walk to (21, 15) and push Boulder (22, 15) East into Hole (23, 15).
  6. Drop through Hole (23, 15) down to 2F to open exit shutter!