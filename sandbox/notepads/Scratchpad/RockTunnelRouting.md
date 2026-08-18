# Rock Tunnel Routing & Traversal Plan

## Active Progression Route (Rock Tunnel B1F -> Ladder 4 -> 1F -> Lavender Town)
1. On B1F (current): Walk East to col 20 at (20, 24), then North along col 20 to row 16.
2. Follow Central-East corridor east to cols 32-33, then North through rows 12-13 to the North Highway (rows 2-5).
3. Follow North Highway west to Ladder 4 at (5, 3).
4. Step onto Ladder 4 at (5, 3) to ascend to Rock Tunnel 1F.
5. On 1F: Traverse to the South Exit at (37, 17) and exit to Route 10 South.
6. Walk south along Route 10 South directly into Lavender Town and heal at the Pokémon Center!

## Battle Menu State Machine Mechanics
- Main Battle Menu:
  `FIGHT (top-left)    PKMN (top-right)`
  `ITEM (bottom-left)   RUN (bottom-right)`
  (Cursor initializes on FIGHT).
- To select Move 1 (Tackle): Send `["A", "A"]` (First A enters Move Menu, Second A selects Move 1).
- To select Move 4 (Bubblebeam): Send `["A", "Down", "Down", "Down", "A"]` (First A enters Move Menu, 3 Downs move to Move 4, Second A selects Bubblebeam).
- Rule: NEVER press `Down` before pressing `A` to enter the Move Menu, otherwise cursor moves to ITEM and opens Bag.
