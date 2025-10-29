## Core Principles
- **IMMEDIATE ACTION:** I must perform tasks like placing markers, updating my notepad, and fixing tools *immediately*. Deferring tasks, like placing map markers, is a process violation. Significant events must be documented *immediately* in the turn they occur.
- **AGENT USAGE:** When stuck for more than 5 turns on a puzzle, I must use the `hypothesis_generator` agent. My `simple_battle_strategist` agent is underutilized and I will prioritize using it for all future wild battles to automate decision-making.
- **PUZZLE DOCUMENTATION:** My entire problem-solving process (observation, hypothesis, test, conclusion) for any puzzle must be documented in this notepad as it happens.
- **MAP MARKER DISCIPLINE:** I must always check for existing map markers before creating a new one to avoid duplicates. I must mark BOTH ends of a warp immediately after traversal.
- **TOOL MAINTENANCE:** I must NEVER defer fixing a broken tool or agent. It is always the highest priority, overriding any in-game objective.
- **TOOL FAILURE:** If a tool fails, my first assumption must be that the tool is broken, not that the game is impossible. I must fix the tool before re-attempting the action.
- **IMMEDIATE CORRECTION:** If my understanding of the game state (e.g., the existence of a tool) is proven wrong, I must immediately correct my documentation (notepad) before any other action.
- **TRUST OBSERVATION:** My biggest obstacle is my own memory. I must only trust in-game observation.
- **Trainer Identification:** I must verify the name and location of a trainer before marking them as defeated to prevent misidentification errors like the Hiker Daniel/Russell mix-up.

## Game Mechanics & Discoveries

### General Mechanics
- Talking to Mom does NOT heal my Pokémon. This is a critical mechanic difference from other games.
- Resting in the player's bed does NOT heal Pokémon.
- Stunning an NPC can break scripted events, causing dialogue loops. It can also be a reliable solution for interacting with moving NPCs.
- The `stun_npc` effect is temporary and resets when changing maps. (Verified in Azalea Pokémon Center)
- Repeatedly interacting with an object (like a sign) without new results can lead to loops. I must dismiss dialogue before attempting to move.
- The 'Select' button on the nicknaming screen toggles between uppercase and lowercase keyboards.
- An item in a Poké Ball on the ground must be interacted with from an adjacent tile, not by walking onto it.

