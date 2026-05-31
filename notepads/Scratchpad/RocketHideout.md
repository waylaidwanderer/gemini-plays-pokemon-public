# Rocket Hideout Exploration & Layout Records
- Started: Turn 31025

## Multi-Floor Navigation & Key Landmarks Directory
| Floor | Feature Type | Coordinates | Connects To / Notes | Status / Turn Verified |
|-------|--------------|-------------|---------------------|------------------------|
| B1F   | Stairs UP    | (21, 1)     | Game Corner (17, 4) | Verified (Turn 31019)  |
| B1F   | Stairs DOWN  | (23, 2)     | Floor B2F (27, 8)   | Verified (Turn 33602, Symmetric Link) |
| B2F   | Stairs UP    | (27, 8)     | Floor B1F (23, 2)   | Verified (Turn 32928, Symmetric Link) |
| B2F   | Stairs DOWN  | (21, 8)     | Floor B3F (25, 6)   | Verified (Turn 33766, Symmetric Link) |
| B2F   | Stairs UP    | (21, 22)    | Floor B1F (21, 25)  | Verified (Turn 31802)  |
| B2F   | Elevator     | (25, 19)    | Elevator Shaft      | Verified (Turn 32141)  |
| B3F   | Stairs UP    | (25, 6)     | Floor B2F (21, 8)   | Verified (Turn 33710, Right Section) |
| B1F   | Stairs DOWN  | (21, 25)    | Floor B2F (21, 22)  | Verified (Turn 34946, Southern Section) |
| B3F   | Stairs DOWN  | (19, 19)    | Floor B4F (19, 10)  | Verified (Turn 35235)  |
| B3F   | Elevator     | (24, 19)    | Elevator Shaft      | Verified (Turn 32141)  |
| B4F   | Stairs UP    | (19, 10)    | Floor B3F (19, 19)  | Verified (Turn 35235, Left Section) |

## Key Dungeon Items & Quest Progression
- **Lift Key**: Needed to operate the elevator.
  - [x] Lift Key: Obtained (Turn 36614)
  
