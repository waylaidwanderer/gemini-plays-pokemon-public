# I. Meta-Progression & Lessons Learned

- **Dead End Area Mismatch (Seafoam B3F):** My previous assertion that Seafoam Islands B3F was a dead end was incorrect. The system reported 4 reachable exits. This was a critical hallucination. **Correction:** I must re-evaluate my understanding of B3F's layout and trust system feedback over my visual interpretation of the map. (Self-correction from Turn 170981).
- **Notepad and Map Marker Update Priority (Turn 171001):** I attempted multiple `define_map_marker` and `find_path` calls before executing a planned `notepad_edit` overwrite. This is a direct violation of the core directive that notepad updates are the highest priority and must be performed immediately. **Correction:** All notepad updates must be performed immediately, prior to any other actions.
- **Fly Menu Navigation Failure (Turn 171342-171352):** I repeatedly overshot the target Pokémon in the party menu and then manually scrolled through the Fly menu. **Correction:** I must use the `fly_menu_navigator` tool as intended and trust its output. The `get_next_pokemon_press` tool was deleted to make space for `fly_menu_navigator` and should not have been used. This also highlights a failure to immediately use a newly defined tool.
- **Deferred Map Marker Creation (Turns 172822, 172872, 172881):** I cut trees but deferred defining map markers for them until a later turn (172829, 172877, 172882). **Correction:** Map markers must be defined immediately on the same turn the event occurs.
- **Repeated `find_path` Calls without Re-evaluation (Turns 172922-172929):** I repeatedly called `find_path` to the same target after it failed without adapting my strategy or re-evaluating the cause of failure. **Correction:** When a tool's output is unexpected, I must immediately adapt my strategy and re-evaluate the underlying cause of the failure.
- **Tool Refinement Failure (Turns 174066-174090, 174151-174157):** I repeatedly used manual navigation or retried a faulty tool after it failed, instead of fixing it immediately. This is a critical violation of my core directives. **Correction:** Faulty tools must be fixed immediately before any other gameplay action.

# II. Game & World Knowledge

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

## B. Field Mechanics
- **Linked Boulder Rotation:** Some water-based boulders rotate in a linked fashion.
- **Hidden Passages:** Impassable-looking walls can sometimes be walked through.
- **Strength Mechanics:** Does not need to be reactivated per push. Player position can change depending on push direction.
- **HM Field Move Usage:** Requires two 'A' presses (prompt + confirmation).

## C. Tile Mechanics Glossary
- **ground:** Standard traversable tile.
- **impassable:** Wall or obstacle. Cannot be entered.
- **cuttable:** Tree that can be cut. Becomes ground after cutting.
- **ledge:** Can be jumped down, but not up. Treat as impassable from below or sides.
- **grass:** Tall grass with wild encounters.
- **water:** Requires Surf to cross.
- **steps:** Allows movement between different elevations (ground and elevated_ground).
- **elevated_ground:** Walkable ground at a higher elevation, accessible only via steps.
- **boulder_switch:** A floor switch activated by a boulder.
- **boulder_barrier:** A barrier that is removed when a corresponding boulder_switch is activated.
- **cleared_boulder_barrier:** A former barrier, now walkable ground.
- **spinner_up/down/left/right:** Tiles that force movement in a specific direction.
- **ladder_up/down:** Warps that lead to a different floor.
- **hole:** A warp tile that drops the player to the floor below.
- **teleport:** An instant warp tile within the same logical location (e.g., inside a building).
- **closed_gate:** An impassable gate.
- **open_gate:** A previously closed gate that is now open and acts as ground.
- **gate_offscreen:** A gate whose state is unknown. Treated as potentially open for pathfinding.
- **Defeated Trainer Obstacle:** In some areas (e.g., Viridian Gym, Victory Road), defeated trainers become impassable obstacles.

## D. Key Event & Puzzle Log

### 1. Major Events (Post-Champion)
- **Route 24 Cave:** Remains blocked after becoming Champion.
- **Silph Co. Elevator (SOLVED):** After selecting a floor, must step on the warp pads to travel.
- **Cerulean City Post-Champion Events:** Misty rematch is triggered after solving the Trashed House backyard puzzle. Battle loop is broken by selecting 'NO' to the rematch prompt.

### 2. Seafoam Islands Puzzle Log
- **Main Obstacle:** Strong water current on B4F blocked progress, solved by a boulder puzzle on B3F.
- **B4F Linked Boulder Rotation:** Boulders at (5, 16) and (6, 16) are part of a linked rotation puzzle to change water flow.

## E. Opponent Information
- **Elite Four Lorelei:** Slowbro (Earthquake), Jynx (Bubblebeam), Gengar (Lv 59), Cloyster (Lv 55, Explosion).
- **Elite Four Bruno:** Hitmonchan (Ice Punch, Thunder Punch), Onix (Explosion), Machamp (Earthquake).
- **Elite Four Agatha:** Gengar (Hypnosis, Dream Eater).
- **Elite Four Lance:** Dragonite (Lv 61, Slam, Thunder Wave, Wrap, Hyper Beam), Gyarados (Slam), Aerodactyl (Earthquake), Charizard (Earthquake, Flamethrower).
- **Misty (Rematch):** Seadra (Lv 64), Golduck (Lv 65, Psychic, Blizzard), Lapras (Lv 64, Hydro Pump, Thunder, Psychic, Blizzard), Vaporeon (Acid Armor), Starmie (Thunderbolt).
- **Kris (Seafoam Islands):** Snorlax (Earthquake, Body Slam, REST), Gengar (Hypnosis, Dream Eater).
- **Craig (Power Plant):** JOLTEON (Lv 55, DIG, THUNDERBOLT, PIN MISSILE, THUNDER WAVE), AERODACTYL (Lv 55, ROCK SLIDE), EXEGGUTOR (Lv 55, MEGA DRAIN, PSYCHIC), SNORLAX (Lv 55, AMNESIA, EARTHQUAKE, BODY SLAM, REST), CLOYSTER (Lv 55, EXPLOSION), ARCANINE (Lv 55, FURBALL).

## F. Wild Legendary Encounters
- **Articuno (Seafoam Islands, Lv 50):** Captured.
- **Zapdos (Power Plant, Lv 50):** AGILITY, THUNDERBOLT. (Fainted accidentally).
- **Craig (Power Plant):** Full team is JOLTEON, AERODACTYL, EXEGGUTOR, SNORLAX, CLOYSTER, ARCANINE.
- **Untested Assumption:** The Snorlax on Route 12 might be movable with the POKé FLUTE. **Test:** After exiting Rock Tunnel, fly to Lavender Town and attempt to use the POKé FLUTE on the Snorlax.