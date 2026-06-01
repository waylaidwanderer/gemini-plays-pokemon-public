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
(Tracking is managed automatically by the game state)

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

## Post-Rescue Progression Plan (Turn 38767)
4. **Saffron City & Silph Co. Progression**: Head to Saffron City to clear Silph Co., rescue the Silph President, defeat Boss Giovanni, and challenge Sabrina at Saffron Gym!
5. **Fuchsia City Progression**: Traverse Cycling Road or Route 12 south to Fuchsia City to challenge Gym Leader Koga.

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
- Benched Healing: Benched healing is 100% functional and allowed in Generation 1 battles. A Potion or other healing item can be used from the bag on a benched (inactive) Pokémon during battle. (Verified on Turn 29275)

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

# Mechanics/PikachuTrainingAndGrindingPlan (Updated Turn 26749)

- Current State & Combat Status (Turn 25557):
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

<h1><code>Locations/Route10</code></h1>

# Route 10 South & Lavender Town Geographical Records

## Overview
- **Map ID**: 0_21 (Route 10 South / Lavender Town transition region)
- **Entrance Warp to Rock Tunnel**: Located at (8, 53) (Map 0_21). Map marker '🚪' defined.
- **Exploration Started**: Turn 28708 (Friday, May 29, 2026 at 10:09 AM PDT).

## Regional Exploration Planning
- **Strategy for Mapping POIs**:
  - As we head south toward Lavender Town, we will systematically document:
    1. Land connections and boundaries.
    2. NPCs, their coordinates, and whether they are trainers or non-combatants.
    3. Wild grass regions, item locations, and any cuttable bushes or barriers.
  - To prevent context bloat, we will record raw exploration logs in temporary scratchpads, and use `lavender_database_agent` to compress them once we reach milestones.

## Lavender Town Transition Hypothesis & Verification Protocol
- **Hypothesis**: Moving further south/east along Route 10 South will trigger a transition into Lavender Town. (VERIFIED on Turn 28826!)
- **Transition Results & Empirical Proof**:
  - **Turn**: 28826 (Friday, May 29, 2026 at 10:34 AM PDT)
  - **Coordinate Transition**: Stepped south from Route 10 South (8, 73) on Map 0_21 and arrived at Lavender Town (8, 0) on Map 0_4.
  - **Verification 1 (Map ID)**: Game State Map ID changed from `0_21` to `0_4`.
  - **Verification 2 (Map Name Display)**: On-screen signpost overlay displayed "LAVENDER TOWN".
  - **Verification 3 (Visual Theme)**: Map palette changed to a purple/lavender color scheme, with the iconic stone wall architecture of the Pokémon Tower visible immediately to the east.
  - **Verification 4 (Audio)**: Background music transitioned to the eerie, melancholic Lavender Town theme.

## NPC Database
- **Jr. Trainer ♀ at (7, 54)**: Defeated on Turn 28728. (Defended by Map Marker '☠️' at 7, 54).
- **Hiker at (3, 57)**: Defeated on Turn 28750 (had Geodude L21, Onix L21; rewarded ¥735). GEMMY evolved into BLASTOISE! (Defended by Map Marker '☠️' at 3, 57).
- **Hiker at (3, 61)**: Defeated on Turn 28780 (had ONIX Lv 19, GRAVELER Lv 19; rewarded ¥665). Conversed on Turn 28768 before battle ("Ah! This mountain air is delicious!"). (Defended by Map Marker '☠️' at 3, 61).
- **Pokémaniac at (11, 64)**: Defeated on Turn 28800 (had CUBONE Lv 20, SLOWPOKE Lv 20; rewarded ¥1000). Intercepted us on Turn 28787 ("Hi kid, want to see my POKéMON?").

<hr>

<h1><code>Locations/RockTunnel</code></h1>

# Locations/RockTunnel Geographical Records (Map 0_82) (Updated Turn 28669)
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
- *Physical Execution Verification*: Checked and verified on Turn 23440 that the entire southeast quadrant of B1F (Columns 34-37, Rows 30-33) is completely inert with no active warp or ladder. The 4th ladder must be in the northwestern section.

## Overview & Major Connections:
- **1F Entrance/Exit**: Connects to Route 10 at (15, 3) (verified on Turn 20628). Map Marker '🚪' placed at (15, 3).
- **Ladders**:
  - Ladder C: Located at (17, 11) on 1F (visually observed but blocked from the western starting chamber).

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

7. **Jr. Trainer ♀ (Turn 28284)**:
   - Location: (11, 14) on B1F (adjacent to the (10, 14) signpost).
   - Opponent: JIGGLYPUFF Lv 21, PIDGEY Lv 21, MEOWTH Lv 21.
   - Strategy: Lead with GEMMY (Wartortle) Lv 34, use BITE to easily defeat.
   - Result: Defeated on Turn 28284! Received ¥420.

---

## Wild Encounters Database:
- **Scientific Tracking Methodology (Established Turn 20858)**:
  - We log every wild encounter inside Rock Tunnel here.

| Species | Levels | Encounter Count | Matchup Strategy | Notes & Verification |
|---------|--------|-----------------|------------------|----------------------|
| ZUBAT   | 15,16,17,18| 11              | Thundershock/Run | Turn 20733 (Lv17), Turn 20784 (Lv18), Turn 21107 (Lv17), Turn 21281 (Lv15), Turn 27833 (Lv17), Turn 27836 (Lv17), Turn 27845 (Lv18), Turn 27867 (Lv18), Turn 27876 (Lv17), Turn 27891 (Lv16), Turn 27936 (Lv17) |
| GEODUDE | 16,17   | 4               | Run              | Turn 21331 (Lv17), Turn 21412 (Lv17), Turn 27825 (Lv16), Turn 27882 (Lv17)                     |
| MACHOP  | 15     | 4               | Run              | Turn 21349 (Lv15), Turn 21361 (Lv15), Turn 21407 (Lv15), Turn 21451 (Lv15)   |
| ONIX    | 13,17   | 2               | Run              | Turn 27819 (Lv17), Turn 27848 (Lv13)                                        |

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

8. **Pokémaniac (Turn 28377)**:
   - Location: (3, 7) on B1F.
   - Dialogue: "You have a POKéDEX? I want one too!" (This was spoken, but the battle is with a Pokémaniac).
   - Opponent: SLOWPOKE Lv 20, SLOWPOKE Lv 20, SLOWPOKE Lv 20, SLOWPOKE Lv 20.
   - Strategy: Lead with GEMMY (Wartortle) Lv 34, use DIG.
   - Result: Defeated on Turn 28428! Received ¥1000.

9. **Hiker (Turn 28307)**:
   - Location: (6, 13) on B1F.
   - Opponent: GEODUDE Lv 21, GEODUDE Lv 21, GRAVELER Lv 21.
   - Strategy: Lead with GEMMY (Wartortle) Lv 34, use BITE or WATER GUN.
   - Result: Defeated on Turn 28331! Received ¥735.
- **Turn 28498 Jr. Trainer ♀ Battle Entry**:
  - Name: Jr. Trainer ♀
  - Location: (36, 21) on Rock Tunnel 1F (0_82).
  - Opponents: BELLSPROUT Lv 22, CLEFAIRY Lv 22.
  - Battle Details:
    - Bellsprout defeated with GEMMY's (Wartortle Lv 35) DIG move (Turn 28488).
    - Clefairy defeated with GEMMY's BITE move (Turns 28493-28497).
  - Payout: ¥440.
  - Verification: Battle fully completed on Turn 28498, and static map marker '☠️' defined at (36, 21).
- **Turn 28529 Jr. Trainer ♀ Battle Entry (Second Trainer)**:
  - Name: Jr. Trainer ♀
  - Location: (36, 24) on Rock Tunnel 1F (0_82).
  - Opponents: PIDGEY Lv 19, RATTATA Lv 19, RATTATA Lv 19, BELLSPROUT Lv 19.
  - Battle Details:
    - Pidgey Lv 19 defeated with GEMMY's (Wartortle Lv 35) BITE move (Turns 28515-28516).
    - Rattata Lv 19 (first) defeated with GEMMY's BITE move (Turn 28521).
    - Rattata Lv 19 (second) defeated with GEMMY's BITE move (Turn 28525).
    - Bellsprout Lv 19 defeated with GEMMY's BITE move (Turn 28528).
  - Payout: ¥380.
  - Verification: Battle fully completed on Turn 28529, and static map marker '☠️' defined at (36, 24).
- **Turn 28659 Trainer Battle Victory Details**:
  - Opponent: Jr. Trainer ♀ at (22, 26) on Rock Tunnel 1F.
  - Pokemon: MEOWTH Lv 20, ODDISH Lv 20, PIDGEY Lv 20.
  - Battle completed on Turn 28649. Got ¥400.
  - Map Marker '☠️' defined at (22, 26).

<hr>

<h1><code>Locations/Route10_North</code></h1>

# Locations/Route10_North (Map 0_21) (Updated Turn 28678)
- Map ID: 0_21
- Created Turn: 26834

## Overview:
- This is the northern segment of Route 10, located outside the northern exit of Rock Tunnel.
- The area connects to Route 9 in the west.

## Points of Interest:
- **Route 10 Pokémon Center (North)**: Located at (11, 19). The door is at (11, 19).
- **Rock Tunnel North Entrance**: Located at (8, 17) (passable cave mouth TYPE_3fe2).

## Overworld Blockages & Key Features:
- A cuttable bush is located directly to the east at (9, 18) (TYPE_5519).
- Another cuttable bush is located at (9, 20) (TYPE_5519).
- A solid fence (TYPE_2889) runs horizontally along Row 19 on Columns 4-7, isolating the northern cave mouth area from the southern path unless we cut the bush at (9, 18).
- Row 19 Column 8 is a solid tree (TYPE_2889).
- Row 19 Column 9 is passable grass (TYPE_3fe2).

## Physical Verification Logs:
- **Turn 26829**: Successfully exited Rock Tunnel onto Route 10 North at (8, 18).
- **Turn 26856**: Used PETAL's CUT to remove the second bush at (9, 20). Path to Route 10 Pokémon Center is now fully open.
- **Turn 26871**: Navigated to (11, 24) on Route 10 North. Visually confirmed a red-haired trainer at (7, 25) facing Right, whose sightline on Row 25 is blocked by a solid tree at (8, 25) (TYPE_2889).
- **Ledge Jump Test (Turn 26878)**: Verified that (14, 29) is a solid rock wall (TYPE_2889) and not a jumpable ledge.

## CRITICAL REALIZATION & CORRECTION (Turn 26898):
- **Visually & Geographically Proven**: We discovered that the area we are in is Route 10 North, not Route 10 South!
- **Proof of Work**:
  1. We exited Rock Tunnel at (8, 17) which is the same entrance we first entered on Turn 20624.
  2. The Pokémon Center at (11, 19) is the Route 10 North Pokémon Center.
  3. Row 30 is completely blocked by a solid, impassable mountain wall (TYPE_2889) across all columns because Route 10 North is separated from Route 10 South by this mountain.
  4. There is no horizontal or vertical passage leading south of Row 29 on the left side of this map.
- **Conclusion**: We did not traverse Rock Tunnel; we just walked in a circle and backtracked out of the north entrance. We must go back into Rock Tunnel to find the correct route to the true south exit!

<hr>

<h1><code>Reflection/Turn28101_Reflection</code></h1>

