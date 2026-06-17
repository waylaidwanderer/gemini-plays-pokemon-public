# Scratchpad: Victory Road Route & Puzzle States
- Started: Turn 96968 (pre-entry routing)

## Party Overworld HM Dependencies & Readiness:
- **SURF (HM03)**: Known by GEMMY (BLASTOISE) (Slot 1, Level 64). Fully functional.
- **STRENGTH (HM04)**: Known by ROCKY (GEODUDE) (Slot 2, Level 15). Fully functional.
- **FLY (HM02)**: Known by BIRBIE (PIDGEOTTO) (Slot 3, Level 18). Fainted but overworld FLY is usable!
- **CUT (HM01)**: Known by PETAL (BELLSPROUT) (Slot 6, Level 13). Fully functional.

## Puzzle Mechanics & Reset Rules (Generation 1):
- **Strength Deactivation**: Moving through stairs/warp transitions completely deactivates the active overworld STRENGTH state. It MUST be manually reactivated from the POKéMON menu upon entering a new floor.
- **Boulder Position Reset**: Transitioning between maps/floors or using DIG/Escape Rope completely resets all boulders on all floors back to their default starting coordinates.
- **Switch Retention**: Standing off a switch usually resets it, but some permanent switches (like plates that open gates) stay pressed once the boulder is pushed onto them. If we leave the floor, they reset.

## Puzzle State Log:

### Victory Road 1F (Map 0_108):
- **Active State**: Completed (Boulder on Switch)
- **Boulders Database**:
  - Boulder A: Initial (5, 15) | Current (17, 13) | Target (17, 13) | Status: [x] Active (secured with Switch A)
  - Boulder A2: Initial (14, 2) | Current (10, 2) | Target (10, 2) | Status: [ ] Active

### Victory Road 2F Map (Map 0_194):
- **Active State**: In Progress
  - **Current Position**: (19, 16) facing Left (Turn 100569)
- **Strength Status**: Active: [x] True
- **Boulders Database**:
  - Boulder B1: Initial (5, 5) | Current (5, 5) | Status: Unmoved
  - Boulder B2: Initial (4, 14) | Current (1, 16) | Status: [x] Pushed onto Switch B1
  - Dropped Boulder (from 3F): Initial (23, 16) | Current (9, 16) | Status: [x] Pushed onto Switch B2 (Turn 100239)
- **Floor Switches**:
  - Switch B1: Coordinate (1, 16) | State: [x] Pressed (secured with Boulder B2)
  - Switch B2: Coordinate (9, 16) | State: [x] Pressed (secured with Dropped Boulder)

### Victory Road 3F (Map 0_198):
- **Active State**: Historical (Returned to 2F)
  - **Current Position**: Historical (Returned to 2F)
  - **East-Wing & Plateau Pivot Start**: Turn 99693
- **Campaign Start (Victory Road 3F)**: Turn 98794 (Time: Wednesday, June 17, 2026 at 7:57 AM PDT)
- **Strength Status**: Active [x]
- **Landing Position**: (23, 7)
- **Warp Translation**: Ladder at (27, 7) on 2F (Map 0_194) connects to landing spot at (23, 7) on 3F (Map 0_198).
- **Boulders Database**:
  - Boulder C1 (Northeast North): Initial (22, 3) | Current (3, 5) | Status: Pushed onto Switch C1
  - Boulder C2 (Northeast South): Initial (24, 10) | Current (24, 10) | Status: Unmoved
  - Boulder C3 (West Upper): Initial (7, 7) | Current (7, 7) | Status: Blocked (tested on Turn 99678, gates at 7,8/7,9 remain solid)
  - Boulder C4 (East Lower): Initial (13, 12) | Current (13, 6) | Status: Pushed North to (13, 6) (Turn 100105)
- **Floor Switches & Holes**:
  - Pit Hole: Coordinate (23, 15) | State: Open [x] (verified on Turn 100130, boulder dropped through)
  - Switch C1: Coordinate (3, 5) | State: Pressed [x]

### Empirical Push Test Failure & Pivot Log (Turn 99693):
- **Verification of Failure**: On Turn 99678, with Boulder C1 resting on Switch C1 at (3, 5), the player attempted to push Boulder C3 at (7, 7) southwards from (7, 6). The push failed due to a solid collision bump, and tiles (7, 8) and (7, 9) remain TYPE_2889 rock walls.
- **Conclusion**: Switch C1 at (3, 5) does NOT open the Column 7 gates. Its function is elsewhere, likely lowering a barrier on the East or Northeast side of 3F.
- **Active Strategy**: Pivot immediately to Contingency A. Walk East along the Row 1 corridor to investigate if any eastern or northeast barrier was lowered, or if there is another switch/trigger on the East side.

## Active Exploration Route & Plan:
- **Active Exploration Strategy**:
  - We are currently exploring the East wing of 3F to inspect the southeastern and northeastern areas, locate Boulder C2 at (24, 10) and Boulder C4 at (13, 12), and search for any other active switches or paths that lead to solving the floor.

