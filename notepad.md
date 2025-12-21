# Gem's Journey in Pokémon Crystal

## Current Strategy
- **Primary Goal:** Catch Red Gyarados.
- **Secondary Goal:** Explore Lake of Rage.
- **Navigation:** Exit Goldenrod Dept Store -> Fly to Lake of Rage.

## Goldenrod Dept Store Notes
- **Directory:**
    - **B1F:** Item (Ether), Unreachable Item (14, 2), Burn Heal (6, 3).
        - Layout: Left side (Elevator) isolated from Right side.
        - Hypothesis: Right side accessible via Goldenrod Underground.
    - **1F:** Receptionist, Exit. Stairs (15,0) lead to 2F (not B1F).
    - **2F:** Items (Balls, Potions, Mail). Bought 10 Great Balls.
    - **3F-4F:** Stat boosters, Vitamins.
    - **5F:** TMs (Punches, Headbutt).
    - **6F:** Vending Machines, Roof.

## World Knowledge & Discoveries
- **Lake of Rage:** Gyarados rampage. Fishing Guru wants Magikarp.
- **Mahogany Town:** Mart has locked stairs.
- **Quest Log:**
    - Bug Catching Contest active.
    - Failed to deliver mail to Fisher (Route 31).

## Mechanics Log
- **Fly Map:** Cursor wraps. Navigation is non-linear.
- **Mail:** Forgery requires original data.
- **PC:** Cannot deposit mail-holding Pokemon.

## Global Tile Mechanics
- FLOOR: Traversable. Standard movement.
- WALL: Impassable.
- WARP_CARPET_DOWN/UP: Traversable. Triggers warp to adjacent map.
- STAIRS: Traversable. Warps to another floor.
- Fly Map Confusion: Solved (Navigation: Goldenrod -> Up -> Ecruteak -> Right -> Mahogany -> Up -> Lake of Rage).
- Fly Map Confusion: 'Right' from Olivine did not change destination (Stayed on Olivine). Trying 'Left'. Note: Ecruteak -> Right -> Olivine in previous turn suggests inverted controls or wrapping.