## Turn 28101 Reflection & Self-Assessment:
- **Immediate Execution**: I am actively navigating from my current position to Ladder B at (27, 3) on Rock Tunnel B1F to bypass the central impassable areas of 1F. We are currently at (25, 18).
- **Notepad Hygiene**: We successfully corrected the `rock_tunnel_navigator` tool's database of passable B1F tiles to include the Rows 10-13, Columns 26-37 Middle-Right corridor, which resolved our BFS navigation bug. The records in `Scratchpad/RockTunnel_Pathfinding` are highly detailed.
- **Map Hygiene**: Map markers are highly accurate and correspond to all verified blockages, trainers, and stairs.
- **Custom Tools**: Corrected and verified `rock_tunnel_navigator` to fully compute and automate our overworld travel step-by-step. Other tool ideas include:
  1. `item_picker` to find item coordinates (redundant in RT).
  2. `battle_escape_helper` to automate selecting run (but manually running is simple and safe).
  3. `heal_pokemon_at_counter` (exists and works).
  4. `grind_in_grass` (exists and works).
  5. `tile_type_dictionary_builder` to catalog tile ID properties (we do this in notepads).
- **Goal Clarity**: Goals are clear. What: Reach Lavender Town. How: Ladder B detour to 1F, then Ladder C back to B1F NW.
- **Error Analysis**: We corrected our tool which had a disconnected graph due to a narrow definition of the B1F Middle-Right corridor.

<hr>

<h1><code>Locations/LavenderTown</code></h1>

# Lavender Town Geographical Records

## Regional Database (Compressed)
- **Lavender Town (Map 0_4)**: Connected North to Route 10 South at (8,0) and South to Route 12 Map 0_23 at (8,17). Warps: Pokémon Center Map 0_141 Door at (3,5) warps to (3,7) | Poké Mart Door at (15,13) | Pokémon Tower 1F Map 0_142 Door at (14,5) warps to (10,17).
- **Locations & NPCs**:
  - Pokémon Center (Map 0_141): Heals party at counter (3,3).
  - Pokémon Volunteer House (Map 0_149): Door exit at (2,7). Volunteer NPC at (3,5) (notes Mr. Fuji is missing), Psyduck at (6,4) ('Gwappa!'), Nidorino at (1,3) ('Gaoo!').
  - Name Rater's House (Map 0_229): Name Rater NPC at (5,3).
  - Poké Mart (Map 0_150): Inventory: Great Ball (¥600), Super Potion (¥700), Revive (¥1500), Escape Rope (¥550), Super Repel (¥500), Antidote (¥100), Burn Heal (¥250), Ice Heal (¥250), Parlyz Heal (¥200).
  - Pokémon Tower 1F (Map 0_142): Stairs to 2F at (18,9). Mourning NPC at (13,7) ("My GROWLITHE... Why did you die?"). Channeler at (17,7) ("There are spirits up to mischief!").
  - Pokémon Tower 2F (Map 0_143): Stairs to 1F at (18,9). Rival Blue stands at (14,5) and initiates battle at (14,6) (vanishes after defeat). Rival Blue Team: Pidgeotto (Lv.25), Gyarados (Lv.23), Growlithe (Lv.22), Kadabra (Lv.20), Ivysaur (Lv.25). Defeated on Turn 29138, gained ~4000 EXP, GEMMY leveled to 37 (max HP 119/119), prize ¥1625.
  - Pokémon Tower 3F (Map 0_144): Stairs to 2F at (3,9). Channeler at (10,13) (defeated Turn 29176, Gastly Lv22, "Be gone! Evil spirit!"). Channeler at (9,10) (defeated Turn 29187, Gastly Lv24, "Kekeke.... Kwaaah!").

## Verified Spiritual Block Mechanics (Turn 29157 - 29161)
- **Empirical Proof of Spiritual Block**:
  - **Context**: On Turn 29157, encountered a wild "GHOST" (L21) at (5, 11) inside Pokémon Tower 3F (Map 0_144).
  - **Attacking Block**: On Turn 29159, selected DIG (GEMMY, Blastoise L37). The attack was completely blocked with the message: "Get out... Get out..." and GEMMY was "too scared to move". This confirms that without the SILPH SCOPE, we cannot damage or battle wild spectral entities in the tower.
  - **Escape Check**: On Turn 29161, selected RUN. Successfully escaped the encounter. This confirms we can safely flee from wild GHOST encounters.
- **Completed Progression**: With the Silph Scope acquired, we successfully bypassed all Ghost blocks, defeated Marowak L30 on 6F, rescued Mr. Fuji on 7F, and obtained the Poké Flute in Lavender Town.

## Pokémon Tower Floor-by-Floor Complete Mapping
  - Pokémon Tower 4F (Map 0_145): Stairs to 3F at (3,9), Stairs to 5F at (18,9). Channeler at (15,8) defeated (Gastly Lv22), Channeler at (5,10) defeated (Gastly Lv22).
  - Pokémon Tower 5F (Map 0_146): Stairs to 4F at (3,9), Stairs to 6F at (18,9). Purified Healing Pad zone at (10,9)-(11,9) (fully restores HP/PP). Channeler at (17,7) defeated (Gastly Lv22), Channeler at (12,8) is friendly ("rest here...").
  - Pokémon Tower 6F (Map 0_147): Stairs to 5F at (18,9). Channeler at (14,10) defeated (Gastly Lv22, Gastly Lv22, Gastly Lv22), Channeler at (16,5) defeated (Gastly Lv24), Channeler at (9,7) defeated (Gastly Lv24). Static Level 30 Ghost of Marowak at (9,16) defeated on Turn 38091 (cannot be caught, must be defeated to unblock the stairs).
  - Pokémon Tower 7F (Map 0_148): Stairs to 6F at (9,16). Rocket Grunt 1 at (10,11) defeated, Rocket Grunt 2 at (12,9) defeated, Rocket Grunt 3 at (9,7) defeated. Rescued Mr. Fuji at (10,3).

## Post-Rescue Verification & Achievements (Turn 38191)
- Rescued Mr. Fuji from Pokémon Tower 7F, resolving the spiritual crisis in Lavender Town.
- Teleported to Pokémon Volunteer House (Map 0_149). Mr. Fuji is now located at (3,1). Speaking to him here rewards the player with the POKE FLUTE.

<hr>

<h1><code>Locations/Route8</code></h1>

# Route 8 Location Records (Map 0_19)

## Overview & Map Transitions
- **Exploration Started**: Turn 29240 (Friday, May 29, 2026 at 12:20 PM PDT).
- **Eastern Exit**: Connects to Lavender Town (Map 0_4) at (0, 8) via the narrow corridor at (59, 8) (verified on Turn 29240).
- **Western Exit**: Leads towards Saffron City Gatehouse.
- **Underground Path**: Connects Route 8 to Route 7, bypassing Saffron City entirely and leading to Celadon City.

## Points of Interest
- **Tall Grass Patches**:
  - Located in the central and northern areas of Route 8.
  - Contains wild Pokémon (to be cataloged).

## NPC & Trainer Directory
- Lass at (51, 12): Defeated on Turn 29293. Gained 319 EXP, got ¥330. Had CLEFAIRY L22. Dialogue: "Stop! Don't be so mean to my CLEFAIRY!"
- Lass Paige at (26, 5): Defeated on Turn 29399. Gained ¥285. Had PIDGEY L19, RATTATA L19, NIDORAN♂ L19, MEOWTH L19, PIKACHU L19. Dialogue: "We must look silly standing here like this!" Note: Her battle was triggered on Turn 29377 by interacting with the Biker at (26, 6) from (26, 7) facing Up, revealing a Gen 1 sprite-to-script mapping glitch.
- Lass Andrea at (26, 3): Defeated on Turn 29437. Gained 576 EXP, got ¥345. Had NIDORAN♀ L23, NIDORINA L23. Dialogue: "Why? Why??"
- Lass Julia at (26, 5): Defeated on Turn 29452. Gained ¥432. Had MEOWTH L24, MEOWTH L24, MEOWTH L24. Dialogue: "MEOWTH is so cute, meow, meow, meow!" Triggered on Turn 29440 when walking to (25, 5).
- Biker at (26, 6): Standing at (25, 6) facing Right and talking to him on Turn 29457, he says: "SAFFRON's gate keeper won't let people through." He is an NPC, not a battleable trainer from this side, or his script has been overridden/linked with Lass Paige.
- Gambler at (46, 13): Defeated on Turn 29312. Gained ¥1680. Had GROWLITHE L24, VULPIX L24. Dialogue: "I'm a rambling, gambling dude!" and "Lanslides!..."
- Super Nerd Erik at (11, 5): Defeated on Turn 29522. Gained ¥500. Had VOLTORB L20, KOFFING L20, VOLTORB L20, MAGNEMITE L20. Dialogue: "Ow! Meltdown!"

## Saffron Gatehouse & Route 8 Underground Path Verification
- **Route 8 Underground Path Verification**:
  - **Step 1 (Verified Turn 29506)**: External building door is located at (13, 3) on Route 8 (Map 0_19).
  - **Step 2 (Verified Turn 29529)**: Entered the building. Internal Map ID is 0_80 (Route 8 Underground Path Entrance). We spawn at (3, 7) facing Up.
  - **Step 3 (Verified Turn 29529)**: The stairs warp to the Underground Tunnel are located at (4, 4) on Map 0_80.
  - **Step 4 (Verified Turn 29535 & 29556)**: Entered the Underground Path (Map 0_121), spawned at (47, 2), walked the horizontal corridor west, and exited via the stairs at (2, 5) to the Route 7 Gatehouse (Map 0_77).
  - **Step 5 (Verified Turn 29562)**: Spawned inside Map 0_77 at (4, 4), walked south through the door warp at (4, 7), and successfully emerged on Route 7 (Map 0_18) at (5, 14) on Turn 29562, establishing a complete overworld verification. We marked the Route 7 Gatehouse Door on Map 0_18 at (5, 13).

## Local Habitat & Wild Encounters
- **Wild Encounters Template (To be documented on future backtracks)**:
  - Species: [Species Name] | Level Range: [Min-Max] | Est. Encounter Rate: [Low/Medium/High] | Notes: [Details]

## Strategic Routing & Passability Discoveries (Turn 29326 - 29334)
- **Ledge Test**: Standing at (44, 13) on Turn 29326, pressed Down. Successfully jumped south over the horizontal barrier to (44, 14), proving the barrier between row 13 and row 14 is a jumpable LEDGE.
- **Fence Passability**: The vertical fence on columns 42/43 ends at row 13. Rows 14 and 15 are open path tiles, which allowed us to walk westward underneath the fence to reach column 41.
- **Cut Bush**: Discovered a cuttable bush at (41, 10) (TYPE_5519) blocking column 41. We positioned ourselves at (41, 11) facing Up on Turn 29334 to cut it using Bellsprout (PETAL).
- **Wall Openings**: Standing at (41, 11) on Turn 29343, we walked Up to (41, 10), Left to (40, 10), and Left again to (39, 10) on Turn 29344. This physical traverse definitively proves that (40, 10) is fully passable with no invisible collision boundaries or map-connection discrepancies, granting us access to the western grass area.
- **Second Cut Bush**: Standing at (30, 12) facing Left on Turn 29353, we successfully cut and cleared the bush at (29, 12) on Turn 29361 using PETAL's CUT. This opened a fully clear pathway to the vertical paved corridor.

<hr>

<h1><code>Locations/Route7</code></h1>

# Route 7 Location Records (Map 0_18)
- **Map Transition**: Entered Route 7 (Map 0_18) from the Route 7 Gatehouse (Map 0_77) by exiting through the southern warp at (4, 7), spawning at (5, 13) on Route 7.
- **Warp Connection**: The Route 7 Gatehouse door on Route 7 is located at (5, 13).
- **Physical Landmarks**:
  - A small building with yellow mesh-patterned windows is at (4, 10) to (7, 12). Entrance at (5, 13).
  - Ledges (TYPE_44f6) are located at row 11. Walkable gap at (8, 11).
  - Walkable gap in the row 7 ledge is at (4, 7).
  - Western exits to Celadon City (Map 0_6) are located at (0, 2) and (0, 3).
