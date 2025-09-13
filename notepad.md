# I. Meta-Strategy & Core Principles
1.  **Immediate Maintenance:** All data management (notepad, markers) and tool/agent refinement is the HIGHEST priority and MUST be performed in the same turn a need is identified, regardless of game state. Deferring these tasks is a critical failure.
2.  **Proactive Automation & Refinement:** Before any complex or repetitive task, I must first consider automating it with a tool or agent. If one doesn't exist, creating it is the new priority. If an agent or tool is suboptimal, I must prioritize refining it immediately.
3.  **Trust, But Verify:** I must trust the outputs of my agents and system data. However, if a tool's output contradicts the Game State Information, my assumption must be that the tool is wrong, and I must debug it.
4.  **Hypothesis-Driven Exploration:** All exploration must be guided by a clear, documented hypothesis. I must avoid wandering aimlessly and systematically test one variable at a time, documenting all results.
5.  **Warp Discipline:** After every warp, my first action must be to check and, if necessary, create/update markers on **both** the departure and arrival maps.
6.  **Mandatory Self-Assessment:** Every 50 turns, I must perform a structured self-review to ensure my strategies, documentation, and tool usage remain optimal and aligned with my core principles.
7.  **Efficiency Over Fixation:** If a simple automation tool fails during a low-stakes, repetitive task (like a wild battle), it is more efficient to complete the task manually and fix the tool later, rather than getting stuck debugging mid-task.
8.  **Battle Menu Anomaly (Confirmed):** The system's tool execution is unreliable when combining directional inputs with an action button ('A') in a single turn. Automation must separate these into separate turns.
9.  **Confirmation Bias Awareness (Self-Assessment Finding):** I must be vigilant against confirmation bias. If a hypothesis fails multiple documented tests, I must actively pivot to a new, different hypothesis rather than repeating the failed approach. I should also formulate tests designed to *disprove* my own theories, not just confirm them. To combat this, I should use the `puzzle_solver_agent` more readily when I feel stuck on a single line of reasoning.

# II. Quest Log
- **Current Quest: The Mt. Moon Fossil**
    - **Objective:** Find a fossil to give to the Rocket Grunt blocking the path at Mt. Moon B2F (30,12).
    - **Status:** Pivoting away from the 'Dig' hypothesis after extensive, failed testing. Now pursuing new leads from the `puzzle_solver_agent`.
    - **Next Step:** Travel to Lavender Town to test the hypothesis that the grunt wants a bone-related item from the Pokémon Tower. Be wary of confirmation bias with this hypothesis; pivot quickly if it yields no results.

