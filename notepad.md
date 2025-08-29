# I. Meta-Progression & Lessons Learned

# I. Core Principles & Lessons Learned
- **Immediate Maintenance:** All data management (notepad, markers, tools, agents) must be performed in the current turn without deferral. This is the highest priority.
- **Trust System & Tools:** Trust game state data, system feedback, and tool outputs over intuition. Verify reachability before debugging a 'no path' result.
- **Scientific Approach:** Observe, hypothesize, test, and document all puzzle-solving attempts. Avoid repeating failed strategies.
- **Strategic Flexibility:** If progress stalls on a primary objective, pivot to a secondary, tertiary, or exploratory goal.
- **Preserve Knowledge:** Do not delete valuable insights from the notepad; only restructure or condense.
- **Dead End Area Mismatch (Seafoam B3F):** My previous assertion that Seafoam Islands B3F was a dead end was incorrect. The system reported 4 reachable exits. This was a critical hallucination. **Correction:** I must re-evaluate my understanding of B3F's layout and trust system feedback over my visual interpretation of the map. (Self-correction from Turn 170981).
- **Notepad and Map Marker Update Priority (Turn 171001):** I attempted multiple `define_map_marker` and `find_path` calls before executing a planned `notepad_edit` overwrite. This is a direct violation of the core directive that notepad updates are the highest priority and must be performed immediately. **Correction:** All notepad updates must be performed immediately, prior to any other actions.
- **Fly Menu Navigation Failure (Turn 171342-171352):** I repeatedly overshot the target Pokémon in the party menu and then manually scrolled through the Fly menu. **Correction:** I must use the `fly_menu_navigator` tool as intended and trust its output. The `get_next_pokemon_press` tool was deleted to make space for `fly_menu_navigator` and should not have been used. This also highlights a failure to immediately use a newly defined tool.
- **Deferred Map Marker Creation (Turns 172822, 172872, 172881):** I cut trees but deferred defining map markers for them until a later turn (172829, 172877, 172882). **Correction:** Map markers must be defined immediately on the same turn the event occurs.
- **Repeated `find_path` Calls without Re-evaluation (Turns 172922-172929):** I repeatedly called `find_path` to the same target after it failed without adapting my strategy or re-evaluating the cause of failure. **Correction:** When a tool's output is unexpected, I must immediately adapt my strategy and re-evaluate the underlying cause of the failure.
- **Recurring Deferred Notepad and Map Marker Updates (Critique from Turn 172930, 173597 - Critical Failure):** The overwatch critique highlighted a recurring lapse in performing notepad and map marker updates *immediately*, citing specific turns where updates were deferred. This is a critical failure to adhere to the core directive that all maintenance must be performed in the *current turn* without deferral. **Correction:** I must ensure all notepad updates and map marker definitions are performed in the *current turn* without deferral, and this issue will be prioritized in all future actions.
- **Tool Refinement (Critique from Turn 173623 - Critical Failure):** I have repeatedly failed to refine my `find_path` tool to provide diagnostic information about *why* a path is blocked. My `menu_navigator` and `select_battle_option` tools exhibit execution issues. I have deferred fixing these, prioritizing the ongoing battle. **Correction:** Tool refinement is a higher priority than any short-term gameplay objective. I must immediately refine faulty tools using `define_tool`.
- **Notepad Redundancy (Critique from Turn 173623 - Critical Failure):** My notepad contains significant outdated and redundant information. **Correction:** I must break down large-scale reorganization into smaller, focused `replace` or `append` actions to avoid destructive changes.
- **Map Marker Usage (Critique from Turn 173623 - Critical Failure):** My map markers section is currently empty, which is a critical failure. **Correction:** I must immediately begin diligently marking every discovered NPC, defeated trainer, used warp, dead end, and key discovery with Map Markers.

# III. Game & World Knowledge

## A. Battle Mechanics & Type Effectiveness
- **Verified Type Chart:**
  - Electric is super-effective against Poison/Flying, Water, Water/Ice, and Water/Psychic.
  - Fighting is super-effective against Ice, Normal, and Rock.
  - Flying is immune to Ground.
  - Ghost is immune to Ground.
  - Grass is super-effective against Ground, Ground/Rock, and Water/Ice.
  - Ground is super-effective against Electric, Ghost, Ground, Psychic, and Rock/Ground.
  - Normal is immune to Ghost.
  - Psychic is super-effective against Poison.
  - Rock is super-effective against Flying.
- **Anomalies & Hypotheses:**
  - **Night Shade Damage:** May be altered in this ROM hack.
  - **Hyper Beam Recharge:** May be conditional or inconsistent.
  - **Move Menu Cursor Reset:** May randomly reset to the top position.

