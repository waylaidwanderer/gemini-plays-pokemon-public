# Celadon City Location Records (Map 0_6)
- **Map Transition**: Entered Celadon City (Map 0_6) from Route 7 (Map 0_18) on Turn 29595, appearing at (49, 10).
- **Warp Connection**: Seamless connection to Route 7 is located at (49, 10) on the eastern boundary of Celadon City.
- **Physical Landmarks**:
  - The floor pattern is yellow/orange checkered pavement.
  - Trees (TYPE_2889) line the borders of the pathway at (49, 12)-(49, 14) and (49, 6)-(49, 9).
  - Walkable pavement (TYPE_3fe2) extends westward through row 10 and row 11: (48, 10), (47, 10), (46, 10), (45, 10) and (48, 11), (47, 11), (46, 11), (45, 11).
- **Celadon Pokémon Center (Map 0_133)**: Door entrance at (41, 9) on Map 0_6 warps to (3, 7) on Map 0_133, facing Up.
- **Celadon Mansion (Condominiums) 1F (Map 0_128)**: Entrance door located at (24, 9) on Map 0_6 warps player to (4, 11) on Map 0_128, facing Up. Red carpet exit warp is at (5, 11).
- **NPCs & Objects**:
  - Wandering Manager Grandma NPC (SPRITE_4081) resides behind the counter (row 8), moving horizontally between columns 0 and 7.
  - Snorlax Doll on table/floor: Located at (0, 8) in the room.

## Celadon Department Store Purchasing & Testing Protocol
- **Objective 1: Map the Celadon Department Store Floor-by-Floor**
  - Locate the Celadon Department Store on Map 0_6 (traditionally a large building in the west or center of Celadon City).
  - Define map markers for the entrance door and register its internal Map ID.
  - For each floor (1F to Rooftop):
    - Document the Floor Name, NPC names, and dialogue scripts.
    - Document all shop inventories, item names, and individual prices in `Locations/CeladonCity`.
- **Objective 2: Purchase Saffron Guard Drinks & Verification**
  - **Budget Allocation**: ¥1000 total.
  - Go to the Rooftop Square Vending Machines.
  - Purchase exactly:
    - 1x Fresh Water (¥200)
    - 1x Soda Pop (¥300)
    - 1x Lemonade (¥350)
  - Verify that each drink resides in our bag with the correct quantities.
- **Objective 3: Saffron Gatehouse Passability Testing Protocol**
  - **Hypothesis**: Giving a drink to any Saffron Gatehouse guard (Route 8, Route 7, Route 5, Route 6) will remove the soft-block and grant entry to Saffron City.
  - **Testing Steps**:
    1. Travel to the Route 7 Gatehouse (Map 0_77) or Route 8 Gatehouse.
    2. Save before speaking to the guard.
    3. Stand adjacent to the guard, face them, and press 'A'.
    4. Observe the exact dialogue:
       - If the guard detects a drink in our bag, record which drink is removed (or if all are options, or if any drink works).
       - Record if Saffron City access is successfully unlocked.
       - Document this empirical "proof of work" with the turn numbers and exact dialogue script.