- **Saffron Gatehouse West Warp (Route 7)**: Saffron Gatehouse (Map 0_76) is entered from Route 7 by standing on column 11 and walking East (Right) into (12, 10). Permanent access to Saffron City was unlocked by giving the guard at (3, 1) FRESH WATER from our bag.

<hr>

<h1><code>Locations/CeladonCity</code></h1>

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
- **Game Corner**: (28, 19) (Visited, Map 0_135). Entering this door warps the player to the massive 20x18 Game Corner interior.
- **Diner**: (33, 19) (Visited, Map 0_137). Entering this door warps the player to the 10x8 Diner interior.
- **Gate at (33, 21)**: Tested on Turn 32547. Confirmed to be solid, impassable wall/post structure (TYPE_2889). No path exists directly north through this tile; one must go around to the eastern opening at (36, 21)-(37, 21) to enter the plaza.
- **Overworld Boundaries & Plaza Walkways**:
  - The northern horizontal street (Rows 10-14) is separated from the southern plaza (containing the Game Corner and Diner) by a continuous horizontal building roof and fence barrier (TYPE_2889) extending across Rows 15-18 on Columns 24-35.
  - To bypass this barrier and access the southern plaza from the north, players must walk East along Row 14 to Columns 36-37, which forms a completely open, 2-tile wide vertical bypass corridor.
  - Rows 20 and 22 are completely open checkered pavement (TYPE_3fe2) across Columns 32-41, providing horizontal walkways within the plaza to navigate around building facades.
  - Row 21 contains gates and posts (TYPE_2889) at Columns 32, 34, 35, 38, 40, and 41, but Columns 36-37 remain open for north-south passage.

## Celadon Department Store Database (Map ID 0_122 - 0_136)
- **Main Entrance**: Located on Celadon City Map 0_6 at (10, 13) (Turn 29690).

### 1F: Service Counter (Map 0_122)
- **Stairs (UP)**: Verified at (12, 1) (leads to 2F)
- **Elevator Door**: Verified at (1, 1) (leads to Elevator Cabin Map 0_127)
- **Directory Sign (11, 4)**: 
  - 1F: SERVICE COUNTER
  - 2F: TRAINER'S MARKET
  - 3F: TV GAME SHOP
  - 4F: WISEMAN GIFTS
  - 5F: DRUG STORE
  - ROOFTOP SQUARE: VENDING MACHINES
- **NPCs & Dialogue**:
  - Receptionist (8, 3) (Behind counter at (8, 4)): "Hello! Welcome to CELADON DEPT. STORE. The board on the right describes the store layout." (Spoken to on Turn 29710)

### 2F: Trainer's Market (Map 0_123)
- **Stairs (DOWN)**: (12, 1) (leads to 1F)
- **Elevator Door**: (1, 1)
- **Left Cashier (6, 3) (Behind counter at (6, 4))**: Sells TMs.
  - Inventory (Turn 29744 - Fully Verified):
    - TM32 (Double Team): ¥1000
    - TM33 (Reflect): ¥1000
    - TM02 (Razor Wind): ¥2000
    - TM07 (Horn Drill): ¥2000
    - TM37 (Egg Bomb): ¥2000
    - TM01 (Mega Punch): ¥3000
    - TM05 (Mega Kick): ¥3000
    - TM09 (Take Down): ¥3000
    - TM17 (Submission): ¥3000
- **Right Cashier (5, 3) (Behind counter at (5, 4))**: Sells standard items.
  - Inventory (Turn 29763 - Fully Verified):
    - GREAT BALL: ¥600
    - SUPER POTION: ¥700
    - REVIVE: ¥1500
    - SUPER REPEL: ¥500
    - ANTIDOTE: ¥100
    - BURN HEAL: ¥250
    - ICE HEAL: ¥250
    - AWAKENING: ¥200
    - PARLYZ HEAL: ¥200
- **NPCs & Dialogue**:
  - Customer at (19, 5): Bald man. "SUPER REPEL keeps weak POKéMON at bay... It's more effective than standard REPEL!" (Spoken to on Turn 29726)
  - Customer at (14, 3): Fat guy. [Wandering]

### 3F: TV Game Shop (Map 0_124)
- **Elevator Door**: (1, 1)
- **Stairs**: Escalator at (12, 1) goes UP. Escalator at (16, 1) goes DOWN (leads to 2F on Turn 30045).
- **NPCs & Dialogue**:
  - Customer NPC (2, 5): "You can identify POKéMON you got in trades by their ID Numbers!" (Spoken to on Turn 30022)
  - Trade NPC (7, 2): "All right! My buddy's going to trade me his KANGASKHAN for my GRAVELER!" (Spoken to on Turn 30025)
  - Trade NPC (8, 2): "Come on GRAVELER! ... GRAVELER turned into a different POKéMON! ... It's Golem!" (Spoken to on Turn 30029)
    - **Trade Evolution Insight**: The dialogue confirms that Graveler evolved into Golem upon being traded. This proves that trade-evolutions function identical to vanilla mechanics in this ROM.
  - Youngster with green shirt (11, 6): "Captured POKéMON are registered with an ID No. and OT, the name of the Original Trainer that caught it!" (Spoken to on Turn 30039)
  - Super Nerd NPC (16, 5): "Oh, hi! I finally finished POKéMON! Not done yet? This might be useful!" (Spoken to across row 4 wood counter on Turn 30056 and 30073). Gave us TM18 (Counter).
- **Shop Counters**: Row 4 has counters. Row 7 has green cashier tiles at (17, 7) and (19, 7).
  - **Empirical Audit (Turn 30056)**: Standing at row 3 facing Down, every counter spot was tested. Verified no active cashiers stand on the green tiles and no items can be purchased on 3F.

### 4F: Wiseman Gifts (Map 0_125)
- **Elevator Door**: (1, 1)
- **Stairs**: Escalator at (12, 1) goes UP. Escalator at (16, 1) goes DOWN (leads to 3F).
- **NPCs & Dialogue**:
  - Youngster NPC (met at (18, 2) on Turn 29976): "I heard something useful. You can run from wild POKéMON by distracting them with a POKé DOLL!"
- **Shop Counters**: Row 3 has counters. Row 4 has green cashier tiles at (3, 4), (5, 4), (7, 4), (9, 4), (13, 4), (15, 4), and (17, 4).
  - **Empirical Audit (Turns 29977 - 30006)**: Standing at row 2 facing Down, every single cashier tile was tested. All tests yielded no textboxes. Conclusion: No cashiers are active on 4F.

### 5F: Drug Store (Map 0_136)
- **Elevator Door**: (1, 1)
- **Left Cashier (5, 3) (Behind counter at (5, 4))**: Sells Battle Items.
  - Inventory (Turn 29844 - Fully Verified):
    - X ACCURACY: ¥950
    - GUARD SPEC.: ¥700
    - DIRE HIT: ¥650
    - X ATTACK: ¥500
    - X DEFEND: ¥550
    - X SPEED: ¥350
    - X SPECIAL: ¥350
- **Right Cashier (6, 3) (Behind counter at (6, 4))**: Sells Vitamins.
  - Inventory (Turn 29815 - Fully Verified):
    - HP UP: ¥9800
    - PROTEIN: ¥9800
    - IRON: ¥9800
    - CARBOS: ¥9800
    - CALCIUM: ¥9800

### Rooftop Square (Map 0_137 / 0_138)
- **Vending Machines (Rooftop)**: Purchased Saffron Guard Drinks (Turn 29885 - 29921)
  - FRESH WATER: ¥200
  - SODA POP: ¥300
  - LEMONADE: ¥350
- **Expected Wallet Change**: Gained 1x of each drink. Wallet went from ¥46393 to ¥45543. (Verified in Bag on Turn 30078).

### Elevator Cabin (Map 0_127)
- **Warp Connection**: Standing at (3, 1) facing Up and pressing A on the control panel at (3, 0) opens the floor selector. Exiting Down from row 3 warps back to the chosen floor's elevator landing at (1, 1).

<hr>

<h1><code>Locations/SaffronCity</code></h1>

# Saffron City Location Records (Map 0_10)

## Overview
- **Entrance**: Unlocked the city via the Route 7 Gatehouse (Turn 30198).
- Entered Saffron City from Route 7 (Map 0_18) via the West Gatehouse on Turn 30221. Spawns at (0, 18) and connects to Saffron's streets at (5, 18).

