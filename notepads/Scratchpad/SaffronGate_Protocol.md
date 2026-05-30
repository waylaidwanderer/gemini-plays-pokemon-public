# Saffron Gatehouse Passability Testing
- Started: Turn 30089, Friday, May 29, 2026 at 4:04 PM PDT

## Hypothesis
- Saffron Gatehouse has a horizontal axis of entry on the West face (column 12) rather than the South face (row 11) or East face (column 17).
- Alternatively, Saffron City gate remains closed, but we must find the exact trigger tile or coordinate.

## Items in Bag
- Fresh Water (Qty: 1)
- Soda Pop (Qty: 1)
- Lemonade (Qty: 1)
- Total Unique Items: 20/20 (FULL BAG ALERT!)

## Inventory Crisis Plan
- Once we test the gatehouse, if we successfully enter Saffron City, we will immediately navigate to the Saffron Pokémon Center to deposit:
  - Helix Fossil (1)
  - S.S. Ticket (1)
  - Town Map (1)
  - Unused TMs: TM01, TM08, TM11, TM12, TM18, TM19, TM34
- If Saffron remains locked, we will backtrack to Celadon Pokémon Center to perform this PC audit.

## Testing Steps
- [x] Step 1: Speak to NPC at (2, 4) in Map 0_77 (Underground Path Entrance). Verified as not Saffron Gatehouse.
- [x] Step 2: Test Saffron Gatehouse southern face (row 11) on column 15. Result: Collided (solid wall).
- [x] Step 3: Test Saffron Gatehouse eastern face (column 17) on rows 12, 13, 14, 15. Result: Collided (all solid fence).
- [ ] Step 4: Test Saffron Gatehouse western face (column 12) by standing at (11, 10) and walking East (Right) into (12, 10).
- [ ] Step 5: Test Saffron Gatehouse southern face on columns 14 and 16 (Up from row 12).
- [ ] Step 6: Log results.