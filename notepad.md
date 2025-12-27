# Tile Mechanics (Global)
- FLOOR: Walkable. Standard collision. [Verified]
- WALL: Impassable. [Verified]
- WATER: Traversable only when using HM03 Surf. [Verified]
- TALL_GRASS: Walkable. Triggers wild encounters. [Verified]
- HEADBUTT_TREE: Impassable. Can be interacted with using Headbutt. [Verified]
- CUT_TREE: Impassable. Can be removed using HM01 Cut. Regrows upon map reload. [Verified]
- WARP_CARPET: Traversable. Triggers map transition. [Verified]
- CAVE: Warp point. [Verified]
- LEDGE: One-way traversal. Blocks movement from the direction it hops into. [Verified]
- PC/COUNTER/SIGN: Impassable. Interact from adjacent tile. [Verified]
- FLOOR_UP_WALL: Impassable from below. [Verified]
- VOID: Impassable. Map boundary. [Verified]
- WARP_CARPET_DOWN: Traversable. Triggers exit to overworld. [Verified]

# Battle and Pokemon Information
## Type Immunities (Target-based)
- Ghost: Immune to Normal, Fighting.
- Ground: Immune to Electric.
- Steel: Immune to Poison.
- Flying: Immune to Ground.
- Dark: Immune to Psychic.

## Party Movesets
- Calcifer (TYPHLOSION): Lv45. Flame Wheel, Headbutt, Smokescreen, Thunderpunch.
- ICARUS (PIDGEY): Lv16. Quick Attack, Sand-Attack, Gust, Fly.
- GNEISS (GRAVELER): Lv44. Earthquake, Defense Curl, Strength, Rollout.
- Ravioli (KRABBY): Lv10. Bubble, Leer, Surf.
- XENON (GASTLY): Lv21. Hypnosis, Lick, Night Shade, Mean Look.
- KIMCHI (GLOOM): Lv21. Absorb, Sweet Scent, Cut, Sleep Powder.

# Event Mechanics: Suicune Hunt (Crystal)
- Status: Suicune appears at fixed sighting locations. Final encounter at Tin Tower 1F.
- Prerequisite: "Tower Shook" event in Ecruteak City + Possession of CLEAR BELL + Fog Badge.
- Trigger: Talk to all three Sages on Tin Tower 1F.
- Sightings Sequence:
  1. Burned Tower (Ecruteak City): Beasts flee. [Cleared]
  2. Cianwood City (North): Suicune observed at (10, 14). [Cleared]
  3. Route 42 (Central Island): Middle Apricorn grove. [Sighting FAILED/SKIPPED]
  4. Route 36 (Sudowoodo junction): [Pending]
  5. Wise Trio Battle: In Tin Tower Gatehouse (Map 4_1). [Cleared]
  6. Tin Tower 1F (Final Battle): Talk to all 3 Sages on 1F. [Current Target]

# Strategy for Beating Suicune
- Status: Lv40 legendary.
- Lead: XENON (Lv21).
- Capture Sequence:
  1. Mean Look (prevent escape).
  2. Hypnosis (induce sleep).
  3. Night Shade (weaken to low HP without KO).
  4. Great Balls (repeat until caught).

# NPC & Interaction Rules
- Sage (4, 6): Passage guard. Granted access after confirming Clear Bell and Fog Badge. [Verified]
- Apricorn Trees: Face and press A to receive an Apricorn. One per day. (27, 16), (28, 16), (29, 16) on Route 42.

# Money & Economy
- Current Balance: ¥373. Need to prioritize trainer battles.

# Trainer Defeats
- Sage Gaku: Defeated in Wise Trio Room (4_2).
- Sage Masa: Defeated in Wise Trio Room (4_2).
- Sage [Third]: Sage at (4, 6) in 4_1 granted passage.

# Tactical Plan: Suicune Capture
1. Lead with XENON (Gastly).
2. Turn 1: Use Mean Look to prevent Suicune from fleeing.
3. Turn 2+: Use Hypnosis until Suicune is asleep.
4. If XENON is at risk, switch to a high-HP wall (GNEISS or Calcifer) to soak hits while throwing Great Balls.
5. Only use Night Shade if Suicune's HP is very high; at Lv21, Night Shade deals exactly 21 damage. Suicune is Lv40 (approx 120-130 HP).
6. Maintain Sleep status as a priority.
- Quest Start: Suicune Encounter (Turn 24238, 2025-12-26 16:30)