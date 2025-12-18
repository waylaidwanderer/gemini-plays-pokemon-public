# Johto Journey: Gem's Log

## Tile Mechanics
- FLOOR: Traversable. Verified on Route 31.
- WALL: Impassable. Verified.
- TALL_GRASS: Traversable; triggers wild encounters. Verified on Route 31.
- LEDGE_HOP_DOWN: One-way jump South. Impassable from the South. Verified on Route 29 (50, 10), Route 30 (7, 17), and Route 31 (6, 9).
- LEDGE_HOP_RIGHT: One-way jump East. Impassable from the East. Verified on Route 31 (13, 6).
- LEDGE_HOP_LEFT: One-way jump West. Impassable from the West.
- COUNTER: Impassable. Face to interact with NPC behind. Verified.
- HEADBUTT_TREE: Impassable. Verified on Route 31.
- CUT_TREE: Impassable. Verified on Route 30.
- WARP_CARPET_DOWN: Exit map South. Verified.
- WARP_CARPET_LEFT: Exit map West. Verified on Route 31 (4, 6).
- LADDER / DOOR / CAVE: Triggers warp. Verified.
- PC: Face to use. Verified.
- WATER: Impassable without HM. Verified in Dark Cave.
- FLOOR_UP_WALL: Collision type for walls that look like they are "above" the floor. Impassable.
- ROCK: Impassable object. Verified in Dark Cave.

## Strategic Plan: Defeat Falkner (Violet City)
- **HOW:** 
  1. Traded Kudzu (Bellsprout) for Rocky (Onix) with KYLE in Violet City. Ready to train for Gym.
  2. Train Calcifer to Lv10 (Ember).
  3. Use Ember to sweep Sprout Tower (Flash HM).
  4. Use Rock-types (Geodude/Onix) to counter Falkner's Flying moves.

## Completed Areas
- **Route 30:** Defeated Joey, Mikey, Don. Path to Route 31 is clear.
- **Route 31:** Caught GNEISS (Geodude) in Dark Cave. Defeated Wade. Bellsprout caught.
- **Violet City:** Arrived and healed at Pokecenter. Located Kyle (Onix Trader).

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
- Violet City: LASS at (27, 28) (Sprout Tower info), KYLE (Youngster) at (6, 6) in house at (21, 29) (Wants Bellsprout for ONIX), Pokefan M at (2, 3) (Traded Pokemon info).

## Lessons Learned
- **Object Collision:** All sprites (NPCs, items) are walls. Interact from an adjacent tile.
- **Pathfinding:** Always use the latest version of custom tools (e.g., `find_path_v3`).
- **Battle Strategy:** Use `battle_strategist_v2` for trainer battles.
- **Ledge Logic:** Ledges are one-way (South, East, West).
- **Critical Hits:** Be extremely cautious when weakening Pokemon for capture; crits can ruin an encounter. Lead with a weaker Pokemon if possible.
- **Capture Strategy:** Get HP to yellow/red. Use status moves (Sleep, Paralysis) if available. Use Smokescreen to stay safe while weakening.

## Strategy for Bellsprout
- Location: Route 31 Tall Grass (8, 11).
- Method: Walk around in grass until encounter.
- Team: Lead with Calcifer (Cyndaquil). Use Smokescreen to reduce accuracy and Tackle to weaken. Avoid Ember and Gust (OHKO risk). Do NOT lead with Gneiss (4x weak to Vine Whip).
- Catching: Use Poké Ball.
- Goal: Trade for ONIX with KYLE in Violet City.
- **Type Weakness (Wild Battles):** Even low-level wild Pokémon can be dangerous if they have a 4x type advantage (e.g., Water vs Rock/Ground). Switch or run immediately.
- **Capture Safety:** When weakening Pokémon for capture, use the weakest available moves or status moves. Avoid high-damage moves that could KO on a mistake.
- Wade (BUG CATCHER): Route 31 (17, 13). Roster: Caterpie (Lv2), Caterpie (Lv2), Weedle (Lv3).

## Area Mechanics: Sprout Tower
- Ghosts: Immune to Normal-type moves. (Verified by Lass in Violet City).
- Strategy: Use Calcifer's Ember (Fire) to defeat ghosts.
- INCENSE_BURNER: Impassable decorative object.
- BOOKSHELF: Impassable object; can be interacted with to read titles.
- RADIO: Impassable object; can be interacted with to listen to broadcasts.