# III. Battle Intel
- **Type Effectiveness Chart (Verified):**
    - Water is super-effective against Rock/Ground (Observed: OMANYTE's SURF vs GEODUDE).
    - Water is not very effective against Bug/Grass (Observed: OMANYTE's BUBBLEBEAM vs PARAS).
    - Poison is not very effective against Poison/Flying (Confirmed: ECHO's SLUDGE vs ZUBAT) and Rock/Ground (Observed: ECHO's SLUDGE vs GEODUDE).
    - Flying is not very effective against Rock/Ground (Observed: ECHO's FLY vs GEODUDE).
- **Notable Trainer Rosters:**
    - **Sabrina (Saffron Gym):** MR. MIME (Lv 65 - PSYCHIC), HYPNO (Lv 64 - PSYWAVE), SLOWBRO (Lv 64 - PSYCHIC), JYNX (Lv 64 - BLIZZARD, BUBBLEBEAM, DREAM EATER, LOVELY KISS), GENGAR (Lv 64 - NIGHT SHADE, PSYCHIC), ALAKAZAM (Lv 65 - THUNDER WAVE, PSYCHIC).
    - **SMITH (Cerulean Cave):** AERODACTYL (Lv 65 - HYPER BEAM, ROCK SLIDE).
    - **Brock (Pewter Gym):** OMASTAR (Lv 64 - HYDRO PUMP, BLIZZARD), ONIX (Lv 65 - EARTHQUAKE, ROCK SLIDE), KABUTOPS (Lv 64 - SWORDS DANCE, SLASH), GOLEM (Lv 64 - ROCK SLIDE), NINETALES (Lv 64 - REFLECT), AERODACTYL (Lv 65 - FLY).
- **Wild Pokémon Locations:**
    - **Cerulean Cave:** WIGGLYTUFF (Lv 62 - LOVELY KISS, DOUBLE-EDGE, REST), SANDSLASH (Lv 63 - SWORDS DANCE, EARTHQUAKE), GOLEM (Lv 64 - EXPLOSION), LICKITUNG (Lv 61 - WRAP), CHANSEY (Lv 63 - DEFENSE CURL, MEGA PUNCH), RAICHU (Lv 64 - AGILITY).

# IV. Fossil Quest - Hypotheses Log
- **Failed Hypotheses:**
    - The fossil is in an interactable rock.
    - The Hiker on 1F at (6,7) will move if shown the revived HELIX fossil Pokémon. (Result: Dialogue unchanged).
    - The scientist in the Cinnabar Lab Fossil Room at (5,3) can 'un-revive' a fossil Pokémon. (Result: Dialogue was generic, asked for a fossil item).
    - The scientist in the Cinnabar Lab Fossil Room at (8,3) can 'un-revive' a fossil Pokémon. (Result: Dialogue confirmed he only revives fossil items, does not reverse the process).
    - Presenting the revived HELIX fossil Pokémon to the Rocket Grunt on B2F will trigger a new event. (Result: Dialogue unchanged, still demands a fossil item).
    - The 'fossil' the Rocket Grunt wants is the MOON STONE. (Reasoning: Wordplay and context of being in Mt. Moon). (Result: Dialogue unchanged).
    - A specific, non-fossil Pokémon from Mt. Moon (e.g., Geodude) will satisfy the Grunt. (Reasoning: Subverting expectations by reinterpreting 'fossil'). (Result: Dialogue unchanged).
    - The Hiker on Mt. Moon 1F at (6,7) is part of a chained quest. (Reasoning: Two path-blockers in one dungeon is suspicious). (Result: Dialogue unchanged, even with different Pokémon in party).
    - The 'fossil' the Grunt wants must be stolen from the Pewter City Museum of Science. (Reasoning: Suggested by puzzle_solver_agent). (Result: Interacting with both fossil exhibits yielded no item or event).
    - The move 'Dig' must be used on a specific, unmarked tile within Mt. Moon to unearth the other fossil. (Reasoning: Suggested by puzzle_solver_agent). (Result: Systematically checked all reachable ground tiles on 1F with no success. The move consistently teleports the player out of the cave).
    - The Rocket Grunt will accept a Pokémon nicknamed 'fossil'. (Reasoning: Suggested by puzzle_solver_agent). (Result: Dialogue unchanged).

- **New Hypotheses (from puzzle_solver_agent - Turn 209957):**
    - **Hypothesis 1:** The scientist in the Cinnabar Lab will provide a 'replica' fossil or the other, unchosen fossil after being shown a fully-evolved version of the fossil he revived.
    - **Hypothesis 2 (Active):** The 'fossil' the Rocket Grunt wants is a bone-related item from the Pokémon Tower in Lavender Town, likely a Thick Club or Rare Bone.
    - **Hypothesis 3:** The Hiker on Mt. Moon 1F at (6,7) will trade you for your revived fossil Pokémon, giving you the other fossil in return.
    - **Hypothesis 5:** The other fossil (the one you didn't pick) has respawned at its original location, but only after a specific flag is triggered, like re-battling the Super Nerd.

# V. Self-Assessment Findings
- **(Turn 209210):** Lapsed in immediacy, exhibited confirmation bias, and failed to verify game state after tool use.
- **(Turn 209672):** Made an untested assumption about search area, a tool failed repeatedly, and used inconsistent map markers.
- **(Turn 209979):** Lapsed in immediate maintenance, fixated on the 'Dig' hypothesis for over 100 turns (confirmation bias), and created a flawed tool (`clear_map_markers_by_emoji`). Pivoting strategy to address this.
- **(Turn 210339):** Hallucinated my location for multiple turns, leading to wasted actions. Failed to document tile mechanics. Identified redundant map markers and inefficient manual processes (flying, marker cleanup) that should be automated. Re-prioritizing tool development and committing to more rigorous verification of game state.
- **(Turn 210442):** Notepad's tile mechanics section was incomplete and automation backlog was out of date. Failed to mark defeated trainers on current map. Addressed all issues immediately.

# VI. Automation Suite
- **Strategy:**
    - **Battle:** Use `comprehensive_battle_agent` for high-stakes battles.
    - **Navigation:** Use `automated_path_navigator` for single-map pathfinding. Use `master_navigator_agent` for complex, multi-map navigation.
- **Tool Development Log:**
    - **(Turn 210051):** Created `initiate_fly` tool to automate opening the Fly menu. This is a direct response to an Overwatch critique about failing to proactively automate repetitive tasks.
    - **Backlog (Priority Order):**
        - **`fly_to_city` Tool:** An enhanced version of `initiate_fly` that can also select the destination city from the map. Requires mapping the Fly screen layout. (HIGH PRIORITY - will prevent inefficient manual menuing).
        - **`clear_map_markers` Task:** Use existing `find_map_markers_by_emoji` tool to get a list of markers, then use `delete_map_marker` in a loop to clear them. (Note: A single tool cannot delete multiple markers at once due to system limitations).
        - **`pc_navigator` Tool:** A tool to automate withdrawing/depositing a specific Pokémon from the PC. `pc_navigate(action, pokemon_name)`.
        - **`item_user` Tool:** A tool to automate using an item from the bag. `use_item_from_bag(item_name, [target_pokemon])`.
        - **`use_hm` Tool:** A tool to automate using a field move like Cut or Flash. `use_hm(hm_name, pokemon_name)`.
        - **`capture_assistant` Agent:** An agent to provide turn-by-turn advice for catching wild Pokémon.
        - **`wild_battle_automator` Tool:** A tool to manage simple wild encounters by repeatedly using the single most effective move until the battle ends.
        - **`TeamCompositionAdvisor` Agent:** An agent that suggests an optimal party from the PC for a specific challenge (e.g., Gym rematch).

# VII. Game Mechanics & Tile Properties
- **ground:** A standard, walkable tile. Can be occupied by objects or lead to warps.
- **impassable:** A solid tile that cannot be entered, such as a wall or a gravestone.
- **grass:** Tall grass where wild Pokémon can be encountered. Walkable.
- **water:** Can be crossed with SURF. Impassable otherwise.
- **steps:** Allows movement between `ground` and `elevated_ground`.
- **elevated_ground:** Walkable ground at a different elevation.
- **ledge:** One-way traversal. Can be jumped down from above (Y-1 to Y+2), but not climbed up.
- **cuttable:** A tree that can be cut with HM Cut. Becomes `ground` after cutting, but respawns on map change or after battle.