- **Silph Scope**: Awarded after defeating Boss Giovanni.
  - [ ] Location: B4F (Giovanni's Office)

## Detailed Dungeon Battle Log
- **Floor B1F (Map 0_199)**:
  - [x] Grunt 1 at (26, 8) (Defeated Turn 31059)
  - [x] Grunt 2 at (12, 6) (Defeated Turn 31154)
  - [ ] Grunt 3 at (28, 18) (In SE-South corridor behind Row 16 table)
- **Floor B2F (Map 0_200)**:
  - [x] Grunt 1 at (20, 13) (Defeated Turn 31616)
- **Floor B3F (Map 0_201)**:
  - [x] Grunt 1 at (17, 25) (Defeated Turn 31831)
  - [x] Grunt 2 at (18, 17) (Defeated Turn 31867)
  - [x] Grunt 3 at (10, 22) (Defeated Turn 33867) (Note: Formerly misidentified as B4F southwest Grunt)
- **Floor B4F (Map 0_202)**:
  - [x] Grunt 1 (Defeated, dropped Lift Key at 10, 2)

## B2F Spinner Maze Traversals (Condensed)
- Traversed B2F upper spinner maze from (16, 13) to (4, 13) on Turn 36664, bypassing left spinners.
- Traversed B2F southern spinner maze from (4, 13) to (24, 19) on Turn 36682, entering the elevator safely.

## Blastoise PP Management and Boss Battle Strategy
- **Lead Pokemon**: GEMMY (Blastoise, Level 44) has moves: DIG (PP: 8/10), BITE (PP: 19/30), WATER GUN (PP: 23/25), TAIL WHIP (PP: 30/30).
- **Inventory Resources**: Gained 1x ETHER (restores 10 PP to a selected move) and 1x MAX ETHER (fully restores all PP to a selected move).
- **PP Depletion Threshold**:
  - We will conserve DIG (our high-damage Ground-type move) for enemies that resist/neutralize Water, or for Giovanni's specific threats.
  - If DIG's PP drops to **2 PP or below** before the final battle with Boss Giovanni, we will use the **ETHER** on DIG.
  - If we run completely out of WATER GUN or BITE PP during the long dungeon traversal or during the Boss battle, we will use the **MAX ETHER** to fully replenish GEMMY's moveset, ensuring she is fully optimized for the boss fight.
- **Giovanni Battle Tactics**:
  - Giovanni leads with Ground-type Pokémon (Onix, Rhyhorn). WATER GUN is super effective (x4.0 against Rock/Ground!) and will easily one-shot them, saving DIG PP.
  - Giovanni's Kangaskhan is Normal-type and bulky. We will use DIG or BITE to deal massive physical damage and take it down quickly.

## B4F Bypass and Elevator Hallway Navigation (Turn 36879)
- **B4F Bypass Verification**: We successfully verified that column 21 on B4F row 14 is open (TYPE_3fe2), allowing us to connect B4F East (from the elevator) directly to B4F West.
- This bypassed Grunt A at (23, 12) and Grunt B at (26, 12) initially, allowing us to explore the western section.
- We have now returned to the elevator hallway to defeat Grunt A and Grunt B for experience and room to navigate to Giovanni.

## B3F Western Spinner Maze Bypass (Completed)
- Successfully navigated and verified on Turns 36406 - 36472. Section cleaned up to reduce clutter.

## Strict Inventory Lock Policy
- **Constraint**: Bag contains exactly 19/20 items. 
- **Rule**: Pick up ZERO additional item balls on the way to or inside Giovanni's office. This prevents a "No more room for items!" blockage when receiving the Silph Scope. Keep this lock active until the Silph Scope is secured in our inventory.

## Rocket Hideout Elevator Mechanics (Verified Turns 36771-36861)
- **Elevator Cabin Map**: Map 0_203 (Rocket Hideout Elevator Cabin).
- **Elevator Control Panel**: Located at (1, 1). To operate, stand at (1, 2) facing UP and press 'A'. This requires the LIFT KEY in our inventory.
- **Active Exit Warps**: Located at (2, 1) and (3, 1) on row 1. Stepping on either will immediately warp the player back to the selected floor's elevator doors. Row 1 consists entirely of active exit warps; we cannot stand on row 1 without warping.
- **Bypass Maneuver to Face UP at (1, 2)**:
  1. Enter elevator from any floor door. We spawn at (3, 1) and automatically walk down to (3, 2) facing DOWN.
  2. Walk Left to (2, 2).
  3. Walk Left to (1, 2)? No, (1, 2) is open but walking straight Left will make us face LEFT. To face UP:
     - Walk Left to (2, 2).
     - Walk Left to (1, 2) facing LEFT.
     - Walk Down to (1, 3) facing DOWN.
     - Walk Up to (1, 2) facing UP.
     - Alternatively, use the row 3 path: Walk Left to (2, 2) -> Down to (2, 3) -> Left to (1, 3) -> Up to (1, 2) (facing UP).
  4. Press 'A' on (1, 1) to open the floor selection menu.

## B4F Column 21 Connection Test (Turn 36876)
- **Hypothesis**: The tile (21, 14) is an open, walkable path (TYPE_3fe2) that physically connects B4F East directly to B4F West on row 14, bypassing the partition wall.
- **Testing Plan**:
  1. We are at (22, 14) facing LEFT.
  2. Press 'Left' to step onto (21, 14).
  3. If successful, step Left again to (20, 14) to confirm direct access to B4F West.
- **HP/PP Audit**: Lead Pokemon Gemmy (Blastoise L44) has 142/143 HP, and moves DIG (8), BITE (19), WATER GUN (25) are fully ready for combat. We are highly combat ready for Giovanni.