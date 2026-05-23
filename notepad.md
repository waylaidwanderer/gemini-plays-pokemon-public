<h1><code>Main</code></h1>

# Pokémon Blue Playthrough Dashboard

## Main Objectives
- [x] Choose first Pokémon (Turn 81 - Squirtle!)
- [ ] Reach Viridian City Poké Mart to get Oak's Parcel
- [ ] Deliver Oak's Parcel to Professor Oak
- [ ] Get Pokédex and Poké Balls from Professor Oak

## Directory
- `Scratchpad/Route1` - Live tracking and active routing on Route 1.
- `Scratchpad/ViridianCity` - Live tracking and active routing in Viridian City.
- `Mechanics/General` - Verified game mechanics and controls.
- `Locations/PalletTown` - Permanently verified Pallet Town location records.

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

<h1><code>Scratchpad/Route1</code></h1>

# Route 1 Exploration Scratchpad
- Live tracking and active routing on Route 1. Started Turn 121 (Saturday, May 23, 2026 at 12:45 PM PDT).

## Hypotheses to Verify:
1. Viridian City Connection:
   - Route 1 goes straight north to Viridian City. (VERIFIED - Turn 209)
2. Wild Encounters:
   - Tall grass on Route 1 contains wild Pidgey and Rattata. (VERIFIED - Turn 194)
3. Item Delivery:
   - Viridian City Poke Mart clerk will give us Oak's Parcel once we talk to him.

## Verified Overworld Facts:
- Route 1 Entrance from Pallet Town is at X=10, 11 on Map 0_0 (Row Y=0) and Map 0_12 (Row Y=35).
- Between Y=35 and Y=32, there is a narrow corridor of tall grass (TYPE_fed7) flanked by ledges/fences (TYPE_2889) at X=9 and X=12.
- At Y=31, a clear path (TYPE_3fe2) begins. There is a ledge (TYPE_44f6) blocking straight north movement at Y=27 on columns X=10 to X=15.
- To bypass the Y=27 ledge, we must walk left to Column X=8 (which has clear path at (8,31) and (8,30)) and then proceed north through columns X=6, 7, or 8.
- Talked to the Poké Mart clerk at (5, 24) on Turn 182 and received a free POTION.

## Active Routing Log:
- Turn 207: Successfully navigated Route 1 from Pallet Town to Viridian City.

<hr>

<h1><code>Scratchpad/ViridianCity</code></h1>

# Viridian City Exploration Scratchpad
- Live tracking and active routing in Viridian City. Started Turn 209 (Saturday, May 23, 2026 at 1:10 PM PDT).

## Connection to Route 1:
- Map 0_1 (Viridian City) Column X=20, 21 on Row Y=35 connects to Route 1 (Map 0_12) Column X=10, 11 on Row Y=0.

## Objectives:
1. Locate the Poké Mart and speak to the clerk to receive Oak's Parcel.
2. Walk south back to Pallet Town via Route 1 to deliver the Parcel to Professor Oak.

## Active Routing Log:
- Turn 209: Arrived in Viridian City at (20, 35), facing Up. Plan: walk Up 4 steps to (20, 31) to reach the city streets.
- Turn 211 (Saturday, May 23, 2026 at 1:11 PM PDT): Standing at (20, 31). Observed a ledge (TYPE_44f6) blocking north progress at row Y=27, except for a flat opening at (19, 27). Plan: move Up 1 to (20, 30), Left 1 to (19, 30), and Up 4 to (19, 26) to bypass the ledge.
- Turn 213 (Saturday, May 23, 2026 at 1:12 PM PDT): Successfully bypassed the Y=27 ledge and arrived at (19, 26). Observed a building on columns X=22 to X=24 labeled "POKé", which is the Pokémon Center, with its entrance doorway at (23, 25). SQUIRTLE (GEMMY) is healthy at 22/22 HP, so we don't need to visit it yet. Plan: walk Right 1 to (20, 26) and Up 4 to (20, 22) to head north.
- Turn 215 (Saturday, May 23, 2026 at 1:12 PM PDT): Standing at (20, 22), facing Up on Map 0_1 (Viridian City). Verified the Pokémon Center is to our right. The path north along column X=20 is entirely open and of type TYPE_3fe2. Plan: Walk Up 4 steps to (20, 18) to continue exploring the town.
- Turn 218 (Saturday, May 23, 2026 at 1:13 PM PDT): Standing at (20, 18), facing Up. Identified the Poké Mart building directly north with its entrance doorway at (21, 15). The fence line at Y=17 (TYPE_2889) blocks moving straight north from Column X=20. Plan: walk Left 1 to (19, 18), Up 2 to (19, 16) to clear the fence, Right 2 to (21, 16), and Up 1 to enter the Poké Mart at (21, 15).
- Turn 222 (Saturday, May 23, 2026 at 1:14 PM PDT): Arrived at the entrance of Map 0_43 at (2, 7). Plan: walk to (3, 6) and face Up to speak to the NPC at (3, 5).
- Turn 227 (Saturday, May 23, 2026 at 1:16 PM PDT): Talked to the student NPC at (3, 5) who told us about notes. Standing at (3, 6). Plan: walk Left 1 to (2, 6), Up 2 to (2, 4), and face Right to check the counter.
- Turn 232 (Saturday, May 23, 2026 at 1:18 PM PDT): Looked at the notebook on the desk. Plan: walk behind the desk to talk to the instructor at (4, 1).
- Turn 235 (Saturday, May 23, 2026 at 1:19 PM PDT): Talked to the instructor at (4, 1) who tells us to read the blackboard carefully. Confirmed that Map 0_43 is actually the Trainer School, not the Poké Mart! We must exit the school to find the real Poké Mart. Plan: exit the building by walking Right 1 to (5, 2), Down 4 to (5, 6), Left 3 to (2, 6), and Down 2 to transition back to Viridian City.
- Turn 239 (Saturday, May 23, 2026 at 1:21 PM PDT): Exited the Trainer School at (21, 16), facing Down. Since this building has a green roof and its sign says "Trainer School" or is confirmed as such, we are going to explore the eastern side of Viridian City to find the actual Poké Mart (which should have a blue/purple roof). Plan: walk Right 5 steps to (26, 16) to get more of the east side in view.
- Turn 246 (Saturday, May 23, 2026 at 1:23 PM PDT): Standing at (26, 16), facing Right. Visually identified the real Poké Mart with its door at (29, 19) and "MART" sign at (30, 19). Plan: walk Right 1 to (27, 16), Down 4 to (27, 20), Right 2 to (29, 20), and Up 1 to enter the Poké Mart door at (29, 19).
- Turn 247 (Saturday, May 23, 2026 at 1:24 PM PDT): Entered the real Poké Mart (Map 0_42) at (3, 7). Scripted dialogue immediately triggered: the clerk behind the counter called out to us, asking if we came from Pallet Town. Plan: Press 'A' to advance dialogue and receive Oak's Parcel.

<hr>