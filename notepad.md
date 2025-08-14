# I. Game Mechanics & World Knowledge

## A. Core Gameplay (Verified)
- **Battle Style:** Set mode.
- **Items in Battle:** Prohibited.
- **Level Caps:** Active and enforced.
- **PC Interaction:** To use a PC, stand on the tile directly *below* it and face *up* before pressing 'A'.
- **Menu Navigation:** The 'B' button is the primary method for exiting/canceling out of menus.

## B. Tile Mechanics & Traversal (Verified)
- `ground` / `grass`: Standard traversable tiles.
- `impassable` / `unknown`: Cannot be entered. Must be navigated around.
- `water`: Requires Surf to traverse.
- `cleared_boulder_barrier`: Acts as a one-way ramp, allowing movement *up* from 'ground' to 'elevated_ground', but not down.
- **Boulder Pushing:** A single button press can both turn the player and push an adjacent boulder one tile. The player's position does not change during the push. Boulders CANNOT be pushed onto 'steps' tiles.

## C. Elite Four Mechanics (Verified)
- **Room Progression:** Attempting to leave a room south triggers a 'Don't run away!' event, which is the key to unlocking the northern warp.
- **Defeated Trainers:** Become impassable obstacles after their defeat speech.
- **Blackout Respawn:** Losing a battle to an Elite Four member causes a blackout, respawning the player with a healed party in the challenge lobby. While this is a consequence of failure, the intended method to access the Pokémon Center is to exit the challenge area and re-enter the Indigo Plateau building from the separate, eastern entrance on Route 23.

# II. Battle Intelligence

## A. Type Effectiveness Chart (Verified)
- **Super Effective (2x damage):**
  - Water > Rock, Ground, Fire
  - Electric > Water
  - Ground > Fire, Electric, Rock, Psychic (Hypothesized - needs more data)
  - Ice > Ground, Grass, Flying, Dragon
  - Fighting > Normal, Rock, Ice
  - Grass > Ground, Rock, Water
  - Psychic > Ghost

- **Not Very Effective (0.5x damage):**
  - Normal !> Rock
  - Ice !> Fighting
  - Psychic !> Psychic

- **Immune (0x damage):**
  - Ground immune to Electric
  - Flying immune to Ground
  - Ghost immune to Ground

## B. Strategic Notes & Hypotheses
- **Opponent Coverage:** Always assume opponents, especially high-level ones like the Elite Four, have coverage moves for their weaknesses. Do not rely solely on primary typing for strategy.
- **Hypothesis Falsification (Ground > Psychic):** To avoid confirmation bias with the 'Ground > Psychic' hypothesis, I must actively try to disprove it. When facing a Psychic-type, I will first test with non-Ground type moves to establish a baseline before using a Ground move.

## C. Battle Logs (Elite Four)
### Battles vs. Agatha (Losses)
- **Multiple Attempts:** Lost to Gengar (Lv 57). Confirmed Moves: Mega Drain, Hypnosis, Night Shade.
- **Key Learnings:**
  - Gengar is extremely fast and can outspeed my entire team.
  - Mega Drain (Grass) is super-effective against Water/Ice (Neptune) and devastating to Rock/Ground types (Crag). Gengar uses it to heal.
  - Night Shade deals fixed damage equal to Gengar's level (57), providing consistent damage output.
  - Hypnosis is a major threat, capable of disabling key Pokémon.
  - **Conclusion:** A fast, high-level Psychic-type (like Kadabra) is essential to outspeed and KO Gengar with a super-effective move before it can act.

### Attempt 2 vs. Lance (Loss)
- **Opponent's Pokémon:**
  - Aerodactyl (Lv 61) - Typing assumed Rock/Flying. Known Moves: EARTHQUAKE.

# III. Meta-Progression & Lessons Learned

## A. Core Methodological Failures (Self-Correction Log)
- **Immediate Action Mandate (CRITICAL FAILURE):** I have repeatedly deferred documentation and tool maintenance instead of performing them immediately. As an LLM, I have no 'later'; all administrative tasks MUST be performed in the current turn and take precedence over gameplay.
- **Tool Maintenance Mandate (CRITICAL FAILURE):** I deferred fixing my broken `generate_path_plan` tool in Victory Road, violating the core directive that maintaining automation is the highest priority. Faulty tools must be fixed immediately.
- **Agent Engineering Failure (`battle_strategist_agent`):** I failed to correctly engineer the `battle_strategist_agent`'s prompt and input schema, leading to suboptimal suggestions. I must prioritize iterative refinement of agents.
- **Scientific Mindset & Hypothesis Testing (CRITICAL FAILURE):** My fixation on a single solution path must be avoided. When a primary hypothesis repeatedly fails, I must actively seek to falsify it by testing alternative routes and solutions. I must be more meticulous in observing, forming a single testable hypothesis, documenting, testing, and then attempting to *falsify* the conclusion.
- **Navigational Failure (Indigo Plateau):** I fundamentally misunderstood the Indigo Plateau layout. I observed the Nurse/PC in the eastern building but failed to pathfind there. My conclusion should have been that the area was physically divided and unreachable from my entrance. Instead of accepting this and forming a new hypothesis (e.g., "The entrance to the Pokémon Center facilities must be a separate entrance on Route 23 that I have missed."), I exhibited confirmation bias, repeatedly trying to enter the same wrong building and assuming my tools were broken. This wasted dozens of turns. The correct scientific process is: 
  - **Observation:** Entered eastern Indigo Plateau building. Can see Nurse/PC, but they are behind an impassable counter. 
  - **Hypothesis 1:** I can walk to the Nurse/PC from my current position. 
  - **Test 1:** Attempt to pathfind. 
  - **Conclusion 1:** Pathfinding failed; system confirmed destination is unreachable. Hypothesis 1 is FALSE. The lobby is physically divided. 
  - **New Hypothesis 2:** The entrance to the Pokémon Center facilities must be a separate entrance on Route 23 that I have missed. I must exit this building and re-explore Route 23.
- **Confirmation Bias (Route 23):** I repeatedly failed to navigate Route 23 because I assumed the path south was a straight shot and that my `generate_path_plan` tool was broken. I wasted many turns trying to force a path through what my own map data clearly showed was an impassable wall of statues. The tool was correct all along; it was my interpretation of the map that was flawed. This is a critical failure in hypothesis testing. I must always verify my assumptions about the map layout *before* blaming my automation.

## D. Tile Mechanic Nuances (Hypotheses & Cautions)
- **Context is Key:** The behavior of a specific tile type (e.g., `cleared_boulder_barrier`) might not be universal. A tile's function can change based on its location and the context of the puzzle. I must test tile mechanics in each new area rather than assuming they will always work the same way.