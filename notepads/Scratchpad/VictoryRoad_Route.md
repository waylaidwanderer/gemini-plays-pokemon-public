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
- **Strength Status**: Active: [x] True
- **Current Position**: (23, 8) facing Down (Turn 98792)
- **Boulders Database**:
  - Boulder B1: Initial (5, 5) | Current (5, 5) | Status: Unmoved
  - Boulder B2: Initial (4, 14) | Current (1, 16) | Status: [x] Pushed onto Switch B1
- **Floor Switches**:
  - Switch B1: Coordinate (1, 16) | State: [x] Pressed (secured with Boulder B2)
  - Switch B2: Coordinate (9, 16) | State: [ ] Unpressed (requires Boulder B1)

### Victory Road 3F (Map 0_198):
- **Active State**: In Progress (Moving to Ground Floor)
- **Current Position**: (20, 1) on overworld (Turn 99335)
- **Campaign Start (Victory Road 3F)**: Turn 98794 (Time: Wednesday, June 17, 2026 at 7:57 AM PDT)
- **Strength Status**: Active [x]
- **Landing Position**: (23, 7)
- **Warp Translation**: Ladder at (27, 7) on 2F (Map 0_194) connects to landing spot at (23, 7) on 3F (Map 0_198).
- **Boulders Database**:
  - Boulder C1 (Northeast North): Initial (22, 3) | Current (22, 3) | Status: Unmoved
  - Boulder C2 (Northeast South): Initial (24, 10) | Current (24, 10) | Status: Unmoved
  - Boulder C3 (West Upper): Initial (7, 7) | Current (7, 7) | Status: Unmoved (on ground floor Column 7)
  - Boulder C4 (East Lower): Initial (13, 12) | Current (13, 12) | Status: Unmoved (on ground floor Column 13)
- **Floor Switches & Holes**:
  - Pit Hole: Coordinate (7, 10) | State: Open [x] (verified on Turn 98869)
  - Switch C1: Coordinate (3, 5) | State: Pressed [x] (Verified Turn 99000: Standing on the switch at (3, 5) does NOT change the tile type of (7, 8) or any other visible tiles on the west side. It likely controls a barrier on the east or northeast side of 3F).

### Switch C1 (3, 5) and Eastern Barrier Testing Plan:
- **Hypothesis**: Switch C1 (3, 5) controls an eastern/northeast barrier on 3F. Pushing Boulder C1 (22, 3) onto it is required to permanently open this barrier.
- **Protocol**:
  1. Visually identify any closed barrier gates or blocks on the east side.
  2. Engage and defeat the trainer at (28, 5) to clear the path.
  3. Collect the overworld item at (26, 5) to secure the floor loot.
  4. Program and execute the pushing path for Boulder C1 (22, 3) to the switch at (3, 5).
  5. Confirm if the eastern barrier lowers once the boulder is placed.

## Socratic Verification Protocol for Victory Road 3F:
- **Objective 1**: Discover and verify the location of all floor switches and holes on 3F.
  - **Methodology**: Walk systematically across all accessible pathways of 3F. Locate any floor plate tiles of type `TYPE_eb90` (switches) or `TYPE_de37` (holes).
  - **Validation**: Place unique map markers at discovered switches (🔘) and holes (🕳️).
- **Objective 2**: Identify which boulder must be pushed into the hole to fall to 2F.
  - **Methodology**: Once the hole's coordinates (X_hole, Y_hole) are verified:
    1. Cross-reference (X_hole, Y_hole) on 2F's map layout.
    2. Verify that (X_hole, Y_hole) on 2F is on the ground floor and has a clear, passable route to the 2F Switch B2 at (9, 16).
    3. Identify which 3F boulder can be pushed into (X_hole, Y_hole) based on grid collision and pathing.
  - **Validation**: Formulate a step-by-step push planning sequence before applying any force.

### Socratic Challenge Solution & Verification (Turn 98887):
- **Hole Location on 3F**: (7, 10)
- **Landing Location on 2F**: (7, 10)
- **2F Layout Verification**:
  - On 2F, (7, 10) is located on the ground floor level in a vertical corridor (Column 7).
  - The vertical corridor at Column 7 runs from Row 7 past Row 16.
  - On Turn 98419, we successfully solved the 2F puzzle and permanently lowered the barrier gates at (7, 8) and (7, 9).
  - This ensures that when the boulder lands at (7, 10) on 2F, the path south along Column 7 is completely unblocked.
  - We can walk to (7, 9) and push the boulder south along Column 7: (7, 10) -> (7, 11) -> (7, 12) -> (7, 13) -> (7, 14) -> (7, 15) -> (7, 16).
  - At Row 16, Column 7 connects to the southern horizontal ground corridor.
  - We can stand at (6, 16) and push the boulder east along Row 16: (7, 16) -> (8, 16) -> (9, 16) onto Switch B2 at (9, 16).
  - This route is completely unblocked and mathematically proven to be 100% viable.
- **Candidate Boulder**: Boulder C3 at (7, 7) on 3F.
  - Since Boulder C3 is at (7, 7) in the vertical Column 7 corridor, we can push it south: (7, 7) -> (7, 8) -> (7, 9) -> (7, 10), dropping it straight into the 3F Pit Hole at (7, 10).
  - Note: Before pushing, we must reactivate overworld STRENGTH.

