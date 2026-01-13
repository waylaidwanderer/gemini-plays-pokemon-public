# Tile Mechanics
- FLOOR: Traversable. Relational: Standard 4-way movement. Verified Turn 45281.
- WALL: Impassable. Relational: Blocks all movement. Verified Turn 45281.
- TALL_GRASS: Traversable. Relational: Standard movement; triggers wild encounters. Verified Turn 45281.
- HEADBUTT_TREE: Impassable. Relational: Blocks movement; can be interacted with for Headbutt. Verified Turn 45281.
- LEDGE_HOP_DOWN: One-way. Relational: Jump south from above; impassable from other directions. Verified Turn 45281.
- LEDGE_HOP_RIGHT: One-way. Relational: Jump east from left; impassable from other directions. Verified Turn 45281.
- WATER: Traversable. Relational: Requires HM03 Surf to enter/move. Verified Turn 45281.
- DOOR/WARP: Warp. Relational: Triggers map transition when entered. Verified Turn 45281.

# Quest: Legendary Hunt
- **Target: Suicune (Tin Tower)**
- Start Turn: 46153 | Timestamp: Tuesday, January 13, 2026 at 11:26 AM PST
- Status: Talked to three Sages on 1F. Heading to center.
- Lore: Three nameless Pokemon perished when Brass Tower burned 700 years ago. Ho-Oh gave them new life as Suicune, Entei, and Raikou.
- Plan: Navigate to Burned Tower -> Release Legendary Beasts -> Defeat Wise Trio -> Talk to Sages in Tin Tower -> Battle Suicune.
- Status: Realized Suicune won't appear until the beasts are released from the Burned Tower basement.
- Burned Tower Location: Northwest corner of Ecruteak City.
- Current Task: Leaving the Tin Tower area to head to the Burned Tower.

## Suicune Battle Plan (Tin Tower)
- Lead: XENON (Haunter, Lv 44).
- Strategy: Use Hypnosis immediately.
- Support: GORP (Snorlax) or GNEISS (Graveler) to tank hits and chip HP (avoid Calcifer Lv 64).
- Capture: Use Ultra Balls (32) while asleep. Switch to Great Balls if needed.
- Backup Sleeper: KIMCHI (Gloom) with Sleep Powder.

## Legendary Progress
- Suicune: Tin Tower (Clear Bell owned).
- Entei/Raikou: Roaming. Unseen in Pokedex. Encounter required to track.
- Roamer Shuffle: ~120 cycles (Turns 45998-46043) on Route 37/Ecruteak. No encounter.

# Quest Log
- Dana's Gift: Route 38.
- Yanma Swarm: Route 35.
- Arnie's Interest: Wants to see Growlithe/Abra (Turn 46152).

# Lessons Learned
- Roamers move on map transitions.
- Fly map list navigation: 'Up' increases index, 'Down' decreases index.
- Silver Cave Pokemon Center has no Mart.
- Start menu cursor is persistent; scroll to EXIT to reset position reliably.
- NPC movement can be unpredictable; use `stun_npc` if they block critical paths.
- Position Hallucination (Turn 46166): Ensure text is cleared before assuming movement success. Wait for confirmation of position after warp/ladder.