## Points of Interest
- **Pokémon Center**: Doorway at (9, 29). Entered from (9, 30) (Turn 30421).
- **Saffron Gym**: Doorway at (34, 3), blocked by Rocket Grunt at (34, 4) (Discovered Turn 30623).
- **Fighting Dojo**: Doorway at (26, 3). Challenged Dojo Master Kiyo and defeated all Blackbelts. Claimed the prize HITMONLEE (KICKY) at (4, 1) (sent to Box 1) on Turn 30781. The Dojo is now successfully cleared!
- **Silph Co. Head Office**: Doorway at (18, 21) blocked by Rocket Grunt at (18, 22) (Turn 30296/30299).
- **Blocked Doorway 2**: Doorway at (13, 11) blocked by Rocket Grunt (Turn 30261).
- **Blocked Northwest House (Copycat's House?)**: Entrance door at (7, 5) blocked by Rocket Grunt at (7, 6) ("What do you want? Get lost!") (Turn 30245).

## Landmarks & Coordinates
- Route 7 Gatehouse Entrance/Exit: at Map 0_10 (0, 18)? Yes, we came from (0, 18).

## Regional Gatehouse Passability Testing Protocol
To systematically verify the region-wide gate unlock rule:
1. **Verification Hypothesis**: Giving Fresh Water to the West Gatehouse guard (Turn 30198) permanently unlocked all Saffron City gatehouses (Route 5 North, Route 6 South, Route 8 East) without requiring additional drinks.
2. **Systematic Tests**:
   - **Route 8 Gatehouse (East)**: When nearby, enter the Route 8 Gatehouse, walk past the guard to Saffron City, and verify if we pass freely without being stopped or prompted for a drink. Record turn number, coordinates, and guard interaction.
   - **Route 5 Gatehouse (North)**: When nearby, enter the Route 5 Gatehouse, walk past the guard to Saffron City, and verify if we pass freely. Record turn number, coordinates, and guard interaction.
   - **Route 6 Gatehouse (South)**: When nearby, enter the Route 6 Gatehouse, walk past the guard to Saffron City, and verify if we pass freely. Record turn number, coordinates, and guard interaction.
3. **Database Logging**: Update this section with the empirical results of each gatehouse test to establish definitive 'proof of work'.

## Saffron City Quadrant Summary
- **SW Quadrant**: Pokémon Center at (9, 29) (Open/Visited).
- **SE Quadrant**: Mr. Psychic's House at (29, 29) (Open/Visited, obtained TM29).
- **NE Quadrant**: Saffron Poké Mart at (25, 11) (Open/Visited).
- **NW Quadrant**: Copycat's House at (7, 5) (Blocked by Rocket Grunt).

## Saffron Gatehouse Passability Test Results:
- **Route 5 Gatehouse (North) Test (Turn 30593)**:
  - **Methodology**: Walked north from Saffron City (Map 0_10) at (18, 2) on Turn 30592.
  - **Results**: Seamlessly warped through Saffron North Gatehouse (Route 5 Gatehouse) past the guard without any text box, prompts, or drink requests, emerging on Route 5 (Map 0_16) at (8, 35) on Turn 30593.
  - **Conclusion**: Confirmed! Route 5 Gatehouse is permanently open and free to traverse bidirectional without further drink requirements. This empirically proves the region-wide unlock is fully operational!
- **Route 7 Gatehouse (West) Test (Turn 30878)**:
  - **Methodology**: Walked West from Saffron City (Map 0_10) at (0, 18) to spawn on Route 7 (Map 0_18) at (19, 10). From there, entered Saffron West Gatehouse (Map 0_76) via its East door at (17, 10) on Turn 30875. Walked West from (5, 4) to (0, 4).
  - **Results**: Traversing Map 0_76 westward from (5, 4) to (0, 4) was completely unobstructed. The guard at (3, 1) made no attempts to stop us or prompt for a drink. We successfully reached the West warp at (0, 4) on Turn 30878.
  - **Conclusion**: Confirmed! Saffron West Gatehouse is 100% open and passable without any drink prompts.

- **Saffron Gatehouse (South) Test (Turn 37360 - 37365)**:
  - **Methodology**: Walked south from Saffron City (Map 0_10) at (20, 36) on Turn 37360.
  - **Results**: Warped directly onto Route 6 (Map 0_17) at (10, 0) on Turn 37361. Found ourselves in a trapped 1x2 alcove:
    - Bounded on the south by the yellow gatehouse building roof at (10, 2) (spans columns 8-13, row 2).
    - Bounded on the sides by grey helmet statues at (9, 0), (9, 1) and (11, 0), (11, 1).
    - Walked Up from Route 6 (10, 0) on Turn 37364 to warp back to Saffron City at (20, 35) on Turn 37365.
  - **Comprehensive Collision & Alignment Mapping**:
    - Direct connection alignment: `Route 6 Column = Saffron Column - 10`, `Route 6 Row = Saffron Row - 36`.
    - Every Saffron south-boundary column (18-23) through the yellow trellis wall is blocked or trapped on Route 6:
      - Saffron Col 18 -> Route 6 Col 8 (Blocked by building)
      - Saffron Col 19 -> Route 6 Col 9 (Blocked by grey pillars)
      - Saffron Col 20 -> Route 6 Col 10 (Warped to trapped 1x2 alcove)
      - Saffron Col 21 -> Route 6 Col 11 (Blocked by grey pillars)
      - Saffron Col 22 -> Route 6 Col 12 (Warped to trapped 1x2 alcove)
      - Saffron Col 23 -> Route 6 Col 13 (Warped to trapped 1x2 alcove)
    - All other Saffron columns are blocked by grey pillars at Saffron Row 38 (columns 16, 17 and columns 24, 25, 26).
  - **Conclusion**: BOTH Saffron East Gatehouse (Route 8) and Saffron South Gatehouse (Route 6) are completely impassable. Direct map connections bypass the gatehouse indoor maps but dump the player into trapped, physical dead-end alcoves because the actual gatehouse buildings block the exit on the target maps.
  - **Status**: Tested and Confirmed Impassable.

- **Saffron Gatehouse (East) Test (Turn 37218 - 37299)**:
  - **Methodology**: Walked East from Saffron City (Map 0_10) at (39, 18) and (39, 19). Warped directly from Saffron City into a 2x3 alcove on Route 8 (Map 0_19) at (0, 10).
  - **Results**: The alcove is physically blocked on the East side by Saffron East Gatehouse building (columns 2-5, rows 8-11). Walked LEFT from Route 8 (0, 8), (0, 9), or (0, 10) to warp back to Saffron City at (39, 16), (39, 17), or (39, 18).
  - **Systematic Row-by-Row Scan of Column 39**:
    - Conducted a complete, empirical boundary scan on column 39 in Saffron City for rows 20 to 30:
      - Row 20: Blocked by wooden post (TYPE_2889)
      - Row 21: Blocked by wooden post (TYPE_2889)
      - Row 22: Blocked by wooden post (TYPE_2889)
      - Row 23: Blocked by grey statue wall (TYPE_2889, verified Turn 37282)
      - Row 24: Blocked by grey statue wall (TYPE_2889, verified Turn 37285)
      - Row 25: Blocked by grey statue wall (TYPE_2889, verified Turn 37291)
      - Row 26: Blocked by grey statue wall (TYPE_2889, verified Turn 37293)
      - Row 27: Blocked by grey statue wall (TYPE_2889, verified Turn 37295)
      - Row 28: Blocked by grey statue wall (TYPE_2889, verified Turn 37296)
      - Row 29: Blocked by grey statue wall (TYPE_2889, verified Turn 37297)
      - Row 30: Blocked by grey statue wall (TYPE_2889, verified Turn 37298)
  - **Conclusion**: Confirmed! The entire eastern boundary of Saffron City from row 20 to 30 is completely blocked by solid fences/walls, and any direct map connections on rows 16 to 18 only place us in a trapped 2x3 alcove. There is NO direct open bypass on these rows. Saffron East Gatehouse interior Map 0_79 is bypassed, and the alcove on Route 8 is a physical dead end. We must seek an alternative route or find a functional door.

## Turn 50 Reflection & Saffron-Route 8 Direct Map Alignment Discovery (Turns 37218-37252)
- **Problem**: Walking east from Saffron City (39, 18) warps the player directly to Route 8 (0, 10). However, the player is trapped in a 2x3 alcove (columns 0-1, rows 8-10) by the Saffron East Gatehouse building (columns 2-5, rows 8-11) and fences (row 7 and row 11).
- **Hypothesis**: The entire eastern edge of Saffron City is connected directly to Route 8 via a direct 1-to-1 map connection offset by 8 rows: `Route 8 Row = Saffron City Row - 8`.
- **Systematic Test Results**:
  - Walked Left from Route 8 (0, 10) -> Saffron City (39, 18) (Turn 37232).
  - Walked Left from Route 8 (0, 8) -> Saffron City (39, 16) (Turn 37238).
  - Walked Left from Route 8 (0, 9) -> Saffron City (39, 17) (Turn 37246).
- **Passability Analysis**:
  - The gatehouse building on Route 8 spans rows 8 to 11.
  - To bypass the building, we need to enter Route 8 above the building (rows 0-7) or below the building (rows 12-15).
  - According to the -8 row offset, Route 8 rows 12-15 correspond to Saffron City rows 20-23.
  - The eastern boundary of Saffron City on rows 20-23 (column 39) is completely blocked by solid fences/walls, making direct physical bypass on these rows impossible. We must utilize Saffron West Gatehouse -> Route 7 -> Route 7/8 Underground Path to access Route 8 proper.

## Socratic Analysis of Saffron Gatehouses & Confinement Mechanics
- **Question**: Saffron City's North and West gatehouses are passable, while East and South dump the player into trapped alcoves. What is the topological reason, and how does physical gatehouse placement explain this?
- **Answer**: Saffron City's overworld connects directly to adjacent Route maps in this ROM, bypassing the indoor gatehouse maps. However, the physical gatehouse buildings still exist as solid structures on the Route 8 and Route 6 overworld maps:
  - **Route 8 (Map 0_19)**: Saffron (39, 16-18) connects to Route 8 (0, 8-10). This drops the player inside a 2x3 alcove trapped by the physical gatehouse building on columns 2-5 and fences on row 7/11.
  - **Route 6 (Map 0_17)**: Saffron (20, 36) connects to Route 6 (10, 0). This drops the player inside a 1x2 alcove trapped by the gatehouse building on columns 8-13, row 2, and grey statues on columns 9 and 11.
  - **Route 7 & Route 5**: Saffron West (0, 18) aligns to Route 7 (19, 10), and Saffron North (18, 0) aligns to Route 5 (8, 35). Both of these landing tiles are on the open streets, completely outside the physical gatehouse buildings. This explains why they are fully passable.

## Socratic Analysis of Inventory Management and Tower Items
- **Question**: How will a 9-slot margin specifically protect you as you traverse Route 8 and enter Pokémon Tower? What items do you expect to acquire and what species to capture?
- **Answer**: The 9-slot margin (currently 11/20 items) provides a critical safety buffer to ensure we can collect vital tower items (Rare Candy, HP Up, Elixir, X Accuracy) and the key item Poké Flute from Mr. Fuji. It allows us to capture wild Pokémon in the tower (Gastly, Haunter, Cubone) without running out of bag space or triggering 'pack is full' messages, completely eliminating backtracking to Saffron PC.

## Saffron Dual-Underground-Path Regional Bypass Strategy
- **Overview**: Since the direct overworld connections of Saffron South Gatehouse (Route 6) and Saffron East Gatehouse (Route 8) drop the player into trapped, dead-end alcoves, the region's dual Underground Paths provide the ONLY functional, completely open pathways to bypass these obstructions:
  - **East-West Bypass**: Use Saffron West Gatehouse (Route 7 Gatehouse) -> Route 7 -> Route 7/8 Underground Path -> Route 8 proper. This connects Celadon/Saffron West to Route 8 proper and Lavender Town.
  - **North-South Bypass**: Use Saffron North Gatehouse (Route 5 Gatehouse) -> Route 5 -> Route 5/6 Underground Path -> Route 6 proper. This connects Cerulean/Saffron North to Route 6 proper and Vermilion City.
- **Future Routing**: This dual-path layout allows us to seamlessly navigate across the entire Kanto region without being impeded by the non-functional East and South gatehouse warps.

<hr>

<h1><code>Reflection/Turn30857_Reflection</code></h1>

# Reflection - Turn 30857 (Gem)

## 2. Socratic Challenge: Route 5 Building
- **Correction**: The building on Route 5 at columns 11-15, rows 32-35 is actually the Pokémon Day Care, not the Underground Path. The actual Saffron-to-Cerulean Underground Path entrance on Route 5 is located further north at (17, 27).
- The sign on the Day Care building (reading "GYM" or similar) is a well-known tileset graphic/mapping glitch caused by shared tile IDs when using Crystal-based visual styles on standard Gen 1 maps.

## 3. Systematic Gatehouse Passability Tests
- **Route 5 Gatehouse (North)**: Verified on Turn 30593. Passed freely without any drink prompts.
- **Route 7 Gatehouse (West)**: Will verify on exit to Route 7 (approx. Turn 30880).
- **Route 6 Gatehouse (South) & Route 8 Gatehouse (East)**: Will systematically test when we travel near those routes.

## 4. Silph Co. Warp mapping strategy
- We will create a dedicated notepad `Mechanics/SilphCoWarps` once we enter Silph Co.
- Structure:
  `| From Floor | Coordinate | To Floor | Coordinate | Verified Turn |`
  `|------------|------------|----------|------------|---------------|`
- This keeps the data extremely compact, structured, and easy for the `saffron_warp_agent` to read.

## 5. Tool Maintenance & Pathing Strategy
- We will avoid using `generate_path` for large city navigations due to unmodeled buildings. Instead, we will use small, visually verified increments or straight-line road segments (such as Column 36/Route 18 main streets) which are 100% reliable.

<hr>

<h1><code>Locations/RocketHideout_B2F_SpinnerMaze</code></h1>

# Rocket Hideout B2F Spinner Maze Layout (Verified Turn 31668)

## Stop Tiles (TYPE_55d4)
- (2, 9)
- (8, 11)
- (14, 15)
- (9, 16)

## Spinners (Arrows)
- (4, 9): Left (TYPE_55d0)
- (4, 11): Right (TYPE_64a2)
- (4, 15): Right (TYPE_64a2)
- (5, 14): Right (TYPE_64a2)
- (8, 9): Left (TYPE_55d0)
- (8, 12): Up (TYPE_cf9b)
- (8, 15): Up (TYPE_cf9b)
- (9, 14): Down (TYPE_55cd)
- (10, 9): Left (TYPE_55d0)
- (10, 10): Up (TYPE_cf9b)
- (10, 15): Up (TYPE_cf9b)
- (11, 14): Down (TYPE_55cd)

## Impassable Obstacles (TYPE_2889)
- (6, 7)
- (2, 8), (3, 8), (4, 8), (6, 8), (8, 8), (10, 8)
- (2, 10), (5, 10), (6, 10), (7, 10), (8, 10), (9, 10), (11, 10)
- (2, 11), (11, 11)
- (2, 12), (4, 12), (5, 12), (7, 12), (9, 12), (11, 12)
- (5, 13), (6, 13), (7, 13), (9, 13)
- (2, 14), (3, 14)
- (11, 24) to (15, 24) (solid divider green blocks, verified Turn 34221)
- Screen-Verified obstacles (Turn 35582):
  - (15, 12) to (17, 12) (Green blocks)
  - (15, 13) (Green block)
  - (12, 14) to (15, 14) (Green blocks)
  - (17, 14) to (17, 16) (Green blocks)
  - (15, 15) (Green block)
  - (12, 15) to (13, 15) (Green blocks) (Physically tested on Turn 36650: attempting to walk Right from (11, 15) results in collision at (12, 15). This confirms these tiles are 100% solid walls)
  - (15, 19) to (15, 22) (Green blocks)
  - (14, 19) (Green block)
  - (11, 21) to (13, 21) (Green blocks)
  - (17, 17) to (18, 17) (Green blocks)
  - (17, 18) to (17, 19) (Green blocks)
  - (18, 14) to (18, 16) (Vertical partition wall blocks)
  - (18, 18) to (18, 19) (Vertical partition wall blocks)
  - (19, 16) to (20, 16) (Horizontal partition wall blocks)
  - (18, 22) (Elevator door block)

## Normal Walkable Floor Tiles (TYPE_3fe2)
- Row 7: (2, 7) to (5, 7), (7, 7) to (11, 7)
- Row 8: (5, 8), (7, 8), (9, 8), (11, 8)
- Row 9: (3, 9), (5, 9) to (7, 9), (9, 9), (11, 9)
- Row 10: (3, 10), (4, 10)
- Row 11: (3, 11), (5, 11) to (7, 11), (9, 11), (10, 11)
- Row 12: (3, 12), (6, 12), (10, 12)
- Row 13: (2, 13) to (4, 13), (8, 13), (10, 13), (11, 13)
- Row 14: (4, 14), (6, 14) to (8, 14), (10, 14)
- Row 15: (2, 15), (3, 15), (5, 15) to (7, 15), (11, 15)

## Southern Area Verified Layout & Routing (Turns 31720-31802)
### Stop Tiles (TYPE_55d4)
- (15, 18): Stop tile below Row 16 exit.
- (11, 20): Stop tile in south-central corridor.
- (9, 24): Stop tile in south-western corner.
- (14, 25): Stop tile in south-eastern corner.

### Spinners (Arrows)
- (13, 18): Left (TYPE_55d0) -> Slides to (11, 20) via (11, 18) Down spinner.
- (13, 22): Left (TYPE_55d0) -> Slides to (9, 24) via (9, 22) Down spinner.
- (10, 25): Right (TYPE_64a2) -> Slides to (14, 25) stop tile.

### Southern Pathways & Walkable Floors (TYPE_3fe2)
- Row 20: (10, 20) to (14, 20) [connected to 11, 20 stop tile]
- Row 21: (16, 21) to (22, 21) [fully open east-west corridor]
- Row 22: (10, 22) to (12, 22), (14, 22) [Row 14, 22 leads to 13, 22 Left spinner]
- Row 25: (11, 25) to (13, 25), (15, 25) to (16, 25) [Row 14, 25 stop tile leads right to 16, 25, then Up to Row 21]

### Key Landmarks & Transitions
- Stairs DOWN to B3F: Located in the south-east corridor at (21, 22) (Verified Turn 31802).
- Elevator Warp: Located at (25, 19). Entering this warp on Turn 32141 takes you to the Elevator Cabin (Map 0_203). It requires the LIFT KEY to operate.
- **Verified Fact (Turn 32686)**: The eastern portion of B2F is completely divided by a solid horizontal wall at row 16 extending from column 18 all the way to column 27 (TYPE_2889). No direct vertical pathway exists from the northeast area down to the southeast area on the east side of row 16. The only way to reach the stairs down at (21, 22) and the elevator at (25, 19) is to navigate the western spinner maze.
- **Spinner Maze (2, 9) to (15, 18) Bypass Route**: Fully verified and corrected on Turn 32928.
  - Starting at (2, 9), walk: `Right, Down, Down, Down, Down, Right, Down, Right, Right, Right, Right, Right, Down, Right, Right, Right, Right, Down` (18 steps).
  - *Correction Note (Turn 32928)*: The previous 17-step sequence was missing a 5th horizontal `Right` step on row 16 (index 11). This caused the player to walk `Down` into a trap at (12, 17) and slide to (16, 13) instead of stepping onto the (13, 16) Right-spinner to slide to (15, 18). Adding the 5th `Right` ensures the player steps onto (13, 16) to slide safely to (15, 18).
  - This path avoids the (8, 11) cul-de-sac trap and safely exits the maze at stop tile (15, 18).
- Route to Stairs: Slide from (15, 18) Left onto (13, 18) -> slides to (11, 20). Go Right to (14, 20) -> Down to (14, 22) -> Left onto (13, 22) -> slides to (9, 24). Go Right to (10, 24) -> Down onto (10, 25) -> slides to (14, 25). Walk Right to (16, 25) -> Up to (16, 21) -> Right to (21, 21) -> Down to (21, 22).
- **Direct Vertical Shortcut (Turn 34066)**: Rows 14 and 15 are completely open and walkable on columns 23 and 24, providing a direct horizontal walkway past the Column 23 partition wall. This allows players to walk directly from the eastern stairs landing at (27, 8) to the western area above the row 16 dividing wall, bypassing the spinners completely.

<hr>

<h1><code>Locations/RocketHideout_B3F_Layout</code></h1>

# Rocket Hideout B3F Detailed Layout & Routing

## Stairs and Key Transitions
- B2F to B3F Stairs: Connected symmetrically from B2F (21, 8) to B3F (25, 6) on Map 0_201. There are NO stairs to B2F in the southeast room of B3F.
- Southeast Room Staircase Correction: The staircase at B2F (21, 22) actually connects UP to B1F southern section (Map 0_199) at (21, 25), NOT B3F!
- B3F to B4F Stairs: Located on B3F West at (19, 19), which warps to B4F (19, 10). (18, 16) is actually an Up-spinner.
- Up-spinner at (19, 17): Stepping here immediately slides the player all the way north to (19, 9), blocking horizontal transit along row 17 and blocking direct southern access to the stairs at (19, 19) from the northeast corridor.
- B3F East-West Connection: Rows 5, 6, and 7 on Map 0_201 form a completely open and walkable northern corridor connecting B3F East (25, 6) to B3F West (11, 6). This completely bypasses the B2F spinner maze backtrack!

## Defeated Trainers & Landmarks
- Rocket Grunt 2: Defeated at (18, 17) (Verified Turn 31867).

## Key Room Layout & Passability
- **Southeast Room**: (18, 21) to (22, 26) is an open rectangular room containing the stairs up to B2F.
- **Row 25 & 26 Corridor**: Located entirely within the western section (Columns 10-22) of B3F. It extends west from Column 22 past Column 17 to Columns 10-11, providing access between B3F West's central area (containing the stairs at (19, 19)) and the western vertical corridor (Columns 10-11). It is completely blocked on the East at Column 23 by the solid Column 23 partition wall, meaning it does not connect to B3F East.
- **Western Corridor**: Columns 10 and 11 form a completely open vertical path from row 26 up to row 17 (Verified Turn 32114).
- **Column 23 Partition Wall**: Solid and impassable wall at (23, 17) to (23, 26). Direct collision tests performed systematically on all rows (17-26) on Turn 32765 - 32836.
- **Barriers**: Column 9 (rows 22-25) is blocked by plants/statues. Columns 12 and 13 (rows 22-24) are blocked by building walls (Verified Turn 32048).
- **Row 17 Northern Corridor**: Open from column 10 to 22. Physically walked on (19, 17), (20, 17), (21, 17), and (22, 17) on Turns 32187-32194 without triggering any warp.
- Row 10 wall: (11, 10), (12, 10), (15, 10), (16, 10), (17, 10), (18, 10), (19, 10), (21, 10) are solid green computer terminal blocks (TYPE_2889). Only (13, 10) and (14, 10) are open. This was visually verified on Turn 36434.
  - Row 19 entry tests: Tried entering columns 12-17 from column 11 on row 19, all collided (Turn 32791-32815).
  - Row 24 entry tests: Tried entering columns 12-17 from row 25, all collided (Turn 32779-32788).
  - Column 18: Walks freely from row 17 to row 21.

## Historical Proof of Work & Testing Logs
- *Turn 32105*: Collision on (23, 18) walking Right.
- *Turn 32193-32194*: Stood on (20, 17) and (19, 17) with no warp occurring.
- *Turn 32232-32235*: Walked along Column 11, verified no warps.
- *Turn 32256-32258*: Walked rows 25 and 26, verified no warps.
- *Turn 32765-32836*: Ran systematic passability tests on Column 23 partition on rows 17-26. Verified 100% solid.
- *Turn 32779-32815*: Ran systematic passability tests on Central Block north/south boundaries. Verified 100% solid.
- *Turn 33134*: Collision on (11, 16) walking Up. Row 16 column 11 verified solid.
- *Turn 33148*: Collision on (10, 16) walking Up. Row 16 column 10 verified solid.
- *Turn 33164*: Collision on (12, 16) walking Up. Row 16 column 12 verified solid.
- *Turn 33175*: Collision on (13, 16) walking Up. Row 16 column 13 verified solid.
- *Turn 33178*: Collision on (14, 16) walking Up. Row 16 column 14 verified solid.
- *Turn 33180*: Collision on (15, 16) walking Up. Row 16 column 15 verified solid.
  - (19, 16): Tested Turn 33261. Result: Confirmed solid wall, no passage.
  - (20, 16): Tested Turn 33274. Result: Confirmed solid wall, no passage.
  - (21, 16): Tested Turn 33280. Result: Confirmed solid wall, no passage.
  - (22, 16): Tested Turn 33291. Result: Confirmed solid wall, no passage.
  - (17, 16): Tested Turn 33295. Result: Confirmed solid wall, no passage.
  - (16, 16): Tested Turn 33297. Result: Confirmed solid wall, no passage.
## B3F Column 18 Corridor Verification (Turn 33477)
- **Verified Fact (Turn 36358)**: Visually and physically verified that B3F (18, 14) is a solid, impassable wall (TYPE_2889).
- **Conclusion**: Column 18 does NOT provide an opening to the north past row 15 on B3F. The wall on row 14 is continuous and solid here.
- **Plan**: We must backtrack along row 15 to the west to Column 16, then utilize the (16, 13) Up-spinner to bypass the row 14 horizontal blockages.
## B1F and B3F Unified Map Architecture (REVISED Turn 35286)
- **Verified Fact**: B1F and B3F are separate maps. B1F is Map 0_199 and B3F is Map 0_201.
- B3F has stairs down to B4F (Map 0_202) at (19, 19).
- B3F has stairs up to B2F (Map 0_200) at (25, 6).
- **Silent Python Scope Leakage Lesson (Turn 36567)**: In previous turns, we used manual BFS helper scripts that utilized loop variable 'y' within list comprehensions or nested loops. Since Python 3 leaks loop variables to the enclosing scope, this silently modified 'y' variables used elsewhere in the script to determine grid coordinates, writing wall tiles for row 12, 13, and 14 to row 22 in our layout representation. This teaches us to always use local scopes (like helper functions or list comprehensions inside clean environments) or distinct variable names when writing automated scripts to analyze layouts, and to always cross-verify layout data against raw visual coordinates.
## B3F Row 17 Passability Testing & Map Conflict Resolution
- **Critical Protocol**: Map 0_199 (B1F) and Map 0_201 (B3F) are completely separate maps with distinct collision layouts, even when visual tiles look identical. Coordinates from B1F must never be conflated with B3F.
- **Empirical Test 1 - Turn 36024**: While at (16, 16) on Map 0_201 (B3F), we attempted to walk Down onto the green computer block at (16, 17).
- **Result**: Collision occurred, and our position remained at (16, 16).
- **Conclusion**: Unlike the passable green terminals on B1F, the green computer terminal at B3F (16, 17) is 100% solid and impassable. This definitively proves that map-specific collision properties govern identical-looking tile types on different floors.
- **Empirical Test 2 - Turn 36041**: While at (17, 16) on Map 0_201 (B3F), we attempted to walk Down onto the green computer block at (17, 17).
- **Result**: Collision occurred, and our position remained at (17, 16).
- **Conclusion**: The green computer terminal at B3F (17, 17) is also 100% solid and impassable. Both terminal tiles on row 17 are solid obstacles on B3F, meaning there is no way to enter the southern corridor by walking directly down from columns 16-17.

## B3F Northeast Section Layout (Migrated from B4F Layout)
- **Entrance**: The stairs from B2F (21, 8) spawn the player facing Down at (25, 6) on B3F.
- **Open Room Area**: Rows 5 to 13, Columns 22 to 28.
- **Obstacles**: 
  - Row 9 contains a solid table/wall structure (TYPE_2889) at columns 22 to 25. Columns 26 to 28 on row 9 are fully walkable.
  - Row 13 contains a solid horizontal table structure (TYPE_2889) across columns 24 to 28. Column 23 on row 13 is open and walkable.
  - **B3F East Southern Area Obstacles**:
    - Row 19 contains solid horizontal tables (TYPE_2889) across columns 22 to 28.
    - Row 20 contains solid bottom wall blocks (TYPE_2889) across columns 22 to 28.
    - Therefore, the southeast area of B3F is completely blocked from above, and can only be entered via the bottom corridor.
  - Column 21 contains a solid vertical partition wall (TYPE_2889) on rows 8 to 13, which divides B3F East and B3F West below row 8. Row 5, 6, and 7 are completely open, allowing direct bypass.

<hr>

<h1><code>Locations/RocketHideout_B1F_Layout</code></h1>

# Rocket Hideout B1F Layout Records
- **Southeast Pocket (Column 28)**:
  - (28, 11) to (28, 15) is an open vertical corridor.
  - On rows 12 to 20, column 28 is separated from column 27 by a solid vertical partition wall.
  - Column 28 is blocked on row 16 by a solid counter at (28, 16) (TYPE_2889).
  - Therefore, (28, 15) is a dead end.
  - **Overworld Steps**: (24, 16) and (25, 16) are step tiles (TYPE_a83b).
    - **Collision Test (Turn 33386)**: Standing at (24, 15) facing Down, we tried to walk Down onto (24, 16) and collided.
    - **Collision Test (Turn 33389)**: Standing at (25, 15) facing Down, we tried to walk Down onto (25, 16) and collided.
    - **Conclusion**: These step tiles are completely impassable from north-to-south. They are either one-way steps (only passable south-to-north) or entirely decorative/solid boundaries. Therefore, the northern and southern sections of B1F are completely separated in this eastern region, and the southern section (row 17+) cannot be reached from the upper-right section.
  - **Rocket Grunt 3**: Standing at (28, 18) looking UP. Can only be reached by walking through the main southeast room (columns 24-27) and stepping onto row 17.

- **Western Section & Central Row 16 Blockage (Turn 33405)**:
  - **Empirical Test**: Backtracked to the western section of B1F (columns 10-15) and walked down to row 14.
  - **Visual Verification**: Visually and physically verified that row 16 is completely solid and blocked by TYPE_2889 walls across all columns from column 9 to column 15.
  - **Overall Conclusion**: Since row 16 is completely blocked from column 9 to column 23, and the stairs at (24, 16) and (25, 16) are impassable from the north, the northern section of B1F (upper floor) is isolated from the southern section of B1F (lower floor, row 17+) across all tested columns (columns 9 to 28). Columns 0 to 8 are completely blocked and separated on B1F by a solid vertical partition wall at column 8 (Verified on Turn 33590).
  - Therefore, Rocket Grunt 3 at (28, 18) and the B1F elevator door are completely unreachable from the upper area of B1F. We MUST obtain the LIFT KEY from B4F first, and then take the elevator to B1F to access the southern area.

## Multi-Floor Connections & Staircase Redirection
- **Staircase Warp at (23, 2)**: This staircase, located in the northeast section of B1F (Map 0_199), connects symmetrically and directly to B2F (Map 0_200) at (27, 8) (Verified Turn 33751).
- **Traversing to B4F**: On Turn 33613, it was historically recorded that taking the B1F (23, 2) staircase warped directly to B4F (Map 0_202) at (25, 6). This was an overworld movement tracking artifact: because the player traversed the stairs B1F (23, 2) -> B2F (27, 8), walked Left to B2F (21, 8), and immediately took the stairs down to B4F (Map 0_202) at (25, 6) in a single turn block, the intermediate B2F movement was overlooked. We have since verified on Turn 33751 and 33766 that these are standard symmetric connections: B1F (23, 2) connects symmetrically to B2F (27, 8), and B2F (21, 8) connects symmetrically to B4F (Map 0_202) at (25, 6). There is no direct asymmetric warp.
- **Correction Note (Turn 35351)**: Separated B3F (Map 0_201) and B1F (Map 0_199) definitions completely. They do not share a Map ID. B3F layout is stored exclusively in "Locations/RocketHideout_B3F_Layout".

<hr>

<h1><code>Locations/RocketHideout_B4F_Layout</code></h1>

# Rocket Hideout B4F Layout Records (Map 0_202)
- **Staircase UP to B2F (Eastern Room)**: Located at (25, 6) on Map 0_201 (B3F). Connects symmetrically to B2F (Map 0_200) at (21, 8). This grants access to the northeast section of B3F.
  - **Staircase UP to B3F (Western Corridor)**: Located at (19, 10) on Map 0_202. Connects symmetrically to B3F (Map 0_201) at (19, 19) (Verified Turn 35235). This grants access to the western/left section of B4F.
  - **Column 21 Physical Separation**: Below row 14, the left (western) and right (eastern) sections of B4F are completely physically separated by a solid partition wall. However, on Turn 36879, it was empirically verified that row 14 contains an open, walkable path (TYPE_3fe2) at (21, 14) that connects B4F East directly to B4F West, providing a seamless horizontal corridor bypass.
- **B3F Northeast Section**: Migrated to Locations/RocketHideout_B3F_Layout on Turn 35674.
- **Defeated Trainers**:
  - Rocket Grunt 1: Standing at (26, 11)/(26, 12) on Map 0_201 (B3F Northeast). Defeated. Speaks about needing the Lift Key to run the elevator.
  - Rocket Grunt 2: Standing at (10, 22) on Map 0_201 (B3F). (Defeated).
  - Rocket Grunt 3: Standing at (11, 22) on Map 0_202 (B4F). (Defeated Turn 33850).
- **Collected Items**:
  - Rare Candy at (20, 14) (Collected Turn 33659).
  - TM10 (Double-Edge) at (26, 17) (Collected Turn 33978).
  - HP UP at (10, 12) (Collected Turn 35246 on B4F Map 0_202).
- **Collision Test at (9, 8)**: Tested on Turn 33693. Stood at (9, 9) facing Up and tried to walk Up onto (9, 8). Result: Collision. (9, 8) is a solid, impassable wall/table (TYPE_2889).
- **Burden of Proof & Northwest Room Openings (Row 8)**: Row 8 is a horizontal divider. Rather than assuming all columns are solid, we must systematically inspect Row 8's columns. On Turn 33944, column 20's Row 8 tile (20, 8) was visually observed to be TYPE_3fe2 (completely walkable floor), allowing direct vertical access from the spinner maze to the northern corridor (rows 5-7). This corridor extends westward to the true northwest section. We will test columns 10-15 on row 6/7/8 to find the true entrance to the northwest room.
- **Collision Test at (9, 25)**: Tested on Turn 33840. Tried to walk Left from (9, 25) but collided. This confirms that Column 8 is a solid, impassable wall boundary (TYPE_2889) in the southwest corner as well.
- **B4F Row 4 Columns 9-24 Systematic Passability and Interaction Testing Plan Results**:
  - We systematically tested the passability of the horizontal table boundary on Row 4 (Columns 9-24) from Row 5 to verify if there was any opening or interactive entity behind the table.
  - **Results**:
    - Columns 9-24 are all 100% solid on row 4. All interaction tests with 'A' on Row 5 facing Up yielded no-ops, proving that there are no interactive NPCs standing directly behind the table.

## B4F Column 21 Passability Testing (Turn 36277 - Turn 36297)
- **Verified Facts**:
  - Row 7: Tried to walk Right from (20, 7) onto (21, 7) on Turn 36277. Result: Collision. (21, 7) is 100% solid.
  - Row 6: Tried to walk Right from (20, 6) onto (21, 6) on Turn 36282. Result: Collision. (21, 6) is 100% solid.
  - Row 5: Tried to walk Right from (20, 5) onto (21, 5) on Turn 36284. Result: Collision. (21, 5) is 100% solid.
  - Row 4: Tried to walk Right from (20, 4) onto (21, 4) on Turn 36290. Result: Collision. (21, 4) is 100% solid.
  - Row 3: Tried to walk Right from (20, 3) onto (21, 3) on Turn 36291. Result: Collision. (21, 3) is 100% solid.
  - Row 2: Tried to walk Right from (20, 2) onto (21, 2) on Turn 36294. Result: Collision. (21, 2) is 100% solid.
  - Row 1: Tried to walk Right from (20, 1) onto (21, 1) on Turn 36296. Result: Collision. (21, 1) is 100% solid.
- **Conclusive Proof**: Column 21 is a completely solid vertical wall across all rows on B4F West, meaning B4F West is completely physically separated from the eastern room where the Lift Key Grunt stands. This confirms we must backtrack through B3F and B2F to access him.

## B4F Eastern Section & Giovanni's Room (Uncovered Turn 36864)
- **Arrival**: Warped from Map 0_203 (Elevator Cabin) at (2, 1) to Map 0_202 (B4F) at (25, 15) facing UP on Turn 36864.
- **Elevator Location**: Elevator doors are located on B4F at (24, 11) and (25, 11).
- **Guards**: Two Rocket Grunts are stationed in the hallway:
  - Grunt A at (23, 12) facing DOWN (guards column 23).
  - Grunt B at (26, 12) facing DOWN (guards column 26).
- **Layout**: Row 15 is blocked on the South by a solid wall on row 16. The corridor leads West via columns 21-22 on rows 14-15.
- **Plan**: Walk UP to row 14, then West to cross column 23, triggering a battle with Grunt A. Once defeated, we will explore the Western/Northern passageways to find Giovanni!

<hr>

<h1><code>Mechanics/CustomTool_GeneratePath_Source</code></h1>

# BFS-based pathfinder that plans a route between start and target coordinates on a specified map,

# with integrated static collision database and custom spinner-sliding simulation for Rocket Hideout floors

# (Map 0_199 = B1F, Map 0_200 = B2F, Map 0_201 = B3F, Map 0_202 = B4F) to ensure valid, obstacle-free overworld routing.

import json
import collections

# Retrieve parameters directly from the globally injected 'input_data' dictionary
map_id = input_data['map_id']
start_x = int(input_data['start_x'])
start_y = int(input_data['start_y'])
target_x = int(input_data['target_x'])
target_y = int(input_data['target_y'])

def find_path():
    impassable = set()
    
    # Define map-specific boundaries and blockages based on empirical data:
    if map_id == "0_10": # Saffron City
        # Main buildings and fences
        # Add fences on column 3:
        for y in range(17, 30):
            impassable.add((3, y))
        # Mr. Psychic's house
        for x in range(26, 32):
            for y in range(25, 30):
                impassable.add((x, y))
        # Pokemon Center
        for x in range(5, 11):
            for y in range(25, 29):
                impassable.add((x, y))
                
    elif map_id == "0_202": # Rocket Hideout B4F
        # Office walls and tables on Row 4
        for x in range(18, 28):
            impassable.add((x, 4))
        # Guard posts and other walls:
        for y in range(1, 15):
            impassable.add((21, y)) # Column 21 partition wall
            
    # Spinner definitions for Rocket Hideout floors (Map 0_199 to 0_202):
    # Spinners map a tile (x, y) to a sliding direction: "Up", "Down", "Left", "Right"
    spinners = {}
    stop_tiles = set()
    
    if map_id == "0_200": # Rocket Hideout B2F Spinner Maze
        # Define spinners:
        spinners[(17, 11)] = "Left"
        spinners[(13, 18)] = "Left"
        spinners[(11, 18)] = "Down"
        spinners[(13, 22)] = "Left"
        spinners[(9, 22)] = "Down"
        spinners[(10, 25)] = "Right"
        
        # Stop tiles:
        stop_tiles.update([(1, 9), (9, 16), (15, 18), (11, 20), (9, 24), (14, 25)])

    # BFS Pathfinder with Spinner Simulation:
    queue = collections.deque([(start_x, start_y, [])])
    visited = set([(start_x, start_y)])
    
    while queue:
        cx, cy, path = queue.popleft()
        if (cx, cy) == (target_x, target_y):
            return path
            
        # Standard moves
        for dx, dy, move in [(0, -1, "Up"), (0, 1, "Down"), (-1, 0, "Left"), (1, 0, "Right")]:
            nx, ny = cx + dx, cy + dy
            
            # Check map boundaries (assumed 100x100 max for general maps)
            if not (0 <= nx < 100 and 0 <= ny < 100):
                continue
            if (nx, ny) in impassable:
                continue
                
            # Spinner sliding simulation:
            if (nx, ny) in spinners:
                # Slide until we hit a stop tile or boundary
                sx, sy = nx, ny
                visited_slide = set([(sx, sy)])
                while (sx, sy) in spinners and (sx, sy) not in stop_tiles:
                    s_move = spinners[(sx, sy)]
                    sdx, sdy = {"Up": (0, -1), "Down": (0, 1), "Left": (-1, 0), "Right": (1, 0)}[s_move]
                    nsx, nsy = sx + sdx, sy + sdy
                    if not (0 <= nsx < 100 and 0 <= nsy < 100) or (nsx, nsy) in impassable or (nsx, nsy) in visited_slide:
                        break
                    sx, sy = nsx, nsy
                    visited_slide.add((sx, sy))
                nx, ny = sx, sy
                
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, path + [move]))
                
    return None