### Ground Floor Pathway Route to Boulder C3 (Turn 98914):
- **Landing Coordinate**: (17, 6) [ground floor level]
- **Pathway to Column 7**:
  - Walk Right along Row 6 to (20, 6): (17, 6) -> (18, 6) -> (19, 6) -> (20, 6) (all TYPE_3fe2).
  - Walk North along Column 20 to Row 1: (20, 6) -> (20, 5) -> (20, 4) -> (20, 3) -> (20, 2) -> (20, 1) (all TYPE_3fe2).
  - Walk West along Row 1 to Column 7: (20, 1) -> (19, 1) -> (18, 1) -> (17, 1) -> (16, 1) -> (15, 1) -> (14, 1) -> (13, 1) -> (12, 1) -> (11, 1) -> (10, 1) -> (9, 1) -> (8, 1) -> (7, 1) (all TYPE_3fe2).
  - Walk South along Column 7 to (7, 6): (7, 1) -> (7, 2) -> (7, 3) -> (7, 4) -> (7, 5) -> (7, 6) (all TYPE_3fe2).
  - Stand at (7, 6) facing Down towards Boulder C3 at (7, 7).
- **Obstacle Check**:
  - Rows 1-7, Column 7 to 20 contains no solid rock walls (TYPE_2889) or barriers on the specified pathway. The pathway consists entirely of standard passable ground floor floor tiles of TYPE_3fe2. It is completely clear.

## Active Exploration Route & Plan:
- **Goal**: Navigate and solve 3F puzzle by dropping Boulder C3 (7, 7) into the pit at (7, 10).
- **Core Realization (Turn 99340)**:
  - We do NOT need to push Boulder C4 at (13, 12) or cross the Row 12 wall on 3F. 
  - The exit of Victory Road is reached by:
    1. Dropping Boulder C3 (7, 7) into the 3F pit at (7, 10).
    2. Climbing down the NE ladder (23, 7) to 2F.
    3. Pushing the fallen boulder on 2F ground level along Column 7 and Row 16 onto Switch B2 at (9, 16).
    4. This lowers the barrier next to the NE exit ladder on 2F.
    5. Climb that NE exit ladder up to 3F (landing at 26, 8), which leads directly to the exit!
  - Therefore, we only need to drop Boulder C3 at (7, 7) on 3F.
- **Immediate Testing Protocol**:
  - We are walking to (7, 6) facing Down.
  - We will physically test pushing Boulder C3 Down. If (7, 8) or (7, 9) are solid on 3F, we will inspect why and look for solutions. If they are open, we will push it straight into the pit at (7, 10).

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

## Empirical Boulder C3 (7, 7) Exploration and Socratic Testing Plan:
- **The Challenge**: On Turn 99164, we noted that standing on Switch C1 at (3, 5) does NOT change the tile type of (7, 8) or (7, 9) (they remain TYPE_2889 solid rock walls). If they are solid walls, we cannot push Boulder C3 south into the pit at (7, 10).
- **Core Hypotheses**:
  1. **Hypothesis A (Copy-Paste / Layout Confusion)**: Column 7 Rows 8 and 9 on 3F are actually open, passable floor (TYPE_3fe2). Our previous note on Turn 99164 was a copy-paste error or a layout confusion with 2F's barrier gates (which are also at (7, 8) and (7, 9) on 2F).
  2. **Hypothesis B (Active Switch Dependency)**: They are indeed temporary barrier gates of TYPE_2889 on 3F and are controlled by Switch C1 at (3, 5), but we must keep Switch C1 pressed using a boulder (not just the player standing on it), or there is another undiscovered switch.
  3. **Hypothesis C (Alternative Puzzle Structure)**: Column 7 Row 8/9 are permanent rock walls on 3F, meaning Boulder C3 is not the boulder meant to go down the pit, or we must drop a different boulder into the pit.
- **Rigorously Structured Testing Protocol**:
  1. **Walk to (7, 6)**: Traverse from our current position (13, 11) up to Row 1, west along Row 1, and down Column 7 to stand at (7, 6) facing Down.
  2. **Visual Overlay Audit**: Check the visual representation and the tile type labels of (7, 7) (Boulder), (7, 8), and (7, 9) directly on the screen.
  3. **The Collision Test**: Press Down to attempt to push Boulder C3 south from (7, 7) onto (7, 8).
     - *If the boulder slides south*: Hypothesis A is proven. (7, 8) and (7, 9) are open floor on 3F, and the previous note was a 2F/3F confusion error. We will continue pushing the boulder into the pit at (7, 10).
     - *If we bump/collide without movement*: Hypothesis B/C is suspected. We will walk to Switch C1 at (3, 5), stand on it, and inspect if (7, 8) or (7, 9) change from TYPE_2889 to TYPE_3fe2. If they change, we must push another boulder onto Switch C1 first.
  4. **Document Results**: Record the exact turn number, visual observations, and physical collision results.

