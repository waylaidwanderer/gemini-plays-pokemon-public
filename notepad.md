# Gem's Journey in Pokémon Crystal

## Current Strategy
- **Primary Goal:** Catch Red Gyarados.
- **Secondary Goal:** Buy Ultra Balls (Goldenrod Dept Store).
- **Navigation:** Shopping (Checking 5F Clerk) -> Fly to Lake of Rage.

## Shop Inventories (Goldenrod Dept Store)
- **2F (Bottom):** Poke Ball, Great Ball, Escape Rope, Repel, Revive, Full Heal, Poke Doll, Flower Mail.
- **2F (Top):** Potion, Super Potion, Antidote, Parlyz Heal, Burn Heal, Ice Heal, Awakening.
- **3F:** X Speed, X Special, X Defend, X Attack, Dire Hit, Guard Spec, X Accuracy.
- **4F:** Protein, Iron, Carbos, Calcium (Vitamins).
- **5F:** TMs (ThunderPunch, Fire Punch, Ice Punch, Headbutt).
- **Olivine Mart:** Great Ball, Super Potion, Hyper Potion, Antidote, Parlyz Heal, Awakening, Ice Heal, Super Repel, Surf Mail.

## Mechanics Log
- **Fly Map:** Cursor wraps. Navigation is non-linear.
- **Mail:** Forgery requires original data.
- **PC:** Cannot deposit mail-holding Pokemon.

## Quest Log
- **Turn 10202:** 5F Clerk sells TMs only. No Ultra Balls. Moving to Roof.

## Past Discoveries
- Gyarados rampage at Lake of Rage.
- Mahogany Mart has locked stairs.
- Bug Catching Contest active.
- Fishing Guru (Lake of Rage) wants Magikarp.
- 5F (TM Corner): Sells TMs (ThunderPunch, Fire Punch, Ice Punch, Headbutt). No Ultra Balls. Checking Roof next.
- 6F (Rooftop Square): Vending Machines. No Clerk. Checking Elevator for Basement.
- B1F: Checking for items or Ultra Balls.
- B1F Layout: Left Corridor (Col 2) connects Row 10 to Row 1. Central Room (Col 4-7). Right Section (Col 8+).
- Access Top Half: Go down to Row 10, enter Left Corridor, go Up.
- Items: (14, 2). Found Ether at (10, 15), Burn Heal at (6, 3).
- B1F Analysis: The room is divided by a wall of boxes. Left side (Elevator) is isolated from Right side (Ladder). Must access Right side from 1F.
- Elevator connects to Left Side of B1F. Right Side (Ladder) is blocked by boxes.
- B1F Item Hypothesis: The unreachable item at (14, 2) and the right side of B1F might be accessed via the Goldenrod Underground, not the Dept Store directly.
- Plan: Buy Great Balls (Ultra Balls not sold here). Fly to Lake of Rage.
## Global Tile Mechanics
- FLOOR: Traversable. Standard movement.
- WALL: Impassable.
- WARP_CARPET_DOWN: Traversable. Triggers warp to adjacent map when stepped on.
- WARP_CARPET_UP: Traversable. Triggers warp to adjacent map when stepped on.
- STAIRS: Traversable. Warps to another floor.
- Correction: I failed to talk to the Machop on B1F due to a button mix-up. If the stairs at (15, 0) don't help, I must return to B1F and talk to Machop.
- Stairs at (15, 0) likely lead to 2F, but need to verify if they also access B1F.
- Observation: Stairs at 1F (15,0) lead Up to 2F. They do not lead to B1F.
- Plan: Check 2F Clerk for Ultra Balls (since I have 6 badges now). Then return to B1F via Elevator and talk to Machop to find a way to the Right Side.