path = find_path()
if path is not None:
    print(json.dumps(path))
else:
    print(json.dumps([]))

<hr>

<h1><code>Mechanics/Gen1ParalysisGlitch</code></h1>

# Gen 1 Paralysis Speed Penalty Glitch
- **Mechanic**: In Generation 1, when a Pokémon is paralyzed, its Speed stat is reduced to 25%. If the status is cured in battle (e.g., using a Parlyz Heal or Full Restore), the status icon is removed, but the Speed penalty persists in the current battle round because the game does not automatically recalculate Speed upon curing unless a stat-altering move (like Agility) is used or the Pokémon is switched out.
- **Application**: Because of this stat re-application glitch, we must be highly cautious about assuming our speed is restored immediately after curing status in battle. Since we are using a HYPER POTION, we are only restoring HP, keeping the paralysis for now. Once we finish this battle, we will step on the overworld Heal Pad at (11, 9) which will clean all status conditions and properly recalculate all stats.

## REST and Paralysis Stat Re-application Glitch
- **Glitch Mechanics**: In Generation 1, when a paralyzed Pokémon uses REST, the status is replaced by Sleep. However, the 25% Speed penalty is NOT recalculated or removed by the REST healing script.
- **Permanent Throttle**: Once Snorlax uses REST, its Speed remains permanently throttled at 25% of its baseline for the remainder of the battle, even after it wakes up from Sleep and has no status icon!
- **Safety Protocol Impact**: This engine bug works heavily in our favor! Once Snorlax is paralyzed initially, we can rely on it being permanently slow for the entire combat duration. Even when it wakes up from REST with full health, we will retain 100% turn priority (outspeeding it) to safely throw Great Balls, heal, or switch without any threat of being outsped.
- **Archive Location**: Verified in Scratchpad/Route16_Snorlax_Fly on Turn 38323 and permanently archived here in Mechanics/Gen1ParalysisGlitch.