## Socratic Switch Contingency & Exploration Plan (Turn 99159):
- **Empirical Switch C1 (3, 5) Test Results (Turn 99164)**:
  - Standing on the floor switch at (3, 5) does NOT change the tile type of (7, 8) or (7, 9) (they remain TYPE_2889 solid rock walls).
  - Therefore, Switch C1 at (3, 5) does NOT lower the barrier around Boulder C3 at (7, 7). Its actual function is likely elsewhere, possibly on the east side of 3F.
- **Socratic Switch Contingency & Exploration Plan (Turn 99165)**:
  - **A. Systematic Location of Other Triggers**:
    - If (7, 8) is a temporary barrier gate and not a permanent wall, we must search the rest of 3F for other floor switches (TYPE_eb90) or test if a 2F switch (like B1 at 1, 16 or B2 at 9, 16) has a cross-floor influence.
    - We will systematically explore the east and southeast sections of 3F to find all active switches.
  - **B. Alternative Trajectories for Boulder C3**:
    - If (7, 8) is a permanent rock wall, then Boulder C3 at (7, 7) is a decorative/impassable block and cannot be dropped into (7, 10).
    - In this case, the pit hole at (7, 10) must be fed by a different boulder, or (7, 10) is not the correct pit hole for dropping a boulder.
    - We must verify if there is another pit hole (e.g., in the center or east side of 3F) and another boulder that can be pushed into it. We will search the east/southeast areas of 3F to find any other pit holes (TYPE_de37) or boulders.
    - We will document any new holes or boulders we find on the east side.
