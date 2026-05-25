<h1><code>Locations/MtMoon_B2F</code></h1>

# Mt. Moon B2F Location Records

## Connections:
- **Ladder to B1F**: Located at (15, 27). Connects to Mt. Moon B1F at (13, 27). Verified on Turn 6309.
- **Stairs to B1F (TYPE_4b8d)**: Located at (24, 23) and (25, 23). Verified on Turn 6238 as passable platform stairs.
- **Southern Section Isolation (Verified Turn 8199)**:
  - The southern section of B2F (accessible via the ladder at (15, 27)) is completely isolated from the northern and central sections by a solid wall of rock at Row 21 (columns 27, 28, 29, 32, and 33 are TYPE_2889 rock walls, and columns 30 and 31 are TYPE_de37 obstacles).
  - Standing at (28, 22) on Turn 8199, we attempted to walk Up into (28, 21) (TYPE_2889) and directly collided with the wall (0 tiles visited), proving that the eastern corridor is blocked and does not connect the southern and northern/central sections of B2F.
  - To traverse Mt. Moon, we must backtrack up the ladder at (15, 27) to B1F, and find another way.

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
- **Verified Fact (Turn 8592)**: The Northern Section (Rows 5-11, Columns 24-30) is a completely enclosed, isolated cul-de-sac pocket. Row 12 Column 25 acts as a solid rock cliff wall (mismarked as TYPE_2770 on the overlay) which prevents any southern traversal to the central stairs. It is a dead end.
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
  - This platform is completely isolated from the Central Elevated Platform and does not allow any western or northern traversal beyond Column 23, making it a dead end where only HP UP was obtained at (25, 21). Verified on Turn 8170.

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
- **Central Vertical Wall Bypass (Verified Turn 8864)**: Column 13 Rows 16, 17, 18, and 19 are fully passable cavern floor of TYPE_3fe2. Walking through Column 13 on these rows allows direct overworld traversal between the east side and west side of Mt. Moon 1F, without needing any underground ladder backtracking. This connects the central-eastern vertical corridor to the central-western open area.

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
- [ ] Traverse Mt. Moon to reach Route 4
- [ ] Reach Cerulean City

## Directory
- `Locations/PalletTown` - Permanently verified Pallet Town location records.
- `Locations/Route1` - Permanently verified Route 1 connections and layout features.
- `Locations/ViridianCity` - Permanently verified Viridian City connections and buildings.
- `Locations/PewterCity` - Permanently verified Pewter City location, gym, and connection records.
- `Locations/Route3` - Permanently verified Route 3 connections, pathing, and bidirectional ledge gaps.
- `Mechanics/General` - Verified game mechanics and controls.
- `Scratchpad/Route3_MtMoon_Cerulean` - Active progression, checklist, and trainer tracking for Route 3 and Mt. Moon.
- `Archive/ViridianForest_Grinding` - Archived grinding, switch-training, and leveling preparation in Viridian Forest.

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

## Verified Team Roster:
- **GEMMY (WARTORTLE)** - Lv 20, Water. Moves: TACKLE, TAIL WHIP, BUBBLE, WATER GUN.
- **BIRBIE (PIDGEY)** - Lv 5, Normal/Flying. Moves: GUST, SAND-ATTACK.
- **REMY (RATTATA)** - Lv 4, Normal. Moves: TACKLE, TAIL WHIP.
- **SPARKY (PIKACHU)** - Lv 11, Electric. Moves: THUNDERSHOCK, GROWL, THUNDER WAVE.
- **BUGGY (BUTTERFREE)** - Lv 12, Bug/Flying. Moves: TACKLE, STRING SHOT, CONFUSION.
- **ROCKY (GEODUDE)** - Lv 7, Rock/Ground. Moves: TACKLE. HP 24/24. Captured on Turn 6720 with a Poké Ball.

## Item Pickup Collision Mechanic:
- **Hypothesis**: Poké Ball items on the floor in Gen 1 are solid sprites that block player movement. To collect them, the player must stand adjacent, face them, and press 'A' to interact, rather than walking onto them.
- **Verification**: On Turn 6803, standing at (28, 5) facing Right towards the Poké Ball item at (29, 5), pressing 'A' successfully collected the item (TM01 - Mega Punch), and the item sprite disappeared, proving that items on the floor are solid sprites in Generation 1.
- **Conclusion**: Floor item sprites are indeed solid and impassable. They must be collected by standing adjacent, facing them, and pressing 'A'.

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

<h1><code>Scratchpad/Route3_MtMoon_Cerulean</code></h1>

# Route 3, Mt. Moon, and Cerulean City Progression Scratchpad
- Started: Turn 4122, Timestamp: Sunday, May 24, 2026 at 6:18 AM PDT

## Current Status:
- Turn 9271: Standing at (32, 9) on Map 0_61 (Mt. Moon B2F) facing Right, adjacent to the Helix Fossil.
- Mt. Moon Progression Start: Turn 5170.

## Progression Roadmap & Checklist:
- [x] Defeat Pewter Gym Leader Brock (Boulder Badge & TM34 secured!).
- [x] Healed team at Pewter City Pokémon Center at (13, 25).
- [x] Stock up on useful items at Pewter Poké Mart at (23, 17) (Secured 4 Potions, 3 Poké Balls, 3 Antidotes, 1 Paralyze Heal; ¥601 remaining).
- [ ] Explore the Museum of Science (optional, northern part of town).
- [x] Navigate east through Route 3 to Mt. Moon entrance.
- [ ] Traverse Mt. Moon to reach Route 4.
- [ ] Reach Cerulean City.