<hr>

<h1><code>Mechanics/StatusCureProtocol</code></h1>

# Battle-Readiness Protocol: Status Cures vs. Multi-Turn Moves
- **Rule**: Never attempt a multi-turn move (like DIG or FLY) while suffering from a status condition that can cause turn loss (like Paralysis or Confusion).
- **Mathematical Proof**: Paralysis has a 25% turn-loss rate. For a single-turn move, the success rate is 75%. For a two-turn move, both turns must succeed, reducing the success rate to 56.25% (and increasing the failure rate to 43.75%).
- **Protocol**: If paralyzed, either:
  1. Use a single-turn move (like WATER GUN) which has a much higher success probability.
  2. Use a curing item (like PARLYZ HEAL) immediately on Turn 1 to completely remove the turn-loss risk before executing any complex or high-commitment moves.

<hr>

<h1><code>Mechanics/PokemonTowerCombatGuide</code></h1>

# Pokémon Tower Combat Guide & Sustainability Plan
- **Primary Sweeper**: Lead with GEMMY (Blastoise). At high levels, GEMMY's high Special stat makes WATER GUN (PP: 25) extremely powerful, capable of one-shotting or two-shotting Gastlys without wasting DIG. Use DIG (PP: 10) for tougher battles.
- **Normal-type Restriction**: In Gen 1, Normal-type moves (like BITE, TACKLE) deal absolutely 0 damage to Ghost-types (Gastly, Haunter). Avoid them during combat in the tower.
- **Channeler Countermeasures**: Channelers use Gastly/Haunter which use Confuse Ray (confusion) and Night Shade (fixed damage equal to level). If GEMMY is confused or low on HP, use HYPER POTION or switch to SPARKY (Pikachu) for neutral THUNDERBOLT or THUNDER WAVE support to paralyze targets.
- **Gen 1 Switching Priority Rule**: Switching out a Pokémon is a high-priority action (+6 priority) that always occurs at the very start of the turn before the opponent can move. This means a low-level leader is 100% safe from Turn 1 moves on switch-training.
- **5F Heal Pad Purified Zone**: 5F has a purified, health-restoring zone at (10,8), (10,9), (11,8), (11,9) that fully restores HP and PP of all party members upon stepping on it.
- **Switch-Grinding Strategy**: Lead with a low-level Pokémon (ROCKY L15, PETAL L13) and immediately switch to GEMMY on Turn 1 of wild battles. Or use BUGGY (Butterfree L13) with CONFUSION (Psychic is super-effective against Ghost/Poison) to gain solo EXP. Identify wild GHOSTs using the SILPH SCOPE.

