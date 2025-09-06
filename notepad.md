# I. Core Directives & Lessons

## A. Core Directives
1.  **IMMEDIATE MAINTENANCE:** All data management (notepad, markers) and tool/agent refinement is the HIGHEST priority and MUST be performed in the same turn a need is identified.
2.  **PROACTIVE AUTOMATION:** Before any complex or repetitive task, I must first consider automating it with a tool or agent. If one doesn't exist, creating it is the new priority.
3.  **TRUST, BUT REFINE:** I must trust the outputs of my agents and system data. If an agent or tool is suboptimal, I must prioritize refining it immediately.
4.  **ABANDON FAILED HYPOTHESES:** If a strategy fails repeatedly, I must recognize the pattern, document it, and pivot to a new approach.

## B. Key Lessons & Recurring Failures
- **Positional & Data Awareness:** I must verify my current coordinates, turn number, and system-provided data from the Game State Information *before* every action and trust it over my own manual assessment.
- **Dead End Definition:** A map is a dead end ONLY if it has 1 or fewer reachable exits (warps/connections) AND 0 reachable unseen tiles. I must be rigorous in this calculation.
- **System vs. Local Reachability:** System warnings about "reachable" tiles/warps are a global check for the entire map and may not reflect what is reachable from my current partitioned location.
- **Confirmation Bias in Problem-Solving:** Persisting with a failed hypothesis is a critical error. After a few failed attempts, I must invalidate the hypothesis and pivot to a new one. My handling of the Officer Jenny puzzle is a key example of this failure.
- **Data Maintenance Efficiency:** Map connection markers (entry and exit) must be placed in the same turn immediately following a map transition to avoid inefficient backtracking.

# II. Game Data

## A. Type Chart (Verified)
- Electric is not very effective against Electric, Grass/Poison, and Bug/Grass types.
- Ground moves do not affect GASTLY (Ghost/Poison).
- Normal moves do not affect Ghost-types.
- Normal is not very effective against GEODUDE (Rock/Ground).
- Poison is not very effective against Ground-types.

## B. Known Pokemon Locations
- **Cerulean Cave:** Ditto, Wigglytuff, Electrode, Golem, Raichu, Sandslash, Parasect, Lickitung, Magneton, Dodrio, RHYDON, VICTREEBEL, GOLBAT, KADABRA.
- **Pokémon Tower:** GASTLY, CUBONE.
- **Mt. Moon:** ZUBAT, SANDSHREW.

## C. Key Trainer Rosters
- **Nurse Joy (Fuchsia Pokecenter):** KANGASKHAN (Lv 65): DOUBLE-EDGE, DOUBLE TEAM; SNORLAX (Lv 65): ICE BEAM, REST

# III. World Data

## B. Solved Puzzles & Key Events
- **Snorlax (Routes 11 & 12):** Awakened using the POKé FLUTE from the ITEM menu.
- **Pokémon Tower Ghost:** Used SILPH SCOPE to reveal the ghost.
- **Seafoam Islands Current:** Solved multi-floor boulder puzzle to stop the strong water current.

## C. Obstacles & Solutions
- **Rocket Grunt (Mt. Moon B2F at 30, 12):** Confirmed via dialogue that he is blocking the path south and demands a fossil to pass.
- **Officer Jenny (Cerulean City):** Blocking path east. All local hypotheses (talking to NPCs, interacting with Pikachu, clearing the backyard area) have failed. The trigger is likely elsewhere.

# IV. Active Hypotheses & Test Results
- **Hypothesis 1 (Invalidated):** The trigger to move Officer Jenny is located in the Trashed House or its immediate backyard. **Test Result:** All interactions within this area, including defeating the Rocket Grunt, talking to NPCs, and interacting with Pikachu/the environment, failed to move her. 
- **Hypothesis 2 (Invalidated):** The trigger to move Officer Jenny is on Route 24/Nugget Bridge. **Test Result:** Explored the entire route, no Team Rocket activity found.
- **Hypothesis 3 (Active):** The fossil needed for the Mt. Moon Rocket Grunt is located on a lower floor of Mt. Moon (B1F or B2F). **Test Plan:** Systematically re-explore all paths on B1F and B2F, starting from known ladders.

- **Hypothesis 3 (Active - From Agent):** The fossil is a reward for defeating a specific trainer, likely the Super Nerd on floor B2F who mentions the Cinnabar Island Lab. **Test Plan:** Locate and defeat this Super Nerd to see if he offers a fossil.

# V. Tool & Agent Development

## A. Development Lessons
- **Lesson: Menu Cursor Behavior:** Menu cursor starting positions are non-deterministic.
- **Lesson: Battle Move Selection:** The move selection menu is a single-column list navigated with UP/DOWN only. LEFT/RIGHT have no effect.
- **Lesson: Fly Destination Verification:** The `automated_fly_navigator` tool correctly identifies invalid destinations. I must verify that a location is on the Fly menu list *before* attempting to navigate to it. Pewter City is not a flyable location.

## C. Fly Menu Order (Data Gathering)
- PALLET TOWN
- SAFFRON CITY
- INDIGO PLATEAU
- CINNABAR ISLAND
- FUCHSIA CITY
- CELADON CITY
- VERMILION CITY
- LAVENDER TOWN
- **Lesson: Mt. Moon Partitions:** The lower floors of Mt. Moon are heavily partitioned. My pathfinding tools were failing because I was trying to navigate between disconnected areas. I repeatedly misidentified these partitions as dead ends, failing to account for all reachable warps. I must trust system data on reachability over my own flawed manual assessments or old markers.
- **Lesson: Mt. Moon Partitions:** The lower floors of Mt. Moon are heavily partitioned. My pathfinding tools were failing because I was trying to navigate between disconnected areas. I repeatedly misidentified these partitions as dead ends, failing to account for all reachable warps. I must trust system data on reachability over my own flawed manual assessments or old markers.
- **Lesson: Mt. Moon Partitions:** The lower floors of Mt. Moon are heavily partitioned. My pathfinding tools were failing because I was trying to navigate between disconnected areas. I repeatedly misidentified these partitions as dead ends, failing to account for all reachable warps. I must trust system data on reachability over my own flawed manual assessments or old markers.