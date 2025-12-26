# Global Tile Mechanics
- FLOOR: Traversable. Standard ground. [Verified]
- WALL: Impassable. Rock faces and boundaries. [Verified]
- WATER: Traversable via Surf. [Verified]
- HEADBUTT_TREE: Impassable. Interaction only. [Verified]
- CUT_TREE: Impassable. Can be removed with Cut. [Verified]
- FLOOR_UP_WALL: Impassable ledge (one-way down). [Verified]
- CAVE: Traversable. Warp point leading to interiors. [Verified]
- WARP_CARPET: Traversable. Transition between maps/gatehouses. [Verified]
- TALL_GRASS: Traversable. Wild Pokémon encounters. [Verified]

# Strategy: Suicune Hunt (Johto)
- Sighting 1: Burned Tower (Complete)
- Sighting 2: Cianwood (Complete)
- Sighting 3: Route 42 (Pending)
- Sighting 4: Route 36 (Next)
- Sighting 5: Fuchsia City (Kanto)
- Final Battle: Tin Tower 1F (Requires Clear Bell)
- Primary Goal HOW: Complete all 5 sightings. Enter Tin Tower 1F. Use Xenon (Gastly) for Hypnosis and Mean Look. Use Ultra/Great Balls.

# Week Siblings Strategy
- Arthur (Thursday): Route 36 (47, 5). Provides Hard Stone. [Urgent - Thursday 10:47 PM]
- How to reach Arthur: From the Violet City entrance (59, 9), head west and then north towards the tree line. Arthur is standing at (47, 5).
- Suicune Hunt Sighting 3 Attempt (Route 42 Island): Swept all floor tiles in the grove (Turns 21733-21741). Flee event did not trigger. Investigating prerequisites.
- Suicune Hunt Start: Turn 21694.
- Primary Goal HOW: Complete all 5 sightings. Enter Tin Tower 1F. Use Xenon (Gastly) for Hypnosis and Mean Look. Use Ultra/Great Balls.
- Rising Badge (Clair): Next Gym Badge required. Need to travel to Blackthorn City.
- Note: Arthur's position is dynamic. He was seen at (47, 5) on Turn 21811.
- Session Start: Turn 21792 (Thursday 10:39 PM).
- Lesson: Moving NPCs like Arthur can be difficult to interact with. Use `stun_npc` to freeze them in place before attempting to talk.
- Lesson: Never mix directional inputs and the A button in the same turn; the system will strip the A button to prevent errors. Move first, then interact in a separate turn.
- Hypothesis: Arthur's dialogue is looping because a prerequisite is missing or I already have the stone (checking party).
- Hypothesis: Suicune sighting 3 on Route 42 requires approaching from a specific direction or triggering another event first.
- Hypothesis: The Pokedex status "Route 38" refers to Raikou/Entei, not Suicune.
- Tile Mechanics:
  - FLOOR: Traversable. Standard ground. [Verified]
  - WALL: Impassable. Rock faces and boundaries. [Verified]
  - WATER: Traversable via Surf. [Verified]
  - HEADBUTT_TREE: Impassable. Interaction only. [Verified]
  - CUT_TREE: Impassable. Can be removed with Cut. [Verified]
  - FLOOR_UP_WALL: Impassable ledge (one-way down). [Verified]
  - CAVE: Traversable. Warp point leading to interiors. [Verified]
  - WARP_CARPET: Traversable. Transition between maps/gatehouses. [Verified]
  - TALL_GRASS: Traversable. Wild Pokémon encounters. [Verified]