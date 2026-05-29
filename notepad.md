<h1><code>Locations/MtMoon_B2F</code></h1>

# Mt. Moon B2F Location Records

## Connections:
- **Ladder to B1F**: Located at (15, 27). Connects to Mt. Moon B1F at (13, 27). Verified on Turn 6309.
- **Stairs to B1F (TYPE_4b8d)**: Located at (24, 23) and (25, 23). Verified on Turn 6238 as passable platform stairs.
- **Southern Section Exploration & Partial Blockage (Turn 8199)**:
  - The eastern corridor at Row 21 on B2F (accessible via the ladder at (15, 27) and moving east) is blocked. Standing at (28, 22) on Turn 8199, we attempted to walk Up into (28, 21) (TYPE_2889) and directly collided with the wall (0 tiles visited), proving that the eastern corridor is blocked at Row 21.
  - **Verified Fact (Turn 10010-10047)**: The western corridor was systematically tested and confirmed completely impassable near Row 21 (due to a solid rock wall at Column 14 Row 21 and solid pillars at Columns 12-13 Rows 22-27). Therefore, there is no horizontal or vertical passage connecting the southern section of B2F to the central/northern section on the west side.

## Layout & Floor Navigation:
- **Passable Cavern Floor**: TYPE_2770 is the primary passable cavern floor.
- **Cavern Obstacles (TYPE_de37)**: Visually structured like rectangular pillars/walls. Tested and confirmed solid (impassable) on Turn 6205 at (13, 25), on Turn 6213 at (14, 28), on Turn 6577 at (15, 28) (by pressing Down from the (15, 27) ladder), and on Turn 6615 at (21, 28) (by pressing Down from (21, 27)). These individual coordinate tests show that TYPE_de37 blocks horizontal and vertical movement at those specific coordinates. Other columns of Row 28 (such as columns 12-14, 16-20, and 22-27) are visual obstacles of TYPE_de37 and are treated as unverified visual theories until tested.
- **Eastern Corridor**: Located at columns 28 & 29. Verified passable from row 26 up to row 22.

## Strategic Markers:
- `(15, 27): 🚪 Ladder to B1F`
- `(15, 24): ☠️ Rocket Grunt defeated`
- `(25, 21): ✅ HP UP collected`
- `(29, 5): ✅ TM01 (Mega Punch) collected (Turn 6803)`
- `(29, 17): ☠️ Rocket Grunt defeated (Turn 7155)`

## Northern Section (Accessible via B1F ladder at (17, 11) leading to B2F at (25, 9)):
- **Verified Fact (Turn 8592, corrected Turn 10809)**: The Northern Section (Rows 5-11, Columns 24-30) is not completely isolated. While Row 12 Column 25 is a solid rock wall, the northern elevated platform (Rows 5-8, Columns 9-16) is fully connected to the southern area via the vertical corridor on Columns 12 and 13.
- Ladder to B1F: Located at (25, 9). Leads to B1F at (17, 11).
- TM01 (Mega Punch) collected at (29, 5) on Turn 6803.
- Turn 6910: Verified that stairs at (28, 7) and (29, 7) are fully passable, bidirectional stairs. They connect the elevated platform (Row 7) to a lower, enclosed 4x2 alcove consisting of rows 5-6 and columns 27-30 (TYPE_2770). This alcove has walls (TYPE_2889) on all other sides (Row 4, column 26, column 31). This is where TM01 (Mega Punch) was collected at (29, 5). No other pathways exist in this small alcove.
- **Ladder to B1F (Central/NW section)**: Located at (21, 17). Connects to Mt. Moon B1F at (21, 17). Verified on Turn 7029. This ladder leads to a central elevated platform area on B2F.
- **Central Elevated Platform Area (around Row 13-18, Columns 20-26)**:
  - Accessible via (21, 17) ladder.
  - Walkable ground is TYPE_2770.
  - To the east (column 25-26), there are tiles of type TYPE_3fe2 at Rows 16-18.
  - Let's explore this platform.
  - Central Platform Stairs: Located at (26, 15) and (27, 15) (TYPE_4b8d), providing transition from the elevated central platform to the eastern floor area.
- **Passable Cavern Floor (TYPE_3fe2)**: Verified on Turn 7064. Successfully moved Down from (26, 15) to (26, 16) (TYPE_3fe2) without collision, proving that the dark patterned tiles in rows 16-18 are fully passable cavern floor on B2F.
- **Eastern Floor Area (Columns 25-31, Rows 16-18)**:
  - Accessible via stairs at (26, 15) and (27, 15).
  - Walkable floor is TYPE_3fe2.
  - Rocket Grunt located at (29, 17) (TYPE_3fe2). Talked to him on Turn 7074, initiating a trainer battle. (Previously misidentified as a floor item due to the orange/black sprite, but confirmed as a Rocket Grunt).

## Southern Platform (Rows 21-23, Columns 23-26):
- **Layout & Isolation Constraint (Turn 8170 Verification)**: 
  - Accessible from the lower floor via stairs at (24, 23) and (25, 23) (TYPE_4b8d).
  - Walkable floor on the platform consists of (23, 21-22), (24-25, 21-22), (26, 21-22), and (25, 23).
  - The western boundary of this platform at Column 22 on Rows 21 and 22, and Column 23 on Row 23, consists of solid rock walls (TYPE_2889).
  - Standing at (25, 21) on Turn 8170, the visual grid overlay clearly confirms (22, 21) and (21, 21) are solid rock walls (TYPE_2889).
  - This platform is a raised dead end where only HP UP was obtained at (25, 21). While the raised platform itself is isolated from the Central Platform, the lower floor of the southern section (accessible via the bottom-left ladder at (15, 27)) has an unverified western corridor (Columns 12-16) near Row 21 that may provide a vertical passage to the central/northern section of B2F. Verified on Turn 8170.
- **Verified Fact (Turn 9694)**: Standing at (32, 11) facing Down, we attempted to walk south onto (32, 12). The action resulted in 0 tiles visited, proving that Row 12 Columns 31-35 consists of a solid rock wall (despite being labeled as TYPE_2770). It is NOT a jumpable ledge. This confirms that the Northern Section of B2F is a completely isolated cul-de-sac dead end.
- **Verified Fact (Turn 9700)**: Since B2F (25, 9) is a dead end, we backtracked up to 1F at (17, 11). The true route to the fossils must be via the Central Platform ladder at B1F (21, 17) -> B2F (21, 17), then walking east to the Central Platform stairs at (26, 15)/(27, 15), walking east past the Rocket Grunt at (29, 17), and finally exploring north on Columns 31-35.
- **Verified Fact (Turn 9771)**: While standing at (34, 12) on the eastern elevated platform of Mt. Moon B2F, we attempted to move north into (34, 11) (TYPE_3fe2) and collided.
- **Verified Fact (Turn 9771)**: While standing at (35, 12) on the eastern elevated platform of Mt. Moon B2F, we attempted to move north into (35, 11) (TYPE_3fe2) and collided.
- **Conclusion**: The entire Row 11/12 boundary from Column 28 to Column 35 is a completely impassable cliff face in both directions, separating the central platform's eastern stairs from the northern section of B2F.
- **Western Corridor Systematic Passability Tests (Turn 10010-10013)**:
  - **Verified Fact (Turn 10010)**: Attempted to walk Up from (14, 22) onto (14, 21) (TYPE_2889) and directly collided (0 tiles visited), proving that Column 14 is physically blocked at Row 21 by a solid rock wall.
  - **Verified Fact (Turn 10013)**: Standing at (14, 22) facing Left, attempted to step onto (13, 22) (TYPE_de37) and directly collided (0 tiles visited), proving that the pillar at (13, 22) is solid and impassable.
  - **Verified Fact (Turn 10029)**: Standing at (14, 23) facing Left, attempted to step onto (13, 23) (TYPE_de37) and directly collided (0 tiles visited), proving that the pillar at (13, 23) is solid and impassable.
  - **Verified Fact (Turn 10040)**: Standing at (14, 24) facing Left, attempted to step onto (13, 24) (TYPE_de37) and directly collided (0 tiles visited), proving that the pillar at (13, 24) is solid and impassable.
  - **Verified Fact (Turn 10042)**: Standing at (14, 25) facing Left, attempted to step onto (13, 25) (TYPE_de37) and directly collided (0 tiles visited), proving that the pillar at (13, 25) is solid and impassable.
  - **Verified Fact (Turn 10044)**: Standing at (14, 26) facing Left, attempted to step onto (13, 26) (TYPE_de37) and directly collided (0 tiles visited), proving that the pillar at (13, 26) is solid and impassable.
  - **Verified Fact (Turn 10047)**: Standing at (14, 27) facing Left, attempted to step onto (13, 27) (TYPE_de37) and directly collided (0 tiles visited), proving that the pillar at (13, 27) is solid and impassable.
  - **Final Western Corridor Bypass Conclusion**: Columns 12 and 13 are completely solid and impassable pillars (TYPE_de37) from Row 19 down to Row 28. Row 21 Column 14 is a solid rock wall (TYPE_2889). Therefore, the southern floor area (Columns 14-19, Rows 22-27) is completely isolated from the western corridor (Columns 10-11). There is no horizontal or vertical passage connecting the southern section of B2F to the central/northern section on the west side. We must use the central platform or eastern pathways to progress.

<hr>

<h1><code>Locations/MtMoon_1F</code></h1>

# Mt. Moon 1F Location Records

## Layout & Floor Navigation:
- **Passable Cave Floor**: TYPE_2770 is verified passable.
  - **Proof of Work**: Tested on Turn 6060 by successfully walking south from (25, 15) (TYPE_3fe2) onto (25, 16) (TYPE_2770) without collision.
- **Platform Height Boundary**:
  - **Verified Fact**: The southern boundary of the platform at Row 20 acts as an impassable wall. Tested on Turn 6955 at (17, 20) (pressing Down from (17, 19)) and on Turn 6959 at (16, 20) (pressing Down from (16, 19)). Both tests resulted in zero movement, physically proving that the platform transition to the lower cavern floor is solid and impassable both ways without stairs.
- **Eastern Corridor**: Rows 14-27, Columns 24-27 are fully passable floor (TYPE_2770). Verified by traversing from (25, 15) down to (25, 23) on Turns 6530-6551.
- **Southern Corridor & Rock Wall Bypass**:
  - **Verified Fact (Turn 7959)**: Columns 21-23 on Row 26 are impassable rock walls despite the grid overlay labeling them as TYPE_2770. Visually they are light-blue rock textures, showing the central vertical rock wall extends down to Row 27.
  - **Verified Fact (Turn 7966)**: Row 28 is a fully passable dark floor corridor of TYPE_3fe2, connecting the Eastern Corridor (Columns 24-25) to the Western/Southern area (Column 20-21) by going underneath the rock wall.
  - **Verified Fact (Turn 8048)**: Column 19 is a solid, impassable wall on Rows 28, 30, 31, and 32, preventing direct horizontal traversal from the Eastern Corridor to the Western area on these southern rows. Tested during systematic overworld collision tests.
- **Ladders**:
  - Ladder to B1F (NE section): Located at (25, 15). Connects to Mt. Moon B1F at (25, 15).
  - Ladder to B1F (North-Central section): Located at (17, 11). Connects to Mt. Moon B1F at (25, 9). Verified on Turn 6689.

## Mt. Moon Trainer Milestones:
- [x] Bug Catcher at (7, 22) (Defeated! Team: Level 11 Weedle, Level 11 Kakuna. Defeated on Turn 5294. BUGGY leveled up to 9!)
- [x] Lass at (16, 22) (Defeated! Team: Level 14 Clefairy. Defeated on Turn 5373. BUGGY and GEMMY gained 102 EXP each.)
- [x] Lass Miriam at (30, 4) (Defeated! Team: Level 11 Oddish, Level 11 Bellsprout. Defeated on Turn 5580. BUGGY evolved into BUTTERFREE at Lv 10!)

## Verified Discoveries:
- [x] Potion: Located at (2, 20) (Obtained on Turn 5202).
- [x] TM12 (Water Gun): Located at (5, 32) (Obtained on Turn 5227).
- [x] Escape Rope: Located at (36, 23) (Obtained on Turn 5250).
- **Platform Height Boundary (Row 21 & Row 19 Verified)**:
  - **Verified Fact (Turn 7838)**: Row 21 acts as a solid rock barrier. Standing at (10, 22) facing Up, attempting to move north into (10, 21) (TYPE_2889) resulted in a direct collision and zero movement, proving this visual boundary is physically solid and impassable.
  - **Verified Fact (Turn 7850)**: Row 19 acts as a solid rock barrier. Standing at (6, 20) facing Up, attempting to move north into (6, 19) (TYPE_2889) resulted in a direct collision and zero movement, proving this visual boundary is physically solid and impassable.
- **Verified Fact (Turn 8293)**: Column 16 is a solid rock wall (TYPE_2889) on Rows 29, 30, 31, 32, 33, 34, and 35. Standing at (15, 33) on Turn 8293, we attempted to walk Right into (16, 33) (TYPE_2889) and directly collided with the wall (0 tiles visited), physically proving that Column 16 is solid. This means there is no direct horizontal connection on the southern rows (Rows 29-35) between Column 15 and the eastern side of the map (Column 20).
- **Central Vertical Wall Bypass Test on Row 11 (Turn 8620-8626)**:
  - **Verified Fact**: Standing at (14, 11) facing Left, attempting to walk left into (13, 11) (labeled TYPE_2889) resulted in a direct collision and zero movement (only 3 tiles visited for 4 movement presses). This physically proves that Column 13 is solid rock on Row 11 as well. Row 11 does not provide a direct overworld bypass to the west.
- **Central Vertical Wall Bypass Test on Row 7 (Turn 8783)**:
  - **Verified Fact**: Standing at (14, 7) facing Left, the visual screen grid clearly shows (13, 7) and (12, 7) are solid rock walls (TYPE_2889). Row 7 is completely blocked by the central vertical wall and does not connect the east and west sides of Mt. Moon 1F on the overworld.
- **Central Vertical Wall Bypass (Verified Turn 8864)**: Column 13 Rows 16, 17, 18, and 19 are fully passable cavern floor of TYPE_3fe2. Walking through Column 13 on these rows allows direct overworld traversal between the east side and west side of Mt. Moon 1F, without needing any underground ladder backtracking. This connects the central-eastern vertical corridor to the central-western open area. Note that Column 12 and 13 on Rows 2-15 are solid rock walls (TYPE_2889), preventing horizontal traversal anywhere else north of Row 16.
- **Verified Fact (Turn 10164)**: Standing at (14, 3) facing Up, the visual screen grid clearly shows Row 1 Columns 10-19 consists of a solid rock wall of TYPE_2889. There is no horizontal or vertical passage through Row 1. Row 0 is completely inaccessible from Row 2, meaning there is no horizontal bypass north of Row 16.

<hr>

<h1><code>Locations/Route2_Gatehouse_North</code></h1>

# Route 2 Northern Gatehouse (Map 0_47) Location Records
- Permanently verified map connections, layout, and NPCs in the Route 2 Northern Gatehouse.

## Connections:
- Southern warp connects to Viridian Forest (Map 0_51) at (4, 7) / (5, 7) area.
- Northern warp connects to Route 2 (Pewter City side) at the top of the room.

## Layout & Spatial Features:
- Standing at (4, 7) facing UP.
- Column X=4 is a clear path.
- An NPC is standing at (2, 5).

## NPC Investigations:
- NPC at (3, 2) (Youngster): "Many POKéMON live in forests" (Verified on Turn 3682).

<hr>

<h1><code>Main</code></h1>

# Pokémon Blue Playthrough Dashboard

## Main Objectives
- [x] Choose first Pokémon (Turn 81 - Squirtle!)
- [x] Reach Viridian City Poké Mart to get Oak's Parcel (Turn 247)
- [x] Deliver Oak's Parcel to Professor Oak (Turn 461)
- [x] Get Pokédex from Professor Oak (Turn 464)
- [x] Get Town Map from Daisy in Pallet Town (Turn 507)
- [x] Return to Viridian City to buy Poké Balls (Turn 825)
- [x] Capture additional wild Pokémon (Pidgey, Rattata, etc.) to build our team
- [x] Navigate north through Route 2 and enter Viridian Forest Gatehouse (Turn 2082)
- [x] Explore Viridian Forest to find and capture Caterpie (Turn 2125)
- [x] Navigate to Pewter City (Turn 3717)
- [x] Defeat Pewter Gym Leader Brock and earn the Boulder Badge (Turn 4083)
- [x] Clear all Route 3 Trainers (Turn 4752)
- [x] Restock items at Pewter Poké Mart (Turn 4848)
- [x] Traverse Mt. Moon to reach Route 4 (Turn 11116)
- [x] Reach Cerulean City (Turn 11225)
- [x] Recover TM28 Dig (Turn 14431) and teach to GEMMY (Turn 14445)
- [x] Defeat Cerulean Gym Leader Misty and earn the Cascade Badge (Turn 14547)
- [x] Board S.S. Anne and obtain HM01 Cut from the Captain (Turn 17395)
- [x] Solve Vermilion Gym's trash can lock puzzle (Turn 19471)

## Directory
- `Locations/PalletTown` - Permanently verified Pallet Town location records.
- `Locations/Route1` - Permanently verified Route 1 connections and layout features.
- `Locations/ViridianCity` - Permanently verified Viridian City connections and buildings.
- `Locations/PewterCity` - Permanently verified Pewter City location, gym, and connection records.
- `Locations/Route3` - Permanently verified Route 3 connections, pathing, and bidirectional ledge gaps.
- `Mechanics/General` - Verified game mechanics and controls.
- `Locations/SSAnne` - Verified S.S. Anne records, cabins, and trainers.

## Notepad Management Protocol (One-In, One-Out)
- To adhere to the 10 loaded notepad limit:
  1. Before loading a new region's notepad, audit current active notepads.
  2. If the loaded count is 9 or 10, identify completed/distant regions (e.g., SSAnne, VermilionCity) to unload.
  3. Execute `unload_notepads` to archive completed notepads before loading new ones.
  - **Specific Milestone**: Upon entering Rock Tunnel, we will proactively unload `Locations/CeruleanCity` and `Locations/Route9` to free up slots for the highly detailed `Scratchpad/RockTunnel_Pathfinding` and future Lavender Town / Celadon City records. This keeps our active context clean and focused on our immediate surroundings.

