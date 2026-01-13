# Tile Mechanics
- FLOOR: Traversable. Relational: Standard 4-way movement. Verified Turn 45281.
- WALL: Impassable. Relational: Blocks all movement. Verified Turn 45281.
- TALL_GRASS: Traversable. Relational: Standard movement; triggers wild encounters. Verified Turn 45281.
- HEADBUTT_TREE: Impassable. Relational: Blocks movement; can be interacted with for Headbutt. Verified Turn 45281.
- LEDGE_HOP_DOWN: One-way. Relational: Jump south from above; impassable from other directions. Verified Turn 45281.
- LEDGE_HOP_RIGHT: One-way. Relational: Jump east from left; impassable from other directions. Verified Turn 45281.
- WATER: Traversable. Relational: Requires HM03 Surf to enter/move. Verified Turn 45281.
- DOOR/WARP: Warp. Relational: Triggers map transition when entered. Verified Turn 45281.
- PIT: One-way warp. Relational: Drop to floor below. Verified Turn 46211.

# Quest: Legendary Hunt
- **Target: Suicune (Tin Tower)**
- Start Turn: 46153 | Timestamp: Tuesday, January 13, 2026 at 11:26 AM PST
- Lore: Three nameless Pokemon perished when Brass Tower burned 700 years ago. Ho-Oh gave them new life as Suicune, Entei, and Raikou.
- Plan: Release Beasts (Burned Tower) -> Defeat Wise Trio (Gatehouse) -> Battle Suicune (Tin Tower).
- Status: Beasts released (Turn 46247). Heading to Tin Tower Gatehouse.
- Rival Search: Started Turn 46227.

## Suicune Battle Plan (Tin Tower)
- Lead: XENON (Haunter, Lv 44).
- Strategy: Use Hypnosis immediately.
- Support: GORP (Snorlax) to tank (Surf/Aurora Beam) and chip HP with Body Slam/Strength.
- Capture: Use Ultra Balls (32) while asleep.
- Backup Sleeper: KIMCHI (Gloom) with Sleep Powder.

## Legendary Progress
- Suicune: Tin Tower (Clear Bell owned). Prerequisite: Release beasts.
- Entei/Raikou: Roaming. Unseen in Pokedex.

# Quest Log
- Dana's Gift: Route 38.
- Yanma Swarm: Route 35.
- Arnie's Interest: Wants to see Growlithe/Abra (Turn 46152).

# Lessons Learned
- Roamers move on map transitions.
- Fly map list navigation: 'Up' increases index, 'Down' decreases index.
- Start menu cursor is persistent.
- NPC movement can be unpredictable.
- Position Hallucination (Turn 46166): Ensure text is cleared before assuming movement success.