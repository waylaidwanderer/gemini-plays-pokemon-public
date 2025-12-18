# Johto Journey: Gem's Log

## Tile Mechanics
- FLOOR: Traversable. Verified.
- WALL: Impassable. Verified.
- TALL_GRASS: Traversable; triggers wild encounters. Verified.
- LEDGE_HOP_DOWN: One-way jump South. Impassable from the South. Verified on Route 29 (50, 10) and Route 30 (7, 17).
- COUNTER: Impassable. Face to interact with NPC behind. Verified.
- TREE / HEDGE: Impassable. Verified on Route 30.
- WARP_CARPET_DOWN: Exit map South. Verified.
- LADDER / DOOR: Triggers warp. Verified.
- PC: Face to use. Verified.
- LEDGE_HOP_LEFT: One-way jump West. Impassable from the West.
- WATER: Impassable without HM. Verified in Dark Cave.
- FLOOR_UP_WALL: Collision type for walls that look like they are "above" the floor. Impassable.
- ROCK: Impassable object. Verified in Dark Cave.

## Strategic Plan: Defeat Falkner (Violet City)
- **HOW:** 
  1. Catch Geodude in Dark Cave (Route 31). DONE.
  2. Catch Bellsprout on Route 31; trade in Violet City for ONIX.
  3. Train Calcifer to Lv10 (Ember) and Icarus to Lv10 (Gust). Icarus is DONE. Calcifer needs training.
  4. Use Ember to sweep Sprout Tower (Flash HM).
  5. Use Rock-types (Geodude/Onix) to counter Falkner's Flying moves.

## Completed Areas
- **Route 30:** Defeated Joey, Mikey, Don. Path to Route 31 is clear.
- **Route 31:** Caught GNEISS (Geodude) in Dark Cave. Defeated Wade.
- **Violet City:** Arrived and healed at Pokecenter.

## Battle and Pokemon Information
### Observed Movesets
- Rattata: Tackle, Tail Whip
- Pidgey: Tackle, Sand-Attack, Gust
- Cyndaquil: Tackle, Leer, Smokescreen
- Caterpie: Tackle (Verified).
- Geodude: Tackle (Verified).
- Bellsprout: Vine Whip (Verified).
- Poliwag: Bubble (Verified).
- Weedle: Poison Sting (Verified).
### Type Effectiveness (Verified)
- Flying vs Bug: Super Effective. (Verified with Gust vs Caterpie).
- Normal vs Rock: Not very effective. (Verified with Tackle vs Geodude).
- Grass (Vine Whip) vs Flying: Not very effective. (Verified).
- Water vs Rock/Ground: Super Effective (4x). (Verified with Poliwag vs Gneiss).

## NPC Archive
- New Bark: ELM (Starter), OFFICER (Rival), MOM (Savings).
- MR. POKEMON: MR. POKÉMON (Egg), OAK (Pokedex).
- Cherrygrove: GRAMPS (Map Card), NURSE JOY (Heal), CLERK (Mart).
- Violet City: LASS at (27, 28) (Sprout Tower info), KYLE (Youngster) at (6, 6) in house at (21, 29) (Wants Bellsprout for ONIX), Pokefan M at (2, 3) (Traded Pokemon info).

## Lessons Learned
- **Object Collision:** All sprites (NPCs, items) are walls. Interact from an adjacent tile.
- **Pathfinding:** Always use the latest version of custom tools (e.g., `find_path_v3`).
- **Battle Strategy:** Use `battle_strategist_v2` for trainer battles.
- **Ledge Logic:** Ledges are one-way (South/Down).
- **Critical Hits:** Be extremely cautious when weakening Pokemon for capture; crits can ruin an encounter. Lead with a weaker Pokemon if possible.

## Strategy for Bellsprout
- Location: Route 31 Tall Grass.
- Method: Walk around in grass until encounter.
- Team: Lead with GNEISS (Geodude). Calcifer's Tackle is too strong (crits kill).
- Catching: Use Poké Ball.
- Goal: Trade for ONIX with KYLE in Violet City.
- **Type Weakness (Wild Battles):** Even low-level wild Pokémon can be dangerous if they have a 4x type advantage (e.g., Water vs Rock/Ground). Switch or run immediately.
- **Capture Safety:** When weakening Pokémon for capture, use the weakest available moves or status moves. Avoid high-damage moves that could KO on a mistake.
- Wade (BUG CATCHER): Route 31 (17, 13). Roster: Caterpie (Lv2), Caterpie (Lv2), Weedle (Lv3).

## Area Mechanics: Sprout Tower
- Ghosts: Immune to Normal-type moves. (Verified by Lass in Violet City).
- Strategy: Use Calcifer's Ember (Fire) to defeat ghosts.