<hr>

<h1><code>Archive/Route2_GrindingHistory</code></h1>

# Scratchpad: Wild Captures and Leveling Goals (Archived from Route 2)

## High-Level Strategy:
- Active Grinding Phase (Started Turn 910)
- Pivot Strategy (Turn 1411): After 42 cumulative steps on Route 2 Columns 8 & 9 (Rows 61-67) with 0 encounters, we hypothesized that encounters on this specific grass patch might be disabled or extremely rare. We pivoted to the northern grass patch.
- Pivot Strategy (Turn 2072): After 60 cumulative steps on Route 2's northern tall grass patch with 6 encounters and 0 Caterpie, we conclude that Caterpie's encounter rate on Route 2 is too low to justify further time investment here. We are pivoting our primary search space north to Viridian Forest, where Caterpie has a significantly higher spawn rate in Pokémon Blue.

## Live Status:
- Turn 2077: SQUIRTLE (GEMMY) is at 14/26 HP (Level 8). BIRBIE (PIDGEY) is at 18/18 HP (Level 4). REMY (RATTATA) is at 16/16 HP (Level 4).
- Money: ¥1075.
- Inventory: 7 Poké Balls, 1 Antidote, 1 Town Map.
- Location: Route 2 (Map 0_13) at (9, 45) - Facing Up (Gatehouse in view).
- Grinding Phase 2: Pivoted.
  - Goal: Explore north to reach Viridian Forest to capture Caterpie.
  - Plan: Move Left 4 times to (5, 45), then Up once to (5, 44) to enter the Viridian Forest gatehouse warp.

## Active Team & Captures Checklist:
- [x] Pidgey (Level 4, Nickname: BIRBIE) - Status: Captured!
- [x] Rattata (Level 4, Nickname: REMY) - Status: Captured! (Turn 1940)
- [ ] Caterpie (Target Level 10 Butterfree) - Status: Not Captured (Pivoted search to Viridian Forest)
- [ ] GEMMY (SQUIRTLE) - Level 8 (Goal: Level 10)

## Route 2 Wild Encounters Strategy:
- Active Patrol: Completed. Tested southern patch (Columns 8 & 9, Rows 61-67, 42 steps, 0 encounters) and northern patch (Columns 4-9, Rows 48-51, 60 steps, 6 encounters: 4 Pidgey, 2 Rattata).

## Target Captures and Leveling Benchmarks:
1. Caterpie (Bug) -> Metapod (Bug) -> Butterfree (Bug/Flying):
   - Level range: 3-5
   - Strategy: Direct Poké Ball or minimal damage.
   - Purpose: Early evolution to Butterfree (Level 10) is extremely valuable because Butterfree learns CONFUSION at Level 12. Confusion deals super-effective damage to Rock/Ground types (like Geodude/Onix) in Pewter Gym, providing a massive tactical advantage!
   - Gamer Girl Nickname Ideas: FLUFFY, BUGGY, SILKY, BUTTERFLY.

## Pewter City Gym Preparation (Gym 1):
- Leader Brock uses Rock/Ground Pokémon (Geodude Level 12, Onix Level 14).
- Squirtle's Bubble/Water Gun (Water-type) is 4x super-effective against Geodude and Onix, making GEMMY our primary sweeper!
- Level 8 SQUIRTLE learns Bubble. Level 15 SQUIRTLE learns Water Gun.
- Goal: Train GEMMY to Level 10+ and secure a Butterfree/Pidgey support team before challenging the Gym.

## Summary of Journey:
- Turns 809-848: Entered Viridian Mart; purchased 10 Poké Balls and 1 Antidote.
- Turns 849-871: Bypassed Trainer School and moved Up Column 19 to (19, 12).
- Turns 872-895: Navigated past old man and transitioned to Route 2 (Map 0_13) at (8, 71).
- Turns 910-934: Patrolled Route 2 Columns 8 & 9. Verified tall grass tile graphics and prepared for wild captures.

## Grinding Cumulative Tally Tracking (Northern Tall Grass):
- **Grinding Run 2 (Completed Turn 2072)**:
  - Current Position: (9, 48) on Route 2.
  - Cumulative steps taken on tall grass: 60 (Turn 2072)
  - Encounters triggered: 6 (Level 3 PIDGEY on Turn 1829, Level 3 PIDGEY on Turn 1861, Level 5 PIDGEY on Turn 1878, Level 5 PIDGEY on Turn 1894, Level 4 RATTATA on Turn 1932, Level 2 RATTATA on Turn 2046)
  - Result 1: Defeated Level 3 Pidgey. GEMMY gained 23 XP, grew to Level 8, and learned BUBBLE! (Turn 1837)
  - Result 2: Successfully ran away to conserve HP. (Turn 1865)
  - Result 3: Successfully ran away to conserve HP. (Turn 1880)
  - Result 4: Successfully ran away to conserve HP. (Turn 1896)
  - Result 5: Successfully captured wild Level 4 RATTATA on Turn 1937! (Nicknamed REMY on Turn 1940)
  - Result 6: Encountered Level 2 RATTATA on Turn 2046. Successfully ran away on Turn 2049.
- Turn 2091: Arrived at Route 2 Gatehouse (4,2) facing Up. Preparing to exit north through (5,0) to enter Viridian Forest.

<hr>

<h1><code>Archive/ViridianForest_Grinding</code></h1>

# Archived Scratchpad: Viridian Forest Grinding and Caterpie/Pikachu Capture
- Started: Turn 2110, Timestamp: Saturday, May 23, 2026 at 8:57 PM PDT
- Finished/Archived: Turn 3724

## Final Status at Archive:
- Turn 3724: Exited Viridian Forest and Route 2, entered Pewter City (Map 0_2) at (18, 35).
- SQUIRTLE (GEMMY): Level 11, HP: 4/32
- METAPOD (BUGGY): Level 8, HP: 3/28
- PIKACHU (SPARKY): Level 6, HP: 5/21
- PIDGEY (BIRBIE): Level 5, HP: 12/20
- RATTATA (REMY): Level 4, HP: 0/16 (Fainted)

## Grinding & Encounters Log:
- Target: Caterpie/Metapod/Kakuna.
- Location: Southernmost grass patch.
- Cumulative steps on grass: 92
- Encounters:
  - Encounter 1: Level 3 CATERPIE (Turn 2114). Decision: Throw Poké Ball. Captured, Nicknamed BUGGY.
  - Encounter 2: Level 5 METAPOD (Turn 2189). Switch-trained.
  - Encounter 3: Level 4 METAPOD (Turn 2801). Switch-trained to GEMMY. Bubble dealt ~25-30% damage, ignoring Defense boost.

## Switch-Training Strategy:
- Lead BUGGY, switch to GEMMY, defeat wild Pokemon. Safely shared EXP.

## Grinding Milestones & Summaries:
- Battle 6 (Turn 2617): Defeated wild Level 5 Metapod. BUGGY reached Level 6.
- Battle 7 (Turns 2656-2678): Defeated wild Kakuna. Shared EXP.
- Battle 8 (Turn 2795): Defeated wild Level 3 Caterpie. Shared EXP.
- Battle 9 (Turn 2810): Defeated wild Level 4 Metapod. Shared EXP.
- Battle 10 (Turn 2880): Defeated wild Level 3 Caterpie. Shared EXP.
- Battle 11 (Turns 3007-3011): Defeated wild Level 3 Caterpie. Shared EXP.
- Battle 12 (Turns 3026-3033): Defeated wild Level 4 Caterpie. Shared EXP.
- Battle 13 (Turns 3039-3047): Defeated wild Level 4 Caterpie. BUGGY reached Level 7 and evolved into METAPOD!
- Battle 14 (Turns 3064-3069): Defeated wild Level 3 Caterpie. Shared EXP.
- Battle 15 (Turns 3083-3089): Defeated wild Level 4 Caterpie. Shared EXP.
- Battle 16 (Turns 3110-3122): Defeated wild Level 4 Caterpie. Shared EXP.
- Battle 17 (Turns 3144-3153): Defeated wild Level 4 Kakuna. Shared EXP.
- Battle 18 (Turns 3161-3175): Captured Level 5 Pikachu (Sparky).
- Battle 19 (Turns 3220-3227): Defeated wild Level 4 Metapod. Shared EXP.
- Battle 20 (Turns 3438-3487): Defeated Bug Catcher trainer at (30, 19). Shared EXP. BUGGY reached Level 8, SPARKY Level 6.

## Viridian Forest North-South Corridor Spatial Layout (Turn 3599):
- Parallel vertical corridors mapped.
1. Westernmost Corridor (Column 2): Leads to exit gatehouse at (2, 1).
2. Middle-Left Corridor (Columns 6-8): Connected to Middle-Right at top (Row 1).
3. Middle-Right Corridor (Columns 11-13).
4. Eastern Corridor (Column 16): Runs south to entrance.

<hr>

<h1><code>Locations/ViridianForest</code></h1>

# Viridian Forest (Map 0_51) Location Records

## Connections:
- Southern entrance connects to Route 2 Gatehouse (Map 0_50) via warp at (17, 47) / (18, 47) area.

## Layout & Spatial Features:
- Entrance area:
  - Gatehouse exit is situated around (17, 47).
  - (17, 46) is blocked by a signpost/tree (TYPE_2889).
  - There is a clear path leading Left to (16, 47) then Up along column 16.
  - An NPC is standing at (16, 43) facing Down.

