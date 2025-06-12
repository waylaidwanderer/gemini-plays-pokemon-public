# Pokémon Yellow Legacy - Hard Mode Notes (Gem's Log)

## Current Status
- Location: Viridian City (Map ID 1) at (18,11).
- Badges: 0
- Level Cap: 12

## Active Pokémon Party
1. SPARKY (PIKACHU): Lv7 (26/26 HP, EXP: 442/512 to Lv8) | Moves: THUNDERSHOCK, GROWL, QUICK ATTACK

## Current Objectives
- **Primary:** Defeat Brock, the Pewter City Gym Leader.
- **Secondary:** Acquire Poké Balls from Viridian City's Poké Mart.
- **Tertiary:** Explore Viridian City for other items and information.

## Game Mechanics & Rules Summary
- Battle Style: Set. No items in battle.
- HMs: Forgettable, menu-use, not PC-storable.
- All 151 Pokémon obtainable. Trade evos by level.
- Smarter AI, tougher bosses, dynamic gym scaling (4-6).
- EXP. All obtainable without special requirements.
- Poison: 1 HP lost per 4 steps outside battle.
- STAT Experience: Significant stat boosts from battling/leveling, enemies don't get this. (Source: Youngster, Route 1)
- Enemy Trainer PP: Unlimited. (Source: Sign, Viridian City)
- PC Log Off: Saves game.
- CUT: Bug-type HM. (Source: Girl, Viridian School House)
- Evolution: By training, no trading needed. (Source: Little Girl, Viridian School House)
- Status Conditions (from School Blackboard):
  - SLP: No attack, persists. Cure: AWAKENING.
  - BRN: Power down, damage, persists. Cure: BURN HEAL.
  - PSN: HP drop, persists. Cure: ANTIDOTE.
  - FRZ: Immobile, persists. Cure: ICE HEAL.
  - PAR: Misfire chance, persists. Cure: PARLYZ HEAL.
- Wild Battle Escapes: Chance depends on lead Pokémon's Speed vs. wild Pokémon's. Equal/greater Speed = 1st try escape. Lower Speed = chance increases with attempts. Lead with fast Pokémon to maximize.
- Pokémon Nicknaming: Always nickname a Pokémon when prompted after catching it.

## Discovered Tile Types & Movement Rules
- **ground**: Walkable.
- **impassable**: Walls, objects, etc. Not traversable.
- **warp**: Map transition. Activation varies (instant 1x1, or 2-step for larger).
- **water**: Requires Surf.
- **grass**: Wild encounters.
- **ledge**: Jump down only.
- **NPC Blocking**:
  - Cannot move onto a tile occupied by a stationary NPC if it's the first step of a path from pathfinder. (Hypothesis - Attempt 1, Turn 649, Balding Guy in Nickname House (6,4) from (6,5) facing Up - pathfinder failed to account for this).
  - Cannot move directly onto a tile occupied by a stationary NPC by pressing in their direction when adjacent and facing them. (Confirmed for Balding Guy in Nickname House at (6,4) - 2 attempts, Turns 648-649. Confirmed for Girl in Viridian City at (18,10) - 2 attempts, Turns 666-667, after facing her in T665).
- **Pikachu Movement**: If Pikachu is adjacent in movement direction & player not facing him, 2 presses needed (1st turns, 2nd moves). Normal otherwise.
- **PC Interaction**: Stand below, face up, press A.

## Type Matchup Discoveries
- Ghost > Psychic.
- Poison > Bug; Bug !> Poison.

## Key NPCs & Trainers Log
(Format: [Name/Type] - [Map] (X,Y) - Outcome/Info)
- Youngster - Route 1 (6,26) - Gave Potion.
- Youngster - Route 1 (16,14) - Explained STAT Experience.
- Girl (Brunette) - Viridian School (4,6) - CUT is Bug HM.
- Girl (Little) - Viridian School (5,6) - Pokémon evolve by training.
- Cooltrainer F - Viridian School (5,2) - Advised reading blackboard.
- Girl - Viridian City (18,10) - "Grandpa needs coffee." (Re: Old Man at (19,10)).
- Old Man - Viridian City (19,10) - Blocks path N. "Private property!" Pushed player back. (Attempt 1 to pass).
- Balding Guy - Viridian Nickname House (6,4) - Nickname advice.

