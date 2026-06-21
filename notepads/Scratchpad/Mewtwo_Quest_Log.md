# Mewtwo Quest Log (Post-Game)
- Started: Turn 111394
- Goal: Enter Cerulean Cave and catch Mewtwo.

## Current Status & Progression
- Currently standing on 1F at (17, 14) on foot.

## Active Hypothesis on 2F West Topology
- Hypothesized Blockages on 2F West:
  - Row 8: Columns 3, 9, 10, 11, 12 verified blocked. Columns 4, 5, 6, 7, 8 are verified blocked on foot (Turn 115147-115167).
  - Column 1 Row 11 (1, 11) is physically verified blocked on foot (Turn 115431).
  - Column 1 Row 10 (1, 10) is physically verified blocked on foot (Turn 115435-115436).
  - Column 2 Row 12 (2, 12) is physically verified blocked on foot (Turn 115454: standing at (2, 11), pressed Down, bumped, remained at (2, 11)).

## Master Routing Plan
- We have completely disproven the 1F Northwest on-foot shortcut by physically testing (4, 1), (4, 2), and (5, 3) and verifying they are solid rock walls (Turns 115518, 115542, 115543).
- We have successfully returned to the central platform at (17, 14) on foot.
- Next Steps:
  1. Walk Down the stairs at (17, 15) to reach (17, 16) on the ground floor.
  2. Walk Left along Row 17 on the ground floor all the way to (1, 14).
  3. Walk Up the wooden stairs at (1, 13) to reach (1, 12) on the elevated southwest plateau.
  4. Climb Southwest Ladder 6 at (3, 11) to reach 2F West.
  5. On 2F West, test if the southwest region (Columns 0-7, Rows 10-13) has an open on-foot path to Column 0 Row 5 (0, 5), allowing us to reach the Northwest Ladder (1, 3).
  6. Document all results with exact turns and outcomes.
## Item Blockage & Solution (Turn 115671)
- We have discovered that the pathway from (5, 15) to (1, 13) is physically blocked at (4, 15) by a solid, overworld item ball sprite.
- In Gen 1, overworld item balls are solid obstacles that prevent walking.
- To clear the blockage, we stand adjacent to the item at (5, 15) facing Left, and press 'A' to collect the item.
- Turn 115682: Pressed A. Successfully collected the ULTRA BALL at (4, 15)! The tile (4, 15) has now changed to TYPE_3fe2 (passable floor).
- This opens up the entire southwest corridor network on 2F West!

## Southwestern Corridor Navigation (Turn 115683)
- Path from (5, 15) to (1, 13) on foot:
  - From (5, 15), walk Left -> (4, 15)
  - Walk Down -> (4, 16)
  - Walk Down -> (4, 17)
  - Walk Left -> (3, 17)
  - Walk Left -> (2, 17)
  - Walk Left -> (1, 17)
  - Walk Up -> (1, 16)
  - Walk Up -> (1, 15)
  - Walk Right -> (2, 15)
  - Walk Up -> (2, 14)
  - Walk Up -> (2, 13)
  - Walk Left -> (1, 13)
- We will execute this in chunks to avoid inputting movement commands during wild encounters.
- Chunk 1: ['Left', 'Down', 'Down'] to reach (4, 17).
### Turn 115749 Verification of 2F West Blockage
- Stood at (1, 7) on 2F West facing Up.
- Visually and physically verified that Column 1 Row 6 (1, 6) is indeed TYPE_2889 (solid rock wall).
- The ladder at (1, 3) is clearly visible directly to the north, but (1, 6) is solid rock, completely blocking direct vertical access.
- Row 6 is solid rock (TYPE_2889) at (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6).
- Column 4 Row 7 (4, 7) is solid rock (TYPE_2889).
- Row 8 is solid rock (TYPE_2889) from Column 2 to Column 6.
- This creates an airtight pocket at (1, 7), (2, 7), (3, 7) that is bounded on all sides by rock walls, except for the entrance at (1, 8).
- This definitively proves that there is NO on-foot path from Southwest Ladder 6 at (3, 11) to the Northwest Ladder at (1, 3) on 2F West!
- Since 2F West is completely blocked from reaching (1, 3) on foot from the south, we must find another way.
## Returning to Southwest Ladder 6 (Turn 115824)
- Current position: (9, 16) facing Down.
- Objective: Navigate back to (3, 11) on 2F West.
- Plan: Use the verified corridor path via Row 16 and Row 17, and then the southwest corridor to reach Southwest Ladder 6.
- Step-by-Step Path from (2, 13) to (3, 11):
  - (2, 13) -> Down x2 to (2, 15)
  - (2, 15) -> Left to (1, 15)
  - (1, 15) -> Down x2 to (1, 17)
  - (1, 17) -> Right x5 to (6, 17)
  - (6, 17) -> Up to (6, 16)
  - (6, 16) -> Right x3 to (9, 16)
  - (9, 16) -> Up x7 to (9, 9)
  - (9, 9) -> Left x6 to (3, 9)
  - (3, 9) -> Down x2 to (3, 11) (ladder)
- We will execute this in safe chunks.
- Chunk 1: ['Left', 'Left', 'Left', 'Down'] to reach (6, 17).
- Turn 115926: Reached (1, 15). Backtracking along the southwest corridors on 2F West to reach Southwest Ladder 6 at (3, 11). Walking to (6, 17) first.
- Turn 115995: Safely arrived back at (9, 16) facing Down. Verified the local grid and confirmed that Column 9 Row 15 is indeed solid (TYPE_2889), and Row 16 has a blockage at (12, 16) of TYPE_2889. The path from (13, 17) back to (9, 16) was successfully navigated via: (13, 17) -> (12, 17) -> (11, 17) -> (11, 16) -> (10, 16) -> (9, 16).
- Next Plan: Navigate from (1, 17) back to (9, 16), then up to (9, 9), left to (3, 9), and down to Southwest Ladder 6 at (3, 11).
  - Verified Constraint: We verified on Turn 116019 that Column 3 Row 13 (3, 13) is a solid rock wall (TYPE_2889) on 2F West, which blocks direct access to (3, 11) from the south on foot via Column 2. Thus, the southwest corridor is a dead end and we must backtrack all the way.
  - Step-by-Step Path: (1, 17) -> Right x5 to (6, 17) -> Up to (6, 16) -> Right x3 to (9, 16) -> Up x7 to (9, 9) -> Left x6 to (3, 9) -> Down x2 to (3, 11).
  - Executing first chunk of path: ['Right', 'Right', 'Right', 'Right', 'Right', 'Up', 'Right'] to reach (7, 16).