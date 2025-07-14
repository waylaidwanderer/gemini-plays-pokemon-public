# I. Core Principles & Lessons Learned
- **Immediate Maintenance & Escalation:** I must perform maintenance (notepad, agents) and fix tools *immediately* when a manual approach fails repeatedly. Deferring these actions is a critical process failure. My repeated failure to fix my `path_planner` tool is a prime example of this lapse.
- **Combat Confirmation Bias:** I must actively try to *disprove* my hypotheses. I wasted significant time assuming my `path_planner` was correct because I was seeking to confirm it worked, rather than testing its limits and questioning my own assumption that the map was fully connected.
- **Agent & Tool Trust is Mandatory:** I MUST trust my custom agents' and tools' advice. My `puzzle_solver_agent` correctly identified the eastern corridor as a potential trap, which I initially dismissed.
- **Systematic Problem Solving:** For any puzzle, I must use my notepad to log observations, form a single testable hypothesis, record the test and its outcome, and then form a conclusion. This structured approach prevents chaos and tunnel vision.

# II. Game Mechanics & Battle Intel

## A. Tile Mechanics & Traversal
- `ground`: Standard walkable tile.
- `impassable`: Walls, furniture, etc. Cannot be walked on.
- `gate_offscreen`: These gates are not on screen. For pathfinding, they must be treated as potentially open to encourage exploration of routes that go off-screen.
- `closed_gate`: A gate that is visibly closed and acts as an impassable wall.
- `open_gate`: A gate that is visibly open and acts as ground.
- `hole`: A tile that causes the player to fall to the floor below.
- `water`: Requires SURF to traverse.

## B. Confirmed ROM Hack Changes
### B1. Type Matchups & Immunities
- **Super Effective:** Psychic > Ghost/Poison; Ghost > Psychic; Electric > Rock/Water; CUT (Normal) > VICTREEBEL (Grass/Poison); Flying > Grass/Poison; Psychic > Flying; Ice > Ground; Ground > Poison; Ground > Fire; Rock > Fire
- **Not Very Effective:** Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic; Bite (Normal) !> HAUNTER (Ghost/Poison); Ice !> Gyarados (Water/Flying); Poison !> Poison; Ice !> Water; Poison !> Ground
- **Immunities:** Flying-type immune to Ground-type moves; Ground-type Pokémon are immune to Electric-type moves; MUK immune to Poison-type moves; HYPNO immune to STUN SPORE (powder moves); MUK immune to THUNDER WAVE (Electric-type status move); MAROWAK (Ground-type) immune to POISON GAS (Poison-type move).

### B2. Battle & Field Mechanics
- **Evasion:** PSYWAVE and CONFUSE RAY can fail against targets with high evasion boosts.
- **Safari Zone:** Has a time limit. When it expires, the player is warped back to the Safari Zone Gate.
- **Gym Battle Loss:** Losing a battle inside a gym does NOT warp you to a Pokémon Center.
- **Run from Battle Mechanic:** Attempting to switch Pokémon from the party screen can sometimes result in running from the battle instead.
- **FLY in battle:** The move FLY can be used to defeat a wild Pokémon and end the battle, even when indoors. This acts as an escape method.
- **FLY in field:** Cannot be used indoors to escape a building.
- **ROAR in battle:** Can end a wild battle by forcing the player's Pokémon to run away.
- **Item Use on Fainted Pokemon:** A FULL RESTORE will not work on a fainted Pokémon.
- **Weird Typing:** My LAPRAS (NEPTUNE) was displayed as a GHOST type in battle. This needs further investigation.
- **'No Will to Fight':** After a Pokémon faints, attempting to switch in the next Pokémon can sometimes fail with the message 'There's no will to fight!'.
- **THUNDERBOLT vs. DIG:** THUNDERBOLT can hit an opponent while it is underground using DIG.

# III. Active Puzzles
- **Pokemon Mansion - Trapped Room Escape:**
  - **Goal:** Escape the isolated room on Pokemon Mansion 2F.
  - **Conclusion:** All conventional hypotheses have failed. The 'blackout' theory is definitively disproven, as the game actively prevents losing battles in this area.
  - **New Hypothesis:** There is a hidden passage through one of the surrounding walls.
  - **Immediate Plan:** Systematically test every single wall tile bordering the platform for a hidden passage, starting with the southern wall.

# IV. Solved & Failed Puzzles

- **Pokemon Mansion B1F - Western Exploration (Failed - Attempt 1):**
    - **Hypothesis:** The solution to opening the eastern gates lies within the unexplored western section of the B1F floor.
    - **Test:** Attempted to pathfind to the western section.
    - **Outcome:** Pathfinding failed; the area is physically disconnected from the eastern section.
    - **Conclusion:** The western and eastern sections of B1F are separate. The solution is not in the west.
- **Pokemon Mansion B1F - Gate Switch Puzzle (Solved):** The switch at (19, 26) opens the northern and western gates, but not the eastern ones.
- **Pokemon Mansion - Trapped Corridor (Solved):** The eastern corridor of 1F is an intentional trap. Escaped via a one-way warp at the southern end that activates after being trapped.
- **Diary Interaction:** Diaries must be interacted with from the side, not from below.
  - **Observation (Trapped Room):** Fell from 3F into an inescapable room on 2F at (19, 15). No visible exits.
  - **Hypothesis 1 (Agent):** The platform has a hidden trigger.
    - **Test:** Walked over every tile of the L-shaped platform at (19-22, 15-16).
    - **Outcome:** No triggers activated.
    - **Conclusion:** Hypothesis is incorrect.
  - **Hypothesis 2 (Agent):** There is a hidden passage through the eastern wall.
    - **Test:** Attempted to walk east from (22, 15) into the wall at (23, 15).
    - **Outcome:** Movement was blocked.
    - **Conclusion:** Hypothesis is incorrect.
  - **Hypothesis 3 (Agent):** The room is an intentional trap, and the only escape is to 'black out' by fainting.
    - **Test (Attempt 1):** Triggered a wild encounter and let one Pokémon faint, then declined to send another.
    - **Outcome:** Ran from the battle ("Got away safely!"). Was not warped out of the room.
    - **Conclusion:** This specific method of losing a battle does not solve the puzzle.
    - **Test (Attempt 2):** Triggered a wild encounter. Attempted to have REVENANT faint by using the non-damaging move FOCUS ENERGY.
    - **Outcome (Failed - 4 attempts):** FOCUS ENERGY failed repeatedly, and the opponent RATTATA did not attack, resulting in a battle stalemate.
    - **Conclusion:** Using non-damaging moves to facilitate a loss is not working in this specific encounter. A new strategy is required.
    - **Test (Attempt 3 - REVISED):** Triggered another wild encounter (Grimer). Attempted to lose by having REVENANT use a non-damaging move (FOCUS ENERGY), which eventually led to it fainting. Then, sent out last Pokémon, CRAG.
    - **Test (Attempt 4):** Used weak attacking moves (BODY SLAM, STRENGTH) with CRAG to try and facilitate a loss.
    - **Outcome (Failed):** The move STRENGTH knocked out the opponent GRIMER. The battle was won, not lost.
    - **Conclusion:** The 'blackout' hypothesis remains untested. Wild Pokémon in this room appear to be unusually passive or weak, making it difficult to intentionally lose. The strategy of using weak attacks has also failed. I will try to trigger one more wild encounter to test the blackout theory. If that fails, I will abandon this hypothesis.
- **Weird Typing:** My LAPRAS (NEPTUNE) was displayed as a GHOST type in battle. This needs further investigation.