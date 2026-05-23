<h1><code>Main</code></h1>

# Pokémon Blue Playthrough Dashboard

## Main Objectives
- [x] Choose first Pokémon (Turn 81 - Squirtle!)
- [x] Reach Viridian City Poké Mart to get Oak's Parcel (Turn 247)
- [x] Deliver Oak's Parcel to Professor Oak (Turn 461)
- [x] Get Pokédex from Professor Oak (Turn 464)
- [ ] Get Town Map from Daisy in Pallet Town
- [ ] Return to Viridian City to buy Poké Balls

## Directory
- `Locations/PalletTown` - Permanently verified Pallet Town location records.
- `Locations/Route1` - Permanently verified Route 1 connections and layout features.
- `Locations/ViridianCity` - Permanently verified Viridian City connections and buildings.
- `Mechanics/General` - Verified game mechanics and controls.
- `Scratchpad/PalletTown` - Active tracking of the return journey and lab events.

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
- Blue's House: Located east of GEM's house.
- Oak's Lab: Located south of Pallet Town.

<hr>

<h1><code>Scratchpad/PalletTown</code></h1>

# Pallet Town Exploration Scratchpad
- Live routing and active thinking in Pallet Town during the return journey to deliver OAK's PARCEL.

## Active Routing Log:
- Turn 395: Arrived at (10, 0) from Route 1. SQUIRTLE (GEMMY) is Level 7, HP 12/24.
- Turn 402: Walked Down 4 steps down Column 10 to reach (10, 4).
- Turn 408: Walked Left 1, Down 2 to reach (9, 6) facing Down.
- Turn 424: Preparing to walk Down 4 steps along Column 9 to (9, 10) to bypass Oak's Lab west side.
- Turn 431: Successfully arrived at (9, 10) on Pallet Town map. SQUIRTLE is at 12/24 HP. The path to Oak's Lab Door at (12, 11) is completely clear: Down 2 steps to (9, 12), Right 3 steps to (12, 12), then Up 1 step to (12, 11).

## Proposed Path to Oak's Lab Door (12, 11):
- From (9, 6):
  1. Down 4 steps to (9, 10) (Verified on-screen clear tiles at rows 7-10).
  2. Continue Down to Row 12 (e.g., (9, 12)) to bypass the lab's southern wall.
  3. Walk Right to Column 12 (e.g., (12, 12)).
  4. Walk Up 1 step to (12, 11) to face and interact with the door of Oak's Lab.
- Turn 435: Inside Oak's Lab at (5, 11). Discovered that Oak is at (2, 10) and Blue is at (1, 10).
  - Crucial Pathfinding Realization: Walking Left to (2, 11) from (5, 11) is dangerous because (4, 11) is an active exit warp tile!
  - Safe Route: Move Up to (5, 10), then Left 2 steps to (3, 10). From (3, 10), we will face Left, directly looking at Oak at (2, 10). We can then press A to initiate dialogue.
  - Verification: (5, 10), (4, 10), (3, 10) are all TYPE_3fe2 (clear floor).