<hr>

<h1><code>Scratchpad/Saffron_SilphCo_Warp_Plan</code></h1>

# Saffron City & Silph Co. Systematic Warp-Logging Strategy
- **Silph Co. Entry Turn**: Turn 38843 (Sunday, May 31, 2026)

## Overview & Cognitive Safeguards
Saffron City and Silph Co. (11 floors) contain a massive, complex network of over 30 warp tiles. Navigating this blindly or relying purely on short-term memory will cause cognitive bloat, backtrack loops, and wasted turns. To prevent this, we will systematically log every warp transition using our specialized custom agent: `warp_network_tracker`.

## Logging Protocol
1. **Identify and Check**: Before stepping on any warp tile, verify our current map ID and coordinate.
2. **Execute and Record**: Step on the warp tile. Once we spawn at the destination, immediately:
   - Call the `warp_network_tracker` agent with `action_type="record_warp"`.
   - Provide `current_map_id`, `current_position` (the warp's origin), and `warp_destination_map_id`, `warp_destination_position` (the spawn location).
3. **Verify in Scratchpad**: Maintain a secondary high-level floor transition index in this scratchpad to maintain quick overworld context.
4. **Route Planning**: When seeking specific objectives (like finding the Card Key on B5F, or reaching Giovanni on 11F), call `warp_network_tracker` with `action_type="plan_warp_route"` to query the database and receive an automated sequence of coordinates to follow.

## High-Level Floor-by-Floor Silph Co. Objectives
- **Target 1**: Obtain the Card Key (traditionally on 5F or adjacent floors).
- **Target 2**: Unlock doors using the Card Key to access locked rooms and valuable items.
- **Target 3**: Defeat Boss Giovanni on 11F to clear Silph Co. Defeating Giovanni here will clear Team Rocket from Saffron City and unlock the Saffron Gym!
- **Target 4**: Defeat Sabrina at Saffron Gym.

## Active Route & Progress Log
- **Turn 38726**: Captured Snorlax at Route 16 (26, 10). Nicknamed SNOOZY and sent to PC Box 1.
- **Turn 38853**: Stood at (13, 11) in Silph Co. 1F facing Up. Socratic Test: Pressed 'A' on elevator door at (13, 10) on 1F. Resulted in no dialogue or menu, proving the elevator is non-functional or uncallable from 1F. We must find the stairs to proceed.

## Saffron & Silph Co. Resources & PP Tracker (Initialized Turn 38824)
- **SPARKY (PIKACHU Lv 24)**: HP 57/57 | THUNDERBOLT: 15/15, GROWL: 40/40, THUNDER WAVE: 20/20, QUICK ATTACK: 30/30
- **ROCKY (GEODUDE Lv 15)**: HP 41/41 | TACKLE: 35/35, DEFENSE CURL: 40/40
- **BIRBIE (PIDGEOTTO Lv 18)**: HP 55/55 | GUST: 35/35, SAND-ATTACK: 15/15, QUICK ATTACK: 30/30, FLY: 15/15
- **BUGGY (BUTTERFREE Lv 13)**: HP 43/43 | TACKLE: 35/35, STRING SHOT: 40/40, CONFUSION: 25/25
- **GEMMY (BLASTOISE Lv 49)**: HP 159/159 | DIG: 7/10, TAIL WHIP: 30/30, BITE: 25/25, WATER GUN: 25/25
- **PETAL (BELLSPROUT Lv 13)**: HP 39/39 | VINE WHIP: 10/10, GROWTH: 40/40, WRAP: 20/20, CUT: 30/30

## Silph Co. 5F Systematic Search Protocol (Turn 39216)
- **Goal**: Clear all trainers, identify Card Key gates, and find the Card Key item on Silph Co. 5F.
- **Search Pattern**:
  1. Explore the western hallway by walking west on Row 1 from (16, 1) to (3, 1).
  2. Map any Card Key doors ('🚪') and warp tiles ('🌀') in the western rooms.
  3. **Detour Protocol**: Since Scientist Beau at (8, 3) is a solid, impassable obstacle in Gen 1, bypass him by walking Up to (8, 1), Right to column 13 at (13, 1), and then Down column 13 to (13, 5) to explore the southern and central sections.
  4. Track and record any new warps using warp_network_tracker.
  5. Avoid stepping onto any warp tiles until all trainers on the floor are cleared and the Card Key is found.
  6. **Eastern Corridor Bypass & Southern Corridor Routing Plan (Turn 39333)**: We are currently on the west side of the solid column 27 partition wall. The southern corridor (row 16) contains a Poké Ball item at (21, 16) (the potential Card Key), but is blocked directly by the wall at (26, 15). To access row 16, we must backtrack north up column 26 to row 9 (or further up), walk east across column 27, then walk south down column 28 to row 16, and finally walk west to (21, 16).
- **Key Healing/Support Items**:
  - GREAT BALL: 20
  - HYPER POTION: 10
  - POTION: 5
  - LEMONADE: 1
  - ELIXER: 1
  - ETHER: 1
  - MAX ETHER: 1
  - PARLYZ HEAL: 2
  - POKé FLUTE: 1 (Infinite-use awake)
## Combat Readiness & Floor Search Protocol
- **Lead Combat Order**: GEMMY (Blastoise L46) leads for maximum type safety and level advantage. Saffron's enemies (Poison, Ground, Normal) are highly vulnerable to DIG and WATER GUN. SPARKY (Pikachu L24) is held in reserve.
- **Floor Search Protocol**:
  1. **Clear Floor**: Clear all Grunts and Scientists on each newly entered floor first to prevent ambush and gain experience.
  2. **Explore Rooms**: Systematically check every room and container on the current floor before utilizing warp tiles.
  3. **Priority Objectives**: Locate the Card Key (expected on 5F or adjacent floor) to unlock Silph Co.'s electronic doors.
  4. **Map Hygiene**: Immediately define a '🪜' marker for stairs and a '🚪' marker for elevator doors upon discovery.
- **Gen 1 Defeated Sprite Solidity & Trapping Risk**:
  - In Gen 1, defeated trainer sprites remain solid, physical overworld obstacles that never disappear or become passable.
  - Constrain Backtracking: If we defeat a trainer in a narrow 1-tile wide corridor, that trainer permanently plugs that corridor, blocking any future bidirectional backtracking.
  - Positioning Safety Protocol:
    1. When approaching a trainer in a 1-tile wide corridor, NEVER fight them inside the corridor if there is only one exit.
    2. If possible, trigger the battle from a wider chamber or from an angle that leaves at least one parallel passable lane.
    3. If we must fight them, verify that we have already fully searched both sides of the corridor, or that we have an alternative route (e.g., stairs, elevator, or a parallel corridor) to return to the rest of the floor.

- **Turn 39186**: Entered Silph Co. Elevator (Map 0_236) from 4F (20, 0). Attempting to use the elevator to go to 5F to look for the Card Key.

- **Turn 39276**: Socratic Analysis of Southwest Compartment Accessibility
  - Observation: Inspected the west side from (19, 8). Identified a Card Key door at (15, 10) and (15, 11) (TYPE_a83b).
  - Boundary Scan: Column 15 is blocked by solid walls at (15, 9) (TYPE_2889) and (15, 12) (TYPE_2889).
  - Conclusion: The western compartments on rows 10-13 (including columns 5-6) are completely sealed off from the eastern section by this column 15 partition and the Card Key doors. They cannot be bypassed on foot without the Card Key. We must proceed with our eastern and southern search to locate the Card Key first.
- **Turn 39439**: Socratic Challenge and Reflection answer:
  - **9F Exploration & Healing**: On 9F, there is a Room with Card Key doors at (18, 10) and (19, 10). Let's unlock them once we have the Card Key and see if we can find the healing NPC.
  - **Warp Alignment Correction (Turn 39504)**: Checked the system note and proved that the 5F-to-9F warp transition connects 5F at (8, 15) and 9F at (17, 15). The warp tile itself on 5F is at (9, 15).
  - **Grunt Battle (Turn 39504)**: Stepped down off the warp tile to (9, 16) on 5F and immediately triggered a battle with the Rocket Grunt at (8, 16) who said: "I heard a kid was wandering around." Let's defeat him.
## 5F Backtracking Safety Analysis (Turn 39544)
- **Problem**: We are currently standing at the bottom of 5F (row 16) near the southwest corner (9, 16). 
  1. Row 15 contains a solid partition wall from column 10 to 27.
  2. Column 28 is completely blocked at row 4 by the defeated Rocket Grunt at (28, 4), which is solid and impassable in Gen 1.
  3. Column 8 and Column 9 contain active warp triggers at (8, 15) and (9, 15) leading to 9F (17, 15). Note that (8, 14) is a completely safe overworld floor tile (empirically verified on Turn 39634).
  - Therefore, there is NO physical overworld path to walk north on 5F from the southern corridor.
- **Solution**: We must step onto the warp trigger at (9, 15) to return to Silph Co. 9F.
- **Route North**:
  1. From (9, 16), step Up onto the warp tile at (9, 15) to transition back to 9F (17, 15).
  2. On 9F, use the open corridors to walk to the elevator foyer.
  3. Ride the elevator back to Silph Co. 5F (or any other floor) to bypass the blockage on foot.
- **9F Inner Room Healing Verification (Turn 39574 - 39593)**:
  - **Methodology**: Unlocked (18, 10) and (18, 4) on Silph Co. 9F. Entered the northwest room with beds. Explored from (18, 5) to (18, 2), then left to (15, 2) and down to (17, 9) and (18, 9).
  - **Results**: Verified that there is NO healing NPC inside this room. The beds at (16, 0) and (18, 0) are non-interactive. The room is completely empty of sprites except for the defeated Scientist at (21, 13) in the hallway.
  - **Conclusion**: There is no healing NPC in this room. We must check other areas of 9F or find where she actually stands.

## Systematic Elevator Sweep Routing Protocol (Turn 39901)
- **Objective**: Methodically clear the remaining floors of Silph Co. in ascending order to optimize EXP and resource collection before challenging Giovanni on 11F.
- **Step 1 (6F)**: Ride the elevator to 6F. Unlock all Card Key gates, defeat all Rocket Grunts and Scientists, and collect any items.
- **Step 2 (8F)**: Ride the elevator to 8F. Fully explore the floor on foot, unlock all Card Key doors, defeat all trainers, and check for items.
- **Step 3 (10F)**: Ride the elevator to 10F. Defeat all trainers and collect items.
- **Step 4 (11F - Final)**: Ride the elevator to 11F. Confront the final Rocket Grunts, unlock the President's boardroom, defeat Boss Giovanni, and rescue the President to claim the Master Ball!

## 5F Central Card Key Gate (15, 11) Optimization Analysis (Turn 39667)
- **Socratic Analysis**:
  - **Question**: Should we walk down to row 16, across to column 16, and go north to unlock the central Card Key gates at (15, 10) and (15, 11), or is it better to bypass them and walk directly to the elevator on foot?
  - **Trade-off Analysis**:
    1. **Unlocking**: Requires backtracking south to row 16, walking east to column 16, walking north to row 11, facing Left, and pressing A. This would take ~15-20 turns. The benefit is permanently connecting the west (cols 0-14) and east (cols 15-27) of 5F on rows 10-11, and connecting them to cols 11-13 (the youngster area).
    2. **Bypassing (Direct Foot Path)**: We are already at (8, 8), which is north of the warp barriers. We can walk directly north to row 1, go east, and reach the elevator at (20, 0) in only ~18 turns total! Once at the elevator, we can ride it directly to the west side of 9F to find the healer. We have no future need to walk across 5F on foot because the elevator connects all floors.
  - **Decision**: Unlocking the central gate is redundant and wastes turns because the elevator provides complete floor-to-floor transit and we already have a direct, completely open path to the elevator foyer on 5F on foot from our current position. Therefore, we will bypass the central gate and proceed directly to the elevator to prioritize saving GEMMY.

## 9F Eastern/Western Compartment Direct Foot Connection (Turn 39936)
- **Discovery**: We verified that Saffron Silph Co. 9F's elevator doors are located at (18, 0) in the eastern compartment, not on the western side.
- **Permanent Overworld Connection**: Since we have unlocked the electronic Card Key doors at (18, 10) and (18, 4) on 9F, the eastern compartment (columns 15-27) and the western compartment (columns 0-13) are permanently connected on foot via the northern rooms.
- **Direct Route to Elevator (18, 0)**: 
  - From the western compartment, we can walk north up column 13 to row 3 or 4, pass east across column 14, and walk directly to (18, 0) on foot!
  - This completely eliminates any need for warping back to 5F, navigating around obstacles, or using the multi-floor backtracking loop. This direct overworld foot route is 100% efficient.

## Socratic Quest Tracking & Agent Status (Turn 39962)
- **Quest Start**: Turn 38843 (Exploration of Silph Co.)
- **Current Turn**: Turn 39962
- **Elapsed Time**: 1119 turns of active navigation and exploration.

## Systematic 6F/8F/10F Layout Mapping & Ambush Protocol (Turn 39962)
- **Mapping Protocol**:
  - Immediately identify and record the coordinate of the elevator landing upon arrival.
  - Map any Card Key gates ('🚪') and warp tiles ('🌀') on the floor using map markers.
  - Traverse the hallways methodically to map any wall partitions.
- **Ambush Handling Protocol**:
  - Before fighting any trainer, verify our position: do not battle them in a 1-tile wide corridor unless we have already searched both sides or have a parallel corridor to bypass their solid defeated sprite.
  - Keep a live resource check: monitor GEMMY's HP and PP. Use single-turn physical/special moves appropriately to conserve DIG PP for bosses or tough Poison-types.

## Systematic Floor Clearance Strategy (Turn 39876)
- **Immediate Step**: Challenge the Rocket Grunt at (2, 4) to clean-sweep the northwest compartment of 9F West.
- **Post-Battle Scan**: Walk all the way up columns 1 and 2 (from row 12 north to row 1) to inspect for hidden items or NPCs.
- **Warp Inspection**: Inspect the warp tile at (9, 3) to see where it connects, using `warp_network_tracker`.
- **Systematic Elevator Sweep**: Once 9F West is fully cleared, return to the elevator at (13, 10). We will ride the elevator to systematically clear all other floors (e.g., 6F, 8F, 10F, 11F) floor-by-floor.
- **Custom Agent Status**: On Turn 39731, we attempted to register the bidirectional warp connection between Silph Co. 5F (0_229) at (9, 15) and Silph Co. 9F (0_233) at (17, 15) using warp_network_tracker. The agent failed with a persistent 503 status code (no body). This entry remains uncorrected in the database due to API failures, so we have documented it here for absolute safety and routing transparency.
- Turn 39834: Unlocked the door at (11, 12) and walked west to (8, 12) on Silph Co. 9F. The western bedroom contains beds at columns 4 and 6. I am now exploring this room to locate the healing NPC.

<hr>

<h1><code>Locations/Route16</code></h1>

# Route 16 Verified Location Records (Map 0_27)
- **Map Connections**:
  - Seamless connection to Celadon City (Map 0_6) is at the eastern boundary on Row 10/11.
- **Physical Landmarks & Obstacles**:
  - Cuttable bush at (34, 9) unlocks access to the northern secret path (Rows 6-9) leading to the Secret House.
  - Snorlax is situated at (26, 10). It blocks the main path leading west.
- **Gatehouse (Map 0_165 / 0_166)**:
  - Route 16 Gatehouse Back Door (West) is at (18, 5).
  - Route 16 Gatehouse Back Door (East) is at (23, 5).
- **Secret House (Map 0_188)**:
  - Entrance door warp is at (7, 5). Entering warps the player to (2, 7) inside the Secret House (facing Up).
  - Inside the Secret House, the girl at (2, 3) gives HM02 (FLY) to the player.

<hr>