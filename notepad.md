<h1><code>Main</code></h1>

# Pokémon Blue Playthrough Dashboard

## Main Objectives
- [ ] Start a new game
- [x] Choose first Pokémon (Turn 81 - Squirtle!)
- [ ] Deliver Oak's Parcel
- [ ] Get Pokédex and Poké Balls

## Directory
- `Scratchpad/GameStart` - Live tracking of the initial game startup, player naming, and rival naming.
- `Mechanics/General` - Verified game mechanics and controls.
- `Scratchpad/PalletTown` - Live tracking of Pallet Town exploration and layout verification.

<hr>

<h1><code>Scratchpad/GameStart</code></h1>

# Game Start Scratchpad
- Turn 0 (11:43 AM): Title screen of Pokémon Blue Version visible.
- Player Naming Plan: Name player "GEM".
- Rival Naming Plan: Name rival "BLUE".

## Milestones
- [x] Select "NEW GAME" (Turn 1)
- [x] Name Player: GEM (Turn 27)
- [x] Name Rival: BLUE (Turn 40)
- [x] Complete Oak's Intro and load into GEM's bedroom (Turn 54)

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

<h1><code>Scratchpad/PalletTown</code></h1>

# Pallet Town Exploration Scratchpad
- Live tracking of Pallet Town layout, POIs, and map connections.

## Hypotheses to Verify:
1. GEM's House:
   - Upstairs: Player's Bedroom. Contains GEM's PC (with 1 POTION inside) and SNES console.
   - Downstairs: Living Room. GEM's Mom is here.
2. Blue's House:
   - Located to the right (east) of GEM's House. Contains Blue's sister.
3. Oak's Lab:
   - Located in the south of Pallet Town. Contains Professor Oak, his aides, and 3 starter Poké Balls.
4. Route 1 Connection:
   - Located to the north of Pallet Town. Leaving Pallet Town via Route 1 without a Pokémon should trigger Professor Oak to stop us.

## Empirical Verification Logs:
- Turn 47: Preparing to load into player's bedroom (GEM's Bedroom).
- Turn 54: Loaded into GEM's Bedroom. Verified starting position is (3,6) facing up. Verified room layout is 8x8 with PC at (0,6), TV/SNES at (3,5), Bed at (3,4). Walking to PC at (0,6) to withdraw Potion.
- Turn 57: Position is (1,6). Walking Up to Row 2, Left to Column 0, and facing Up to interact with the PC at (0,1).
- Turn 61: PC storage list is open with cursor on 'POTION'. Preparing to press A to select it.
- Turn 63: Successfully withdrew POTION from PC! It is now in our inventory. PC is empty. Exiting PC menu.
- Turn 66: Position is (0,2). Potion successfully withdrawn. Walking to the stairs at (3,0) to go downstairs.
- Turn 67: Verified (3,0) is an impassable partition wall (TYPE_fed7) and NOT the stairs. Visually identified the stairs are located at (7,1). Current position is (3,1). Planning to walk Right 4 times to step on (7,1) and warp downstairs.
- Turn 69: Arrived downstairs in GEM's Living Room (Map 0_37) at (7,1). Visually verified Mom is at (5,4) and table at (3,4)-(4,4). Planning to walk to (5,5) to go around them.
- Turn 70: Position is (5,5) facing Left. Walking Down to Y=6, Left to X=2, and Down to (2,7) to exit the house.
- Turn 73: Position is (2,2) on Map 0_0. Verified northwestern corner has an impassable boundary fence at Row Y=1 (TYPE_2889). Walking East along Row 2 to find Route 1.
- Turn 77: Forced transition to Oak's Lab (Map 0_40) at (5,3). Verified Oak is at (5,2), Blue is at (4,3), and 3 starter Poké Balls are on the table to our right at Y=3, Columns X=6, 7, 8. Dialogue is at Blue asking 'Gramps! What about me?'.

<hr>