## NPCs & Interactions:
- NPC at (16, 43): Wearing a blue cap. Facing Down near the entrance. (Status: Interacted on Turn 2104. Dialogue: "I came here with some friends! They're out for POKéMON fights!")
- Friendly Bug Catcher NPC at (27, 40): Standing near the southern grass patch. (Status: Interacted on Turn 3377. Dialogue: "Ssh! You'll scare the bugs away!")
- Bug Catcher Trainer at (27, 33): Challenged player on Turn 3385. (Status: Defeated on Turn 3415. Money reward received, player's cash now ¥1135.)
- Bug Catcher Trainer at (30, 19): Spotted player and walked to (27, 19) on Turn 3437. (Status: Defeated on Turn 3487. Money reward received, player's cash now ¥1205.)

<hr>

<h1><code>Archive/GameStartIntro</code></h1>

# Game Start Intro Archive
- Turn 0 (11:43 AM): Title screen of Pokémon Blue Version visible. Gengar and Red are on the screen.
- Plan:
  1. Press Start to access the main menu.
  2. Select "NEW GAME".
  3. Name the Player.
  4. Name the Rival.
- Turn 1: Screen shows main menu with cursor on 'NEW GAME'. Pressing A to start.
- Turn 3: Professor Oak's intro has begun. Naming plan: Player = GEM, Rival = BLUE. Pressing A to advance dialogue.
- Turn 5: Screen shows 'Welcome to the world of POKéMON!'. No down arrow visible. Pressing A to advance to the next screen.
- Turn 6: Screen shows 'My name is OAK! People call me' with a down arrow (▼). Pressing A to advance.
- Turn 7: Dialogue is at 'People call me the POKéMON PROF!' with no down arrow. Pressing A to advance.
- Turn 8: Dialogue says 'This world is inhabited by' with Nidorino on screen. There is no down arrow. Pressing A to advance.
- Turn 9: Screen shows 'inhabited by creatures called'. The harness is in dialogue mode. Wait, there is no down arrow on the current screenshot, but there was a down arrow after 'called' in standard dialogue. Let's see what the next text is. Pressing A to advance the dialogue.
- Turn 10: Screen is white (fade transition). Intermediate state shows 'creatures called POKéMON!' text was advanced. Now fading to the next dialogue. Pressing A.
- Turn 11: Screen shows 'For some people, POKéMON are' with a down arrow (▼). Nidorino is still on screen. Pressing A to advance.
- Turn 12: Screen shows 'For some people, POKéMON are' with a down arrow (▼). Nidorino is on screen. Pressing A to advance the dialogue.
- Turn 13: Screen shows 'pets. Others use' with a down arrow (▼) and Nidorino on screen. Pressing A to advance the dialogue.
- Turn 14: Screen shows 'pets. Others use them for fights.' with down arrow (▼). Pressing A to advance dialogue.
- Turn 15: Screen shows 'Myself...' with no down arrow. This is the transition to naming ourselves. Pressing A to proceed.
- Turn 16: Dialogue shows 'I study POKéMON as a profession.' with no down arrow, and Nidorino is still on screen. Pressing A to advance the dialogue.
- Turn 17: Screen shows 'I study POKéMON as a profession.' with no down arrow, and Nidorino is still on screen. Pressing A to advance the dialogue.
- Turn 18: Screen shows 'First, what is your name?' with down arrow (▼). Pressing A to go to the naming menu.
- Turn 19: Character name selection screen is displayed. Options:
  - ▶NEW NAME
  - BLUE
  - GARY
  - JOHN
  Preparing to select 'NEW NAME' to input our custom name 'GEM'. Cursor is currently at 'NEW NAME'. Pressing A.
- Turn 22: Keyboard screen for character name entry is loaded. The cursor is currently pointing to 'A' at (0, 4).
  Plan to spell 'GEM' and select 'END' (ED):
  1. To 'G' (6, 4): Press Right 6 times, then A.
  2. To 'E' (4, 4): Press Left 2 times, then A.
  3. To 'M' (3, 5): Press Left 1, Down 1, then A.
  4. To 'ED' (8, 8): Press Right 5, Down 3, then A.
  Sequence to execute: ['Right', 'Right', 'Right', 'Right', 'Right', 'Right', 'A', 'Left', 'Left', 'A', 'Left', 'Down', 'A', 'Right', 'Right', 'Right', 'Right', 'Right', 'Down', 'Down', 'Down', 'A']
- Turn 28: Player name 'GEM' is confirmed by Oak! Screen says 'Right! So your name is GEM!'. Pressing A to continue.

<hr>

<h1><code>Locations/Route2_Gatehouse</code></h1>

# Route 2 Gatehouse (Map 0_50) Location Records
- Permanently verified map connections, layout, and NPCs in the Route 2 Gatehouse.

## Connections:
- Southern warp connects to Route 2 (Map 0_13) at (3, 43).
- Northern warp connects to Viridian Forest.

## Layout & Spatial Features:
- Standing at (4, 2) facing Up.
- Column X=4 is a completely open, clear checkered path running north-south from the southern door at (4, 7) straight through to the northern side.
- Counter desks are located on the east side around Row Y=3.
- Exit to Viridian Forest is located at (5, 0) of TYPE_3fe2.

## NPCs:
- Scientist/Aide NPC located around (2, 4) on the west side.
- Blue-haired female trainer NPC located at (8, 4) facing Down.

## Route 2 Northern Gatehouse Map Transition (Turn 3675):
- **Warp Connection**: Successfully stepped UP from (1, 0) on Map 0_51 (Viridian Forest) to transition north into the Route 2 Gatehouse (Map 0_47).
- **Current Position**: Standing at (4, 7) facing UP inside the Gatehouse.
- **Physical Layout**:
  - The Gatehouse is a 10x8 grid (X from 0 to 9, Y from 0 to 7).
  - Row Y=7 is the southern entrance/exit leading back to Viridian Forest at (4, 7) / (5, 7).
  - An NPC (likely a Scientist) is standing at (2, 5).
  - The northern exit leading to Route 2 (Pewter City side) is at the top of the room.
- **Immediate Plan**: Walk north through the gatehouse, talk to the NPC at (2, 5) to see if they offer any helpful items or dialogue, and then exit north onto Route 2.

<hr>

<h1><code>Archive/RouteToViridian_Turns521_557</code></h1>

# Route to Viridian Archive (Turns 521-557)
This archive preserves the turn-by-turn log of Gem's journey from Pallet Town back to Route 1 (up to column 8 positioning) with Squirtle at 12/24 HP.

- Pallet Town Phase (Turns 521-529): Successfully navigated from Blue's House at (13, 6) through Pallet Town northwards to the Route 1 transition at (10, 0) with Squirtle at 12/24 HP. We prepared the route, bypassed obstacles, and entered the tall grass of Route 1.
- Turn 536: Arrived on Route 1 at (10, 35). Verified screen layout matches our records. Fences block Left (9, 35) and Right (12, 35). Straight north is tall grass (TYPE_fed7) from Y=35 to Y=32. Y=31 is a clear path (TYPE_3fe2).
  Plan: Move Up to (10, 31). Steps:
  1. Up to (10, 34)
  2. Up to (10, 33)
  3. Up to (10, 32)
  4. Up to (10, 31)
- Turn 538: Successfully stepped north to Route 1 (10, 34). No wild encounter. Facing north. SQUIRTLE's health remains 12/24 HP. Moving north to (10, 33).
- Turn 541: Arrived at Route 1 (10, 33). No wild encounter. SQUIRTLE health at 12/24 HP. Preparing to move north to (10, 32).
- Turn 543: Successfully moved Up to (10, 32). No wild encounter. Facing north. Ready to step onto the clear row at (10, 31). SQUIRTLE's health is 12/24 HP.
- Turn 545: Position (10, 32), facing north. SQUIRTLE's HP is 12/24. Verified Row 31-28 layout.
  Plan to bypass the Row 27 ledge (which blocks columns 10-15):
  1. Move Up to (10, 31).
  2. Move Left to (9, 31) and then (8, 31).
  3. Move Up to (8, 30), then (8, 29), and (8, 28).
  This will put us at (8, 28) facing north, clear of the ledge on columns 10-15.
- Turn 548: Position (10, 32), facing north. SQUIRTLE HP is 12/24. Ready to move Up to (10, 31) to reach the clear path.
- Turn 553: Successfully reached (10, 31) on Route 1. Facing north. SQUIRTLE is at 12/24 HP. Bypassing the ledge at Row 27 requires moving Left to (8, 31). Ready to execute.
- Turn 557: Arrived at Route 1 (8, 31) successfully. Facing left. SQUIRTLE's health is 12/24 HP. Moving Up to (8, 30), which is clear path.
- Turn 567: Arrived at Route 1 (8, 30) successfully. No wild encounter. SQUIRTLE's health is 12/24 HP. Moving Up to (8, 29), which is tall grass (TYPE_fed7).
- Turn 572: Performing active steps to break execution stagnation. SQUIRTLE at 12/24 HP. Preparing to step north to (8, 29).
- Turn 580: Arrived at Route 1 (8, 28) facing North. SQUIRTLE's health is 12/24 HP. Bypassed the tall grass corridor! Ready to move Up to (8, 27), which is a clear path.
- Turn 586: Position (8, 27), facing north. SQUIRTLE's health is 12/24 HP. Bypassed the row 27 ledge. Looking ahead to row 23, column 8 is blocked by TYPE_2889 (stone block/fence). We must walk Right to column 12 to pass row 23 through tall grass.
  Plan:
  1. Move Up 3 steps to (8, 24).
  2. Move Right 4 steps to (12, 24).
  3. Move Up 2 steps to (12, 22).
- Turn 601: Position (12, 24), facing north. SQUIRTLE's health is 12/24 HP. Successfully walked Right 4 steps to reach Column 12 on Turn 595, positioning us in front of the Row 23 grass passage. Now moving Up 3 steps to reach the clear path at (12, 21).
- Turn 608: Position (12, 21), facing north. SQUIRTLE's health is 12/24 HP. No wild encounters. Preparing to execute the Row 19 ledge bypass by moving Left 3 steps to Column 9, then Up 4 steps to (9, 17).
- Turn 612: Position (9, 17) facing north. SQUIRTLE's health is 12/24 HP. Analyzed layout for Row 13 barrier: columns 5 to 9 are blocked by ledges (TYPE_44f6) or obstacles, and columns 10 to 13 are blocked by stone blocks (TYPE_2889). Column 14 has tall grass (TYPE_fed7) which is open and passable at Row 13.
  Plan to proceed north:
  1. Move Right 5 steps to (14, 17) [TYPE_3fe2].
  2. Move Up 1 step to (14, 16) [TYPE_3fe2].
  3. Move Up 3 steps to (14, 13) [TYPE_fed7 - tall grass] and step beyond Row 13 to (14, 12).
- Turn 627: Standing at (14, 17) facing Left. SQUIRTLE is at 12/24 HP. No wild encounters. Clerk NPC (SPRITE_853c) has wandered to (15, 13) which leaves Column 14 at Row 13 completely open!
  Immediate action: Move Up to (14, 16) [TYPE_3fe2 - clear path, no encounter risk] to turn north and establish our position on Column 14.

<hr>

<h1><code>Locations/PewterCity</code></h1>

# Pewter City (Map 0_2) Location Records

## Connections:
- South exit connects to Route 2 (Northern side) via map boundary transition.
- East exit connects to Route 3 (initially blocked by a Brock fan NPC, open after defeating Brock).

## Key Buildings & POIs:
- Pokémon Center: Located at (13, 25), inside Map 0_58. Healed team on Turn 3999. Left counter at (3, 3) facing UP. (🏥 marked)
- Pewter Gym: Located at (16, 17), inside Map 0_54. Exit at (4, 13). (🏋️ marked)
- Pewter Poké Mart: Located at (23, 17) (entrance door). (🏪 marked)
- Museum of Science: Located in the northern part of Pewter City. (Status: Not yet explored).

## Gym Leader Brock Defeated:
- Defeated on Turn 4083.
- Team:
  - GEODUDE (Level 12) - KO'd in 1 hit by GEMMY's Bubble (Critical hit!).
  - ONIX (Level 14) - KO'd in 2 hits by GEMMY's Bubble (used Bide, did nothing).
- Reward: Boulder Badge and TM34 (Bide).
- SQUIRTLE (GEMMY) reached Level 14. We took 0 damage in the gym!

## Verified Route around Pewter Gym:
- Bypassed the gym from the north side via Row 13 (columns 10 to 19) to reach the eastern corridor, then walked down column 19 to Row 26 (street level) and left to the Pokémon Center entrance at (13, 25).
- Note: A blocking NPC stands at (17, 25), and a fence covers (18, 18) to (18, 21), making the north-east direct route impassable, so the Row 13 bypass is the primary path.

<hr>

<h1><code>Locations/PalletTown</code></h1>

# Pallet Town Location Records
- Permanently verified map connections, buildings, and POIs in Pallet Town.

## GEM's House:
- Upstairs (GEM's Bedroom - Map 0_38):
  - Starting position: (3,6) facing Up.
  - TV/SNES at (3,5) (TYPE_2889). Bed at (3,4) (TYPE_2889).
  - GEM's PC at (0,1) (adjacent (0,2)), containing 1 POTION. Potion withdrawn on Turn 63.
  - Dresser at (0,6) (TYPE_2889).
  - Stairs down at (7,1) (TYPE_fed7).
- Downstairs (GEM's Living Room - Map 0_37):
  - Stairs up at (7,1) (TYPE_fed7).
  - GEM's Mom is seated at (5,4) (TYPE_3fe2).
  - Table with tea at (3,4) and (4,4) (TYPE_2889).
  - TV/cabinet at (3,5) and (4,5) (TYPE_2889).
  - Front door exit at (2,7) and (3,7) (TYPE_3fe2 warp mat).

## Overworld (Pallet Town - Map 0_0):
- GEM's House Front Door: (5,5) (exits to (5,6)).
- Northwestern boundary: Impassable fence at Row Y=1 (from X=0 to X=7).
- Route 1 Entrance (North exit): Located at Column X=10 and X=11, Row Y=0 (tall grass trigger).
- Blue's House Front Door: (13,5) (exits to (13,6)).
- Oak's Lab Entrance Door: (12,11) (exits to (12,12)).

<hr>

<h1><code>Locations/MtMoon_B1F</code></h1>

# Mt. Moon B1F Location Records

## Layout & Floor Navigation:
- **Passable Cave Floor**: TYPE_2770 is verified passable.
  - **Proof of Work**: Tested on Turn 6060 by successfully walking south from (25, 15) (TYPE_3fe2) onto (25, 16) (TYPE_2770) without collision.
- **Eastern Corridor**: Rows 14-27, Columns 24-27 are fully passable floor (TYPE_2770). Verified by traversing from (25, 15) down to (25, 23) on Turns 6530-6551.
- **Southern Corridor**: Rows 26-27, Columns 21-27 connects the eastern corridor (Columns 24-27) to the south-western area.
- **Ladders**:
  - Ladder to 1F (NE section): Located at (25, 15). Leads to Mt. Moon 1F at (25, 15).
  - Ladder to B2F (NW section): Located at (21, 17). Leads down to Mt. Moon B2F at (21, 17). Verified on Turn 7029.
  - Ladder to 1F (North-Central section): Located at (25, 9). Leads to Mt. Moon 1F at (17, 11). Verified on Turn 6689.
  - Ladder to B2F (SE section): Located at (13, 27). Leads to Mt. Moon B2F.
  - Ladder to B2F (NW section): Located at (17, 11). Leads to Mt. Moon B2F at (25, 9). Verified bidirectional connection on Turn 6929 by taking the B2F (25, 9) ladder and arriving here.
- **Ladder to 1F (Far-NW pocket)**: Located at (5, 5). Connects to Mt. Moon 1F at (5, 5). Verified on Turn 7002. Leads to an isolated north-south corridor on B1F.
- **Horizontal Corridor (Row 16/17)**: Connects the far-NW pocket's southern end at (5, 16) to the central ladder at (21, 17). Walkable floor is TYPE_2770 from column 5 to column 21, bounded by solid rock walls (TYPE_2889) at Row 15 and Row 18. This provides a direct path from the (5, 5) NW ladder of Mt. Moon 1F to the (21, 17) ladder leading to B2F.
- **Northeast Section Isolation (Verified Turn 8827)**:
  - The northeast area around the (25, 9) ladder is an isolated pocket on B1F. Column 25 is blocked at Row 12 and Row 13 by solid rock walls (TYPE_2889). Row 12 of columns 21-27 consists of solid rock (TYPE_2889), preventing any southern traversal to the eastern/southern corridors of B1F.

<hr>

<h1><code>Locations/PewterCity_Gym</code></h1>

# Pewter City Gym (Map 0_54) Location Records

## Connections:
- Southern exit door is at (4, 13) / (5, 13) which warps back to Pewter City (Map 0_2) at (16, 17).

## Layout & Spatial Features:
- Entrance area:
  - Player spawns at (4, 13) facing UP.
  - Pillars/statues are located on the left and right:
    - Left pillar: (3, 9) and (3, 10) of TYPE_2889.
    - Right pillar: (6, 9) and (6, 10) of TYPE_2889.
  - Central pathway: Columns 4 and 5 are open, clear paths of TYPE_3fe2 going north.

## NPCs & Interactions:
- Gym Guide: Standing at (7, 10). (Status: Not yet interacted).
- Gym Trainer: Standing at (3, 6) facing RIGHT. (Status: Defeated on Turn 3928. Reward: ¥220. GEMMY reached Level 12).
- Gym Leader Brock: Standing at (4, 1) (Status: Defeated on Turn 4083. Reward: Boulder Badge and TM34 Bide).

<hr>

<h1><code>Locations/ViridianCity</code></h1>

# Viridian City Location Records
- Permanently verified map connections, buildings, and POIs in Viridian City.

## Connections:
- South exit connects to Route 1 (Map 0_12) at Viridian City Column X=20 and X=21 (Row Y=35).
- North exit leads towards Route 2 / Viridian Forest.
- West exit leads to Route 22.

## Key Buildings & POIs:
- Pokémon Center: Located on Columns X=22 to X=24, with its entrance door at (23, 25).
- Trainer School: Located on Columns X=20 to X=23, rows Y=14 to Y=15, with its entrance door at (21, 15). Inside (Map 0_43), there is a student at (3, 5) and teacher at (4, 1).
- Poké Mart: Located on Columns X=29 to X=32, rows Y=17 to Y=19, with its entrance door at (29, 19) and "MART" sign at (30, 19).
  - Inside (Map 0_42), the clerk at (1, 4) hands over OAK's PARCEL (delivered on Turn 461) and subsequently sells standard items.
  - Verified Shop Inventory (Turn 832):
    1. POKE BALL (¥200)
    2. ANTIDOTE (¥100)
    3. PARLYZ HEAL (¥200)
    4. BURN HEAL (¥250)
    5. CANCEL
  - Note: Potions are NOT sold at the Viridian City Poké Mart.
- Map Layout & Points of Interest:
  - Viridian Gym: Located in the northeastern section of the city. Doors are locked, and the gym leader is currently away.
  - Old Man: Located in the northern part of the city. He initially blocks the path to Route 2, complaining about not having his coffee. After delivering Professor Oak's Parcel, he is no longer blocking the road and can teach the player how to catch Pokémon.
  - Center Pond: A large water pond is located in the center of the city.
  - Cut Tree: A small cuttable tree is located near the southern entrance, which can be cut down once HM01 (Cut) is obtained.
  - Route Connections:
    - Route 1 Exit/Entrance: (20, 35) and (21, 35).
    - Route 2 Exit/Entrance: (18, 0).
    - Route 22 Exit/Entrance: (0, 18) and (0, 19).

<hr>

<h1><code>Locations/Route3</code></h1>

# Route 3 (Map 0_14) Location Records

## Connections:
- West exit connects directly to Pewter City (Map 0_2) at (0, 10) via map boundary transition.
- East exit connects to Route 4 West / Mt. Moon Exterior (Map 0_15) at (59, 0) and (61, 0) via northern boundary map connections.

## Structural Layout & Key Pathing:
- **Northern and Southern Corridors**: The map is split horizontally by a ledge on Row 7.
- **Row 4 & Row 5 Passageway**:
  - Column 17 has solid trees (TYPE_2889) blocking Rows 6-10.
  - Rows 4 and 5 at Column 17 are completely clear of trees (TYPE_3fe2), providing the primary passageway to go east from the western section.
  - Note: Bug Catcher Greg stands at (19, 5), so walking east requires using Row 4 to bypass him.
- **Row 7 Horizontal Ledge**:
  - Separates the northern area (Rows 4-6) from the southern area (Rows 8-10).
  - Ledge Gap at (11, 7): Flat ground (TYPE_3fe2), completely passable in both directions (verified on Turn 7319). Allows bypassing the horizontal ledge on Row 7 by walking north from (11, 9) to (11, 6).
  - Ledge Gap at (15, 11): Flat ground (TYPE_3fe2), completely passable in both directions (verified on Turn 4360). Allows bypassing the tree line by moving between (15, 11) and (15, 12).
  - Ledge Gap at (27, 7): Flat ground (TYPE_3fe2), completely passable in both directions (verified on Turn 7365). Allows bypassing the rock wall at column 28 by moving south to Row 8, then east.
  - Ledge Gap at (31, 7): Flat ground (TYPE_3fe2), completely passable in both directions (verified on Turn 7256). Allows access to the northern section from (31, 8).
  - Ledge Gap at (49, 7): Flat ground (TYPE_3fe2), completely passable in both directions (verified on Turn 7662). Allows crossing between northern and southern corridors at Column 49. (↔️ marked)
- **Eastern Blockage (Columns 28-31)**:
  - Rows 4-7 are occupied by a massive mountain wall of TYPE_2889 starting at Column 28, blocking direct eastern progression on those rows.
  - **Empirical Collision Verification**: Physically tested on Turn 7355. Walking Right from (27, 5) against the wall at (28, 5) resulted in zero movement, confirming the wall is solid and impassable.
  - To continue east towards Mt. Moon, players must walk south through the (27, 7) ledge gap onto Row 8 or Row 9, which are completely clear of mountain walls to the east.

## Inactive Tall Grass Patch:
- The westernmost tall grass patch at (2, 10) (Rows 8-11, Columns 2-5) has disabled or extremely rare wild spawns. Verified on Turn 4982: we took 150 overworld steps (15 loops) with exactly zero wild encounters.

## Defeated Trainers:
- Bug Catcher Colton at (10, 6)
- Youngster Albert at (14, 5)
- Lass Janice at (15, 9)
- Bug Catcher Greg at (19, 5)
- Lass at (23, 4)
- Bug Catcher at (24, 6)
- Youngster Ben at (22, 9)
- Lass at (33, 9)

<hr>

<h1><code>Locations/Route1</code></h1>

# Route 1 Location Records
- Permanently verified map connections, layout features, and key points of interest on Route 1.

## Connections:
- South exit connects to Pallet Town (Map 0_0) at Route 1 Column X=10 and X=11 (Row Y=35).
- North exit connects to Viridian City (Map 0_1) at Route 1 Column X=10 and X=11 (Row Y=0).

## Layout & Spatial Features:
- Between Y=35 and Y=32: A narrow corridor of tall grass (TYPE_fed7) flanked by impassable fences (TYPE_2889) at X=9 and X=12.
- At Y=31: A clear path (TYPE_3fe2) begins.
- At Y=27: A one-way southward ledge (TYPE_44f6) blocks straight north movement on Columns X=10 to X=15.
- Row Y=27 Ledge:
  - Northbound Bypass: Walk Left to Column X=8 (clear path at (8,31) and (8,30)), then proceed north through Columns X=6, X=7, or X=8.
  - Southbound Bypass: Jump directly south over the ledge from Column X=4 (Turn 341).
- Row Y=5 Ledge:
  - Northbound Bypass: The Row 5 ledge (TYPE_44f6) blocks Columns X=6 to X=13. Columns X=14 and X=15 are completely open clear path (TYPE_3fe2) at (14,5) and (15,5). To bypass, walk Right to Column X=14 or X=15, and head north to Viridian City.
  - Southbound Bypass: Jump directly south over the ledge from (10,4) to (10,6) (Turn 262).

## Key Interactions & POIs:
- Poké Mart Clerk NPC: Located at (5, 24). Talked to him on Turn 182 and received a free POTION.
- Wild Pokémon: Tall grass contains wild Pidgey and Rattata (verified Turn 194). SQUIRTLE leveled up to Level 7 here.

<hr>

<h1><code>Mechanics/General</code></h1>

# General Mechanics & Controls
- Verified basic game mechanics, controls, and UI behaviors.

## Battle Mechanics:
- Turn-based combat. First starter battle triggers immediately after selecting starter and rival picking theirs.
- Lead Pokémon (first slot) is automatically sent out first.
- HP (Hit Points) represents health. Our starter SQUIRTLE (GEMMY) starts with 20 max HP.
- Moves have PP (Power Points) representing usage limits. SQUIRTLE's Tackle has 35 PP, Tail Whip has 30 PP.

## Overworld Navigation:
- PC in player's room can store items. Potion withdrawn on Turn 62 successfully.
- Warps (stairs, doors) transition between maps and are activated by walking onto them.

## Ledge Mechanics:
- Ledges (TYPE_44f6) are one-way drop-offs.
- Verified on Turn 262: Moving South (Down) from (10, 4) to (10, 6) over a ledge at (10, 5) successfully jumps over the ledge.
- Moving North (Up) against a ledge is impassable.
- **Ledge Blockage Mechanic (Verified Turn 6981)**:
  - **Verified Fact**: A ledge jump (such as jumping south from (3, 17) over the (3, 18) ledge to (3, 19) on Mt. Moon 1F) is completely blocked and impassable in both directions if its landing tile (Row 19) is occupied by a solid, impassable obstacle (such as the rock wall at (3, 19)). Ledges cannot be jumped if the landing tile is solid rock/wall.

## Pokémon Center Counter Mechanics:
- Test 4: Left Counter Tile Interaction Check
  - **Hypothesis**: The player can interact with Nurse Joy from (3, 3) facing Up (the left counter tile) to heal their Pokémon, bypassing the blocking NPC at (4, 3).
  - **Methodology**:
    - Turn 1679: Standing at (3, 3) facing Up.
    - Action: Press 'A' to interact with the counter directly above us at (3, 2).
    - Verification: Check if Turn 1687 state shows the Pokémon Center healing dialogue on screen.
  - **Results**:
    - Turn 1687: Successfully verified! The screen shows "Shall we heal your POKéMON?" and the interactive menu `▶HEAL / CANCEL` is open, with the cursor pointing at `▶HEAL`.
    - **Conclusion**: Confirmed! In Generation 1, you can talk to Nurse Joy and heal your Pokémon from the left counter tile (3, 3) facing Up. You do not need to stand in the center (4, 3). This is an incredibly useful mechanic to bypass any NPC blocking the center counter spot.

## Verified Route 2 Mechanics:
### Test 1: Red Flower Tile Collision Check
- **Hypothesis**: Red flower tiles (visually red flowers, system tile type `TYPE_3fe2`) are passable and do not block player movement.
- **Results**: Verified on Turn 1042. Player successfully moved from (4, 66) to (5, 66) (a red flower tile). Red flower tiles are passable.

### Test 2: Route 2 Southern Tall Grass Patch Wild Encounters Check
- **Hypothesis**: Tall grass tiles (TYPE_3fe2) in the southern portion of Route 2 (Columns 8 & 9, Rows 61-67) contain wild Pokémon encounters.
- **Results**: Completed on Turn 1411. Player took 42 cumulative steps on these tiles between Turn 1052 and Turn 1411 without triggering a single wild encounter. Consistently negative. Encounters on this specific grass patch are either disabled or extremely rare.

### Test 3: Route 2 Northern Tall Grass Patch Wild Encounters Check
- **Hypothesis**: The TYPE_fed7 tall grass patch (starting at Y=51, Columns X=4 to X=9) contains active wild encounters.
- **Results**: Completed on Turn 1554. On Turn 1537, at 13 cumulative steps, we triggered a wild Level 4 PIDGEY encounter (captured as BIRBIE). The northern tall grass patch contains active wild encounters.
## Gen 1 Battle Move Menu Structure Insight (Turn 4492 Verification):
- In Pokémon Red/Blue, the battle moves menu is a single vertical column of 4 moves, NOT a 2x2 grid.
  - Position 1 (top): Move 1 (TACKLE)
  - Position 2: Move 2 (TAIL WHIP)
  - Position 3: Move 3 (BUBBLE)
  - Position 4 (bottom): Move 4 (WATER GUN)
- The moves menu remembers its last selected position. If you used Move 2 last round, the cursor starts on Move 2.
- The menu allows wrapping. Pressing Up on the 1st move wraps down to the 4th move. Pressing Down on the 4th move wraps up to the 1st move. Verified on Turn 4492!

## Item Pickup Collision Mechanic:
- **Hypothesis**: Poké Ball items on the floor in Gen 1 are solid sprites that block player movement. To collect them, the player must stand adjacent, face them, and press 'A' to interact, rather than walking onto them.
- **Verification**: On Turn 6803, standing at (28, 5) facing Right towards the Poké Ball item at (29, 5), pressing 'A' successfully collected the item (TM01 - Mega Punch), and the item sprite disappeared, proving that items on the floor are solid sprites in Generation 1.
- **Conclusion**: Floor item sprites are indeed solid and impassable. They must be collected by standing adjacent, facing them, and pressing 'A'.
## Gen 1 Confusion Move PP Consumption (Turn 12533 Verification):
- **Verified Fact**: In Generation 1, if a Pokémon selects a move but hurts itself in confusion instead of attacking, 1 PP is still consumed from the selected move. Verified on Turn 12532/12533: GEMMY selected BITE (starting at 22 PP), hurt itself in confusion, and BITE's PP was successfully reduced to 21 despite the move not executing.

## S.S. Anne Sprite Wrapping and rendering duplicate protocol
- When exploring upper floors on a horizontal edge boundary (such as Column 13 of Map 0_100), Gen 1's engine edge-wraps and duplicates the sprite slots of the adjacent loaded map.
- These rendering artifacts can execute the dialogue script of the underlying RAM sprite slots (e.g., interacting with Bug Catcher at (11, 13) on Map 0_100 executed the Kitchen Sailor's script).
- **Verification Rule:** If an NPC is positioned at the extreme boundary column of an indoor map section, confirm its physical collision and speech script. If it mimics an NPC from another floor, document it as a mirrored duplicate and skip combat/grinding assumptions for that duplicate.

## Randomized ROM Mechanics (Verified Turn 17672):
- **Hidden Items Rule**: In this randomized ROM, standard hidden item locations (such as the S.S. Anne Kitchen trash cans or similar spots) are completely scrambled or empty. To prevent wasting turns, do not systematically search vanilla hidden item spots (including the Vermilion Gym trash cans for items, except when mathematically/mechanically necessary for puzzle progression).

<hr>

<h1><code>Locations/Route2_North</code></h1>

# Route 2 Northern Side (Map 0_13) Location Records
- Track connections, layout, and safety routes between the Northern Gatehouse and Pewter City.

## Connections:
- Southern entrance: Route 2 Gatehouse (North) door at (3, 15).
- Northern entrance: Leads directly into Pewter City (Map 0_03).

## Spatial Layout:
- Player exits gatehouse at (3, 11) facing UP.
- There is a patch of tall grass (TYPE_fed7) from X=0 to X=7 around Row Y=7.
- Safety Bypass: A clear path of TYPE_3fe2 exists at Column X=8, allowing us to walk around the tall grass to avoid wild encounters.
- Cuttable tree is located at (5, 10) (TYPE_5519).

<hr>

<h1><code>Locations/MtMoon_Exterior</code></h1>

# Route 4 West / Mt. Moon Exterior (Map 0_15) Location Records

## Overview & Connections:
- Map 0_15 is the western portion of Route 4, commonly referred to as the Mt. Moon Exterior area.
- This area acts as a crucial transition zone between Route 3 (Map 0_14) and the entrance to Mt. Moon 1F.
- Southern boundary warps connect directly back to Route 3 (Map 0_14) at (9, 17) and (11, 17).
- East cave entrance warp leads directly into Mt. Moon 1F at (14, 35). This transition is located at (18, 5) on Map 0_15.

## Key Buildings & Points of Interest:
- **Mt. Moon Pokémon Center**: Located at (11, 5) on Map 0_15. Inside, Nurse Joy stands at the counter to heal our team. It also has a PC for storing/restoring Pokémon and items, and an NPC who sells a Magikarp for ¥500. This is an extremely useful checkpoint for healing during team training.
- **Mt. Moon 1F Main Cave Entrance**: Located at (18, 5) on Map 0_15. Walking into this dark cave opening warps the player directly into Mt. Moon 1F at (14, 35). This is the primary gateway to progress through Mt. Moon to reach Route 4 East and Cerulean City.

## Structural Layout & Key Pathing:
- **Southern Corridor (Row 17-18)**: This is where players spawn when entering Map 0_15 from Route 3.
  - The map boundary at (9, 17) and (11, 17) is completely bidirectional.
- **Row 15 Ledge Barrier**:
  - Row 15 contains south-facing ledges (TYPE_44f6) across columns 6 to 9. These ledges allow players to jump south from the northern area to the southern corridor, but completely block horizontal/vertical progression when walking north.
  - Column 10 (10, 15) is a flat, passable grass tile (TYPE_3fe2), providing a key vertical corridor that allows players to safely walk north from the southern corridor to the main northern area.
  - Column 11 (11, 15) is also a flat, passable grass tile (TYPE_3fe2).
- **Ledges at Row 17 (Columns 12-13)**:
  - There are south-facing ledges at (12, 17) and (13, 17) that block players from walking east along the southern edge of the map, forcing navigation north through the column 10/11 corridor.
- **Northern Plains & Grinding Area**:
  - The main northern area (Rows 5-14) consists of open pathways, grass, and mountain borders.
  - Our team members can be trained in the grass here before entering Mt. Moon. This is an incredibly useful area to grind if we need.

<hr>

<h1><code>Reflection/Turn7412</code></h1>

# 50-Turn Self-Assessment & Reflection (Turn 7412)

## 1. Progress & Execution:
- We have successfully navigated across the Mt. Moon Exterior (Map 0_14) after bypassing Pewter City and Route 3.
- We bypassed major overworld blockages (column 17 trees, Greg, Lass, and the eastern mountain wall) and reached the cave entrance at (47, 4).
- We completed an empirical collision test on the left door tile (47, 3) on Turn 7406 and found it solid. We are now immediately testing the right door tile (48, 3) to find the warp.

## 2. Notepad Hygiene & Strategy:
- Completed a major reorganization of 'Locations/MtMoon_Exterior' and 'Scratchpad/Route3_MtMoon_Cerulean'.
- Removed all play-by-play overworld turn journals, converting them into structured reference-grade permanent facts with cited empirical proof of work.
- Decided to stop running redundant path-checking 'run_code' scripts to avoid over-planning paralysis and turn lag.

## 3. Map Hygiene:
- Placed strategic map markers at (11, 7) and (37, 7) to record the bidirectional ledge gaps on this map.
- Kept trainer markers up-to-date for defeated NPCs.

## 4. Custom Tools Evaluation:
- We have the custom tool 'heal_pokemon_at_counter' which is highly robust.
- Five discrete future tools to consider:
  1. 'grind_wild_exp' - Automates grass grinding and switch-training.
  2. 'find_path_overworld' - A general A* pathfinding script using tile properties.
  3. 'test_adjacent_warps' - Automates walking to and testing doors/warps.
  4. 'use_items_in_battle' - Evaluates when to heal/status-cure in combat.
  5. 'route_trainer_bypass' - Computes paths that minimize trainer sightlines.

## 5. Goals & Strategy:
- Primary Goal: "Traverse Mt. Moon to reach Route 4" (Clear WHAT).
- Secondary Goal: "Enter Mt. Moon 1F via the entrance" (Clear WHAT).
- All specific navigation methods (HOW) are safely documented in our scratchpad and location records.

<hr>

<h1><code>Reflection/Turn7883</code></h1>

# 50-Turn Self-Assessment & Reflection (Turn 7883)

## 1. Progress & Strategic Achievements:
- Successfully performed direct collision testing on the Row 19 and Row 21 platform boundaries on Mt. Moon 1F, scientifically proving they are solid rock walls (TYPE_2889).
- Migrated these verified physical constraints to the permanent 'Locations/MtMoon_1F' notepad.
- Kept our 'Scratchpad/Route3_MtMoon_Cerulean' clean and in sync at Turn 7873 (standing at (16, 24)).

## 2. Evaluation of 5 Discrete Custom Tools & Agents:
1. `find_path_astar` (Custom Tool): A Python-based A* pathfinder that uses map tile grids to output step-by-step button sequences. Worth adding for long cavern maps.
2. `battle_strategy_engine` (Custom Agent): An LLM-based agent to analyze enemy Pokémon and moves to output battle options. Low priority because GEMMY at level 20 dominates easily.
3. `exp_tracker` (Custom Tool): A tool to track, analyze, and estimate grinding times and remaining EXP. Worth adding to avoid "Time Blindness".
4. `map_maker` (Custom Agent): An agent dedicated to formatting and keeping town/dungeon POI lists clean. Worth adding to maintain perfect reference-grade records.
5. `ledge_jump_evaluator` (Custom Tool): A tool to verify if a ledge is jumpable based on landing-tile types. Useful but highly specialized.

## 3. Goals & Roadmap:
- Primary Goal: Traverse Mt. Moon to reach Route 4 East.
- Secondary Goal: Reach Mt. Moon B2F NW section via B1F NW pocket.
- Next Steps: Move east along Row 24 to Column 25 (Eastern Corridor), then head north to Row 15 to access the northern corridors.

<hr>

<h1><code>Archive/MtMoon_ExplorationHistory</code></h1>

# Mt. Moon Historical Exploration Archive

## Northeastern Section Systematic Exploration Live Log (Turn 10460):
- Starting Turn: 10460
- Starting Timestamp: Monday, May 25, 2026 at 3:15 PM PDT
- Current Position: (32, 9)
- Visual Map Data from `<CurrentScreen turn="10460">`:
  - Columns 32 to 35, Rows 5 to 11 are visible on screen.
  - Let's map out the tiles:
    - Row 9:
      - (32, 9): Player standing here (TYPE_3fe2).
      - (33, 9): TYPE_2889 (solid rock wall).
      - (34, 9): TYPE_3fe2 (cavern floor).
      - (35, 9): TYPE_3fe2 (cavern floor).
    - Row 8:
      - (32, 8): TYPE_3fe2 (cavern floor).
      - (33, 8): TYPE_3fe2 (cavern floor).
      - (34, 8): TYPE_3fe2 (cavern floor).
      - (35, 8): TYPE_3fe2 (cavern floor).
    - Row 7:
      - (32, 7): TYPE_3fe2 (cavern floor).
      - (33, 7): TYPE_3fe2 (cavern floor).
      - (34, 7): TYPE_3fe2 (cavern floor).
      - (35, 7): TYPE_3fe2 (cavern floor).
    - Row 6:
      - (32, 6): TYPE_3fe2 (cavern floor).
      - (33, 6): TYPE_3fe2 (cavern floor).
      - (34, 6): TYPE_3fe2 (cavern floor).
      - (35, 6): TYPE_3fe2 (cavern floor).
    - Row 5:
      - (32, 5): TYPE_2889 (solid rock wall).
      - (33, 5): TYPE_2889 (solid rock wall).
      - (34, 5): TYPE_2889 (solid rock wall).
      - (35, 5): TYPE_2889 (solid rock wall).
  - This is fascinating! Row 5 is a solid rock wall (TYPE_2889) on Columns 32-35.
  - This means the northern wall of this area is at Row 5.
  - Let's look further left on Row 5:
    - (31, 5): TYPE_2889 (solid wall)
    - (30, 5): TYPE_2770 (cavern floor)
    - (29, 5): TYPE_2770 (cavern floor)
    - (28, 5): TYPE_2770 (cavern floor)
  - Wait, columns 28 to 30 on Row 5, 6, 7 are accessible?
    - Yes, (29, 5) is where we collected TM01!
  - Let's check Row 6 and Row 7:
    - (31, 6) is TYPE_2889 (solid rock wall).
    - (30, 6) is TYPE_2770 (cavern floor).
    - (31, 7) is TYPE_2889 (solid rock wall).
    - (30, 7) is TYPE_2889 (solid rock wall).
    - (29, 7) is TYPE_4b8d (stairs).
    - (28, 7) is TYPE_4b8d (stairs).
  - This means Column 31 is a solid wall on Rows 5, 6, 7.
  - Wait, is Column 31 a solid wall on Rows 8, 9, 10, 11?
    - Let's look at the screen for Turn 10460:
      - (31, 8) is TYPE_3fe2.
      - (31, 9) is TYPE_3fe2.
      - (31, 10) is TYPE_3fe2.
      - (31, 11) is TYPE_3fe2.
    - These are cavern floors! This means there is a gap/passage between Column 31 and Column 32 on Rows 8 to 11.
  - Wait, let's look at Columns 36 and 37:
    - Column 36:
      - (36, 5): TYPE_2770
      - (36, 6): TYPE_2770
      - (36, 7): TYPE_2770
      - (36, 8): TYPE_2889 (solid rock)
      - (36, 9): TYPE_2889 (solid rock)
      - (36, 10): TYPE_2889 (solid rock)
      - (36, 11): TYPE_2889 (solid rock)
      - (36, 12): TYPE_2770
    - This means Column 36 is solid from Row 8 to Row 11!
    - So the cavern's eastern boundary on Rows 8-11 is at Column 36.
  - Let's find out what is in this open area (Columns 32-35, Rows 6-8):
    - Wait! Is there an NPC or item here?
    - On the screen, we see some sprite at (33, 9)? Wait, (33, 9) is TYPE_2889 (rock wall).
    - Wait! Is there any NPC in Columns 32-35 on Rows 6-8?
    - On the screen of Turn 10460, there is a giant blue-ish/gray-ish dome-shaped sprite at (33, 9)? No, wait, (33, 9) has a round rock sprite, which is the standard rock wall tile TYPE_2889.
    - Wait, Rows 6, 7, 8: they are completely empty cavern floor.
    - Wait, is there anything further to the right or left?
    - Let's walk north:
      - From (32, 9), walk Up to (32, 8).
      - From (32, 8), walk Right to (35, 8) to explore Row 8.
      - Let's walk to (35, 8):
        - Up 1 to (32, 8)
        - Right 3 to (35, 8)
- Turn 10486: Standing at (35, 7) on Map 0_61 (B2F). We have arrived at (35, 8) on Turn 10461 and moved to (35, 7) on Turn 10475.
- Cliff Boundary Discovery (Turn 10476): We attempted to walk Right from (35, 7) onto (36, 7) and directly collided with an impassable cliff face (visited 0 tiles). This empirically proves that Column 36 (Rows 4-7) is an elevated upper platform (TYPE_2770), and Column 35 is on the lower level (TYPE_3fe2). There is a vertical cliff boundary separating them, making the eastern elevated chamber currently inaccessible from this lower eastern area.

## B1F Column 25 Eastern Boundary Verification (Turn 10549):
- **Objective**: Physically test if Column 25 is a solid, impassable wall blocking any eastern traversal to Column 26 on Rows 8, 10, and 11.
- **Hypothesis**: Column 26 on Rows 8, 10, and 11 is solid rock, meaning Column 25 is the eastern boundary of B1F in this section.
- **Visual Check (Turn 10549)**: Standing at (24, 10), we can see:
  - (25, 9) is indeed a ladder (labeled TYPE_3fe2).
  - (25, 10) is labeled TYPE_2770, which is passable floor.
  - (25, 8) is labeled TYPE_2770, which is passable floor.
  - (25, 11) is labeled TYPE_2770, which is passable floor.
  - Column 26 on Rows 8, 9, 10, and 11 is labeled TYPE_2889 (solid rock).
- **Physical Test Plan**:
  - 1. Standing at (24, 10), walk Right to step onto (25, 10).
  - 2. Facing Right at (25, 10), press 'Right' to attempt to step onto (26, 10) (labeled TYPE_2889).
  - 3. Verify if player collides or is blocked, proving that Column 26 is impassable.
- **Execution of Step 1 (Turn 10550)**: Walk Right 1 step to stand on (25, 10).
- **Execution of Step 2 (Turn 10555)**: From (25, 10), pressed Right to walk into (26, 10) (labeled TYPE_2889).
- **Result (Turn 10556)**: Player collided with the wall (visited 0 tiles) and remained at (25, 10).
- **Final Verification Conclusion**: Column 26 is physically verified as solid rock wall and completely impassable. This definitively disproves the hypothesis of an eastern passage on B1F in this section. The B1F northeast section is indeed a completely isolated pocket. We must seek another way to access the eastern elevated chamber on B2F.
- **Next Action Plan**:
  - We will backtrack by taking the (25, 9) ladder up to 1F (17, 11).
  - From there, we will proceed to 1F (17, 17) -> 1F (11, 17) -> 1F (5, 5) -> B1F (5, 5) -> B1F (21, 17) -> B2F (21, 17) to access the Central Platform.
  - On the Central Platform, we will walk east down the stairs at (26, 15)/(27, 15), walk east past the Rocket Grunt at (29, 17) to (34, 13) or (35, 13), and systematically test the vertical passability of Row 12 on Columns 34 and 35. This is our primary remaining unexplored route on B2F!

<hr>

<h1><code>Locations/CeruleanCity</code></h1>

# Cerulean City Location Records

## Layout & Exploration:
- Entered Cerulean City from Route 4 West at (0, 18) on Turn 11225.
- The entry path runs east along Row 18 & Row 19, bounded by water (TYPE_4e8c) to the north (Rows 14-16) and a rock wall (TYPE_2889) to the south (Row 20, Columns 0-4).
- **Ledge Bypass Route (Verified Turn 12113)**:
  - Column 8 at Row 15 is a flat, clear pathway (TYPE_3fe2) between the western rock wall (Column 7) and the ledges (Columns 9-11).
  - This provides a completely open, bidirectional path connecting the southern street (Row 18) and the northern area (Row 14), allowing players to walk back north after visiting the Pokémon Center.

## Points of Interest:
- **Cerulean Pokémon Center**: Located at (19, 17) on Map 0_3. Inside, Nurse Joy is at (3, 1) and can heal our team. The counter is at Y=2 and we can interact with Nurse Joy through the counter (3, 2) from (3, 3) facing Up (the left counter tile).
- **Cerulean Poké Mart**: Located at (25, 25) on Map 0_3. The door is at (25, 25) with a passable tile in front of it at (25, 26).
  - **Interior Layout (Map 0_67)**:
    - Clerk/Cashier NPC: Standing behind the counter at (0, 5). To talk to them, stand at (2, 5) facing Left.
    - Customer NPC 1 (green hair): Stands/wanders on Column 3 (e.g., at (3, 6) or (3, 7)), gives a tip about using REPEL.
    - Customer NPC 2 (brown hair): Stands/wanders on Rows 2-3 near the shelves (e.g., (6, 2) or (7, 2)).
    - **Verified Poké Mart Inventory (Turn 11629)**:
      - POKé BALL: ¥200
      - POTION: ¥300
      - REPEL: ¥350
      - ANTIDOTE: ¥100
      - BURN HEAL: ¥250
      - AWAKENING: ¥200
      - PARLYZ HEAL: ¥200
- **Unknown Blue-Roofed Building (Left)**: Located at Columns 18-23, Rows 24-25. It has no entrance on its south side (Row 25) which consists of solid brick wall (TYPE_2889).
- **Unknown Blue-Roofed Building (Right)**: Located at Columns 28-30, Rows 24-25. It blocks rows 24-25. No south entrance is visible. Row 22 and 23 above it are passable.
- **Cerulean Bike Shop (Map 0_66)**: Entrance door at (13, 25) in Cerulean City, with a passable tile in front at (13, 26). Inside, the shop owner is behind the counter at (6, 2). Bicycles cost ¥1,000,000, which is physically impossible to buy with money (wallet limit is ¥999,999). To get a Bicycle, we must obtain the Bike Voucher from the Pokémon Fan Club in Vermilion City and exchange it here. Do NOT attempt to grind money for it! 
- **Cuttable Bush**: Located at (19, 28) (TYPE_5519) within the Row 28 tree boundary. It blocks south access on column 19.
- **Overworld Obstacles**: A signpost at (17, 29) and fence at (16, 29) block Y=29 south passage on columns 16-17, even though Y=28 is passable there.

## NPCs & Dialogues:
- **Slowbro**: Standing at (28, 26) in Cerulean City. Talking to it yields: "SLOWBRO ignored orders..."
- **Girl NPC**: Standing at (29, 26) in Cerulean City, next to the Slowbro. She tells us about Slowbro and orders.

## Trainers:
- None met yet.
- **Badge Describer Door**: Located at (9, 11) in northern Cerulean City (Map 0_3). Leads to Badge Describer's House (Map 0_230). Unlocked after helping Bill.
- **Trade House Door**: Located at (13, 15) in northern Cerulean City (Map 0_3). Leads to In-Game Trade House (Map 0_63) where an NPC trades JYNX for POLIWHIRL.
- **Burglarized House (Map 0_62)**: Located at the northeastern part of the city.
  - **Front Door**: Entrance is at (27, 11) on Map 0_3 (marked with 🚪 map marker). Spawns player at (2, 7) inside Map 0_62 facing Up.
  - **Back Exit (Hole in Wall)**: Located at (3, 0) inside Map 0_62. Walking onto it spawns the player in the backyard of the house at (27, 9) on Map 0_3.
  - **Route 9 Passage**: From the backyard at (27, 9), walk east to Columns 32-33, walk south to Row 16, and walk east through (38, 16) and (39, 16) to cross the map boundary and enter Route 9. Fully verified on Turn 19929.

<hr>

<h1><code>Locations/CeruleanCity_Gym</code></h1>

## Overview & Transition:
- Entered from (30, 19) in Cerulean City on Turn 11456.
- Spawns us at (4, 13) inside the Gym.
- Leading Pokémon: SPARKY (PIKACHU, Level 11).

## Gym Guide Advice (Turn 11465):
- Advice: "The LEADER, MISTY, is a pro who uses water POKéMON! You can drain all their water with plant POKéMON! Or, zap them with electricity!"

## Layout & Exploration:
- Gym Guide is standing at (7, 10).
- Entrance corridor leads from (4, 13) to (4, 11) / (7, 11).
- Floor contains large water pools (TYPE_4e8c) and solid platforms.

## Trainers Defeated:
- [x] Swimmer ♂ at (6, 7): Defeated on Turn 11502. Team: Level 16 HORSEA, Level 16 SHELLDER. Sparky and Gemmy switch-trained. Received ¥80!
- [x] Jr. Trainer ♀ at (2, 3): Defeated on Turn 14511. Team: Level 19 GOLDEEN. Gemmy switch-trained and leveled up to 27! Received ¥380!
- [x] Gym Leader Misty at (4, 2): Defeated on Turn 14547. Team: Level 18 STARYU, Level 21 STARMIE. Gemmy swept with DIG! Received Cascade Badge and TM11 (Bubblebeam)!

## Misty Defeated (Turn 14547):
- Successfully challenged and defeated Gym Leader Misty using GEMMY (WARTORTLE) with TM28 Dig, earning the Cascade Badge and TM11 (Bubblebeam). This completed our Gym objective.

<hr>

<h1><code>Mechanics/PikachuTrainingAndGrindingPlan</code></h1>

# Mechanics/PikachuTrainingAndGrindingPlan (Updated Turn 25337)

- Current State & Combat Status (Turn 25337):
- **Level**: 24
- **Current Moves & PP**:
  - THUNDERSHOCK (PP: 24)
  - GROWL (PP: 40)
  - THUNDER WAVE (PP: 20)
  - QUICK ATTACK (PP: 30)
- **Current Stats**: HP: 6/57. We are exploring Rock Tunnel B1F. SPARKY's THUNDERSHOCK PP is at 24.
- WARTORTLE is Level 33, HP: 80/93. PP of Moves: DIG (10), TAIL WHIP (30), BITE (16), WATER GUN (14).
- Synchronized to Turn 25337.

---

## Species Empirical Stats & Combat Readiness Summaries:
The following summaries are compiled from empirical tests conducted in Route 25 tall grass:

### 1. PIDGEY (Lv 13 - Flying/Normal)
- **Speed Tier**: SPARKY consistently outspeeds under normal priority (100% of trials).
- **Offensive Output**: Thundershock (super-effective, 2.0x) is a guaranteed 1HKO (100% damage).
- **Survival Margin**: 0 damage taken (faints before it can move).
- **EXP Yield**: 102 EXP.
- **Combat Recommendation**: Ideal lead matchup. Use Thundershock for 1HKO.

### 2. CATERPIE (Lv 8 - Bug)
- **Speed Tier**: SPARKY consistently outspeeds (100% of trials).
- **Offensive Output**: Thundershock (neutral, 1.0x) is a guaranteed 1HKO.
- **Survival Margin**: 0 damage taken.
- **EXP Yield**: 60 EXP.
- **Combat Recommendation**: Defeat immediately with Thundershock.

### 3. METAPOD (Lv 9 - Bug)
- **Speed Tier**: SPARKY consistently outspeeds (100% of trials).
- **Offensive Output**: Thundershock (neutral, 1.0x) is a guaranteed 2HKO (~80-85% damage on Hit 1).
- **Survival Margin**: 0 damage taken (consistently uses Harden).
- **EXP Yield**: 100+ EXP (based on level).
- **Combat Recommendation**: Use Thundershock or Quick Attack to defeat.

### 4. BELLSPROUT (Lv 12-13 - Grass/Poison)
- **Speed Tier**: SPARKY consistently outspeeds under normal priority (100% of trials).
- **Offensive Output**: Thundershock is resisted (0.5x). QUICK ATTACK (neutral, 1.0x) is a guaranteed 2HKO on Lv 13 (~55% damage per hit).
- **Survival Margin**: Took 0 damage (Bellsprout consistently uses Growth on Turn 1, faints before attacking).
- **EXP Yield**: 144 EXP (Lv 12), 156 EXP (Lv 13).
- **Combat Recommendation**: Use QUICK ATTACK to conserve Thundershock PP, bypass resistance, and 2HKO safely.

### 5. ABRA (Lv 12 - Psychic)
- **Behavior**: Always uses Teleport on Turn 1 under normal priority.
- **Capture Testing**: Threw Poké Balls on Turn 1 on multiple occasions. Abra broke free instantly on the first wobble and escaped.
- **Resource Trade-Off**: Extremely low catch rate on Turn 1. Throwing Poké Balls wastes valuable resources (¥200 per ball) and yields 0 EXP.
- **Grinding Protocol**: Do NOT throw Poké Balls. Run from wild Abras or use high-priority moves (Quick Attack) to defeat them if we can 1HKO. Running is the preferred zero-cost option.

### 6. KAKUNA (Lv 7 - Bug/Poison)
- **Speed Tier**: SPARKY consistently outspeeds (100% of trials).
- **Offensive Output**: THUNDERSHOCK (neutral, 1.0x) is a guaranteed 1HKO (100% damage).
- **Survival Margin**: 0 damage taken.
- **EXP Yield**: 71 EXP.
- **Combat Recommendation**: Use THUNDERSHOCK for 1HKO.

---

## Party Resource & Healing Strategy:
- **Heal Budget**: 10 POTIONs in pocket inventory.
- **Zero-Cost Healing**: Route 5 and 6 are connected by the Underground Path. We can return to Cerulean Pokémon Center to restore all HP and PP for free.
- **Mid-Battle Emergency Protocol**: If SPARKY's HP drops to 10 or below, use a Potion or immediately switch to GEMMY (WARTORTLE, Lv 27) or BUGGY (BUTTERFREE, Lv 13) to sweep.
- **Safe Switch-Training**: Set ROCKY (GEODUDE) or BIRBIE (PIDGEY) in Slot 1. In battles, immediately switch on Turn 1 to GEMMY or SPARKY. The leading Pokémon safely gains 50% EXP.

---

<hr>

<h1><code>Locations/Route24_Route25</code></h1>

# Route 24 & Route 25 Geographical Records

## Map Transitions & Connections:
- **Route 24 Southern Boundary**: Connects to Cerulean City at (21, 0) from Route 24 (11, 35).
- **Route 24/25 Transition**: Route 24 (19, 8) connects directly to Route 25 (0, 8).

## Active Overworld Blockades (Trainer Coordinates):
These coordinates represent solid overworld sprites of defeated trainers. They act as physical barriers that must be bypassed during routing.

### Route 24 (Nugget Bridge) Blockades:
- **Cale**: (11, 31) - blocks Column 11.
- **Ali**: (10, 28) - blocks Column 10.
- **Youngster**: (11, 25) - blocks Column 11.
- **Lass**: (10, 22) - blocks Column 10.
- **Bug Catcher**: (11, 19) - blocks Column 11.
- **Rocket Grunt**: (11, 15) - blocks Column 11.

### Route 25 Blockades:
- **Franklin**: (8, 4) - blocks Column 8.
- **Youngster**: (14, 3) - blocks Column 14 (on Row 3, leaving Row 4 clear).
- **Green-Vest**: (18, 5) - blocks Column 18 Row 5.
- **Lass**: (18, 8) - blocks Column 18 Row 8 (Note: Row 7 is clear between Green-Vest and Lass).
- **Nob**: (23, 9) - blocks Column 23.
- **Jr. Trainer ♂**: (24, 6) - blocks Column 24 Row 6.
- **Lass (Picnicker)**: (32, 3) - blocks Column 32.
- **Lass (Bug Catcher)**: (37, 4) - blocks Column 37.

## Nugget Bridge Defeated Trainer Bypass Routes (Going North):
To walk north up Nugget Bridge from the Cerulean City transition at (21, 0) to Route 25 while completely avoiding collisions with the solid, defeated trainer sprites:
1. Transition onto Route 24 at (11, 35).
2. Walk Left 1 step to (10, 35).
3. Walk Up 5 steps along Column 10 to (10, 30) (bypassing Bug Catcher Cale at (11, 31)).
4. Walk Right 1 step to (11, 30).
5. Walk Up 3 steps along Column 11 to (11, 27) (bypassing Lass Ali at (10, 28)).
6. Walk Left 1 step to (10, 27).
7. Walk Up 3 steps along Column 10 to (10, 24) (bypassing Youngster at (11, 25)).
8. Walk Right 1 step to (11, 24).
9. Walk Up 3 steps along Column 11 to (11, 21) (bypassing Lass at (10, 22)).
10. Walk Left 1 step to (10, 21).
11. Walk Up 13 steps along Column 10 to (10, 8) (bypassing Rocket Grunt at (11, 15) and Bug Catcher at (11, 19)).
12. Walk Right 1 step to (11, 8) and walk north into Route 25.

## Route 25 Ledge Bypass Route (Going North):
- **Column 9 Ledge Bypass**: Column 9 at Row 7 is a flat, clear grass tile (TYPE_3fe2) with no ledge.
- This provides a completely open, bidirectional path connecting the southern pathway (Row 8) and the northern grass area (Row 6), allowing players to walk back north/west to the tall grass patch (Columns 2-7, Rows 4-5) without walking all the way east to Column 17.
- Path: Stand at (9, 8) south of the ledge, walk Up 2 steps to (9, 6), then walk West as needed. Fully verified on Turn 12805.

<hr>

<h1><code>Archive/Route24_Route25_BattleLogs</code></h1>

# Completed Battle Logs Archive (Moved from Active Location Record)
- Completed Turn 13131

## Nugget Bridge Defeated Trainers:
- **Nugget Bridge No. 1**: Bug Catcher Cale at (11, 31). Defeated on Turn 12014.
- **Nugget Bridge No. 2**: Lass Ali at (10, 28). Defeated on Turn 12050.
- **Nugget Bridge No. 3**: Youngster at (11, 25). Defeated on Turn 12211.
- **Nugget Bridge No. 4**: Lass at (10, 22). Defeated on Turn 12309.
- **Nugget Bridge No. 5**: Bug Catcher No. 5 at (11, 19). Defeated on Turn 12447.
- **Rocket Grunt (Map 0_35)**: (11, 15). Defeated on Turn 12536.

## Route 25 Defeated Trainers:
- **Route 25 Trainer No. 1**: Hiker Franklin at (8, 4). Defeated on Turn 12638.
- **Route 25 Trainer No. 2**: Youngster at (14, 3). Defeated on Turn 12667.
- **Route 25 Trainer No. 3**: Green-Vest Trainer at (18, 5). Already defeated.
- **Route 25 Trainer No. 4**: Lass at (18, 8). Defeated on Turn 12727.
- **Route 25 Trainer No. 5**: Hiker Nob at (23, 9). Defeated on Turn 12907.
- **Route 25 Trainer No. 6**: Jr. Trainer ♂ at (24, 6). Defeated on Turn 12946.
- **Route 25 Trainer No. 7**: Lass at (32, 3). Defeated on Turn 12983.
- **Route 25 Trainer No. 8**: Lass at (37, 4). Defeated on Turn 13019.

<hr>

<h1><code>Locations/CeruleanCity_TradeHouse</code></h1>

# Cerulean City - In-Game Trade House (Map 0_63)

## Overview & Transition:
- Entrance door in Cerulean City (Map 0_3) is at (13, 15).
- Spawns player at (2, 7) facing Up inside Map 0_63.

## NPCs & Objects:
- **Husband (Trader)**: Stands/sits at the table. He wants to trade a JYNX (LOLA) for a POLIWHIRL.
- **Wife NPC**: Standing at (5, 4) facing south. She mentions her husband loves trading.
- **Other NPC**: Girl standing at (1, 2) facing south.
- **Warp / Exit**:
  - Front door exit is at (2, 7) (interior), which leads back to Cerulean City at (13, 16).
  - Back door exit: None! The tile at (2, 0) is a solid wood wall (TYPE_2889), unlike the Badge Describer's House which has a functional back door warp there. This is a critical layout difference!

## Exploration & Dialogue Logs:
- Turn 13250: Entered the Trade House.
- Turn 13254: Spoke to the wife NPC at (5, 4) who asked if we want to trade. Declined/exited dialogue.
- Turn 13256: Verified that the back door at (2, 0) is solid/closed (TYPE_2889).
- Turn 13258: Returning to Cerulean City.

<hr>

<h1><code>Locations/CeruleanCity_BadgeDescribersHouse</code></h1>

# Cerulean City - Badge Describer's House (Map 0_230)

## Overview & Transition:
- Entered from (9, 11) in Cerulean City on Turn 13228.
- Spawns player at (2, 7) facing Up inside Map 0_230.

## NPCs & Objects:
- **Badge Describer NPC**: Standing at (5, 3) facing south. He explains the functions and secrets of the 8 League Badges.
- **Floor Item (Poké Ball sprite)**: Located at (7, 7) on the floor. This is a solid/impassable sprite.
- **Warp / Exit**:
  - Front door exit is at (2, 7) (interior), which leads back to Cerulean City at (9, 12).
  - Back door exit: Doorway at (2, 0).

## Exploration & Dialogue Logs:
- Turn 13230: Spoke with the Badge Describer at (5, 3). He opened a menu to choose a Badge to describe. Let's close this menu and check the item at (7, 7).

<hr>

<h1><code>Locations/Route5_UndergroundPath</code></h1>

# Route 5 Underground Path (Map 0_71) Records

## NPC Trades & Information:
- **Trade NPC**: Female trainer NPC standing at (2, 3).
- **Trade Details**: Offers her NIDORAN♀ (SPOT) in exchange for a NIDORAN♂.
- **Verification (Turn 14969)**: Interacted and verified trade proposal. Declined since we do not currently have Nidoran♂ in our Pokédex or party.

## Layout & Navigation:
- Entrance from Route 5 door at (17, 27) spawns us at (3, 7) facing Up.
- Stairs to the Underground Path tunnel are located at (4, 4).
- Red-carpeted pathway is clear between Row 7 and Row 4.
- Counter walls are located on Column 1 and Column 6.
- Exit door at the south (3, 7) leads back to Route 5.

<hr>

<h1><code>Locations/Route6_UndergroundPath</code></h1>

# Route 6 Underground Path (Map 0_74) Records

## NPC Trades & Information:
- **NPC**: Female trainer NPC standing at (2, 3).
- **Layout & Navigation**:
  - Spawn point from tunnel stairs is at (4, 4) facing Down.
  - Exit door at the south (Row 7, Columns 3 & 4) has red carpet and is TYPE_3fe2.
  - Bounded by counters on Column 1 and Column 6.
  - Stairs leading to the Underground Tunnel (Route 5) are at (4, 4).

<hr>

<h1><code>Locations/Route6</code></h1>

# Route 6 Location Records (Map 0_17)
- Map 0_17 is Route 6, connecting Vermilion City (south) and Saffron City gatehouse (north).

## Points of Interest:
- **Underground Path Building (Route 6 Door)**: (17, 13) (🚪 marked)
  - Connects to Route 5 via the Underground Path, bypassing Saffron City.
- **Saffron South Gatehouse Southern Entrance**: (9, 36) on Route 6 map? Wait, let's verify map IDs and coordinates.
  - Wait, our position is at (9, 35) on Map 0_17.
  - Map 0_12 is the Saffron South Gatehouse (the guard house leading to Saffron City from Route 6).
  - The southern exit of this gatehouse is at (9, 36).
- **Wild Grass Patches**:
  - Located on Route 6 (Map 0_17).
  - Contains wild Pokémon such as Bellsprout, Oddish, Meowth, Pidgey, Rattata, etc.

## Map Transitions:
- Route 6 (Map 0_17) to Vermilion City (Map 0_5): Walk south from Row 35 of Route 6.
- Route 6 (Map 0_17) to Saffron South Gatehouse (Map 0_12): Enter the gatehouse building door at (9, 35) or (10, 35) on Map 0_17.
- Saffron South Gatehouse (Map 0_12) Southern Exit: at (9, 36) leading to Route 6 (Map 0_17).
- Saffron South Gatehouse (Map 0_12) Northern Exit: leading to Saffron City (Map 0_6). Currently blocked by a thirsty guard.

## Walkable Boundaries & Obstacles:
- **Row 32 Fence**:
  - Horizontal fence barrier stretching from Columns 10 to 39.
  - Precise gap allowing transit between northern and southern Route 6 areas is at Column 8 (8, 32) and Column 9 (9, 32). Columns 10 and above are completely blocked by the solid fence (TYPE_2889).
- **Row 29 Fence (Disproven)**:
  - Empirically disproven on Turn 18210. We successfully stepped Up onto (15, 29) without collision, proving that Row 29 is completely clear and passable at Column 15. The grey fence is only present at Row 32 (Columns 11-19). Row 29 contains clear passable path/grass tiles (TYPE_3fe2).
- **Row 13 Fence**:
  - Horizontal fence barrier running from Columns 20 to 29.
  - Blockage verified at (20, 13) through (29, 13).
- **Stationary Trainers**:
  - Camper at (11, 31) and Picnicker at (11, 30) block Column 11 completely, forming solid overworld obstacles after defeat.

<hr>

<h1><code>Locations/VermilionCity</code></h1>

# Vermilion City Location Records (Map 0_5)
- Map 0_5 is the native, unmodded Vermilion City.
- Entrance from Route 6: (19, 0) inside Map 0_5.

## Points of Interest:
- **Pidgey House (Map 0_93)**:
  - Entrance door at (23, 19) on Map 0_5.
  - Inside, there is a youngster NPC at (5, 3) and a Pidgey Pokémon sprite wandering around.
- **Pokémon Fan Club (Map 0_90)**:
  - Entrance door at (9, 13) on Map 0_5.
  - Inside, the Chairman sits behind the table at Row 2. We can talk to him to get the Bike Voucher.
- **Vermilion Pokémon Center**:
  - Expected on the north-west side (approx. Column 11, Row 5) or north-east side. We will search for its red roof.
- **Vermilion Poké Mart**:
  - Expected directly north of the Pidgey House (approx. Columns 23-25, Row 13).

## Overworld Navigation & Layout:
- Column 19 between Row 18 and Row 21 is a water/dock barrier (TYPE_4e8c).
- Row 17 is a clear paved horizontal street (TYPE_3fe2) that allows bypassing Column 19's water barrier to travel west.
- Row 22 and below is sea water (TYPE_4e8c).
- **Vermilion City Landmarks**:
  - Poké Mart Entrance: (23, 13) (🏪 marked)
  - Fishing Guru House Entrance: (15, 13) (🚪 marked)
  - Pokémon Center Entrance: (11, 3) (🏥 marked)
  - Pokémon Fan Club Entrance: (9, 13) (🚪 marked)
  - Pidgey House Entrance: (23, 19) (🚪 marked)
- Column 6 & 7 Western Corridor (Blocked): Columns 6 and 7 are blocked at Row 19 by a solid fence (TYPE_2889 at (6, 19)) and a post/mailbox (TYPE_2889 at (7, 19)), meaning they do NOT form a continuous passable vertical street to the southern docks. This was empirically verified on Turn 16325. The correct path to reach the southern docks/pier is via the eastern pier along Column 30.

## Snorlax Blockage (Verified Turn 17930):
- A sleeping Snorlax occupies (35, 13) on Map 0_5, completely blocking the entrance to Diglett's Cave at (34, 13) and (35, 13). Diglett's Cave is currently inaccessible from the Vermilion City side until Snorlax is awakened.

<hr>

<h1><code>Locations/SSAnne</code></h1>

# Verified S.S. Anne Records

## First Floor (1F) Cabins:
- **Cabin 1 (Map 0_102, Columns 10-13)**: First cabin door from the left.
  - **Trainer**: Gentleman Thomas at (11, 2). Defeated on Turn 15610. Used Nidoran♂ (Lv 19) and Nidoran♀ (Lv 19).
  - **Items**: None.
  - **Status**: 100% Cleared.

- **Cabin 2 (Map 0_102, Columns 20-23)**: Second cabin door from the left.
  - **NPC**: Sailor at (22, 5). Non-combat NPC. Spoke on Turn 15630.
  - **Items**: None.
  - **Status**: 100% Cleared.

- **Cabin 3 (Map 0_102, Columns 0-3)**: Third cabin door from the left (doorway at (15, 8) on Map 0_95).
  - **NPCs**: 
    - Lass at (2, 11) - Non-combat ("I always travel with WIGGLYTUFF!").
    - Wigglytuff at (3, 11) - Lass's partner Wigglytuff.
    - Youngster at (0, 14) - Non-combat ("A cruise is so elegant yet cozy!").
  - **Items**: None.
  - **Status**: 100% Cleared.

- **Cabin 4 (Map 0_102, Columns 10-13)**: Fourth cabin door from the left (doorway at (11, 8) on Map 0_95).
  - **Trainers**:
    - Youngster Tyler at (11, 13). Defeated on Turn 15681. Used Nidoran♂ (Lv 21).
    - Lass at (13, 11). Defeated on Turn 15711. Used Pidgey (Lv 18) and Nidoran♀ (Lv 18).
  - **NPC**: Blue-haired girl at (10, 13). Non-combat ("We are cruising around the world.").
  - **Item**: Poké Ball at (12, 15) containing TM08 (Body Slam). Collected on Turn 15714.
  - **Status**: 100% Cleared.

- **Cabin 5 (Map 0_102, Columns 20-23)**: Fifth cabin door from the left (doorway at (7, 8) on Map 0_95).
  - **NPC**: Global Police agent at (23, 13). Non-combat NPC. Spoke on Turn 15745.
  - **Items**: None.
  - **Status**: 100% Cleared.

- **B1F Cabin 1 (Map 0_103, Columns 0-3)**: First cabin door from the left on B1F (doorway at (9, 11) on Map 0_96).
  - **NPC**: Sailor at (1, 2) facing DOWN. Shows Snorlax Pokédex picture (non-combat).
  - **Item**: Poké Ball at (0, 3) containing MAX ETHER. Collected on Turn 15822.
  - **Status**: 100% Cleared.

- B1F Cabin 2 (Map 0_103, Columns 10-13): Second cabin door from the left on B1F (doorway at (13, 11) on Map 0_96).
  - Trainers:
    - Sailor at (13, 4) (Defeated, Turn 15910).
    - Gentleman at (11, 2) (Defeated, Turn 15922).
  - Items: None (Verified on Turn 15946).
  - Status: 100% Cleared.
- B1F Cabin 3 (Map 0_103, Columns 20-23): Third cabin door from the left on B1F (doorway at (17, 11) on Map 0_96).
  - NPC: Sailor at (21, 2) facing South. Non-combat flavor text ("Ah yes, I have seen some POKéMON ferry people...").
  - NPC: Super Nerd at (22, 1) facing South. Non-combat flavor text ("POKéMON can CUT down small bushes.").
  - Items: None (the red/white object at (20, 3) is a passable stool, verified on Turn 16016).
  - Status: 100% Cleared (Verified on Turn 16021).
- B1F Cabin 4 (Map 0_103, Columns 0-3, Rows 10-15): Fourth cabin door from the left on B1F (doorway at (21, 11) on Map 0_96).
  - Trainers:
    - Gentleman at (1, 14) (Defeated, Turn 16074).
    - Lass at (2, 11) (Defeated, Turn 16130).
  - Items: None (the red/white object at (0, 12) is a passable stool).
  - Status: 100% Cleared.
- B1F Cabin 5 (Map 0_103, Columns 10-13, Rows 10-15): Fifth cabin door from the left on B1F (doorway at (25, 11) on Map 0_96).
  - NPCs:
    - Sailor at (12, 12) facing DOWN (Non-combat NPC, gave Safari Zone info on Turn 16474).
    - Sailor at (11, 14) facing UP (Non-combat NPC, gave Safari Zone info on Turn 16488).
  - Items: None (the Poké Ball-like sprite at (10, 13) is a passable stool, verified on Turn 16484).
  - Status: 100% Cleared (Turn 16491).
- **Cabin 6 (Map 0_102, Columns 0-3, Rows 0-5)**: Sixth cabin door from the left (doorway at (31, 8) on Map 0_95).
  - **NPC**: Sailor at (2, 3). Non-combat/unresponsive NPC (solid, did not trigger dialogue or battle on Turn 16585).
  - **Items**: None.
  - **Status**: 100% Cleared.

## Second Floor (2F) Hallway & Cabins (Map 0_100):
- **2F Hallway**:
  - **NPC**: Gentleman at (1, 1) facing DOWN. Non-combat ("You, mon petit! We're busy here! Out of the way!").
  - **NPC**: Gentleman at (9, 1) facing DOWN. Non-combat ("I'm so busy I'm getting dizzy!").
  - **Stairs to 1F**: Located at (6, 0).

- **Cabin A (Columns 2-7, Rows 5-15, Doorway at (4, 5)/(5, 5))**:
  - **NPC**: Bug Catcher at (5, 12) facing UP. Non-combat ("I saw an odd ball in the trash.").
  - **Items**: None (symmetrical room with 2 beds, no trash cans or items).
  - **Status**: 100% Cleared (Turn 16660).

- **Cabin B (Columns 8-9, Rows 5-10, Doorway at (8, 5)/(9, 5))**:
  - **NPCs**: None.
  - **Items**: None (empty gap/corridor running south).
  - **Status**: 100% Cleared (Turn 16691).

- **Cabin C (Columns 10-15, Rows 5-15, Doorway at (12, 5))**:
  - **NPCs**: None (Column 13 is the eastern edge-wrapping border that renders ghost duplicate sprites from RAM).
  - **Items**: None (symmetrical room with 2 beds on Columns 10 & 11, dressers and mugs).
  - **Status**: Cabin C itself is cleared.
  - **Southern Hallway Corridor (Rows 11-13)**: Features a Bug Catcher sprite at (11, 13) facing UP. Verified on Turn 16998 as a RAM-mirrored ghost duplicate of the Chef's dialogue script. Status: 100% Cleared / Verified Glitch.

## Deck Cabins (Map 0_104):
- **Cabin 1 (Map 0_104, Columns 0-3, Rows 10-15, Doorway at (2, 15))**: First cabin from the right on S.S. Anne Deck (doorway at (19, 3) on Map 0_98).
  - **Entrance/Exit Warp**: (2, 15).
  - **Trainer**: Sailor at (2, 11) (walked down to (2, 13) to battle). Defeated on Turn 16845. Used Level 17 Horsea and Level 17 Shellder.
  - **Trainer**: Sailor at (0, 13) facing RIGHT. Defeated on Turn 16888. Used Level 21 Shellder and Level 17 Tentacool.
  - **Items**: None (symmetrical cabin layout).
  - **Status**: 100% Cleared.

- **Cabin 2 (Map 0_104, Columns 10-13, Rows 10-15, Doorway at (12, 15))**: Second cabin from the right on S.S. Anne Deck (doorway at (23, 3) on Map 0_98).
  - **Entrance/Exit Warp**: (12, 15).
  - **NPCs**: Youngster at (10, 13) (non-combat, speaks of Machoke), Machoke at (11, 12) (non-combat, "Gwoh! Goggoh!").
  - **Item**: Poké Ball at (12, 11) containing ETHER. Collected on Turn 16929.
  - **Status**: 100% Cleared.

## S.S. Anne Kitchen (Map 0_99):
  - **Entrance/Exit Warp**: (13, 6) (🚪 exit marked).
  - **Trainers**:
    - Sailor at (10, 7). Defeated on Turn 17495. Used Level 17 Machop and Level 17 Tentacool.
    - Sailor at (4, 4). Defeated on Turn 17584. Used Level 17 Machop and Level 17 Shellder.
  - **NPC**: Chef at (5, 2) facing DOWN (Non-combat, "The party's over. The ship will be departing soon."). Spoke on Turn 17593.
  - **NPC**: Chef/Sailor at (4, 9).
  - **Items**: All reachable counters on left and right walls (including (1, 5), (1, 8), (2, 9), (12, 5), (13, 8), (12, 8), (12, 9), (12, 10), (12, 11)) were searched and verified empty. No Great Ball found due to ROM randomization.
  - **Status**: 100% Cleared (Verified on Turn 17672).

## S.S. Anne Custom Map Warp Connections:
- **B1F to 2F Hallway Connection**: B1F (Map 0_96) at (2, 12) contains a staircase warp that connects directly to S.S. Anne 2F Hallway (Map 0_97) at (19, 3), bypassing 1F. Verified on Turn 17308 and Turn 17436.
- **2F Hallway to Kitchen Connection**: S.S. Anne 2F Hallway (Map 0_97) at (0, 3) contains a doorway warp that connects directly to S.S. Anne Kitchen (Map 0_99) at (13, 6). Verified on Turn 17461. This confirms our S.S. Anne Kitchen Redirection Theory: the developer swapped the unmodded S.S. Anne Kitchen (Map 0_101) with the Captain's Cabin (Map 0_99), meaning the Kitchen is now located on Map 0_99, and the Captain's Cabin is on Map 0_101.
- **Warp Engine Explanation**: These direct, non-standard transitions highlight how Pokémon Gen 1's engine handles warps via a static map transition table, linking a specific tile warp ID on one map to a destination coordinate on another, without requiring physical 3D architectural consistency.

## Progression Strategy History:
- **Rival Battle & Captain**: We defeated Rival Blue on B1F on Turn 17378, then went up to the Captain's Cabin on Map 0_101 via Warp 8 at (36, 4) on B1F. We obtained HM01 Cut from the Captain on Turn 17395.
- **Kitchen Clearing Plan**: After securing HM01, we backtracked to S.S. Anne 2F Hallway (Map 0_97) and navigated to (0, 3) to enter S.S. Anne Kitchen (Map 0_99) to defeat any remaining trainers/Chefs and collect items before leaving the ship.
- **Switch-Training History**: Used Slot 1 lead switch-training to successfully raise BIRBIE (Pidgey) to Level 15 on Turn 17378. (Note: BIRBIE did not evolve at Lv 15, confirming Pidgey's true evolution level is 18. We will continue training her to Level 18).

<hr>

<h1><code>Archive/Route3_MtMoon_Cerulean</code></h1>

# Route 3, Mt. Moon, and Cerulean City Progression Scratchpad (Archived)
- Started: Turn 4122, Timestamp: Sunday, May 24, 2026 at 6:18 AM PDT

## Progression Roadmap & Checklist:
- [x] Defeat Pewter Gym Leader Brock (Boulder Badge & TM34 secured!).
- [x] Healed team at Pewter City Pokémon Center at (13, 25).
- [x] Stock up on useful items at Pewter Poké Mart at (23, 17) (Secured 4 Potions, 3 Poké Balls, 3 Antidotes, 1 Paralyze Heal; ¥601 remaining).
- [x] Navigate east through Route 3 to Mt. Moon entrance.
- [x] Defeat Super Nerd Miguel and secure the Helix Fossil (Turn 11013).
- [x] Exit Mt. Moon to Route 4 West (Turn 11116).
- [x] Navigate Route 4 East to Cerulean City (Turn 11225).
- [x] Locate Cerulean Pokémon Center (Turn 11248).
- [x] Locate and explore Cerulean Bike Shop (Turn 11368).
- [x] Explore Cerulean City, locate the Poké Mart and Gym.

### TM28 Dig Utilization Strategy:
TM28 Dig is a 100 power Ground-type physical move in Generation 1.
- **Wartortle (GEMMY)**: Ground is super-effective against Electric (Wartortle's only weakness!). Teaching Dig to GEMMY provides perfect coverage for Lt. Surge's Gym and future Electric/Poison/Rock threats.
- **Pikachu (SPARKY)**: Can also learn Dig, but Ground does not cover Pikachu's Ground weakness (which Pikachu shouldn't stay in against anyway).
- **Decision**: Teach TM28 Dig to GEMMY (WARTORTLE) to secure a massive advantage against Lt. Surge's Electric Gym and Poison/Fire/Rock opponents.
- [x] Taught TM28 Dig to GEMMY (Turn 14445), replacing TACKLE.

### Current Status & Fan Club Progression:
- Turn 15394: Progressed to Vermilion City (Map 0_5). Located the Pidgey House at (23, 19) and successfully cured SPARKY's poison. Located and entered the Pokémon Fan Club (Map 0_90) at (9, 13) on Map 0_5 and obtained the BIKE VOUCHER. Healed team fully at Vermilion Pokémon Center (11, 3). Now standing at (19, 12) in Vermilion City ready to head to S.S. Anne.

### S.S. Anne & Lt. Surge Combat Strategy:
- **ROCKY (GEODUDE, Level 11)**: Our primary defensive pivot against Lt. Surge. Being Ground/Rock, Rocky is immune to Electric attacks (Thundershock, Thunderbolt). We will switch-train Rocky on S.S. Anne to reach Level 15+.
- **GEMMY (WARTORTLE, Level 27)**: Our primary sweeper. GEMMY knows TM28 Dig (100 power physical Ground move in Gen 1), which is super-effective against Electric-types! However, she is a Water-type, so she must either outspeed or OHKO opponents to avoid taking massive Electric damage.
- **SPARKY (PIKACHU, Level 21)**: Resists Electric-type attacks. Sparky can utilize Thunder Wave to paralyze fast opponents like Surge's Level 24 Raichu.
- **BIRBIE (PIDGEY, Level 9)**: Switch-trained to Level 9 on Route 6.

<hr>

<h1><code>Reflection/Turn19214</code></h1>

# Reflection Turn 19214

## 1. Immediate Execution
- Over the last 50 turns, we have systematically navigated Vermilion Gym's trash can puzzle on Trial 15.
- We have checked: (1, 11), (3, 11), (5, 11), (7, 11), (9, 11), and (9, 9). All were empty.
- We are currently standing at (7, 10) facing UP, preparing to check (7, 9).

## 2. Notepad Hygiene
- Cleaned up obsolete movement details from `Scratchpad/SSAnne_Sweep`.
- Backported rigorous mathematical deductions for second-switch elimination to all historical trials in `Scratchpad/VermilionGym_Puzzle`.
- Updated turn stamps in `Mechanics/PikachuTrainingAndGrindingPlan`.

## 3. Map Hygiene
- Defeated trainers (Dwayne, Tucker, Baily) are correctly marked with '☠️' emojis linked to their defeated states.
- Gym Guide is correctly marked with '💡' emoji.
- All markers are highly accurate and there is no clutter.

## 4. Custom Tools & Agents
- 5 discrete tool/agent concepts evaluated:
  1. `gym_battle_strategist` (Agent): A custom agent to plan type matchups and switch-training setups for Lt. Surge's Voltorb, Pikachu, and Raichu.
  2. `trash_can_pathfinder` (Tool): Automatically paths and aligns the player adjacent to a target trash can.
  3. `switch_probability_calc` (Tool): Calculates exact mathematical probabilities of remaining cans being the second switch based on layout edge rules.
  4. `team_readiness_validator` (Tool): Reads game RAM to verify all party members' HP/PP are exactly at 100% before starting a major boss battle.
  5. `move_pp_monitor` (Tool): Tracks remaining move PP to prevent running out of key coverage moves like GEMMY's DIG during grinding or gym runs.

## 5. Tool Maintenance
- Our custom tool `heal_pokemon_at_counter` is fully functional and does not require debugging or edits. No broken tools exist.

## 6. Goal Clarity
- Goals are perfectly defined as outcomes ("WHAT"), while detailed routing plans and trial logs ("HOW") are kept clean in `Scratchpad/VermilionGym_Puzzle`.

## 7. Error Analysis & Hypothesis Review
- Discovered and confirmed that the second switch in Gen 1 can glitch out-of-bounds.
- Developed an optimal checking policy: always check both valid adjacent cans before resetting. This minimizes costly first-switch resets. Our spatial reasoning is grounded and robust.

<hr>

<h1><code>Reflection/Turn19474</code></h1>

# Reflection Turn 19474

## 1. Immediate Execution
- We successfully found the 1st switch at (1, 7) on Turn 19468 and the 2nd switch at (3, 7) on Turn 19471.
- The motorized door is now open!
- Next steps are to swap GEMMY (Wartortle, Lv 29) to the lead slot using the party menu, walk north to Lt. Surge, and battle him using our DIG strategy.

## 2. Notepad Hygiene
- Documented the successful completion of the trash can puzzle in `Scratchpad/SSAnne_Sweep` and `Scratchpad/VermilionGym_Puzzle`.
- Updated the main dashboard to mark the puzzle as completed.

## 3. Map Hygiene
- All gym trainers are correctly marked as defeated.
- Guide is marked.
- We will add a marker for Lt. Surge once we are adjacent to him.

## 4. Custom Tools & Agents
- 5 discrete concepts:
  1. `party_swapper` (Tool): Automatically navigate menus to swap Pokemon slots.
  2. `save_game` (Tool): Automatically save the game via the start menu.
  3. `gym_battle_strategist` (Agent): Already defined; plans battle matchups.
  4. `surge_damage_calculator` (Tool): Calculates DIG damage ranges against Surge's team.
  5. `overworld_pathfinder` (Tool): Automatically paths through clear tiles.

## 5. Tool Maintenance
- Verified that all custom tools are clean and functional.

## 6. Goal Clarity
- Primary goal: Defeat Lt. Surge.
- Secondary goal: Prepare party alignment.
- Tertiary goal: Maintain team health.

## 7. Error Analysis & Hypothesis Review
- Our systematic serpentine search and optimal checking policy (always checking both valid adjacent cans before resetting) directly led to solving the puzzle in Trial 19.

<hr>

<h1><code>Locations/Route9</code></h1>

# Route 9 Geographical Records (Map 0_20)

## Map Transitions & Connections:
- **West Exit**: Connects back to Cerulean City (Map 0_3) at Column 0, Row 8 (spawns at (39, 16) on Map 0_3). Fully verified on Turn 19934.
- **East Exit**: Leads towards Route 10 and Rock Tunnel.

## Structural Layout & Obstacles:
- **Corridor entrance**: A narrow east-west pathway between Row 7 and Row 10 (which are bounded by solid rock walls, TYPE_2889).
- **Cuttable Bush**: Located at (5, 8) (TYPE_5519). This bush completely blocks the pathway to the east. We must use CUT on (5, 8) to proceed.
- **Signpost/Rock**: Located at (4, 9) (TYPE_2889), which blocks Row 9, forcing the player to use CUT at (5, 8).

## Wild Encounters Database & SPARKY Training Log:
- **SPARKY Grinding Goal**: Train SPARKY (Pikachu) to Lv 24.
- **Active Grinding Log**:
  - Starting Level: 22 (Turn 20126)
  - Current Level: 23 (Turn 20588)
  - EXP gained on Route 9: 0 EXP
  - Grinding Sessions:
    - Session 1 (Start Turn 20215): Grinding on Row 12 (Columns 10-16) grass patch. Lead: SPARKY (PIKACHU) Lv 22, HP 52/52.
    - Session 2 (Start Turn 20282): Grinded on Row 14 (Columns 29-43) grass patch. Met and defeated Hiker trainer at (45, 15) on Turn 20334.
    - Session 3 (Start Turn 20424): Defeated Bug Catcher at (40, 8) on Turn 20415 and Hiker at (43, 3) on Turn 20459.
    - Encounters Tracked: none yet.

| Species | Levels | Encounter Count | Matchup Strategy | Notes & Verification |
|---------|--------|-----------------|------------------|----------------------|
| Rattata | -      | 0               | Neutral EXP      | Not encountered yet  |
| Spearow | -      | 0               | Super-effective  | Not encountered yet  |
| Ekans   | -      | 0               | Neutral EXP      | Not encountered yet  |
| Sandshrew | -    | 0               | Avoid with Sparky| Not encountered yet  |

## Trainer Matchups & Battle History:
- **Trainer 1**: Jr. Trainer ♀ at (13, 10)
  - Team: ODDISH Lv 18, BELLSPROUT Lv 18, ODDISH Lv 18, BELLSPROUT Lv 18
  - Matchup: SPARKY (PIKACHU) Lv 22 vs. ODDISH Lv 18 (Won), SPARKY (PIKACHU) Lv 22 vs. BELLSPROUT Lv 18 (Slept Sparky), BIRBIE vs. BELLSPROUT Lv 18 (Slept Birbie), GEMMY Lv 30 vs. BELLSPROUT Lv 18 (Won), GEMMY Lv 30 vs. ODDISH Lv 18 (Won), GEMMY Lv 30 vs. BELLSPROUT Lv 18 (Won)
  - Battle Status: Defeated on Turn 20048
- **Verified Corridor: Column 19, Row 13 (Verified on Turn 20238)**:
  - This tile is a completely flat, bidirectional passage connecting the upper grass strip (Row 12) and the lower pathway (Row 14).
  - Test proof: We successfully walked Down from (15, 12) to (19, 14) through (19, 13) on Turn 20227, and successfully walked back Up from (19, 14) to (19, 12) through (19, 13) on Turn 20233. This proves there are no invisible colliders or one-way triggers blocking movement in either direction.
- **Trainer 2**: Bug Catcher at (40, 8)
  - Team: CATERPIE Lv 20, WEEDLE Lv 20, VENONAT Lv 20
  - Battle Status: Defeated on Turn 20415
- **Trainer 3**: Hiker at (43, 3)
  - Team: GEODUDE Lv 20, MACHOP Lv 20, GEODUDE Lv 20
  - Battle Status: Defeated on Turn 20459

<hr>

<h1><code>Scratchpad/Route9_Route10_RockTunnel_Strategy</code></h1>

# Route 9, Route 10, and Rock Tunnel Active Strategy & Planning (Turn 25339)

## Route 10 Active Progress (Turn 25339):
- See Locations/Route10 and Locations/RockTunnel for detailed permanent records of Route 10 overworld and Rock Tunnel entrance milestones.

## Rock Tunnel Navigation Strategy:
- Rock Tunnel is a dark cave in Generation 1.
- Options to traverse:
  1. Blind Navigation: Use a highly precise, tile-by-tile coordinate map of Rock Tunnel's layouts (1F and B1F) to navigate in the dark without Flash. This requires careful tracking of coordinates and turns.
  2. HM05 Flash: Return to Route 2 to get HM05 Flash from Professor Oak's Aide.
     - Requirement: Catch 10 or more unique species of Pokémon. (We currently have 12 unique species caught, which is sufficient!)
     - Path: To return to Route 2, we must traverse Diglett's Cave. However, Diglett's Cave Vermilion City entrance is currently blocked by a sleeping Snorlax. We need the Poké Flute to wake up Snorlax.
     - Obtaining the Poké Flute: Requires rescuing Mr. Fuji from the top of Pokémon Tower in Lavender Town, which first requires the Silph Scope from the Rocket Hideout in Celadon City.
     - Therefore, we cannot get Flash before entering Rock Tunnel! We must traverse Rock Tunnel first in the dark (or we must explore other pathways if possible, but Rock Tunnel is the only path to Lavender Town).
- Thus, our plan is to navigate Rock Tunnel 1F and B1F in the dark, using coordinates and tile-by-tile routing. We will document our precise path and steps in a dedicated scratchpad.

<hr>

<h1><code>Locations/Route10</code></h1>

# Route 10 Geographical Records (Map 0_21) (Updated Turn 25333)

## Map Transitions & Connections:
- **West Entry**: Connects to Route 9 at (0, 8) (verified on Turn 20493).
- **North/East Exploration**: Complete (B1F bisected, Row 15 solid on Columns 20-27).

## Structural Layout & Obstacles:
- Bounded on the north by water/river on Rows 2 and 3 (TYPE_4e8c).
- Bounded on row 5 by a line of stone statues/shield-like cave walls (TYPE_2889).
- Passage going north on Columns 2 & 3 between statues (2, 5) and (3, 5) leads to the horizontal river path at (2, 4) and (3, 4).
- River (impassable without Surf) blocks direct north passage on Columns 2 and 3 at Rows 2-3.
- Row 4 is a clear land corridor (TYPE_3fe2) running east-west, bypassing the tall grass on Row 6 and below.
- **Water Collision Verification (Turn 20539)**: Attempted to walk Right from (15, 4) onto (16, 4). Movement failed (bumped), proving that (16, 4) is water with active solid collision and the horizontal river blocks any further east or north exploration from this upper plateau.

## Points of Interest:
- **Route 10 Pokémon Center**: Located at (11, 19) on Map 0_21 (verified on Turn 20574). The entrance warp is at (11, 19), with the approach path from the east side (Column 14) via Row 20 (Columns 11-14).

## Trainer Matchups & Battle History:
- None yet.

<hr>

<h1><code>Scratchpad/RockTunnel_Pathfinding</code></h1>

# RockTunnel_Pathfinding (Updated Turn 25322)
- Current Turn: 25351
- Current Position: (17, 11) on Rock Tunnel 1F
- Active Exploration Duration: 3860 turns (Started B1F backtracking on Turn 21491, synchronized Turn 25351)

## Verified Structural Layout Discoveries:
1. Column 17 on 1F: Solid blockage at (17, 15) prevents direct north passage along Column 17.
2. Column 16 on 1F: Fully passable at Rows 14 and 15, allowing us to successfully reach Ladder C at (17, 11).
3. Ladder C (1F 17, 11 <-> B1F 23, 11): Taken down on Turn 24525, taken up on Turn 25009, and down again on Turn 25025.
4. B1F Northern Passage: Fully open from Column 23 via Column 17 north to Row 4, but blocked at Columns 24 and 25 on Rows 2-4 (verified Turn 24546).
5. B1F East-West crossing at Row 20: Physically verified to be BLOCKED on Turn 24686. Columns 18 and 19 on Row 20 are solid rock walls (TYPE_2889).
6. B1F Column 20 Row 14/15 Blockage: Physically verified to be BLOCKED on Turn 24708. Row 14 Column 20 is a solid rock wall (TYPE_2889).
7. B1F East-West crossing via starting chamber: Fully open on Rows 10-13, Columns 14-23.
8. B1F East-West bypass highway: Row 16 has Columns 20-37 open, connecting directly to Column 37 (Ladder D).
9. Column 15 on B1F at Row 22 is solid rock blockage (verified Turn 24763).
10. Column 12 on B1F is a solid vertical wall (TYPE_2889) on Rows 18-25, isolating Columns 10-11.
11. Column 11 on B1F: Blocked at Row 29 by solid rock wall TYPE_2889 (verified Turn 24878, map marker placed).
12. B1F Column 23 Row 14 Blockage: Physically verified to be BLOCKED on Turn 24946. Column 23 Row 14 is a solid rock wall (TYPE_2889).
13. B1F Row 12 Columns 24-25 Blockage: Physically verified to be BLOCKED on Turn 24928. Row 12 Columns 24-25 are solid rock walls (TYPE_2889).
14. Columns 18-19 on B1F are solid rock walls on Rows 14 to 23 (verified Turn 25322).
15. Columns 13 to 19 are solid rock walls on Rows 22 and 23 (verified Turn 25322).

## Physical Verification Logs for Active Route:
- Turn 25158: Reached (22, 5). Physically verified that Columns 18-22 on Row 5 are 100% passable (TYPE_3fe2).
- Turn 25180: Walked Right onto (23, 5), physically proving Row 5 Column 23 is 100% passable (TYPE_3fe2).
- Turn 25183: Attempted to walk Right from (23, 5) into (24, 5) (TYPE_2889) and collided (0 tiles visited), physically proving that Row 5 Columns 24-25 consists of a solid, impassable rock wall. This confirms that there is no direct eastern bypass on Row 5, and we must proceed south down Column 23.
- Turn 25195: Attempted to walk Down to (23, 8) and collided, physically proving that Column 23 Rows 8-9 consists of a solid rock wall (TYPE_2889).
- Turn 25217: Reached (19, 5) and got interrupted by a wild Geodude battle.
- Turn 25218: Escaped the Geodude battle safely.
- Turn 25224: Reached (22, 10) and got interrupted by a wild Machop battle.
- Turn 25226: Escaped the Machop battle safely.
- Turn 25228: Attempted to navigate south down Column 22 but collided at Row 14, physically and mathematically proving that B1F (22, 14) is blocked by a solid rock wall (only 3 Down steps processed successfully before we hit Row 14 and remained at (22, 13) for the other 2 Down steps, then stepped Right onto (23, 13) and encountered a wild Geodude).
- Turn 25236: Currently in wild Geodude battle at (23, 13).
- Turn 25244: Detoured through Column 21 on Row 14 but collided, physically and mathematically proving that B1F (21, 14) is blocked by a solid rock wall (only 2 Left steps processed successfully to (21, 13) before the 2 Down steps collided, then stepped Right back to (23, 13) and collided Down on (23, 14), triggering a wild Zubat encounter).
- Turn 25258: Walked Left 6 steps along Row 13 to (17, 13) without collision, proving Row 13 is fully passable from Column 23 to Column 17. Attempted to step Down to (17, 14) and triggered a wild Zubat battle, proving that Column 17 is accessible on B1F.
- Turn 25287: Escaped from wild Zubat battle safely at (17, 13).
- Turn 25305: Walked Down Column 17 from (17, 13) to (17, 16) without collision, proving Column 17 is open on Rows 14 to 16.
- Turn 25310: Walked Down Column 17 from (17, 16) to (17, 20) without collision, proving Column 17 is open on Rows 17 to 20.
- Turn 25322: Verified visual representation showing Row 22 and Row 23 are blocked on Columns 13 to 19, and Columns 18-19 are blocked on Rows 14 to 23. This isolates B1F south quadrant from Column 17. We must backtrack to Ladder C at (23, 11) to climb to 1F.

<hr>

<h1><code>Locations/RockTunnel</code></h1>

# Rock Tunnel Geographical Records (Map 0_82) (Updated Turn 25326)
- **Verified Wall Blockage (Turn 24686)**: Physically collided with the solid rock wall at B1F (18, 20) and (19, 20). There is no horizontal bypass on Row 20; Columns 18-19 on Row 20 are solid, impassable rock wall (TYPE_2889).

## Socratic Challenge (The Impassable Floor Contradiction) Answer:
- In Mt. Moon B2F, TYPE_2770 is the primary passable cavern floor. However, on Rock Tunnel 1F, we attempted to step onto (4, 22) (labeled TYPE_2770) and collided (0 tiles visited), concluding that TYPE_2770 is impassable. 
- *Physical Contradiction Explained*: The tile type ID itself does not change its collision properties dynamically. In Gen 1, collision is determined by the tileset's collision byte map. If TYPE_2770 is passable in Mt. Moon, it must share the same tile index or metatile index in the cavern tileset. 
- Wait, are Mt. Moon and Rock Tunnel using the exact same cavern tileset? Yes, both use the "cave" tileset.
- However, our collision at Rock Tunnel 1F (4, 22) was not because of TYPE_2770 itself. Let's look closer at (4, 22) on 1F: row 22 is the southern boundary wall on 1F! The tile at (4, 22) is visually a wall or part of the border. But why was it labeled TYPE_2770? The overlay labels are based on automated tile type classification which might map visually distinct cavern border tiles to the same index (such as a solid black tile or cave wall corner that has a different collision bit).
- Specifically, the border tile of the cavern tileset is a solid block, which is impassable. Thus, (4, 22) is part of the solid cave border/wall, causing direct collision. The collision rule is consistent because the tile ID under the hood for that specific wall/border tile has the impassable bit set.
- **Physical Collision Verification of TYPE_2770 on 1F Y=22**:
  - *Methodology*: Standing at (14, 21), walked Right on Turn 24431 to (15, 21), then attempted to walk Down to (15, 22) (labeled TYPE_2770).
  - *Result 1*: Direct collision encountered (player remained at (15, 21)), physically and mathematically proving that TYPE_2770 on Row 22 of Rock Tunnel 1F has active solid, impassable collision. Therefore, Row 22 and Row 23 form a continuous solid rock wall across Columns 2 to 19, and we cannot walk south across Row 22 in this western section.
  - *Result 2 (Turn 24447)*: Standing at (20, 21), attempted to walk Down to (20, 22) (labeled TYPE_2770). Collision encountered (player remained at (20, 21)), physically proving that (20, 22) has solid, impassable wall collision.
  - *Result 3 (Turn 24453)*: Standing at (21, 21), attempted to walk Down to (21, 22) (labeled TYPE_2889). Collision encountered (player remained at (21, 21)), physically proving that (21, 22) has solid, impassable wall collision.

## Socratic Challenge (Southeast B1F Sweep) Answer:
- In Locations/RockTunnel (line 123), we documented a plan to systematically sweep B1F Columns 34-37 on Rows 30-33 to search for a new ladder or exit.
- *Physical Execution Verification*: We actually did NOT physically execute this 4x4 grid sweep yet! We only walked along Row 33 (from Column 37 to Column 2 on Turn 21591-21625) and tested Columns 2-4 on Rows 31-33 (the bottom-left quadrant). We completely skipped sweeping the rest of Columns 34-37 on Rows 30-32!
- Therefore, the true exit ladder (Ladder 4 in vanilla Rock Tunnel, which leads to 1F bottom-right exit) could very likely be hiding in this unexplored southeastern quadrant of B1F!
- We are currently standing at (33, 15) and will immediately head to (33, 30) and sweep Columns 34-37 on Rows 30-33 systematically!

## Overview & Major Connections:
- **1F Entrance/Exit**: Connects to Route 10 at (15, 3) (verified on Turn 20628). Map Marker '🚪' placed at (15, 3).
- **Ladders**:
  - Ladder A: Located at (17, 11) on 1F (visually observed but blocked from the western starting chamber).

---

## Rock Tunnel 1F Layout & Discoveries:
- **Chamber 1 (Western Starting Area)**:
  - Bounded on the West by Column 13.
  - Rows 4-7 are passable corridors extending East from Column 14 to at least Column 28.
- **Solid Wall Barriers**:
  - Column 18-19 has a continuous solid rock wall (TYPE_2889) extending from Row 8 to at least Row 15, blocking direct South movement on those columns.
  - Rows 14 and 15 form a completely solid horizontal barrier of rock across Columns 18-33.
  - Column 17 is blocked at Rows 8 and 9 by TYPE_2889 solid rock, isolating the Western Chamber from the (17, 11) ladder.
- **Eastern Corridor (Rows 10-13)**:
  - Connects to the western chamber and Pokémaniac's area.
  - Extends East from Column 20 to at least Column 33 as a wide, open corridor.

---

## Rock Tunnel B1F Layout & Discoveries (Updated Turn 23041):
- **Chamber 1 (B1F Starting Chamber)**:
  - Bounded on the North by Row 21 (solid wall TYPE_2889).
  - Bounded on the East by Column 38 (solid wall TYPE_2889).
  - Bounded on the West by Columns 26-27 (continuous solid rock wall TYPE_2889 extending from Row 21 to Row 30).
  - The ladder to 1F is located at (33, 25).
  - Passages: The main exploration route leads South (beyond Row 29) on Columns 28-34. Exploration of the West-facing passage is blocked at Row 30 by the extension of the solid Column 26-27 rock wall, but we have successfully bypassed this wall at Row 31 (X=26, Y=31) (verified on Turn 20872).
- **Southern B1F Corridor (Rows 30-33, Columns 2-37)**:
  - Discovered on Turn 21591-21592.
  - Bounded on the North by Row 29 (solid rock TYPE_2889) for Columns 2-13 and 21-27. Column 14 at Row 29 is potentially passable (TYPE_3fe2).
  - Bounded on the South by Row 34 (solid rock TYPE_2770/TYPE_2889) for all columns 2-37.
  - Bounded on the West by Column 1 (solid rock TYPE_2889) for Rows 29-35.
  - This forms a wide, 4-tile-tall horizontal corridor (Rows 30-33) extending from the eastern Starting Chamber (Column 37) all the way West to Column 2 (completely mapped on Turn 21626).
- **Western Connecting Passage (Rows 24-29, Columns 14-20)**:
  - Discovered and physically verified on Turns 21665-21685.
  - Connects the Southern Corridor (Rows 30-33) to the Western Bypass Corridor (Columns 20-25).
  - Specific path:
    - Column 14, Row 28 is blocked by the defeated Jr. Trainer ♀ sprite.
    - However, Column 15 is fully open and passable on Rows 24-29, allowing complete bypass of the trainer blockage!
    - At Row 24, Columns 14-20 are completely open (TYPE_3fe2), connecting directly to Column 20 (Western Bypass Corridor).
  - This provides a secondary, fully open pathway connecting the Southern B1F corridor directly to the upper B1F areas and the eastern starting chamber!
- **Upper Bypass Corridor (Proven Connection)**:
  - Verified on Turn 21081 via the Systematic Upper Connection Testing Protocol.
  - Rows 18 and 19 form a completely open, passable corridor extending from Column 20 to at least Column 29.
  - This corridor runs directly over the top of the solid Column 26-27 rock wall (which ends at Row 20).
  - It connects the Western vertical/horizontal bypass corridor (Columns 20-25, Rows 21-25) directly to the Eastern starting chamber's Column 29 boundary.
  - This is a verified loop-free corridor, allowing direct, unobstructed travel between the starting chamber and the far western regions of B1F!

## B1F Systematic Layout Tracking & Exploration Protocol:
- **Intersection Tracking**: Every branching path will be logged by its coordinate (X, Y) with all available directions.
- **Loop Identification**: We will cross-reference newly reached coordinates against our existing logs. If a coordinate is already logged, we classify it as a circular loop. If not, it is a new path.
- **Notepad Management Milestone**: Upon reaching the next ladder on B1F or exiting to Lavender Town, we will unload "Locations/Route9" and "Locations/Route10" to maintain a clean notepad environment and prevent hitting the 10-loaded-notepad limit.

---

## Trainer Battles Database (Updated Turn 21239):
### Rock Tunnel 1F:
1. **Pokémaniac (Turn 20677)**:
   - Location: (22, 8) on 1F.
   - Opponent: CUBONE Lv 23 (Ground).
   - Strategy: Switched SPARKY immediately to GEMMY (Wartortle) Lv 31.
   - Result: Defeated!

2. **Hiker (Turn 21239)**:
   - Location: (5, 17) on 1F (walks south to intercept player at 5, 18).
   - Dialogue: "Hmm. Maybe I'm lost in here..."
   - Opponent: ONIX Lv 20, ONIX Lv 20, GEODUDE Lv 20.
   - Strategy: Lead with GEMMY (Wartortle) Lv 32, use WATER GUN (4x super-effective).
   - Result: Defeated on Turn 21251!

3. **Hiker (Turn 21295)**:
   - Location: (16, 14) on 1F (intercepts player at 16, 15).
   - Dialogue: "Outsiders like you need to show me some respect!"
   - Opponent: GEODUDE Lv 21, GRAVELER Lv 21.
   - Strategy: Lead with GEMMY (Wartortle) Lv 33, use WATER GUN (4x super-effective).
   - Result: Defeated on Turn 21310!

### Rock Tunnel B1F:
2. **Pokémaniac / Jr. Trainer ♀ Sofia (Turn 20872)**:
   - Location: (26, 31) on B1F.
   - Dialogue: "I draw POKéMON when I'm home."
   - Opponent: SLOWPOKE Lv 25 (Water/Psychic).
   - Strategy: Lead with SPARKY (Pikachu) Lv 23, switch to GEMMY (Wartortle) Lv 31.
   - Result: Defeated on Turn 20925! GEMMY finished Slowpoke with a critical hit BITE.

3. **Jr. Trainer ♀ (Turn 20976)**:
   - Location: (16, 28) on B1F (walks east to intercept player at 17, 28).
   - Dialogue: "I don't often come here, but I will fight you."
   - Opponent: ODDISH Lv 22, BULBASAUR Lv 22.
   - Strategy: Lead with GEMMY (Wartortle) Lv 31, use BITE to defeat.
   - Result: Defeated on Turn 20989! GEMMY gained EXP and remains in perfect health.

4. **Pokémaniac (Turn 21028)**:
   - Location: (20, 21) on B1F (walks east to intercept player at 24, 21).
   - Dialogue: "Do you know about costume players?"
   - Opponent: CHARMANDER Lv 22, CUBONE Lv 22.
   - Strategy: Lead with GEMMY (Wartortle) Lv 32, use WATER GUN (super-effective) to defeat.
   - Result: Defeated on Turn 21038! GEMMY leveled up to 32 and learned no new moves.

5. **Hiker (Turn 21137)**:
   - Location: (35, 5) on B1F (walks east to intercept player at 36, 5).
   - Dialogue: "Hit me with your best shot!"
   - Opponent: MACHOP Lv 20, ONIX Lv 20.
   - Strategy: Lead with GEMMY (Wartortle) Lv 32. Use BITE on Machop and WATER GUN (4x super-effective) on Onix.
   - Result: Defeated on Turn 21147! Got ¥700.

---

## Wild Encounters Database:
- **Scientific Tracking Methodology (Established Turn 20858)**:
  - We log every wild encounter inside Rock Tunnel here.

| Species | Levels | Encounter Count | Matchup Strategy | Notes & Verification |
|---------|--------|-----------------|------------------|----------------------|
| ZUBAT   | 15,17,18| 4               | Thundershock/Run | Turn 20733 (Lv17), Turn 20784 (Lv18), Turn 21107 (Lv17), Turn 21281 (Lv15) |
| GEODUDE | 17     | 2               | Run              | Turn 21331 (Lv17), Turn 21412 (Lv17)                                         |
| MACHOP  | 15     | 4               | Run              | Turn 21349 (Lv15), Turn 21361 (Lv15), Turn 21407 (Lv15), Turn 21451 (Lv15)   |

### Southeast B1F Exploration Plan & Socratic Answer (Turn 21807):
- **Socratic Question 1 (Southeast Exploration Protocol)**: Sweep B1F Columns 34-37 on Rows 30-33 to search for a new ladder or exit.
  - **Verified Result (Turn 23440)**: Fully executed the 4x4 grid sweep on Columns 34-37, Rows 30-33, and confirmed that the entire southeast quadrant of B1F contains no exit, ladder, or active warp. This proves the southeast quadrant is inert.

### B1F Middle-Right Corridor Verified Layout & Discoveries (Resolved Turn 22081):
- **Empirical Status**: Fully Resolved!
- **Verified Corridor**: Rows 10-13 on Columns 26-37 form a wide, completely open, passable corridor (TYPE_3fe2).
- **Vertical Connection**: There is a wide vertical gap on Columns 32-35 across Rows 14 and 15 connecting this upper corridor directly to the lower area (Rows 16-17 on Columns 26-35).
- **Obstacles**:
  - Row 14 & 15 form a completely solid rock barrier (TYPE_2770, TYPE_2889) across Columns 26-31.
  - Column 30 has a Hiker at (30, 12) who walks down to (30, 13) to intercept. He was successfully defeated on Turn 22049.

6. Hiker (Turn 22042):
   - Location: (30, 12) on B1F (walked down to intercept player at 30, 13).
   - Dialogue: "My POKéMON techniques will leave you crying!"
   - Opponent: GEODUDE Lv 25.
   - Strategy: Lead with GEMMY (Wartortle) Lv 33, use WATER GUN (4x super-effective).
   - Result: Defeated on Turn 22049! Received money and registered map marker '☠️' at (30, 12).

### Socratic Question (The Middle Corridor Connection & 4th Ladder) - Resolved Turn 22085:
- **Socratic Question**: Does this middle-right corridor connect directly to the middle-left corridor (Columns 17-23, Rows 10-13) to form a single continuous East-West highway across B1F? If so, where is the 4th ladder (leading to the south-east exit area of 1F)?
- **Empirical Status**: Fully Resolved!
- **Direct Connection Finding**:
  - Columns 24 and 25 on Rows 9-15 are completely solid rock walls (TYPE_2889/TYPE_2770), dividing the eastern Middle-Right Corridor from the western Middle-Left Corridor on these rows.
  - However, Columns 24 and 25 on Rows 16 and 17 are completely open and passable (TYPE_3fe2), forming a direct horizontal connection between the eastern and western sides of B1F!
- **Connecting Path**: From (26, 13), we can walk East to (32, 13), Down to (32, 16), West to (23, 16), and Up to B1F Ladder C at (23, 11). However, Row 16 has a solid wall blockage at Column 18-19, meaning the eastern Middle-Right zone is completely isolated from the western system on Rows 16-17.
- **The 4th Ladder Search**:
  - Since the Middle-Right Corridor (Rows 10-13) and its vertical connector (Columns 32-35) connect to B1F Row 16, let's explore if there's a 4th ladder along this connection.
  - **B1F Rows 16-17 Corridor (Columns 14-37) - Resolved Turn 22174**:
    - **Verification**: Fully verified that Rows 16-17 from Column 14 to Column 37 form a wide open, passable corridor (TYPE_3fe2) with a solid blockage at Column 18-19.
    - **The 4th Ladder Finding**: Visually and physically verified that no ladder exists at (37, 17) or any other Column 32-37 coordinate on Rows 16-17 on B1F.
    - **East-West Blockage**: Physically proved on Turn 22203 that Column 18-19 is completely blocked on Row 16 by solid rock wall TYPE_2889. Therefore, B1F Rows 16-17 do not form a direct, continuous horizontal connection across the entire map, and the eastern Middle-Right zone remains isolated from the western system on Row 16.

### Transition Protocol to Lavender Town (Overwatch Alignment):
- **Objective**: Prevent context bloat and ensure high-efficiency database management.
- **Trigger**: Upon exiting Rock Tunnel onto Route 10 South / Lavender Town.
- **Step-by-Step Procedure**:
  1. **Unload Completed Notepads**: Unload the following 5 notepads immediately:
     - `Locations/RockTunnel`
     - `Locations/Route10`
     - `Scratchpad/RockTunnel_Pathfinding`
     - `Scratchpad/Route9_Route10_RockTunnel_Strategy`
     - `Mechanics/PikachuTrainingAndGrindingPlan` (or save its core strategy to Main/Archive and unload)
  2. **Initialize Lavender Town Database**: Create and load:
     - `Locations/LavenderTown_PointsOfInterest` (for verified POIs/NPCs/buildings)
     - `Scratchpad/LavenderTown_Exploration` (for live exploration notes)
  3. **Employ Regional Database Agent**: Call the custom `regional_database_agent` to systematically parse and compress all raw exploration logs, landmark coordinates, and points of interest for Lavender Town, Route 10 South, and surrounding areas to prevent context memory bloat.
  4. **Establish Strategic Map Markers**: Define markers for the Lavender Pokémon Center, Pokémon Tower, and Volunteer House.
- Turn 23706: Tested walking Down from (16, 7) onto (16, 8) (TYPE_2770). Movement failed (bumped), proving that TYPE_2770 at (16, 8) has solid, impassable collision on Rock Tunnel 1F. Therefore, Columns 14-17 are completely blocked at Rows 8 and 9, meaning there is no way to walk directly Down from the upper corridor (Rows 4-7) to the middle area (Rows 10-11) on these columns.

<hr>