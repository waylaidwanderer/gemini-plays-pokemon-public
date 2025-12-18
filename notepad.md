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
  3. Train Calcifer to Lv10 (Ember) and Icarus to Lv10 (Gust). DONE.
  4. Use Ember to sweep Sprout Tower (Flash HM).
  5. Use Rock-types (Geodude/Onix) to counter Falkner's Flying moves.

## Current Area: Route 31
- **Objectives:**
  - Reach Violet City and heal. (Current Focus)
  - Locate and catch Bellsprout in tall grass (Start Turn: 959). (Paused for healing)

## Completed Areas
- **Route 30:** Defeated Joey, Mikey, Don. Path to Route 31 is clear.
- **Route 31:** Caught GNEISS (Geodude) in Dark Cave.

## Battle and Pokemon Information
### Observed Movesets
- Rattata: Tackle, Tail Whip
- Pidgey: Tackle, Sand-Attack, Gust
- Cyndaquil: Tackle, Leer, Smokescreen
- Caterpie: Tackle (Verified).
- Geodude: Tackle (Verified).
- Bellsprout: Vine Whip (Verified).
- Poliwag: Bubble (Verified).
- Weedle: Poison Sting (Predicted).
### Team Status
- Calcifer (CYNDAQUIL): Lv8 (13/25 HP). Needs 14 XP for Lv9 (Growth: Medium Slow).
- ICARUS (PIDGEY): Lv10 (17/30 HP). Needs 173 XP for Lv11 (Growth: Medium Slow).
- GNEISS (GEODUDE): Lv4 (0/18 HP, Fainted).
### Type Effectiveness (Verified)
- Flying vs Bug: Super Effective. (Verified with Gust vs Caterpie).
- Normal vs Rock: Not very effective. (Verified with Tackle vs Geodude).
- Grass (Vine Whip) vs Flying: Not very effective. (Verified).
- Water vs Rock/Ground: Super Effective (4x). (Verified with Poliwag vs Gneiss).

## NPC Archive
- New Bark: ELM (Starter), OFFICER (Rival), MOM (Savings).
- MR. POKEMON: MR. POKÉMON (Egg), OAK (Pokedex).
- Cherrygrove: GRAMPS (Map Card), NURSE JOY (Heal), CLERK (Mart).

## Lessons Learned
- **Object Collision:** All sprites (NPCs, items) are walls. Interact from an adjacent tile.
- **Pathfinding:** Always use the latest version of custom tools (e.g., `find_path_v3`).
- **Battle Strategy:** Use `battle_strategist_v2` for trainer battles.
- **Ledge Logic:** Ledges are one-way (South/Down).
- **Critical Hits:** Be extremely cautious when weakening Pokemon for capture; crits can ruin an encounter. Lead with a weaker Pokemon if possible.

## Strategy for Bellsprout
- Location: Route 31 Tall Grass.
- Method: Walk around in grass until encounter.
- Team: Lead with GNEISS (Geodude) or use Smokescreen/Leer to avoid accidental KO. Calcifer's Tackle is too strong (crits kill).
- Catching: Use Poké Ball.
- Goal: Trade for ONIX in Violet City.
- **Note:** Accidentally fainted first Bellsprout with a crit Tackle on Turn 973. Need to find another.
- **Type Weakness (Wild Battles):** Even low-level wild Pokémon can be dangerous if they have a 4x type advantage (e.g., Water vs Rock/Ground). Switch or run immediately.
- **Capture Safety:** When weakening Pokémon for capture, use the weakest available moves or status moves. Avoid high-damage moves that could KO on a critical hit.
- Wade (BUG CATCHER): Route 31 (16, 14). Roster: Caterpie (Lv2), Caterpie (Lv2), Weedle (Lv?). Stats (Icarus Lv10): Atk 17, Def 15, SpA 15, SpD 15, Spe 19.