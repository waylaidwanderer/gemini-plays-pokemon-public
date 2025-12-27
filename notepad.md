## Suicune Quest Log (Crystal Version)
- Prerequisites: Clear Bell (Obtained).
- Quest Start: Turn 24182.
- Re-verification Start: Turn 26780.
- Sequence:
  1. Burned Tower (Flee event observed).
  2. Cianwood City North (Flee event observed).
  3. Eusine Battle (Cianwood) - Defeated (Turn 21034).
  4. Route 42 sighting: REQUIRED (Re-verifying). Target: (26, 15).
  5. Route 36 sighting: REQUIRED (Re-verifying). Target: (35, 9).
  6. Tin Tower / Wise Trio: Final stage.

## Strategy for Wise Trio Battle
- Sages use Noctowl (Normal/Flying) and Kadabra (Psychic).
- Lead: Calcifer (Typhlosion) with Thunderpunch (for Noctowl).
- Backup: Gneiss (Graveler).

## Tile Mechanics - Global
- FLOOR / GATEHOUSE_FLOOR: Traversable on foot.
- WALL / VOID / HEADBUTT_TREE: Impassable.
- WATER: Traversable via SURF. Interaction from land (facing water) triggers SURF menu.
- CUT_TREE: Impassable. Requires CUT to clear. Regrows after leaving map.
- TALL_GRASS: Traversable on foot. Wild encounters.
- LEDGE_HOP: One-way jump (usually downward/outward). Impassable in opposite direction.

## General Lessons Learned
- **Tool Failure Recognition:** If 'find_path_v6' or any automation fails to progress for 2+ turns, switch to manual control or specialized tools immediately.
- **SURF Transitions:** BFS must account for the interaction required to enter water.
- **Sequential Events:** Legendary beast sightings are strictly sequential. Do not skip steps.

## Progress Tracking
- Suicune Quest: Ongoing. Re-verifying overworld sightings.
- Route 42 Target: (26, 15).
- Route 36 Target: (35, 9).
- Hypothesis: Sighting might require map reset or specific approach.
- Status: Island at (26, 15) appears empty. Checking map reset via Mt. Mortar.