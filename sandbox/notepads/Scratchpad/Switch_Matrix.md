# Pokémon Mansion - Switch Matrix & Shutter Gate Log

## Overview
- Switches are located on Mewtwo statues. They toggle the states of electronic shutter gates globally across all floors.
- Standard state of gates has two modes: **DEFAULT (State A)** and **TOGGLED (State B)**.
- Note: Changing floors (via stairs, ladders, or pits) in Pokémon Mansion preserves the global switch state! It does NOT reset!

## Switch Locations
- **2F:** Mewtwo statues located at `(12, 9)` and `(12, 11)` (east-central corridor). 
- **3F:** Mewtwo statue located at `(2, 11)` (northwest diary room).
- **B1F:** Mewtwo statue switch located near the center-left.

## Gate Configurations by State

### DEFAULT STATE (State A)
- **1F B1F stairs gate at `(18, 8)`/`(19, 8)`:** **CLOSED** (Blocks access to bottom-right of 1F).
- **1F 1F/2F stairs gate at `(22, 2)`:** **CLOSED** (Blocks stairs going up to 2F).
- **1F central gates at `(5, 8)`/`(6, 8)`/etc.:** **CLOSED** (Blocks north to south traversal).
- **2F stairs gate at `(5, 7)`:** **OPEN** (Allows direct access to 3F stairs at 5, 10).
- **3F gate at `(21, 5)`:** **CLOSED** (Blocks column 21 access to northeast room/pit).

### TOGGLED STATE (State B)
- **1F B1F stairs gate at `(18, 8)`/`(19, 8)`:** **OPEN** (Allows access to bottom-right of 1F).
- **1F 1F/2F stairs gate at `(22, 2)`:** **OPEN** (Allows access to 2F stairs).
- **1F central gates at `(5, 8)`/`(6, 8)`/etc.:** **OPEN** (Allows north to south traversal).
- **2F stairs gate at `(5, 7)`:** **CLOSED** (Blocks Column 5).
- **3F gate at `(21, 5)`:** **OPEN** (Allows access to column 21 and the northeast room/pit).
- **B1F Secret Key Room:** **OPEN**.

## Standard Routing to B1F & Secret Key (Verified Turn 48184)
1. Enter Mansion (State A).
2. Walk UP column 5 on 1F, step onto (5, 10) stairs to warp to 2F (lands at (5, 11)).
3. On 2F, walk Left to (2, 12) along row 12, face UP, and toggle the Mewtwo statue switch at (2, 11) to State B.
4. With State B now active, walk Right to (5, 11), Up to (5, 10), and warp back to 1F (lands at (5, 11) on 1F).
5. On 1F, since the central gates are now OPEN in State B, walk Down to row 26, then East along row 26 to column 19, Up column 19, Right to column 21, and down the stairs to B1F at `(21, 24)`!
6. Retrieve the Secret Key from B1F.

## Verified Stair Warps (State A - Default)
- **1F (5, 10) <-> 2F (5, 10)**: Stepping onto (5, 10) on 1F warps player to 2F (5, 10), automatically stepping down to (5, 11). Stepping onto (5, 10) on 2F warps player back to 1F (5, 11).
- **1F (7, 10) <-> 2F (7, 10)**: Stepping onto (7, 10) on 1F warps player to 2F (7, 10), automatically stepping down to (7, 11). Stepping onto (7, 10) on 2F warps player back to 1F (7, 11).

## Crucial 1F-2F Enclosed Warp Loop & 2F Layout Constraints (Discovered Turn 47983-47990)
- **2F Solid Wall:** Row 8 is completely blocked by solid walls across columns 5 to 17 on 2F. The northern half and southern half of 2F are physically separated on these columns!
- **Warp Loop:**
  - Stepping Left from `(15, 6)` on 1F warps the player to `(2, 7)` on 2F.
  - Stepping Up from `(16, 5)` on 1F (stepping onto `(16, 4)`) warps the player to `(2, 7)` on 2F.
  - Stepping Up from `(12, 5)` on 1F (stepping onto `(12, 4)`) warps the player to `(2, 7)` on 2F.
  - Stepping Down from `(3, 7)` on 2F warps the player back to `(16, 5)` on 1F.
- **Enclosed Loop:** The northern/western room on 2F and the central room on 1F form an ENCLOSED loop with no physical overworld exit. 
- **Escape Protocol:** To escape this 1F-2F loop, the player must use **DIG** (on TRUFFLE in our party)! This warps the player completely out of the Pokémon Mansion to Cinnabar Island, resetting our position to enter the Mansion normally!