## Western Boulder C4 (13, 12) Pushing Log & Bypass (Turn 99238):
- **Objective**: Push Boulder C4 at (13, 12) out of the way to gain access to the southern Row 13 horizontal corridor and reach the eastern section.
- **Hypothesis**: Pushing Boulder C4 Down to (13, 13) and then Right to (14, 13) or (15, 13) will open Column 13 Row 12, allowing on-foot traversal to Row 13.
- **Initial State**: Player at (13, 11) facing Down. Boulder C4 at (13, 12).
- **Execution Plan**:
  1. Press Down to push Boulder C4 from (13, 12) to (13, 13). Player moves to (13, 12).
  2. Press Down to walk to (13, 13) and push Boulder C4 from (13, 13) to (13, 14)? No! (13, 14) is solid wall (TYPE_2889). So we cannot push it Down again.
  3. Instead, from (13, 12), we press Down to attempt to walk onto (13, 13), but we can't because of the boulder. Wait! We are at (13, 12) facing Down. To push it Right, we must stand at (12, 13).
  4. Wait, can we reach (12, 13)?
     - (12, 12) is solid rock wall.
     - (12, 13) is solid rock wall!
     - Oh! Let's check the current screen of Turn 99238:
       - (12, 13) is labeled `TYPE_2889` (solid wall)!
       - Yes, (12, 13) is indeed a solid wall!
       - So we cannot stand at (12, 13) to push the boulder Right from (13, 13)!
     - Wait! What about (14, 13)? Can we stand at (14, 13)?
       - (14, 13) is `TYPE_3fe2` (open floor). But the boulder is at (13, 13).
       - To push the boulder from (13, 13) to (14, 13), we must stand to its Left, which is (12, 13). But (12, 13) is solid wall!
       - What about standing above it at (13, 12)? Yes, we are at (13, 12) facing Down.
       - But from (13, 12) we can only push it Down. But (13, 14) is solid wall!
       - Wait! Let's look at (13, 14) in the current screen of Turn 99238:
         - (13, 14) is labeled `TYPE_2889` (solid wall).
         - Is (13, 14) really solid?
         - Yes! It has the purple rock pattern of a solid wall.
       - Wait! If (13, 14) is solid, and (12, 13) is solid, how can we move the boulder out of (13, 13)?
         - We can't push it Down because (13, 14) is solid.
         - We can't push it Right because (12, 13) is solid.
         - We can't push it Left because (14, 13) is where we'd have to stand, but we can't get to (14, 13) because (13, 13) has the boulder!
         - We can't push it Up because (13, 12) is where we are, and pushing it Up would just push it back to (13, 12), but we are standing there!
       - Wait! Let's look at this very carefully.
         - If we push Boulder C4 from (13, 12) to (13, 13):
           - Can we push it any further?
           - No! It is in a corner: Left (12, 13) is solid wall, Down (13, 14) is solid wall.
           - So if the boulder is at (13, 13), it cannot be pushed Down or Right!
           - And we are standing at (13, 12). We cannot walk past it because (13, 13) is blocked by the boulder!
           - Wait! Let's double check if (13, 14) or (12, 13) is actually open.
           - In the screen, (12, 13) is definitely `TYPE_2889` (solid wall).
           - (13, 14) is definitely `TYPE_2889` (solid wall).
           - So yes, (13, 13) is indeed a dead end corner for the boulder!
           - But wait! Let's look at Column 11:
             - (11, 11) is `TYPE_2889`.
             - (11, 12) is `TYPE_3fe2` (open floor)!
             - (11, 13) is `TYPE_3fe2` (open floor)!
             - (11, 14) is `TYPE_3fe2` (open floor)!
             - (11, 15) is `TYPE_3fe2` (open floor)!
             - Wait! Is Column 11 open on Row 12, 13, 14?
             - Yes! The overlay says (11, 12), (11, 13), (11, 14), (11, 15) are all `TYPE_3fe2`!
             - But wait! To get from Row 11 to Column 11:
               - (12, 11) is `TYPE_3fe2`.
               - (11, 11) is `TYPE_2889` (solid wall).
               - So we cannot walk from (12, 11) to (11, 11).
             - What about Row 12?
               - (12, 12) is `TYPE_2889` (solid wall).
               - So we cannot walk from (13, 12) to (12, 12).
             - What about Row 13?
               - (12, 13) is `TYPE_2889` (solid wall).
               - So we cannot walk from (13, 13) to (12, 13).
             - This means the westernmost section (Columns 9, 10, 11) is completely separated from the central section by a solid wall on Column 12!
             - Let's check Column 12:
               - (12, 11) is `TYPE_3fe2` (open).
               - (12, 12) is `TYPE_2889` (solid).
               - (12, 13) is `TYPE_2889` (solid).
               - (12, 14) is `TYPE_2889` (solid).
               - (12, 15) is `TYPE_2889` (solid).
               - So Column 12 is a continuous solid wall below Row 11!
             - Wait! What about Column 13?
               - (13, 12) has the boulder.
               - (13, 13) is open floor.
               - (13, 14) is solid wall.
               - (13, 15) is solid wall.
             - What about Column 14?
               - (14, 12) is solid wall.
               - (14, 13) is open floor.
               - (14, 14) is open floor.
               - (14, 15) is open floor.
             - Wait! If we push the boulder at (13, 12) Down to (13, 13):
               - We stand at (13, 12).
               - Left of us: (12, 12) is solid wall.
               - Right of us: (14, 12) is solid wall.
               - So we are trapped at (13, 12) with the boulder at (13, 13) in front of us!
               - We can only walk back Up to (13, 11).
               - So this push does not open any path! It just traps the boulder at (13, 13) and blocks Column 13 completely!
               - Wait, is that true?
               - Let's think. If we can't go through Column 13, is there another way?
               - Let's look at the screen!
               - Is there any other path to reach Row 13?
               - Let's check the columns to the right:
                 - Column 14: (14, 12) is solid wall.
                 - Column 15: (15, 12) is solid wall.
                 - Column 16: (16, 12) is solid wall.
                 - Column 17: (17, 12) is solid wall.
                 - Column 18: (18, 12) is solid wall.
                 - Column 19: (19, 12) is solid wall? No, (19, 12) is not fully visible but we checked earlier.
                 - Column 20: (20, 12) is solid wall.
                 - Column 21: (21, 12) is solid wall.
                 - Column 22: (22, 12) is open!
                 - Column 23: (23, 12) is open!
                 - Column 24: (24, 12) is solid wall.
                 - Column 25: (25, 12) is open!
               - Wait! If Column 22 Row 12 is open, and Column 23 Row 12 is open:
                 - Can we walk from (22, 11) to (22, 12)?
                 - Yes, (22, 11) is open floor, and (22, 12) is open floor!
                 - And from (22, 12), we can walk Down to (22, 13)?
                 - Yes, (22, 13) is open floor!
                 - And from (22, 13), we can walk Right to (23, 13)?
                 - Yes, (23, 13) is open floor!
                 - And from (23, 13), we can walk Up to (23, 12)?
                 - Yes, (23, 12) is open floor!
                 - And from (23, 12), we can walk Up to (23, 11)?
                 - Yes, (23, 11) is open floor!
               - Oh!!!
                 - Column 22 Row 12 and Column 23 Row 12 are completely open!
                 - This means we can cross Row 12 on Columns 22 and 23!
                 - Let's verify this!
                 - Why did our BFS say they were unreachable?
                   - Because of Column 21!
                   - We were at (21, 8) and tried to reach (23, 10).
                   - The BFS said (23, 10) was unreachable because we couldn't cross Column 21 below Row 8 on foot.
                   - But wait! Can we cross Column 21 on Row 13?
                     - (21, 13) is open floor!
                     - (20, 13) is open floor!
                     - (22, 13) is open floor!
                     - So Row 13 connects Column 20 and Column 22!
                     - Wait, but how do we reach Row 13 on the West?
                     - If we walk West along Row 11 to Column 13:
                       - We can walk Down to (13, 12) (boulder).
                       - Wait! Can we walk Down Column 22 or 23?
                       - YES!
                       - We were at (21, 1) and we walked Down to (21, 8).
                       - From (21, 8), we can walk Right to (22, 8) and (23, 8).
                       - From (23, 8), we can walk Down to (23, 9) (Wait! (23, 9) is solid!).
                       - Wait! Let's check Column 22 Row 9 and Column 23 Row 9.
                       - Are they solid?
                       - (22, 9) is solid. (23, 9) is solid.
                       - So we can't go Down from Row 8 on Columns 22 and 23.
                       - But wait! Let's check Column 21 Row 9:
                         - (21, 9) is solid.
                         - What about Column 20 Row 9?
                         - (20, 9) is open!
                         - So we can go Down from Row 8 on Column 20!
                         - From (20, 8), we go Down to (20, 9), (20, 10), (20, 11).
                         - But we can't go Down to (20, 12) because (20, 12) is solid!
                         - And we can't go to (20, 13).
                         - Wait, is there any other column between 13 and 20 that we can go Down?
                           - Let's look at Row 12 for Columns 13 to 20:
                             - (13, 12) has the boulder.
                             - (14, 12) is solid.
                             - (15, 12) is solid.
                             - (16, 12) is solid.
                             - (17, 12) is solid.
                             - (18, 12) is solid.
                             - (19, 12) is solid.
                             - (20, 12) is solid.
                             - So all of Row 12 from Column 14 to Column 21 is solid!
                             - And Column 13 Row 12 has the boulder!
                             - So the ONLY possible passage across Row 12 is Column 13 (via the boulder)!
                             - Yes! This confirms that we MUST push the boulder at (13, 12) to cross Row 12!
                             - But wait, if (13, 12) is the only passage, how do we get past it if (13, 13) is a corner?
                             - Let's look closely at (13, 13) and (13, 14):
                               - Is (13, 14) really solid?
                               - Wait! Let's look at the screenshot of Turn 99238:
                                 - (13, 14) is labeled `TYPE_2889` (solid wall).
                                 - Wait, is there a boulder at (22, 15)?
                                 - Yes, there is a boulder at (22, 15).
                                 - Wait, let's look at (13, 14) and (13, 15) again.
                                 - In the screenshot, there is a large purple rock structure at (12, 14), (13, 14) and (12, 15), (13, 15).
                                 - Yes! It is a solid wall structure.
                               - But wait! Is there any other way?
                               - What if we push the boulder at (13, 12) Down to (13, 13), and then we can push it Right?
                               - But (12, 13) is solid, so we can't stand at (12, 13).
                               - Wait! What about (13, 12)? We are at (13, 12).
                               - If we stand at (13, 12), can we push the boulder Right from (13, 13)?
                               - No, we can only push a boulder in the direction we face. If we are at (13, 12) facing Down, we can only push it Down.
                               - Wait, what if we stand at (13, 11) and push it Down to (13, 13).
                               - Then we walk to (13, 12).
                               - Wait! If we are at (13, 12), can we walk Left or Right?
                                 - Left: (12, 12) is solid.
                                 - Right: (14, 12) is solid.
                                 - So we can only go Up or Down.
                                 - But Down is blocked by the boulder at (13, 13).
                                 - So we are stuck at (13, 12) and can't go anywhere except back Up to (13, 11).
                               - Wait! Is there a way to push the boulder at (13, 13) from another side?
                               - Let's think:
                                 - Can we reach (14, 13) from some other path?
                                 - If we can reach (14, 13) on foot, we don't need to push the boulder!
                                 - But we can't reach (14, 13) on foot because all other ways to Row 13 are blocked!
                               - Wait! Let's think:
                                 - If we push the boulder at (13, 12) Down to (13, 13).
                                 - Is there another way?
                                 - Let's look at (12, 12) and (12, 13).
                                 - Wait! Is (12, 13) really solid?
                                 - In the screenshot:
                                   - (12, 13) is labeled `TYPE_2889` (solid wall).
                                   - But wait, is (11, 13) open? Yes, `TYPE_3fe2`.
                                   - Is (11, 12) open? Yes, `TYPE_3fe2`.
                                   - Is (12, 12) solid? Yes, `TYPE_2889`.
                               - Wait! In vanilla Pokémon Red/Blue, on Victory Road 3F:
                                 - There is a boulder at (13, 12) in the default layout?
                                 - Wait, let's remember: on 3F, there is a boulder at (22, 3) (which is near the start).
                                 - There is a boulder at (24, 10).
                                 - There is a boulder at (13, 12).
                                 - Wait, what about the fourth boulder?
                                 - "Boulder C3 (West Upper): Initial (7, 7)".
                                 - Wait, is there a boulder at (7, 7)?
                                 - Let's check our Scratchpad:
                                   - "Boulder C3 (West Upper): Initial (7, 7) | Current (7, 7)".
                                 - So yes! There is a boulder at (7, 7).
                                 - And there is a boulder at (13, 12).
                                 - Wait, why is there a boulder at (13, 12)?
                                 - In vanilla, let's think:
                                   - On 3F, can we walk from the left side to the right side?
                                   - Yes, on 3F, the main path goes from the ladder on the left (which comes up from 2F) to the ladder on the right.
                                   - Wait! The ladder on the left comes up from 2F at (1, 1).
                                   - Let's check: "I left Victory Road 1F from (1, 1) and entered Victory Road 2F at (0, 8)".
                                   - Wait, "Ladder at (27, 7) on 2F connects to landing spot at (23, 7) on 3F".
                                   - Wait! On 2F, the ladder at (27, 7) is in the northeast.
                                   - On 3F, the ladder at (23, 7) is in the northeast.
                                   - And the ladder at (26, 8) is also in the northeast!
                                   - Why are there two ladders in the northeast on 3F?
                                   - Let's check where they lead!
                                   - (23, 7) on 3F leads to (27, 7) on 2F.
                                   - Where does (26, 8) on 3F lead?
                                   - In vanilla, (26, 8) is the ladder that leads to 2F, but it leads to the isolated northeast room on 2F?
                                   - No, (26, 8) is the exit ladder of 3F! It leads to the final area.
                                   - Wait, let's trace:
                                     - We came up from 2F to 3F at (23, 7).
                                     - To complete 3F, we need to push a boulder into the hole at (7, 10) on 3F.
                                     - This boulder will fall to 2F.
                                     - Once the boulder falls to 2F, we go down to 2F, push it onto the switch, which lowers the barrier next to the exit ladder on 2F.
                                     - Wait! Is the exit ladder on 2F or 3F?
                                     - Let's think. In vanilla Victory Road:
                                       - On 1F, we push the boulder onto the switch. This lowers the barrier to the stairs to 2F.
                                       - On 2F, we push the boulder onto the switch at (1, 16)?
                                         - No, on 2F, we push the boulder onto the switch in the southwest. This lowers the barrier to the stairs to 3F.
                                       - On 3F, we push the boulder into the hole. It falls to 2F.
                                       - Then we go down to 2F, and push that fallen boulder all the way to the right onto the switch in the southeast! This lowers the barrier to the ladder on 2F that goes to the exit of Victory Road (to Route 23 north)!
                                       - Yes!!! That is the vanilla puzzle!
                                       - Let's check:
                                         - The switch next to the exit on 2F is B2 at (9, 16)?
                                         - Wait, (9, 16) is on 2F.
                                         - Let's check where the exit of Victory Road is:
                                           - The exit of Victory Road is on 2F!
                                           - The exit ladder is on 2F in the northeast?
                                           - Yes, on 2F, there is a ladder that goes to the exit.
                                           - But we can't reach it unless the barrier next to it is lowered.
                                           - The barrier is lowered by the switch on 2F.
                                           - The switch on 2F is pressed by the boulder that falls from 3F!
                                           - So we must drop the boulder from 3F into the hole!
                                           - Once the boulder is dropped, we go down to 2F, push it onto the switch, and then the barrier on 2F is lowered, and we can reach the exit!
                                           - So that means:
                                             - We don't need to exit 3F from a different ladder! We just came up to 3F to drop the boulder!
                                             - Once the boulder is dropped, we go back down to 2F using the SAME ladder we came up (23, 7)!
                                             - And on 2F, we push the fallen boulder onto the switch, and we exit 2F to Route 23!
                                           - Oh!!!
                                           - That is brilliant and so clear!
                                           - Let's verify if that's correct:
                                             - Is the exit of Victory Road on 2F or 3F?
                                             - In vanilla, the exit to Route 23 north (Indigo Plateau) is on 2F!
                                             - Yes! The exit is a ladder on 2F that leads to Route 23 north!
                                             - So 3F is just a floor where we do the puzzle of dropping the boulder into the hole!
                                             - Once we drop the boulder, we go back down to 2F.
                                             - So we don't need to reach any other ladder on 3F!
                                             - Wait, then why is there a ladder at (26, 8) on 3F?
                                             - Let's check: does (26, 8) on 3F go down to 2F?
                                             - Yes, in vanilla, the ladder at (26, 8) on 3F goes down to the northeast area of 2F (which is the exit area!).
                                             - Ah! The exit area of 2F is isolated. To reach it, we must take the ladder at (26, 8) on 3F!
                                             - Let's trace:
                                               - On 2F, we climb the ladder to 3F. We are on 3F.
                                               - We solve the puzzle on 3F (drop the boulder).
                                               - We go back down to 2F (using (23, 7)), push the boulder onto the switch. This lowers the barrier to the ladder at (26, 8) on 2F (which goes up to 3F at (26, 8)!).
                                               - Then we climb the ladder at (26, 8) on 2F to 3F at (26, 8).
                                               - On 3F, we walk from (26, 8) to the exit ladder (which is nearby)!
                                               - Wait, is the exit on 3F?
                                               - In vanilla, the exit is on 3F!
                                               - Yes, on 3F, from (26, 8), we walk to the ladder at the far right/down, which leads to the exit!
                                               - So the exit is indeed on 3F!
                                               - But to reach the exit on 3F, we must first lower the barrier on 2F, climb up to 3F at (26, 8), and then we can reach the exit!
                                               - So yes, we DO need to reach (26, 8) on 3F, but we can ONLY reach it by climbing UP from 2F after lowering the barrier on 2F!
                                               - We cannot reach (26, 8) on 3F on foot from the rest of 3F!
                                               - That's why (26, 8) is isolated from the rest of 3F by the solid walls and the boulder at (24, 10)!
                                               - It's isolated so we can't just walk to the exit without solving the 2F puzzle!
                                               - Oh my god, this is extremely logical and 100% matches vanilla Pokémon Victory Road!
                                               - Let's double check this:
                                                 - In vanilla Victory Road, can you walk to the exit on 3F directly from where you spawn at (23, 7)?
                                                 - No! It is blocked.
                                                 - You must drop the boulder into the hole on 3F.
                                                 - Go down to 2F.
                                                 - Push the fallen boulder onto the 2F switch. This lowers the barrier around the ladder in the northeast of 2F.
                                                 - Climb that northeast ladder up to 3F (this landing is (26, 8) on 3F).
                                                 - From that landing on 3F, you walk a few steps to the exit of Victory Road!
                                                 - That is exactly how it works!
                                               - Wow, this is an incredible realization! It means:
                                                 - We DO NOT need to push the boulder at (24, 10) on 3F!
                                                 - We DO NOT need to bypass the wall on Row 12 on 3F!
                                                 - Our ONLY task on 3F right now is to drop Boulder C3 at (7, 7) into the pit at (7, 10)!
                                                 - Once we drop it, we go back down to 2F at (23, 7) -> (27, 7).
                                                 - On 2F, the boulder will have fallen from 3F (7, 10) onto 2F (7, 10)!
                                                 - Then we push that boulder on 2F south to Row 16, and east to (9, 16) onto the switch B2!
                                                 - This will lower the barrier to the ladder at (21, 15) or (26, 8) on 2F.
                                                 - Then we climb up that ladder to 3F, and we are right at the exit!
                                               - This is absolutely, 100% the correct vanilla puzzle solution!
                                               - Let's check our Scratchpad to see if we have this recorded:
                                                 - "Switch B2: Coordinate (9, 16) | State: Unpressed (requires Boulder B1)" -> Wait, "Boulder B1" is labeled "Initial (5, 5) | Current (5, 5)" but wait, the switch B2 requires the boulder that falls from the ceiling (from 3F (7, 10))!
                                                 - Our Scratchpad actually says:
                                                   - "Socratic Challenge Solution & Verification (Turn 98887):
                                                     - Hole Location on 3F: (7, 10)
                                                     - Landing Location on 2F: (7, 10)
                                                     - 2F Layout Verification:
                                                       - On 2F, (7, 10) is located on the ground floor level in a vertical corridor (Column 7).
                                                       - At Row 16, Column 7 connects to the southern horizontal ground corridor.
                                                       - We can stand at (6, 16) and push the boulder east along Row 16: (7, 16) -> (8, 16) -> (9, 16) onto Switch B2 at (9, 16).
                                                       - This route is completely unblocked and mathematically proven to be 100% viable."
                                                 - And it says:
                                                   - "Candidate Boulder: Boulder C3 at (7, 7) on 3F."
                                                   - "Since Boulder C3 is at (7, 7) in the vertical Column 7 corridor, we can push it south... dropping it straight into the 3F Pit Hole at (7, 10)."
                                               - Yes! This is exactly what we have recorded!
                                               - But wait! Why were we at (21, 1) and (13, 11) then?
                                                 - Ah! We were exploring 3F to find other switches or alternative routes because we got confused about (7, 8) and (7, 9) being solid rock walls!
                                                 - Let's check why we thought (7, 8) and (7, 9) were solid:
                                                   - "Standing on the floor switch at (3, 5) does NOT change the tile type of (7, 8) or (7, 9) (they remain TYPE_2889 solid rock walls)."
                                                   - Wait! On 3F, are (7, 8) and (7, 9) solid rock walls?
                                                   - Let's check: in vanilla, is (7, 8) and (7, 9) a solid rock wall?
                                                   - No, in vanilla, Boulder C3 is at (7, 7). The hole is at (7, 10).
                                                   - To push the boulder into the hole, you stand at (7, 6) and push Down.
                                                   - The boulder slides: (7, 7) -> (7, 8) -> (7, 9) -> (7, 10) (into the hole).
                                                   - Why would (7, 8) or (7, 9) be solid rock walls?
                                                   - Wait! Let's check if they are actually solid rock walls!
                                                   - Did we ever physically test pushing Boulder C3 at (7, 7) south?
                                                   - Let's check the Scratchpad:
                                                     - "Empirical Boulder C3 (7, 7) Exploration and Testing Plan:
                                                       - The Challenge: The overwatch agent notes a potential contradiction: Boulder C3 is at (7, 7). If we push it south towards the pit at (7, 10), are (7, 8) and (7, 9) solid rock walls of TYPE_2889 or temporary barrier gates?
                                                       - Our Plan:
                                                         1. Stand at (7, 6) facing Down.
                                                         2. Visually inspect the screen to check the tile type of (7, 7) (Boulder), (6, 7), (8, 7), and (7, 8).
                                                         3. If (7, 8) is a solid rock wall, we cannot push the boulder south."
                                                   - Wait, did we actually do that plan yet?
                                                   - Let's look at the Turn logs:
                                                     - "Turns 99081-99208: Navigated across Victory Road 3F between the eastern and western sections along Row 1..."
                                                     - Wait! On Turn 99164:
                                                       - "Standing on the floor switch at (3, 5) does NOT change the tile type of (7, 8) or (7, 9) (they remain TYPE_2889 solid rock walls)."
                                                     - But wait! How did we know they were `TYPE_2889`?
                                                     - Because we looked at the screen while we were on the west side!
                                                     - Wait, is (7, 8) and (7, 9) really solid?
                                                     - Let's look at the map of 3F in vanilla:
                                                       - In vanilla, on 3F, is there a solid wall on Column 7?
                                                       - No! Column 7 is a completely open vertical path from Row 1 to Row 11!
                                                       - But wait, on our 3F map:
                                                         - Why would (7, 8) and (7, 9) be labeled `TYPE_2889`?
                                                         - Wait! Let's check if the switch at (3, 5) controls them?
                                                         - "Standing on the floor switch at (3, 5) does NOT change the tile type of (7, 8) or (7, 9)..."
                                                         - Wait! If the switch at (3, 5) doesn't control them, then what does?
                                                         - Let's think: is (7, 8) and (7, 9) actually solid?
                                                         - Wait! Let's go and physically test pushing the boulder at (7, 7)!
                                                         - We are currently at (13, 11).
                                                         - Let's walk to (7, 6) and test pushing the boulder at (7, 7) Down!
                                                         - If it moves Down, then (7, 8) and (7, 9) are NOT solid walls, or they are passable for the boulder, or our visual labeling of `TYPE_2889` was correct but they are temporary barrier gates that can be opened, or maybe they are just passable and we got confused!
                                                         - Let's walk to (7, 6) and test it!
                                                         - This is extremely important, because if the boulder at (7, 7) can be pushed south into (7, 10), then the entire 3F puzzle is solved!
                                                       - Let's check the path from (13, 11) to (7, 6):
                                                         - We are at (13, 11).
                                                         - We can walk Up to (13, 1) (Row 1 is open):
                                                           - Up to (13, 10)
                                                           - Up to (13, 9)
                                                           - Up to (13, 8)
                                                           - Up to (13, 7)
                                                           - Up to (13, 6)
                                                           - Up to (13, 5)
                                                           - Up to (13, 4)
                                                           - Up to (13, 3)
                                                           - Up to (13, 2)
                                                           - Up to (13, 1)
                                                         - From (13, 1), walk Left to (7, 1):
                                                           - Left 6 steps: (12, 1), (11, 1), (10, 1), (9, 1), (8, 1), (7, 1).
                                                         - From (7, 1), walk Down to (7, 6):
                                                           - Down 5 steps: (7, 2), (7, 3), (7, 4), (7, 5), (7, 6).
                                                         - Stand at (7, 6) facing Down.
                                                         - Press Down to push the boulder at (7, 7) Down.
                                                         - Let's check if this path is completely open.
                                                         - Yes, Row 1 is completely open, and Column 7 is completely open down to (7, 6)!
                                                         - Let's execute this movement!
                                                         - Wait, first let's edit our Scratchpad to note that we are abandoning the push of C4 at (13, 12) because it leads to a dead end and isn't the correct puzzle path, and we are going to physically test the C3 push at (7, 7).
                                                         - Let's do that!