## Agent Development & Performance
### Defined Agents:
1.  **route_pathfinder**: Calculates move sequence. Input: {start_x, start_y, end_x, end_y}. Output: {path_found, steps[]}. (Code-enabled, Updated Prompt T667)
2.  **exploration_prioritizer_agent**: Suggests exploration target. Input: {player_x, player_y, current_map_id, current_objectives, last_warp_details (optional)}. Output: {prioritized_target_type, target_coordinates, reasoning}. (Code-enabled, Updated Prompt T667)
3.  **item_finder_agent**: Locates items/buildings or suggests paths. Input: {target_description, player_x, player_y}. Output: {target_found, target_coordinates, exploration_suggestion, reasoning}. (Code-enabled, Defined T667)

### Planned Agents:
(None currently)

### Agent Failures & Notes:
-   **route_pathfinder**:
    -   Turn 477 (Route 1): Failed (Agent LLM resp missing content).
    -   Turn 649 (Nickname House): Path (Up, Up, Left, Left, Left, Down) from (6,5) to (3,4) failed. First 'Up' to (6,4) blocked by Balding Guy. Prompt needs to consider NPCs as obstacles.
    -   Turn 787 (Route 1): Failed (Agent LLM resp missing content) when trying to path from (11,29) to (12,1). Agent appears unreliable for complex pathing or has intermittent issues.
-   **exploration_prioritizer_agent**:
    -   Turn 534 (Viridian): Suggested Pokécenter after exiting. Unhelpful.
    -   Turn 621 (Viridian): Suggested Pokécenter again after exiting. Unhelpful. Prompt needs significant refinement to avoid recently used/explored locations.

## Lessons Learned & Strategy Refinements
-   **WKG**: Record transitions immediately. Use descriptive names/tags. Verify entry points.
-   **Map Markers**: Mark used warps, defeated/info NPCs, key points, obstacles, static signs. Use distinct emojis.
-   **Interaction**: Avoid repeated interactions if first attempt yields no new info/progress. Mark loops.
-   **NPCs**: Can block paths unexpectedly. Be prepared to reroute or use `stun_npc` if essential.
-   **Efficiency**: Avoid excessive time in optional areas if main goals are pending (e.g., Nickname House). Plan longer movement sequences instead of single steps for exploration.

- Adopt a scientific mindset: form hypotheses, test systematically, document failures (with attempt counts), and avoid repeating unsuccessful strategies.

## Planned Agents (New Ideas - T718)
(None currently - focusing on existing agent performance or removal.)

- **exploration_prioritizer_agent / item_finder_agent (T718 Monitoring Note):** Continue to monitor these agents. If they consistently fail to produce valid JSON, provide unhelpful/generic suggestions, or exhibit flawed reasoning (e.g., about visited status of warps or WKG data), their prompts may need further refinement or they might be too unreliable for consistent use.

## Viridian Mart (Turns 734+)
- Received OAK'S PARCEL from the clerk at (1,6). New objective: Deliver to Prof. Oak in Pallet Town.
- Clerk at (1,6) gave OAK'S PARCEL.
- Attempted to buy Poké Balls from clerk at (1,6) three times after receiving parcel (Turns 741, 743, 744). Each time, clerk repeated 'Okay! Say hi to PROF.OAK for me!' and did not open shop. Hypothesis: Shop is locked until OAK'S PARCEL is delivered.

## Oak's Lab (Post-Parcel Delivery - Turn 775)
- Delivered OAK'S PARCEL to Professor Oak.
- Received POKéDEX from Professor Oak.
- New objective: Complete the Pokédex for Professor Oak (long-term task).

## Ledge Mechanics Clarification (Turn 798)
- Ledges can only be jumped *down*. They cannot be climbed *up*.
- If you are on a ground tile (X, Y_current) and an adjacent tile (e.g., (X, Y_current-1) for 'Up') is a 'ledge' type tile that would represent the higher elevation of that ledge, you cannot move onto it from the lower ground.
- To jump down a ledge: You must be on the higher ground adjacent to the ledge tile. For example, if (X, Y_Ledge) is the ledge tile and (X, Y_Ledge+1) is the ground below it, you'd typically be on ground at (X, Y_Ledge-1), move Down onto (X, Y_Ledge), and the game would then move you to (X, Y_Ledge+1).