## Active B2F Exploration and Exit Strategy (Completed & Isolated):
- **Conclusion**: On Turn 9107, we completed systematic boundary testing of the Row 11/12 cliff. The eastern platform of B2F is completely isolated from the northern section containing the exit.
- **Systematic Boundary Testing**:
  - Turn 9047: Tested Column 32 Row 11/12 boundary by pressing Up. Blocked by an impassable cliff wall.
  - Turn 9069: Tested Column 31 Row 11/12 boundary. Blocked by an impassable cliff wall.
  - Turn 9078: Tested Column 33 Row 11/12 boundary. Blocked by an impassable cliff wall.
  - Turn 9087: Tested Column 34 Row 11/12 boundary. Blocked by an impassable cliff wall.
  - Turn 9107: Tested Column 35 Row 11/12 boundary. Blocked by an impassable cliff wall. (Completed - Eastern Platform is fully isolated!)

## Active B2F Northern Section Exploration:
- Started Turn 9271, Timestamp: Monday, May 25, 2026 at 9:32 AM PDT.
- **Empirical Breakthrough (Turn 9296)**:
  - We confirmed that the Northern Section (dark-purple area, TYPE_3fe2) is an isolated upper platform.
  - The Helix Fossil at (33, 9) was actually a standard background rock wall tile (TYPE_2889) with a swirly design.
  - The true fossils, Super Nerd Miguel, and the exit ladder are on the LOWER floor of B2F (the light-blue area, TYPE_2770).
  - To reach the lower floor, we must backtrack to the Central Section of B2F and walk north from the Eastern Floor Area.
- Backtracking Steps:
  1. [ ] Go west from (29, 10) to the ladder at (25, 9) on B2F and climb UP to B1F.
  2. [ ] On B1F, walk west to the ladder at (25, 9) and climb UP to 1F (17, 11).
  3. [ ] On 1F, walk west to (5, 5) and go DOWN to B1F (5, 5).
  4. [ ] On B1F, walk east along the horizontal corridor to (21, 17) and go DOWN to B2F (21, 17).
  5. [ ] On B2F, descend the central stairs to the Eastern Floor Area and walk north to the lower floor corridor.

- **Multi-Floor Backtracking Backup Strategy (If Column 35 is blocked)**:
  - If Column 35 is blocked, we will:
    1. Backtrack west along the Row 16 lower floor back to the central platform stairs.
    2. Ascend to (21, 17) and take the ladder back up to B1F.
    3. From B1F (21, 17), walk west along the horizontal corridor (Row 16/17) back to the far-NW pocket ladder at (5, 5).
    4. Ascend the (5, 5) ladder to 1F. (Completed!)
    5. On 1F, walk east along the Row 15 corridor to the north-central ladder at (17, 11). (Active!)
    6. Take the (17, 11) ladder down to B1F (25, 9).
    7. From B1F (25, 9), walk to (17, 11) and take the ladder down to B2F (25, 9) (the Northern Section).
    8. Walk east past the fossils and the Super Nerd to the exit ladder at (33, 9) leading to Route 4 East!

## Mt. Moon Team-Training Strategy & Timestamps (Turn 4801):
- Starting Turn for Pewter Restocking: Turn 4801
- Target Level-Ups:
  - **BUGGY (METAPOD)**: Lv 12 achieved! Learned Confusion!
  - **SPARKY (PIKACHU)**: Train to Level 11 to learn Quick Attack.

### SPARKY Training Session Log (Turn 6126):
- Starting Turn for SPARKY training: Turn 6126
- Starting Level: Level 6 (0/117 EXP)
- Target Level: Level 16 (to learn Quick Attack in Red/Blue)
- Timestamp: Sunday, May 24, 2026 at 3:25 PM PDT.
- Grinding Progress:
  - Turn 6149: Reached Level 7 after defeating Rocket Grunt's Level 11 Sandshrew (gained 108 EXP).
  - Turn 6168: Gained 66 EXP after defeating Rocket Grunt's Level 11 Rattata.
  - Turn 6198: Reached Level 8 after defeating Rocket Grunt's Level 11 Zubat (gained 63 EXP).
  - Turn 6263: Gained 69 EXP after defeating wild Level 9 Zubat.
  - Turn 6289: Gained 55 EXP after defeating wild Level 9 Geodude.
  - Turn 6307: Reached Level 9 and learned THUNDER WAVE! (Defeated wild Level 10 Zubat, gained 75 EXP).
  - Turn 6339: Gained 49 EXP after defeating wild Level 8 Geodude. SPARKY is now at Level 9 with 98/148 EXP.
  - Turn 6377: Gained 77 EXP after defeating wild Level 10 Zubat. SPARKY is now at Level 9 with 175/148 EXP.
  - Turn 6430: Gained 46 EXP after defeating wild Level 6 Zubat. SPARKY is now at Level 9 with 221/148 EXP.
  - Turn 6460: Defeated wild Level 8 Zubat. SPARKY gained 61 EXP (now Level 9 with 282/148 EXP).
  - Turn 6613: Defeated wild Level 10 Zubat. SPARKY gained 38 EXP and reached Level 10!
  - Turn 6825: Used RARE CANDY on SPARKY. He grew to Level 11! We discovered Pikachu learns Quick Attack at Level 16 in Red/Blue (unlike Level 11 in Yellow). Updating target to Level 16.

## Verified 1F Overworld Connections:
- **Row 15 Corridor (Turn 8382)**: Verified that Row 15 is a fully passable horizontal corridor (TYPE_3fe2) across Columns 21-25, connecting the western half of Mt. Moon 1F to the eastern half (specifically to the NE ladder at (25, 15)). This allows us to walk directly to the NE ladder from the southern/western areas without underground backtracking.

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