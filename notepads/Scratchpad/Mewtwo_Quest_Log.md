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
- Current position: (8, 14) facing Down.
- Objective: Navigate back to (3, 11) on 2F West.
- Plan: Return to 1F Southwest via Southwest Ladder 6. However, our testing showed that Southwest Ladder 6 is in an isolated 2-tile pocket at (3, 11) on 2F West. On-foot navigation from the southwest corridors (Row 13-17) to (3, 11) is completely blocked because Row 12 is solid rock (TYPE_2889) and Column 1 Row 11 is solid rock (TYPE_2889). Therefore, we cannot backtrack to Southwest Ladder 6 on foot from (1, 15). We must use a different route or check if there is an alternative way to exit. Wait! If we cannot reach (3, 11) on foot, we can use DIG or escape from here? No, DIG/Escape Rope will take us out of the cave. Is that what we want? Let's check our notes. Yes, we want to go to 1F Northwest, but we can also just walk back to 1F via a different ladder if we can reach one? Wait, can we reach any other ladder from the southwest corridors of 2F West?
  - Let's check: Column 9 is open vertically, so we can walk from (9, 16) to (9, 9) on foot, and then Left to (3, 9). Can we walk from (3, 9) to any other ladder?
  - Wait, (9, 1) is Ladder 5! Can we reach (9, 1) on foot from Column 9?
  - Let's check: (9, 9) to (9, 1) is Column 9. Is Column 9 Row 8 blocked? Yes, (9, 8) is solid rock. So we cannot walk directly Up Column 9 past Row 8.
  - Can we walk from (9, 9) to (12, 9), then Up? But (13, 11) and (16, 13) are blocked, and 2F East is blocked.
  - Let's trace if there is any other way.
  - Wait, let's look at the BFS pathfinder output: it found a path from (1, 15) to (3, 11) using the following route: (1, 15) -> Down 2 -> (1, 17) -> Right 5 -> (6, 17) -> Up -> (6, 16) -> Right 3 -> (9, 16) -> Up 7 -> (9, 9) -> Left 6 -> (3, 9) -> Down -> (3, 10) -> Left -> (2, 10) -> Down -> (2, 11) -> Right -> (3, 11).
  - Wait! This path uses (9, 9) and (3, 9) and (2, 11), which means they ARE connected on foot!
  - This is amazing! Our BFS pathfinder successfully found a complete on-foot path of 26 steps connecting (1, 15) and (3, 11). This mathematically proves that Southwest Ladder 6 is NOT completely isolated from the southwest corridors on foot! We can walk there!
- Corrected Step-by-Step Path:
  - (8, 14) -> Right x2 to (10, 14)
  - (10, 14) -> Down x2 to (10, 16)
  - (10, 16) -> Left to (9, 16)
  - (9, 16) -> Left x3 to (6, 16)
  - (6, 16) -> Down to (6, 17)
  - (6, 17) -> Left x5 to (1, 17)
  - (1, 17) -> Up x2 to (1, 15)
  - (1, 15) -> Right to (2, 15)
  - (2, 15) -> Up x2 to (2, 13)
  - (2, 13) -> Left to (1, 13)
  - (1, 13) -> Up to (1, 12)
  - (1, 12) -> Left to (0, 12) -> Up to (0, 11) (blocked! Wait, let's test if there's any pathway at 1, 13 to 3, 11).
  - Wait, let's execute the path to (9, 16) first in safe chunks.