- Plan: Up, Left, Left, then face Left (which is automatic since we just walked Left) and press A.
- Turn 438: Inside Oak's Lab at (5, 11) facing Up. Blue has moved to (1, 8). Professor Oak is at (2, 10). Executing Up, Left, Left to arrive at (3, 10) facing Left, ready to talk to Oak.
- Turn 440: Successfully walked Up, Left, Left to arrive at (3, 10) facing Left. Oak is at (2, 10) directly to our left. Preparing to press A to deliver Oak's Parcel.
- Turn 443: Dialogue on screen says "I study POKéMON as PROF.OAK's AIDE." confirming (2, 10) is an Aide, not Oak. Plan: Clear text box, step Right to (4, 10), and walk Up the central aisle (Column 4/5) to the northern part of the lab to find Professor Oak.
- Turn 447: Standing at (3, 10) facing Left after clearing the dialogue box. Executing step Right to (4, 10) to enter the central corridor of the lab so we can head north to find Professor Oak.
- Turn 453: Standing at (4, 5) inside Oak's Lab, facing Up. Oak is visible at (5, 2). Plan: step Right to (5, 5), then Up 2 steps to (5, 3). This will position us directly in front of Oak facing Up, ready to talk to him.
- Turn 455: Standing at (5, 3) facing Up, directly in front of Professor Oak at (5, 2). Ready to talk to him to deliver OAK's PARCEL.
- Turn 458: Initiated dialogue with Professor Oak. He says: "What? You have something for me?" and there is a down arrow. Pressing A to hand over the parcel.
- Turn 461: Still in dialogue with Professor Oak. On screen: "What? You have something for me?▼". The harness auto-advance stopped here because it requires a manual A press. Plan: press A to continue.
- Turn 463: Dialogue with Professor Oak and Blue continues. Dialogue on screen: "BLUE: What did you call me for?". OAK's PARCEL is confirmed gone from inventory (successfully delivered). SQUIRTLE is still Level 7, HP 12/24. Plan: Press A to advance dialogue.
- Turn 473: Successfully received the Pokédex and delivered the parcel. SQUIRTLE is Level 7, HP 12/24. Plan: walk Down 8 steps along Column 5 from (5, 3) to (5, 11) to exit Oak's Lab. Then we'll head north/east in Pallet Town to Blue's house to get the Town Map.
- Turn 476: Standing at (5, 11) in Oak's Lab, facing Down. Executing 1 step Down to exit the lab and warp to Pallet Town.
- Turn 479: Standing at (5, 11) in Oak's Lab, facing Down on the warp tile. Preparing to press Down once to trigger the transition into Pallet Town.
- Turn 485: Successfully exited Oak's Lab and transitioned back into Pallet Town (Map 0_0) at (12, 12) facing Down. Plan to head to Blue's House at (13, 5) to speak with Daisy and acquire the Town Map. Path: walk Left 3 to (9, 12), then walk Up 6 to (9, 6), then Right 4 to (13, 6), then Up 1 to enter the door at (13, 5).
- Turn 488: Standing at (9, 12) facing Left. Path north up Column 9 is completely clear of obstacles. Plan: walk Up 6 steps to reach (9, 6). Then we will proceed east to Blue's House.
- Turn 491: Standing at (9, 12) facing Left on Map 0_0. Commencing the 6 steps Up along Column 9 to (9, 6). This is completely clear on-screen at rows 8-11. Then we'll turn Right and walk to Blue's House.
- Turn 494: Successfully walked Up 6 steps to reach (9, 6) on Pallet Town map. We are facing Up. The horizontal path on Row 6 is completely clear to reach Blue's House at Column 13. Plan: walk Right 4 steps to (13, 6), then Up 1 step to (13, 5) to enter Blue's House and obtain the Town Map from Daisy.
- Turn 497: Standing at (9, 6) facing Up on Map 0_0. The path to Blue's House is verified completely clear on screen. Plan: Walk Right 4 steps to (13, 6), then Up 1 step to (13, 5) to enter the house.

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
- Ledge Bypass (going North): Walk Left to Column X=8, which has a clear path at (8,31) and (8,30), then proceed north through Columns X=6, X=7, or X=8.
- Ledge Bypass (going South): You can jump directly south over the Y=5 ledge from (10, 4) to (10, 6), or jump south over the Y=27 ledge from Column X=4.

## Key Interactions & POIs:
- Poké Mart Clerk NPC: Located at (5, 24). Talked to him on Turn 182 and received a free POTION.
- Wild Pokémon: Tall grass contains wild Pidgey and Rattata (verified Turn 194). SQUIRTLE leveled up to Level 7 here.

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
  - Inside (Map 0_42), the clerk at (1, 4) hands over OAK's PARCEL (delivered on Turn 461) and subsequently sells standard items like Poké Balls.

<hr>