### Battle Mechanics
*Ignis learned EMBER at Lv12.*
*Ignis grew to Lv21 and learned QUICK ATTACK, replacing SMOKESCREEN.*
*Type Effectiveness Chart*:
- Ground is super-effective against Fire. (Verified in battle vs Falkner's Pidgey's MUD-SLAP).
- Normal is not very effective against Rock/Ground. (Verified in battle vs Hiker Daniel's Onix).

### PC Storage
- Currently empty.

### Tile Traversal and Movement Rules
- **BOOKSHELF**: Impassable. (Verified)
- **BUOY**: Traversability unknown, assumed impassable. Might require Surf. (Observed on Route 32)
- **CAVE**: Traversable warp.
- **COUNTER**: Impassable. (Verified by observation)
- **CUT_TREE**: Impassable, requires a specific ability/item to remove. (Verified)
- **DOOR**: Traversable, acts as a warp tile. (Verified)
- **FLOOR**: Traversable. (Verified)
- **FLOOR_UP_WALL**: One-way traversal. Can only be entered by moving up onto it. (Verified)
- **HEADBUTT_TREE**: Impassable. (Verified by observation)
- **LADDER**: Traversable warp. Must be activated by moving *onto* the tile from an adjacent tile. Standing on the ladder and pressing A or a direction does nothing. (Verified)
- **LEDGE_HOP_DOWN/LEFT/RIGHT**: One-way traversal.
- **LONG_GRASS**: Traversable, contains wild Pokémon. (Verified by encounters on Route 30)
- **MART_SHELF**: Impassable. (Verified by pathfinder consistently treating it as a wall)
- **PC**: Impassable. Interacting from an adjacent tile can trigger events. (Verified)
- **PILLAR**: Conditionally passable. Becomes impassable after a short time. Interaction with a specific Sage at (12, 3) makes it passable. (Verified)
- **RADIO**: Impassable. (Verified by attempting to walk on it)
- **STAIRCASE**: Traversable, acts as a warp tile. (Verified)
- **TALL_GRASS**: Traversable, contains wild Pokémon. (Verified)
- **TOWN_MAP**: Impassable. (Verified by observation)
- **TV**: Impassable. (Verified)
- **VOID**: Impassable. (Verified)
- **WALL**: Impassable. (Verified)
- **WARP_CARPET_DOWN**: Traversable warp. Requires pressing 'Down' on the tile to activate. (Verified)
- **WARP_CARPET_LEFT**: Traversable warp. Must be activated by moving left onto the tile. (Verified)
- **WARP_CARPET_RIGHT**: Traversable warp. Must be activated by moving right onto the tile. (Verified)
- **WATER**: Impassable. (Verified by pathing attempts)
- **WINDOW**: Impassable. (Verified)

## World Knowledge & Location Notes

### Route 29
- The southern path is a dead end.
- The western path is blocked by CUT_TREEs and HEADBUTT_TREEs.

### Route 30
- MR. POKEMON's house is located here. (Confirmed)

### Route 32
- The eastern and western paths are separate at the northern end. The eastern path is a dead end due to one-way ledges.
- Hidden SUPER POTION at (11, 40).

### Violet City
- Building at (21, 29) is a house with a trade NPC, not the Gym.
- The city is not divided by a river; the two sides are connected by walkable paths.
- YOUNGSTER at (5, 18) mentioned a 'wiggly tree' that 'squirms and dances'. This is likely a hint about how to interact with HEADBUTT_TREEs.
- Violet Mart Path: The path to the clerk is blocked. Talking to the Cooltrainer M at (5, 2) does not open it.
- Violet City Gatehouse Warp: Currently impassable and a dead end for now.
#### Sprout Tower
- 1F Path: A solid wall at x=4 divides the first floor, making the Sage at (3, 5) unreachable from the east. Defeating other Sages does not alter the layout.
- 2F Pillar: Numerous simple interaction tests (re-interacting with the Sage, checking other objects/walls, etc.) have failed to make the central pillar move again after its initial movement.

### Route 33
- Hiker Anthony is on this route. He gives his phone number instead of battling.

### Azalea Town
- Hiker Anthony called to say there are lots of DUNSPARCE in DARK CAVE.
- **CONFIRMED LEAD:** The Charcoal Man's apprentice is at (7, 28) in Ilex Forest. His FARFETCH'D, which knows CUT, has run off. I need to find the FARFETCH'D to get CUT. This was mentioned by a Youngster (6, 9) and the Charcoal Man himself (2, 3).

## Puzzles & Solutions
### Ilex Forest FARFETCH'D Puzzle
- **Objective:** Herd the FARFETCH'D back to the apprentice at (7, 28).
- **Mechanic:** The FARFETCH'D moves in response to player interaction. The direction it moves seems to depend on the direction the player is facing when interacting.
- **Attempt 1:** Interacted with FARFETCH'D at (15, 25) while standing at (15, 26) (facing up). It moved east to (20, 24).
- **Alternative Hypothesis 1:** The FARFETCH'D moves to pre-scripted points regardless of player position. Test: Interact from the same direction twice and see if the outcome is different.
- **Alternative Hypothesis 2:** The goal is not to herd it all the way to the apprentice, but to trap it or lead it to a specific trigger point.

## Untested Assumptions & Future Tests
- Test the damage of EMBER vs. QUICK ATTACK on a Water-type.
- Test one-way ledges (`LEDGE_HOP_DOWN`) by trying to move up *and sideways* off them to fully verify movement restrictions.
- Test `HEADBUTT_TREE`s by interacting with them with different Pokémon in the lead to see if any move can be used.
- Test traversability of BUOY tiles.
- Test movement off a FLOOR_UP_WALL tile in all directions (sideways, down) to verify it's not just a one-way-up path.
- **Sprout Tower 2F Pillar Hypotheses:**
  1. All other Sages on Sprout Tower 2F must be defeated before interacting with the Sage at (12, 3).
  2. The interaction with the Sage at (12, 3) only makes the pillar passable during a specific time of day (e.g., night).
  3. The floor tiles in the room with the Sage at (12,3) contain a visual pattern or clue that needs to be followed or replicated.

## Future Agent & Tool Ideas
- Pathing Strategist Agent: Could suggest stun-vs-reroute strategies for dealing with moving NPCs.
- Puzzle Solver Agent: Could analyze the state of a puzzle (like the FARFETCH'D herding) and suggest the optimal next move.

## Critical Self-Correction Log
- The 'Poké Ball machine' in Elm's lab was a hallucination.
- Hallucinated a warp at (9, 35) on Route 30. There is no warp there.
- Hallucinated a warp at (13, 9) on Route 30. The actual house entrance is at (17, 5).
- **CRITICAL HALLUCINATION (Turn 2667):** Believed I was on Sprout Tower 2F at (17, 3) when I was actually on Sprout Tower 1F at (17, 2).
- **CRITICAL HALLUCINATION (Turn 2886):** Believed I was on Sprout Tower 2F at (6, 4) when I was actually on Sprout Tower 1F at (6, 3).
- **Pathfinder Tool Issue (Corrected):** The pathfinder was incorrectly assumed to be faulty. After extensive debugging, it was confirmed to be working correctly. The repeated failures were caused by my own hallucination of a traversable path on Route 32 where a large, one-way ledge system actually exists.
- **CRITICAL HALLUCINATION (Turn 3658):** Believed I was on Sprout Tower 2F at (6, 4) after climbing a ladder, but was actually still on Sprout Tower 1F at (6, 3). This invalidated my entire plan.
- **CRITICAL HALLUCINATION (Turns 4838-4866):** I was stuck in a multi-turn loop attempting to 'fix' the `find_path_to_target` tool by removing a debug print. I repeatedly submitted identical, already-correct code. The tool had been fixed in turn 4833. This was a significant failure of state tracking and a major hallucination that wasted many turns.
- **CRITICAL HALLUCINATION (Turn 5590):** Believed I had exited Union Cave and was on Route 32 at (6, 79). I was actually still inside Union Cave at (17, 3), standing on the exit warp. This caused my pathfinder to fail and my entire plan to be based on an incorrect reality.
- **CRITICAL HALLUCINATION (Turn 5640):** Believed I had a tool named `find_closest_reachable_unseen_tile`. This tool does not exist.
- **CRITICAL HALLUCINATION (Turn 5961):** Believed I had descended the ladder to AzaleaPokecenter1F (map 8_1). I was still on Pokecenter2F (map 20_1). This also re-confirmed that ladders are used by moving onto them, not by pressing a direction while standing on them.
- **CRITICAL HALLUCINATION (Turn 5981):** Believed I had a tool named `find_reachable_unseen_tiles` and tried to delete it. The tool never existed.
- **CRITICAL HALLUCINATION (Turn 5981):** Believed my `get_on_screen_object_locations_json` tool definition failed in a previous turn when it had actually succeeded. This was a state-tracking failure.
- **CRITICAL HALLUCINATION (Turn 6045):** Believed I had entered Kurt's house (map 8_4) when I was still in Azalea Town (map 8_7).
- **CRITICAL HALLUCINATION (Turn 6050):** Believed I was in Azalea Town (map 8_7) when I was actually inside the Charcoal Kiln (map 8_2).

## Tool Issues & Bugs
- The built-in `select_battle_option` tool failed during a trainer battle (Turn 6112), claiming the battle menu was not visible when it was. The tool is unreliable and should not be used. Manual battle menu navigation is required until a fix is identified.
- **Attempt 2:** Interacted with FARFETCH'D at (20, 24) while standing at (20, 23) (facing down). It turned to face up but did not move. Hypothesis: Path was blocked by trees behind it. After I cleared the dialogue, the FARFETCH'D disappeared.