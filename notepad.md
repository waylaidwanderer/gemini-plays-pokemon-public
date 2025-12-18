# Johto Journey: Gem's Log

## Tile Mechanics
- FLOOR: Traversable. Verified on Route 31 and Sprout Tower.
- WALL: Impassable. Verified.
- TALL_GRASS: Traversable; triggers wild encounters. Verified on Route 31.
- LEDGE_HOP_DOWN: One-way jump South. Impassable from the South. Verified on Route 29 (50, 10), Route 30 (7, 17), and Route 31 (6, 9).
- LEDGE_HOP_RIGHT: One-way jump East. Impassable from the East. Verified on Route 31 (13, 6).
- LEDGE_HOP_LEFT: One-way jump West. Impassable from the West. Predicted; not yet verified.
- COUNTER: Impassable. Face to interact with NPC behind. Verified.
- HEADBUTT_TREE: Impassable. Verified on Route 31.
- CUT_TREE: Impassable. Verified on Route 30.
- WARP_CARPET_DOWN: Exit map South. Verified.
- WARP_CARPET_LEFT: Exit map West. Verified on Route 31 (4, 6).
- LADDER / DOOR / CAVE: Triggers warp. Verified.
- PC: Face to use. Verified.
- WATER: Impassable without HM. Verified in Dark Cave.
- FLOOR_UP_WALL: Collision type for walls that look like they are "above" the floor. Impassable. Verified in Sprout Tower.
- ROCK: Impassable object. Verified in Dark Cave.
- INCENSE_BURNER: Impassable decorative object. Verified in VioletKylesHouse.
- BOOKSHELF: Impassable object; can be interacted with to read titles. Verified in VioletKylesHouse.
- RADIO: Impassable object; can be interacted with to listen to broadcasts. Verified in VioletKylesHouse.

## Primary Goal Strategy: Defeat Falkner (Violet City)
- **Team Composition:**
  - Calcifer (Cyndaquil): Target Lv12 for Ember to handle Sprout Tower and potentially Falkner's Pidgey.
  - ROCKY (Onix) & GNEISS (Geodude): Primary counters for Falkner's Flying-type Pokémon. Normal-type moves like Tackle are "Not very effective" against them.
- **Plan:**
  1. Complete Sprout Tower to obtain HM05 Flash and train the team.
  2. Ensure Rocky and Gneiss are healthy for the Gym battle.
  3. Use Rock-types to soak up Normal/Flying hits and chip away at Falkner's team.

## Completed Areas
- **Route 30:** Defeated Joey, Mikey, Don. Path to Route 31 is clear.
- **Route 31:** Caught GNEISS (Geodude) in Dark Cave. Defeated Wade. Bellsprout caught.
- **Violet City:** Arrived and healed at Pokecenter. Traded Kudzu (Bellsprout) for Rocky (Onix) with Kyle.

## Battle and Pokemon Information
### Observed Movesets
- Rattata: Tackle, Tail Whip
- Pidgey: Tackle, Sand-Attack, Gust
- Cyndaquil: Tackle, Leer, Smokescreen
- Caterpie: Tackle (Verified).
- Geodude: Tackle (Verified).
- Bellsprout: Vine Whip (Verified).
- Poliwag: Bubble (Verified on Route 31).
- Hoothoot: Growl, Tackle? (Verified on Route 31).
- Weedle: Poison Sting (Verified).
### Type Effectiveness (Verified)
- Flying vs Bug: Super Effective. (Verified with Gust vs Caterpie).
- Normal vs Rock: Not very effective. (Verified with Tackle vs Geodude).
- Grass (Vine Whip) vs Flying: Not very effective. (Verified).
- Water vs Rock/Ground: Super Effective (4x). (Verified with Poliwag vs Gneiss).
- Fire (Ember) vs Grass: Super Effective (Predicted).

## NPC Archive
- New Bark: ELM (Starter), OFFICER (Rival), MOM (Savings).
- MR. POKEMON: MR. POKÉMON (Egg), OAK (Pokedex).
- Cherrygrove: GRAMPS (Map Card), NURSE JOY (Heal), CLERK (Mart).
- Violet City: LASS at (27, 28) (Sprout Tower info), KYLE (Youngster) at (6, 4) in house at (21, 29) (Traded Bellsprout for ONIX), Pokefan M at (2, 3) (Traded Pokemon info), EARL (Spinning Master) at (25, 14).
- Sprout Tower: GRANNY found in tower; Sage at (7, 4) confirmed HM is at top; Sage (Trainer) Chow at (3, 1); Sage at (6, 7) (moving); Teacher at (9, 9); Sage (Trainer) Edmond at (9, 14).

## Lessons Learned
- **Object Collision:** All sprites (NPCs, items) are walls. Interact from adjacent tile.
- **Pathfinding:** Use latest version of custom tools (`find_path_v3`).
- **Battle Strategy:** Use `battle_strategist_v2` for trainer battles.
- **Ledge Logic:** Ledges are one-way (South, East, West).
- **Critical Hits:** Be extremely cautious when weakening Pokemon for capture.
- **Capture Strategy:** Get HP to yellow/red. Use status moves. Use Smokescreen to stay safe.
- **Type Weakness (Wild Battles):** Even low-level wild Pokémon can be dangerous with 4x advantage.
- **Capture Safety:** Use weakest moves or status moves to avoid accidental KO.
- Wade (BUG CATCHER): Route 31 (17, 13). Roster: Caterpie (Lv2), Caterpie (Lv2), Weedle (Lv3).
- **Level Requirements:** Cyndaquil learns Ember at Lv12 in Pokémon Crystal.
- **Battle Menus:** Selecting NO when asked to change Pokémon is faster if the current one is fine.
- **Tool Hygiene:** Always provide full moveset data to `battle_strategist_v2`.

## Area Mechanics: Sprout Tower
- Ghosts: Immune to Normal-type moves. (Verified by Lass in Violet City).
- Strategy: Use Calcifer's Ember (Fire) to defeat ghosts.
- Training: Target Lv12 for Calcifer (Ember).
- Navigation: WARP_CARPET_DOWN at (9, 15) and (10, 15) leads to Violet City (23, 5).
- Objects: STATUE and SPROUT_TOWER_STATUE are impassable.
- The central pillar is a giant Bellsprout, causing the tower to shake.
- HM Flash is at the top of the tower.

## Timestamps
- Started Academy visit Turn 1167.
- Entered Sprout Tower Turn 1213.

## Sprout Tower 2F (Turn 1311)
- Arrived via ladder at (2, 6) from 1F.
- Goal: Find ladder to 3F.
- Calcifer (Cyndaquil) needs ~244 more EXP for Lv12 (Ember).
- Exploring reachable unseen tiles to map the floor.
- Sage at (9, 14) on 2F.