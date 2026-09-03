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

## Floor 3F Topology & Progression Route (Verified Turns 23847-23862)

## Floor 3F Progression Strategy
1. Ascend to 3F via SE Ladder at (25, 14) (arrival at 3F (23, 7)).
2. Explore upper northern sector and solve 3F Boulder switch puzzle to open barriers.
3. Reach southern sector containing Pit Boulder (22, 15) and Hole (23, 15).
4. Push Pit Boulder East into Hole (23, 15).
5. Jump down Hole (23, 15) to 2F to activate switch and unlock exit route to Indigo Plateau.

## Floor 3F Boulder 1 -> Switch Plate Master Route (VERIFIED ARCHITECTURE)
- Corridor Row Structure: Row 0 is the northern boundary row; Row 1 is the open bypass row.
- Bridge Location: Elevated bridge spans columns 6-7 from row 1 to row 6.
- CRITICAL MECHANIC: Above (7, 0) is row -1 (solid wall); therefore, to push Boulder South down the bridge, Boulder MUST travel along ROW 1 so player can stand at (7, 0) on Row 0 and push South into (7, 1)!
- Master Push Sequence from default Boulder 1 at (22, 3):
  1. Stand at (23, 3) -> Push West to (21, 3).
  2. Walk to (21, 4) -> Push North 2 times: (21, 3) -> (21, 2) -> (21, 1). (STOP at Row 1!).
  3. Walk around to (22, 1): (21, 3) -> (21, 4) -> (22, 4) -> (22, 1).
  4. Push West along ROW 1 across cols 21 down to 7: (21, 1) -> (20, 1) -> ... -> (7, 1).
  5. Step from (8, 1) -> (8, 0) -> (7, 0) to face South above Boulder at (7, 1).
  6. Push South down column 7 across bridge to row 6!
  7. Push Boulder from bridge exit onto Switch Plate at (3, 5).