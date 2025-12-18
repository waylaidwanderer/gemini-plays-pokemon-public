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
  1. Catch Geodude in Dark Cave (Route 31) for Rock-type advantage.
  2. Catch Bellsprout on Route 31; trade in Violet City for ONIX.
  3. Train Calcifer to Lv10 (Ember) and Icarus to Lv9 (Gust).
  4. Use Ember to sweep Sprout Tower (Flash HM).
  5. Use Rock-types (Geodude/Onix) to counter Falkner's Flying moves.

## Current Area: Dark Cave
- **Status:** Geodude caught! Nicknaming her "Gneiss".

## Completed Areas
- **Route 30:** Defeated Joey, Mikey, and Don. Talked to Cooltrainer F. Path to Route 31 is clear.
- **Route 31:** Navigated to Dark Cave.

## Battle and Pokemon Information
### Observed Movesets
- Rattata: Tackle, Tail Whip
- Pidgey: Tackle
- Cyndaquil: Tackle, Leer, Smokescreen
- Caterpie: Tackle (Verified).
- Geodude: Tackle (Verified).
### Team Status
- Icarus (Pidgey): Lv9. Moves: Tackle, Sand-Attack, Gust.
- Calcifer (Cyndaquil): Lv8. Moves: Tackle, Leer, Smokescreen.
- Gneiss (Geodude): Lv4. Moves: Tackle.
### Type Effectiveness (Verified)
- Flying vs Bug: Super Effective. (Verified with Gust vs Caterpie).
- Normal vs Rock: Not very effective. (Verified with Tackle vs Geodude).

## NPC Archive
- New Bark: ELM (Starter), OFFICER (Rival), MOM (Savings).
- Mr. Pokémon: MR. POKÉMON (Egg), OAK (Pokedex).
- Cherrygrove: GRAMPS (Map Card), NURSE JOY (Heal), CLERK (Mart).

## Lessons Learned
- **Object Collision:** All sprites (NPCs, items) are walls. Interact from an adjacent tile.
- **Pathfinding:** Always use the latest version of custom tools (e.g., `find_path_v3`).
- **Battle Strategy:** Use `battle_strategist_v2` for trainer battles to ensure type advantages are utilized.
- **Ledge Logic:** Ledges are one-way (South/Down) and cannot be bypassed from the bottom. Verified on Routes 29 and 30.

## Strategy for Geodude
- Location: Dark Cave.
- Method: Walk around in dark areas until encounter.
- Team: Use Icarus (Pidgey) for Tackle/Sand-Attack or Calcifer for Tackle/Leer. Avoid using Gust if it's not effective (Geodude is Rock/Ground).
- Catching: Use Poké Ball when HP is low.
- **CAUTION:** `autopress_buttons` from overworld navigation persists into battles. Buffered buttons can disrupt menu navigation.