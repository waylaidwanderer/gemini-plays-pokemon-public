# Saffron Gatehouse Passability Testing
- Started: Turn 30089, Friday, May 29, 2026 at 4:04 PM PDT

## Hypothesis
- Saffron Gatehouse has a horizontal axis of entry on the West face (column 12) rather than the South face (row 11) or East face (column 17). (VERIFIED: Entering (12, 10) from (11, 10) on Route 7 successfully warps inside).
- Giving a drink to any Saffron Gatehouse guard (Route 8, Route 7, Route 5, Route 6) will remove the soft-block and grant entry to Saffron City. (VERIFIED: Guard took Fresh Water on Turn 30198).

## Items in Bag
- Soda Pop (Qty: 1)
- Lemonade (Qty: 1)
- Total Unique Items: 19/20 (Inventory cleared by 1 slot!)

## Inventory Crisis Plan
- Saffron City is officially unlocked! We are heading directly to the Saffron Pokémon Center (Map 0_114 or equivalent) to use the PC and deposit:
  - Helix Fossil (1)
  - S.S. Ticket (1)
  - Town Map (1)
  - Unused TMs: TM01, TM08, TM11, TM12, TM18, TM19, TM34
- This will free up 10 slots and resolve our 19/20 full bag status.

## Testing Steps
- [x] Step 1: Speak to NPC at (2, 4) in Map 0_77 (Underground Path Entrance). Verified as not Saffron Gatehouse.
- [x] Step 2: Test Saffron Gatehouse southern face (row 11) on column 15. Result: Collided (solid wall).
- [x] Step 3: Test Saffron Gatehouse eastern face (column 17) on rows 12, 13, 14, 15. Result: Collided (all solid fence).
- [x] Step 4: Test Saffron Gatehouse western face (column 12) by standing at (11, 10) and walking East (Right) into (12, 10). Result: Warped successfully into Saffron Gatehouse (Map 0_76) on Turn 30191.
- [x] Step 5: Test Saffron Gatehouse passability. Result: Attempting to walk to Saffron City triggered Guard interception at (3, 4). Guard took our FRESH WATER from our bag on Turn 30198, cleared Saffron City passability region-wide, and told us we can pass. Verified that Fresh Water is consumed first when multiple drinks are held.
- [ ] Step 6: Walk East to Saffron City and locate Pokémon Center.