## B. Tile & Field Mechanics
- **Linked Boulder Rotation:** Some water-based boulders rotate in a linked fashion.
- **Hidden Passages:** Impassable-looking walls can sometimes be walked through.
- **Strength Mechanics:** Does not need to be reactivated per push. Player position can change depending on push direction.
- **HM Field Move Usage:** Requires two 'A' presses (prompt + confirmation).

## C. Tool & Agent Development

### 3. Development Ideas & Testing Plans

- **`endurance_battle_advisor` Agent Idea:** Create an agent that analyzes prolonged battle scenarios, like a potential battle loop, to advise whether continuing the battle is more efficient than a strategic blackout to reset the encounter.
- **`hidden_passage_finder` Agent Idea:** Create an agent that takes the coordinates of a bounded, isolated area as input and generates a systematic, efficient search pattern to find a hidden passage.
- **`teach_hm_automator` Tool Idea:** Create a tool that takes an HM and a Pokémon name as input and generates the full sequence of button presses to teach the move.
- **`interrupt_handler_navigator` Tool Idea:** Create a tool that takes a final destination, generates a path, and automatically handles interruptions like wild battles by re-pathing.
- **`notepad_analyzer_agent` Idea:** Create an agent that can parse the entire notepad, identify redundancies or contradictions, and suggest organizational improvements.
- **`puzzle_reset_automator` Tool Idea:** Create a tool that automates the process of resetting a puzzle by generating and executing a path to the nearest map transition and back.
- **Agent Refinement: `master_battle_agent` `recommended_lead`:** The `master_battle_agent`'s reasoning for `recommended_lead` could be more robust, especially when the opponent's full team is not known. This is an area for potential future refinement.

### 4. Tool Limitations (Observed)
- **`notepad_edit` `replace` Flaw:** The `replace` action cannot distinguish between two identical strings in the notepad. If a string appears multiple times, the tool fails to replace a specific instance, making it impossible to remove targeted duplicates. (Observed Turn 162963).
- **`teleporter_mapper` Tool (Blocked):** This tool cannot be implemented. Its function requires persistent memory to build a graph of teleporter connections across multiple turns. The current tool execution environment is stateless and does not support this. Development is blocked pending a system update that allows for persistent tool state.

## D. Key Event & Puzzle Log

### 1. Major Events (Post-Champion)
- **Route 24 Cave:** Remains blocked after becoming Champion.
- **Silph Co. Elevator (SOLVED):** After selecting a floor, must step on the warp pads to travel.
- **Cerulean City Post-Champion Events:** Misty rematch is triggered after solving the Trashed House backyard puzzle. Battle loop is broken by selecting 'NO' to the rematch prompt.

### 2. Seafoam Islands Puzzle Log
- **Main Obstacle:** Strong water current on B4F blocked progress, solved by a boulder puzzle on B3F.
- **B4F Linked Boulder Rotation:** Boulders at (5, 16) and (6, 16) are part of a linked rotation puzzle to change water flow.
- **Articuno Captured:** Successfully captured Articuno on B4F at (7,2).

## E. Opponent Information
- **Lorelei (E4):** Slowbro (Earthquake), Jynx (Bubblebeam), Gengar (Lv 59), Cloyster (Lv 55, Explosion).
- **Bruno (E4):** Hitmonchan (Ice Punch, Thunder Punch), Onix (Explosion), Machamp (Earthquake).
- **Agatha (E4):** Gengar (Hypnosis, Dream Eater).
- **Lance (E4):** Dragonite (Lv 61, Slam, Thunder Wave, Wrap, Hyper Beam), Gyarados (Slam), Aerodactyl (Earthquake), Charizard (Earthquake, Flamethrower).
- **Misty (Rematch):** Seadra (Lv 64), Golduck (Lv 65, Psychic, Blizzard), Lapras (Lv 64, Hydro Pump, Thunder, Psychic, Blizzard), Vaporeon (Acid Armor), Starmie (Thunderbolt).
- **Kris (Snorlax):** Snorlax (Earthquake, Body Slam, REST).
- **Craig (Power Plant):** JOLTEON (Lv 55, DIG, THUNDERBOLT, PIN MISSILE, THUNDER WAVE), AERODACTYL (Lv 55, ROCK SLIDE), EXEGGUTOR (Lv 55, MEGA DRAIN, PSYCHIC), SNORLAX (Lv 55, AMNESIA, EARTHQUAKE, BODY SLAM, REST).

## F. General Game Tips (ROM Hack Specifics)
- **Normal vs Electric Neutrality (Hypothesis):** Need to verify if Normal-type moves are neutral against Electric-types by observing battle text in a future encounter.