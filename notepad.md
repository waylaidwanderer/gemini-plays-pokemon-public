# I. Battle Intel

## A. Type Effectiveness Chart (Verified)
- **Super Effective (2x):** Psychic > Ghost, Poison; Ghost > Psychic; Electric > Rock, Water; Flying > Grass, Poison, Fighting; Ice > Ground, Grass, Flying, Dragon; Ground > Poison, Fire, Electric, Rock; Rock > Fire, Ice, Flying, Bug; Fighting > Normal, Rock, Ice; Water > Fire, Ground, Rock; Grass > Water, Ground, Rock; Bug > Grass, Poison, Psychic; Poison > Grass, Bug.
- **Not Very Effective (0.5x):** Normal !> Rock; Electric !> Grass, Electric, Dragon; Rock !> Ground, Fighting; Psychic !> Psychic; Poison !> Poison, Ground, Rock, Ghost; Ice !> Water, Ice, Fire; Fighting !> Poison, Flying, Psychic, Bug; Water !> Water, Grass, Dragon; Grass !> Fire, Grass, Poison, Flying, Bug, Dragon.
- **Immune (0x):** Flying immune to Ground; Ground immune to Electric; Ghost immune to Normal, Fighting.

## B. Trainer Rosters & Movesets
### Giovanni (Viridian Gym)
- **Dugtrio (Lv53):** Knows Rock Slide, Earthquake, Fissure, Slash.
- **Nidoqueen (Lv54):** Knows Body Slam, Earthquake, Thunderbolt, Ice Beam.
- **Nidoking (Lv54):** Knows Blizzard, Earthquake, Thunderbolt, Ice Beam.
- **Persian (Lv55):** Knows Bubblebeam, Slash, Hyper Beam, Thunderbolt.

# II. Game Mechanics & Tile Types
- `ground`: Standard walkable tile.
- `impassable`: Walls, objects, cannot be traversed.
- `cuttable`: Tree that can be cut with HM Cut.
- `ledge`: One-way traversal. Can be jumped down (from Y-1 to Y+2 in one step), but not climbed up.
- `spinner_up`, `spinner_down`, `spinner_left`, `spinner_right`: Forces movement in the specified direction.
- `spinner_stop`: Stops movement from a spinner tile.
- `grass`: Tall grass where wild Pokémon can be encountered.
- `warp`: Teleportation tile that moves the player to a new location, often on a different map.

# III. Strategic Plans

## A. Plan to Defeat Giovanni
1.  **Analyze Roster:** Use the `team_composition_advisor_agent` to get an optimal team recommendation based on my entire Pokémon roster and Giovanni's known team.
2.  **Assemble Team:** Go to the Pokémon Center PC and withdraw the recommended Pokémon.
3.  **Navigate Gym:** Find the path to Giovanni at (3, 2).
4.  **Battle Strategy:** In battle, use the `battle_strategist_agent` for turn-by-turn advice, leveraging the known weaknesses and movesets.

## B. Plan to Train for Giovanni
1.  **Level Goal:** Train the entire party (REVENANT, CRAG, NEPTUNE, LEGION, TITANESS) to the level cap of 55.
2.  **Location Scouting:** My current assumption is that Route 22 is the best training spot. I must verify this.
    - **Hypothesis:** Other high-level areas may offer better EXP per battle.
    - **Test:** Battle several wild Pokémon on Route 22 and note the average EXP gain. Then, Fly to other potential locations (e.g., Route 15, Seafoam Islands) and repeat the process.
    - **Conclusion:** Determine the most time-efficient location and focus training efforts there.

### C. Training Location Analysis
- **Route 15:** Tested wild encounters. Found Level 30 Weepinbell and Level 26 Bellsprout. EXP gain is too low for current party level. **Conclusion: Inefficient training spot.**