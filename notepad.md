## Core Principles & Critical Lessons

### Core Principles
- **IMMEDIATE ACTION:** I must perform tasks like placing markers, updating my notepad, and fixing tools *immediately*. Deferring tasks, like placing map markers, is a process violation. Significant events must be documented *immediately* in the turn they occur.
- **AGENT USAGE:** When stuck for more than 5 turns on a puzzle, I must use the `hypothesis_generator` agent. My `simple_battle_strategist` agent is underutilized and I will prioritize using it for all future wild battles to automate decision-making.
- **PUZZLE DOCUMENTATION:** My entire problem-solving process (observation, hypothesis, test, conclusion) for any puzzle must be documented in this notepad as it happens.
- **MAP MARKER DISCIPLINE:** I must always check for existing map markers before creating a new one to avoid duplicates. I must mark BOTH ends of a warp immediately after traversal.
- **TOOL MAINTENANCE:** I must NEVER defer fixing a broken tool or agent. It is always the highest priority, overriding any in-game objective.
- **TOOL FAILURE:** If a tool fails, my first assumption must be that the tool is broken, not that the game is impossible. I must fix the tool before re-attempting the action.
- **IMMEDIATE CORRECTION:** If my understanding of the game state (e.g., the existence of a tool) is proven wrong, I must immediately correct my documentation (notepad) before any other action.
- **TRUST OBSERVATION:** My biggest obstacle is my own memory. I must only trust in-game observation.
- **Trainer Identification:** I must verify the name and location of a trainer before marking them as defeated to prevent misidentification errors like the Hiker Daniel/Russell mix-up.

### Critical Self-Correction Log (Hallucinations)
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

## Game Mechanics & Discoveries

### General Mechanics
- Talking to Mom does NOT heal my Pokémon. This is a critical mechanic difference from other games.
- Resting in the player's bed does NOT heal Pokémon.
- Stunning an NPC can break scripted events, causing dialogue loops. It can also be a reliable solution for interacting with moving NPCs.
- Repeatedly interacting with an object (like a sign) without new results can lead to loops. I must dismiss dialogue before attempting to move.
- The 'Select' button on the nicknaming screen toggles between uppercase and lowercase keyboards.

### Battle Information
*Ignis learned EMBER at Lv12.*
*Ignis grew to Lv15 after defeating a wild Gastly.*
*Ignis grew to level 18 after defeating Picnicker Liz's Nidoran.*
*Ignis grew to Lv19 after defeating Fisher Ralph's Goldeen.*
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
- **WARP_CARPET_DOWN/RIGHT**: Traversable warp. The 'DOWN' variant requires pressing 'Down' on the tile to activate. (Verified)
- **WARP_CARPET_LEFT**: Traversable, acts as a warp tile. (Verified)
- **WATER**: Impassable. (Verified by pathing attempts)
- **WINDOW**: Impassable. (Verified)

## World Knowledge & Location Notes

### Route 29
- The southern path is a dead end.
- The western path is blocked by CUT_TREEs and HEADBUTT_TREEs.

### Route 30
- MR. POKEMON's house is located here. (Confirmed)

### Violet City
- Building at (21, 29) is a house with a trade NPC, not the Gym.
- Sprout Tower is a separate building from the Gym.
- The city is not divided by a river; the two sides are connected by walkable paths.
- YOUNGSTER at (5, 18) mentioned a 'wiggly tree' that 'squirms and dances'. This is likely a hint about how to interact with HEADBUTT_TREEs.