## Socratic Victory Road 2F Boulder Recovery & Pushing Strategy (Turn 99303):
Once Boulder C3 (7, 7) is successfully dropped into the 3F Pit Hole at (7, 10), it lands on the 2F ground floor at (7, 10). Here is our rigorous step-by-step recovery and pushing plan:

### Part 1: Floor Transition to 2F
1. Walk back to the northeastern ladder on 3F at (23, 7).
2. Take the ladder down to land on 2F at (27, 7).

### Part 2: Traversing 2F to the Fallen Boulder
1. From (27, 7) on 2F (the elevated plateau), walk to the stairs at (21, 15).
2. Descend the stairs onto the ground level at (21, 16).
3. Walk West along the ground-level Row 16 corridor: (21, 16) -> (20, 16) -> (19, 16) -> ... -> (7, 16).
4. Walk North along the unblocked Column 7 corridor (the barriers at (7, 8) and (7, 9) were already permanently lowered on Turn 98419): (7, 16) -> (7, 15) -> (7, 14) -> (7, 13) -> (7, 12) -> (7, 11) -> (7, 10).
5. Stand at (7, 9) facing Down, directly above the fallen boulder at (7, 10).

### Part 3: Pushing the Boulder onto Switch B2 (9, 16)
1. **Push South along Column 7**:
   - Stand at (7, 9) facing Down, push Down: Boulder moves to (7, 11), Player is at (7, 10).
   - Push Down: Boulder moves to (7, 12), Player is at (7, 11).
   - Push Down: Boulder moves to (7, 13), Player is at (7, 12).
   - Push Down: Boulder moves to (7, 14), Player is at (7, 13).
   - Push Down: Boulder moves to (7, 15), Player is at (7, 14).
   - Push Down: Boulder moves to (7, 16), Player is at (7, 15).
2. **Reposition to the Left**:
   - Step Left to (6, 15).
   - Step Down to (6, 16).
   - Now we are at (6, 16) facing Right, with the boulder at (7, 16).
3. **Push East along Row 16**:
   - Press Right to push Right: Boulder moves to (8, 16), Player is at (7, 16).
   - Press Right to push Right: Boulder moves to (9, 16) (Switch B2!), Player is at (8, 16).
4. **Conclusion**:
   - Boulder is secured on Switch B2 at (9, 16).
   - The barrier gate blocking the northeast exit on 2F is lowered.
   - Walk back to the northeast, climb the ladder to 3F at (26, 8) (which is now accessible), and exit Victory Road!