# Gem's Journey in Pokémon Crystal

## Current Strategy
- **Primary Goal:** Stop Team Rocket.
- **Secondary Goal:** Investigate Radio Tower (Team Rocket takeover).
- **Navigation:** Navigate to Rocket Grunt at (16, 23).
- **Status:** In Goldenrod City (10, 30).
- **Plan:**
    1. Move West to X=9 (Main N/S path on west side).
    2. Move North to Y=23.
    3. Move East to X=15 to approach the Grunt.
    4. Check if he battles or blocks the way.

## Tile Mechanics
- **FLOOR:** Standard walkable tile.
- **WALL:** Impassable.
- **COUNTER:** Impassable, but interactable from adjacent tile if an NPC is behind it.
- **LADDER:** Warp tile to another map.

**Goldenrod City Notes:**
- Name Rater is at (15, 7).

## Reflections & Lessons
- **Fly Mechanic:** Must verify destination text before confirming. Do not batch navigation and confirmation.
- **Map Markers:** Distinguish PC types (Storage vs Research) to avoid confusion.
- **Menu Hygiene:** Ensure menus are fully closed to avoid state desync.
- **Navigation Lesson:** Always verify the path against specific tile data (Mental Map/ASCII) to identify obstacles like Headbutt Trees or Walls before defining a path plan. Straight lines are rarely safe.
- **Observation:** The Super Nerd at (6, 9) in the Underground appears to be already defeated (or friendly), as he didn't trigger a battle on sight. This suggests I might have cleared this area before or he's a non-hostile NPC.
- **Hypothesis Check:** If the "Uniform" quest isn't active, maybe I can just walk into the Radio Tower? But I couldn't reach the door. The Underground is the best lead for now.