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
- To clear the blockage, we must stand adjacent to the item at (5, 15) facing Left, and press 'A' to collect the item. Once collected, the tile (4, 15) will become passable (TYPE_3fe2), opening up the entire western corridor system on foot!
- We are executing ['Left', 'A'] on Turn 115671 to collect the item and clear the path.