## Archived Investigations (Solved/Debunked)
- **Healing Methods (New Bark Town):** Conclusion: Neither Mom nor the player's bed heals Pokémon.
- **Fisher NPC Interaction (New Bark Town):** Conclusion: Moving NPCs can disrupt interactions. Stunning them first is a reliable solution.
- **Nickname Screen Controls (Violet City):** Conclusion: The 'Select' button toggles the keyboard case.
- **Violet Mart Path (Violet City):** Conclusion: The path to the clerk is blocked. Talking to the Cooltrainer M at (5, 2) does not open it.
- **Violet City Gatehouse Warp:** Conclusion: Currently impassable and a dead end for now. All simple interaction hypotheses failed.
- **Sprout Tower 1F Path:** Conclusion: A solid wall at x=4 divides the first floor, making the Sage at (3, 5) unreachable from the east. Defeating other Sages does not alter the layout.
- **Sprout Tower 2F Pillar:** Conclusion: Numerous simple interaction tests (re-interacting with the Sage, checking other objects/walls, etc.) have failed to make the central pillar move again after its initial movement.
- **Route 32 Pathing:** Conclusion: The eastern and western paths are separate at the northern end. The eastern path is a dead end due to one-way ledges.
- **Route 32 Item Pickup:** Conclusion: An item in a Poké Ball on the ground must be interacted with from an adjacent tile, not by walking onto it.
- **Route 32 Hidden Item (SUPER POTION):** Conclusion: The hidden item at (11, 40) was successfully retrieved by approaching from an adjacent tile ((10, 40)) while already facing the item, then pressing 'A'.
- **Sprout Tower Puzzle - New Hypotheses (from Agent - Turn 3590):**
  1. All other Sages on Sprout Tower 2F must be defeated before interacting with the Sage at (12, 3).
  2. The interaction with the Sage at (12, 3) only makes the pillar passable during a specific time of day (e.g., night).
  3. The player must have a specific Pokémon in the first slot of their party when interacting with the Sage at (12, 3). (DEBUNKED - Switched lead to Aether, no effect.)
  4. The floor tiles in the room with the Sage at (12,3) contain a visual pattern or clue that needs to be followed or replicated.
- **Union Cave Exit Puzzle (Ongoing):**
  - **Observation:** At (17, 3) on a `WARP_CARPET_DOWN` tile. Cannot exit.
  - **Failed Hypotheses:**
    1. Stepping onto the tile from above (17, 2). (FAILED)
    2. Pressing 'A' while on the tile. (FAILED)
    3. Stepping onto the tile from the left (16, 3). (FAILED)
  - **New Hypothesis:** The name `WARP_CARPET_DOWN` implies I must press 'Down' while standing on the tile to activate it.
  - **Test:** Pressing 'Down' while at (17, 3).

## Current Objectives & Open Puzzles

### General Tasks & Tests
- Test one-way ledges by trying to move up them.
- Test traversability of BUOY tiles.

## Untested Assumptions & Future Tests
- Test the damage of EMBER vs. QUICK ATTACK on a Water-type.
- Fully test the traversability of `FLOOR_UP_WALL` tiles.

## Route 33
- Hiker Anthony is on this route. He gives his phone number instead of battling.
- **CRITICAL HALLUCINATION (Turn 5961):** Believed I had descended the ladder to AzaleaPokecenter1F (map 8_1). I was still on Pokecenter2F (map 20_1). This also re-confirmed that ladders are used by moving onto them, not by pressing a direction while standing on them.
* The `stun_npc` effect is temporary and resets when changing maps. (Verified in Azalea Pokémon Center)

## Untested Assumptions & Future Tests
- Test one-way ledges (`LEDGE_HOP_DOWN`) by trying to move up them.
- Test `HEADBUTT_TREE`s by interacting with them with different Pokémon in the lead to see if any move can be used.

## World Knowledge & Location Notes
### Azalea Town
- The warps to the Gym (10, 15) and Slowpoke Well (31, 7) are currently blocked by Team Rocket grunts. I cannot reach them to investigate and mark them until I find a way to move the grunts.

## Untested Assumptions & Future Tests
- Test one-way ledges (`LEDGE_HOP_DOWN`) by trying to move up them.
- Test `HEADBUTT_TREE`s by interacting with them with different Pokémon in the lead to see if any move can be used.

## World Knowledge & Location Notes
### Azalea Town
- The warps to the Gym (10, 15) and Slowpoke Well (31, 7) are currently blocked by Team Rocket grunts. I cannot reach them to investigate and mark them until I find a way to move the grunts.