## Socratic Verification of Item (18, 9) Collection:
- **Hypothesis**: The player stood at (18, 10) facing Up on Turn 98639 and pressed 'A' to collect the item at (18, 9). Since our inventory was at 20/20 and no stackable quantities changed, we must verify if the item was successfully collected or if it remained on the floor due to a full bag.
- **Empirical Test Protocol**:
  - We will transition floors (e.g., take the ladder at (27, 7) to 3F and re-enter 2F) to trigger a map/sprite reset.
  - We will walk back to (18, 10) and check if the Poké Ball sprite at (18, 9) is visible.
  - If the Poké Ball is visible, our collection failed due to a full bag. We must free a slot (e.g., use a Calcium, Carbos, or Iron on a Pokémon, or use an Elixir, or toss a fainted Pidgeotto's Great Ball if allowed? No, we can just use Calcium/Carbos/Iron on Gemmy to instantly free a slot!) and re-collect it.
  - If the Poké Ball is gone, the collection was successful.
- **Status**: Pending floor transition.

## Archive: Completed Pushing Logs & Discoveries
- **TM05 Collection**: Collected TM05 at (9, 11) on Turn 98542.
- **Item at (26, 5) Collected**: Successfully retrieved Max Revive on Turn 99083.
- **Boulder B2 Pushing Log (Switch B1 at 1, 16) [Turn 98419]**:
  - Push 1: Pushed Down from (4, 14) to (4, 15) [Turn 98392]
  - Push 2: Pushed Left from (4, 15) to (3, 15) [Turn 98397]
  - Push 3: Pushed Down from (3, 15) to (3, 16) [Turn 98402]
  - Push 4: Pushed Left from (3, 16) to (2, 16) [Turn 98411]
  - Push 5: Pushed Left from (2, 16) onto Switch B1 at (1, 16) [Turn 98419]

## Gen 1 Boulder Pushing Animation/Timing Note:
- When pushing a boulder, the movement animation takes some frames. Sending consecutive movement presses too quickly (e.g., standard 500ms overworld presses) can cause the engine to ignore subsequent pushes because the boulder is still moving.
- Solution: Chunk presses into single steps or insert generous sleeps (e.g., 'sleep 1000') between consecutive pushes.

- **Discovery (Turn 100130)**: Located the real pit hole on Victory Road 3F at (23, 15).
- **Discovery (Turn 100130)**: Located a boulder on the ground level at (22, 15) directly adjacent to the pit hole at (23, 15).
- **Discovery (Turn 100130)**: Located another boulder on the ground level at (24, 10).
- **Physical Blockages on 3F**: Column 21 Rows 10, 11, and 12 are blocked by rock walls (TYPE_2889), dividing the eastern side of Row 11 from the western side of the ground floor. 

## Elite Four & Champion Preparation Plan (Blizzard PP Strategic Response - Turn 100193):
- **Observation**: GEMMY (BLASTOISE) has 0 PP remaining on Blizzard, which is our prime move for sweeping dragons.
- **Strategic Constraint**: DIG/FLY/Escape Rope to heal at a Pokémon Center or retrieve MAX ETHER from the PC will completely reset all solved boulder puzzles on 1F, 2F, and 3F, forcing us to redo them.
- **Strategic Plan**:
  1. Complete the 2F boulder puzzle and Victory Road to reach Indigo Plateau without leaving.
  2. Avoid fighting wild encounters by running (flee_battle) to conserve remaining Surf (8 PP), Hydro Pump (5 PP), and Earthquake (4 PP).
  3. Once we reach Indigo Plateau, heal the entire team at the Pokémon Center, restoring all HP and PP (including Blizzard) to full, and retrieve any needed items from the PC before entering the Elite Four lobby.
- **Gemmy's Remaining PP Limits (Turn 100329)**:
  - Surf: 8/15 PP
  - Hydro Pump: 5/5 PP
  - Earthquake: 4/10 PP
  - Blizzard: 0/5 PP (Strategic reserve: will heal at Indigo Plateau PC)

- **Turn 100511 Progress**:
  - **Empirical Test Results (All Blocked)**:
    - Turn 100485: Walking Up from (16, 12) to (16, 11) resulted in a BUMP.
    - Turn 100499: Walking Up from (24, 12) to (24, 11) resulted in a BUMP.
    - Turn 100504: Walking Up from (25, 12) to (25, 11) resulted in a BUMP.
    - Turn 100506: Walking Up from (26, 12) to (26, 11) resulted in a BUMP.
    - **Conclusion**: The entire Row 11-12 boundary across Columns 16-26 is an impassable vertical cliff face. The northeast ground-floor area on 2F is completely isolated on foot.
  - **Active Plan**: Walk to (25, 14) and take the ladder warp to 3F. From 3F (27, 15), we will walk to the (23, 15) hole, drop down to 2F (22, 16), and push the reset dropped boulder (at (23, 16)) onto Switch B2 at (9, 16) to lower the 2F northeast barrier. Once lower, we will walk to the 2F northeast ladder (27, 7) via 3F (23, 7) and take the final exit.

## Turn 100557 Reflection:
- **Progress Audit**: Over the last 50 turns, we successfully navigated from 2F to 3F, cleared the Northeast South boulder obstacle (C2), dropped through the (23, 15) pit hole, landing at (22, 16) on 2F.
- **Hypothesis Verified**: The 3F dropped boulder is persistent and did not reset back to 3F. It is at (23, 16) on 2F.
- **Immediate Task**: Get behind the boulder at (24, 16) and push it Left all the way to Switch B2 at (9, 16).
- **Tool Maintenance**: `activate_strength` was successful, but we must handle menus carefully due to wrapping.
- **Goal Clarity**: Primary goal is still Victory Road completion. Methods (specifically step-by-step boulder pushing) are detailed in this notepad.
- **Database Synchronization**: Fully updated active states. 3F is In Progress, 2F is Active. Current position is (22, 17) facing Left.