## I. Game Mechanics & Battle Intel

### A. Tile Mechanics & Traversal Rules
- **Ground/Impassable:** `ground` tiles are walkable, `impassable` tiles are solid walls. All objects (NPCs, items, signs) function as impassable walls.
- **Water:** Surfable tiles. To initiate SURF, I must be adjacent to a water tile and use the move from the party menu. Only Water-type Pokémon can use SURF in the field.
- **Gates (`closed_gate`/`open_gate`):** `closed_gate` tiles are usually impassable barriers. `open_gate` tiles are previously closed gates that are now open and act as `ground`. The state of these can be toggled by switches or other triggers.
- **Ledges:** One-way only. Can be jumped down (from Y-1 to Y+2 in one move), but are impassable from below (Y+1) and from the sides (X-1, X+1).
- **Spinner Tiles:** Force movement in a specific direction. Destinations must be mapped manually.
- **Hole Tiles:** Warp tiles that lead to a lower map area. Often function as one-way drops.

### B. Confirmed ROM Hack Changes
#### B1. Type Matchups & Immunities
- **Super Effective:** Psychic > Ghost/Poison; Ghost > Psychic; Electric > Rock/Water; CUT (Normal) > VICTREEBEL (Grass/Poison); Flying > Grass/Poison; **Psychic > Flying** (confirmed: KADABRA's PSYBEAM vs ECHO's GOLBAT)
- **Not Very Effective:** Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic; Bite (Normal) !> HAUNTER (Ghost/Poison); **Ice !> Gyarados (Water/Flying)** (confirmed: NEPTUNE's AURORA BEAM vs Fisherman's GYARADOS); Poison !> Poison (confirmed: ECHO's SLUDGE vs MUK).
- **Immunities:** Flying-type immune to Ground-type moves; MUK immune to Poison-type moves; **Electric is effective vs Sabrina's Psychic team, confirming Psychic types are NOT immune to Electric.**; **HYPNO immune to STUN SPORE** (powder moves); **MUK immune to THUNDER WAVE** (Electric-type status move).

#### B2. Battle & Field Mechanics
- **Evasion:** PSYWAVE and CONFUSE RAY can fail against targets with high evasion boosts (e.g., from MINIMIZE).
- **'No Will to Fight':** A fainted or sleeping Pokémon cannot be switched into battle.
- **EXP Distribution:** Experience is shared between the Pokémon that started the battle and any that participated via switch-in.
- **Safari Zone:** Has a time limit. When it expires, the player is warped back to the Safari Zone Gate.
- **Gym Battle Loss:** Losing a battle inside a gym does NOT warp you to a Pokémon Center. You respawn in front of the trainer you lost to.
- **Two-Turn Moves:** The `battle_strategist_agent` initially failed to account for the inefficiency of two-turn moves (like FLY) when a one-turn KO is possible. The agent has been refined to prioritize faster knockouts.

## II. Puzzle & Hypothesis Log

### A. Active Hypotheses
- **Pokemon Mansion 1F 'Reachable Barrier' Contradiction:** The game's source of truth insists multiple closed gates are 'Reachable Barriers', but they appear impassable. All standard interaction attempts have failed. The puzzle_solver_agent has identified this contradiction as the key.
  - **Agent Hypothesis (Attempt #1 - Failed):** A non-standard game mechanic allows passage through barriers marked as 'reachable'.
          - **Test (Failed):** Walk south through gate at (27, 28).
          - **Test (Failed):** Walk south through gate at (28, 28).
        - **Agent Hypothesis (Attempt #2 - Failed):** Gates can be opened by direct interaction.
          - **Test (Failed):** Interact with gate at (27, 28).
          - **Test (Failed):** Interact with gate at (28, 28).
        - **Agent Hypothesis (Attempt #3):** A hidden, non-obvious switch is nearby and must be activated to open the gates.
          - **Test:** Search the area around the player for a hidden mechanism.
          - **Test (Failed):** Walk south through gate at (28, 28).
        - **Agent Hypothesis (Attempt #2 - Failed):** Gates can be opened by direct interaction.
          - **Test (Failed):** Interact with gate at (27, 28).
          - **Test (Failed):** Interact with gate at (28, 28).
        - **Agent Hypothesis (Attempt #3):** A hidden, non-obvious switch is nearby and must be activated to open the gates.
          - **Test:** Search the area around the player for a hidden mechanism.

### B. Solved Puzzles
- **Pokemon Mansion B1F Dynamic Gates (Solved):** The switch at (19, 26) toggles which set of gates (Western, Northern, or Eastern) is affected by a dynamic trigger.

### C. Deprecated Hypotheses (Pokemon Mansion 1F)
- **Multi-Floor Pathing:** Hypothesized path to the east was on another floor. **Invalidated by 'Reachable Barriers' notification.**
- **Direct Gate Interaction:** Hypothesized gates could be opened by direct interaction ('A' button). **Failed.**
- **Hidden Item:** Hypothesized a hidden item was needed. **ITEMFINDER found nothing.**
- **Walk-Through Gates (General):** Hypothesized that 'reachable' closed gates could be walked through. **Failed.** This was based on the agent's initial identification of a contradiction. Re-testing with a more specific target is the current active hypothesis. This was based on the agent's initial identification of a contradiction. Re-testing with a more specific target is the current active hypothesis.