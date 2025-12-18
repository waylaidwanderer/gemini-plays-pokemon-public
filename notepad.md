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
- Violet City: LASS at (27, 28) (Sprout Tower info), KYLE (Youngster) at (6, 4) in house at (21, 29) (Traded Bellsprout for ONIX), Pokefan M at (2, 3) (Traded Pokemon info).
- Sprout Tower: GRANNY found in tower; Sage at (7, 4) confirmed HM is at the top; Sage at (3, 5) is a Trainer; Sage at (7, 7) is a moving NPC.

## Lessons Learned
- **Object Collision:** All sprites (NPCs, items) are walls. Interact from an adjacent tile.
- **Pathfinding:** Always use the latest version of custom tools (e.g., `find_path_v3`).
- **Battle Strategy:** Use `battle_strategist_v2` for trainer battles.
- **Ledge Logic:** Ledges are one-way (South, East, West).
- **Critical Hits:** Be extremely cautious when weakening Pokemon for capture; crits can ruin an encounter. Lead with a weaker Pokemon if possible.
- **Capture Strategy:** Get HP to yellow/red. Use status moves (Sleep, Paralysis) if available. Use Smokescreen to stay safe while weakening.
- **Type Weakness (Wild Battles):** Even low-level wild Pokémon can be dangerous if they have a 4x type advantage (e.g., Water vs Rock/Ground). Switch or run immediately.
- **Capture Safety:** When weakening Pokémon for capture, use the weakest available moves or status moves. Avoid high-damage moves that could KO on a mistake.
- Wade (BUG CATCHER): Route 31 (17, 13). Roster: Caterpie (Lv2), Caterpie (Lv2), Weedle (Lv3).

## Area Mechanics: Sprout Tower
- Ghosts: Immune to Normal-type moves. (Verified by Lass in Violet City).
- Strategy: Use Calcifer's Ember (Fire) to defeat ghosts.
- Training: Sprout Tower is a good place to train Calcifer to Lv12 for Ember (Cyndaquil learns Ember at Lv12 in Crystal). Onix (Rocky) and Geodude (Gneiss) will also gain EXP.
- Navigation: WARP_CARPET_DOWN at (9, 15) and (10, 15) leads to Violet City (23, 5).
- Objects: STATUE and SPROUT_TOWER_STATUE are impassable.

## Timestamps
- Started Academy visit Turn 1167.
- Met Earl (Spinning Master) Turn 1210.
- Entered Sprout Tower Turn 1213.

## Sprout Tower Exploration
- Sprout Tower 2F entered Turn 1240.
- The central pillar is a giant Bellsprout, causing the tower to shake.
- HM Flash is at the top of the tower.