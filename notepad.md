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
- Fly Map Navigation Hypothesis: Controls might be inverted (Right moved West to Olivine from Ecruteak). Plan: Reset to Goldenrod, go Up to Ecruteak, then try Left to go East.
- Fly Map Logic: 'Up' from Olivine wraps to New Bark Town. 'Left' from Ecruteak goes to Olivine. 
- Path Plan: From New Bark, 'Left' -> Cherrygrove -> 'Left' -> Violet -> 'Up' -> Ecruteak -> 'Right' -> Mahogany -> 'Up' -> Lake of Rage.
- Current Action: Pressing Left x2 to reach Violet City.
- Fly Map Logic Refined: 'Left' moves West (Goldenrod -> Ecruteak -> Left = Olivine). 'Up' from Olivine wraps to New Bark.
- Hypothesis: Movement is point-to-point including Routes. Ecruteak -> Right -> Route 42 -> Right -> Mahogany.
- Plan: Reset to Goldenrod. Up (Ecruteak), Right (Route 42?), Right (Mahogany?). Verifying destination.
- Fly Map Navigation Retry: Map was closed. Re-opening ('A'). From Goldenrod (assumed start): Up -> Ecruteak. Right -> ? (Checking if East).
- Fly Map Navigation: At Cherrygrove. 'Up' moved New Bark -> Cherrygrove. Testing 'Left' to reach Violet City (West).
- Goal: Reach Ecruteak -> Mahogany -> Lake of Rage.
- Fly Map Experiment: 'Left' from Cherrygrove did nothing. 'Up' from New Bark went to Cherrygrove.
- Hypothesis: 'Up' cycles forward through the town list (New Bark -> Cherrygrove -> Violet -> ...).
- Action: Pressing 'Up' x3 to verify sequence (Expected: Violet -> Azalea -> Goldenrod).
- Fly Map Logic Confirmed: 'Up' cycles through the town list in standard Johto order (New Bark -> Cherrygrove -> Violet -> Azalea -> Goldenrod).
- Prediction: Goldenrod -> Ecruteak -> Olivine -> Cianwood -> Mahogany -> Lake of Rage.
- Action: Pressing 'Up' x5 to reach Lake of Rage from Goldenrod.
- Arrived at Lake of Rage.
- Phone Call (Wade): Bug-Catching Contest is at National Park today.
- Plan: Talk to Gramps at (20, 26), then Surf to find Red Gyarados.
- Battle Strat: Use Muscle's Rock Smash (Not Very Effective) to weaken Gyarados safely.
- Gramps Dialogue: "The GYARADOS are angry! It's a bad omen!"
- Next Step: Surf onto the lake and locate the Red Gyarados.
- Gyarados Battle Plan:
  1. Lead with Muscle (Machoke, Lvl 42).
  2. Use Rock Smash (Fighting vs Water/Flying = Not Very Effective).
  3. Whittle HP to Red.
  4. Throw Great Balls (have 10).
  5. Backup: Lapis/Lucid for Hypnosis if desperate (risk of OHKO).