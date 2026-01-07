# Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable.
- TALL_GRASS: Traversable. Triggers wild encounters.
- LEDGE_HOP: One-way traversal (South/West/East).
- CAVE: Warp to indoor areas.
- WATER: Traversable with HM03 SURF.
- CUT_TREE: Removed with HM01 CUT.
- BOULDER: Pushed with HM04 STRENGTH.
- COUNTER: Interaction point for NPCs behind desks.
- WARP_CARPET: Map transition tile at exits.

# Strategy: Rising Badge (Gym Leader Clair)
- Tactical Plan: Use Xenon's Night Shade for fixed damage. Gneiss for physical bulk and STAB Earthquake. Calcifer's Thunderpunch for neutral coverage.
- Training Goal: Level Xenon and Kimchi to 30+ in Route 45 grass.

# Strategy: Johto League Training
- Method: Switch-training. Lead with Kimchi or Xenon to share EXP, then switch to finisher (Gneiss/Calcifer).
- Efficiency: Grind in Route 45 grass (4,12)-(5,12).
- Resource Management: Return to Blackthorn PC via FLY when Xenon's Night Shade or Gneiss's Earthquake PP is depleted.
- Grinding Session 1: Started Turn #31060 (Tuesday, Jan 6, 2026).

# Ground-Type Safety Protocol (Lethal Threat)
- Problem: Xenon (Poison/Ghost) is weak to Ground. Magnitude 10/Earthquake are OHKO threats.
- Solution: NEVER lead or switch Xenon into Ground-types (Geodude, Graveler, Donphan, Gligar) if they are likely to use a Ground move.
- Ground Move Resistances:
  - Icarus (Flying): Immune (0x).
  - Kimchi (Grass/Poison): Neutral (1x).
  - Ravioli (Water): Neutral (1x).
  - Gneiss (Rock/Ground): Weak (2x).
  - Calcifer (Fire): Weak (2x).
  - Xenon (Ghost/Poison): Weak (2x).

# Progress Tracker
- Target Lv30: 21760 EXP (~4571 left for Kimchi, ~1595 left for Xenon).
- Encounter Log Summary: Donphan (Lv25/30), Geodude (Lv23), Graveler (Lv23/25/27), Gligar (Lv24), Skarmory (Lv24).

# Key NPC Locations & Gifts
- Dana (Lass): Route 38. Has a gift. (Turn #31604)

# Battle Strategies & Observations
- Night Shade: Deals fixed damage equal to user level. Cannot hit Normal-types.
- Sleep Powder: Effective for neutralizing threats before switching.
- Type Immunities: Ghost-types (Xenon) immune to Normal/Fighting moves (e.g., Selfdestruct, Quick Attack).
- Move Mechanics: Selfdestruct is used by Graveler/Geodude; Xenon is immune. Hypnosis/Sleep Powder are effective for safe switches.

# General Mechanics & Lessons
- Route 45: Ledges divide the route into vertically separated sections. Paths are one-way SOUTH. Use HM02 FLY to return to Blackthorn City.
- Fly Map: Systematic navigation required. Confirm destination name in screen text before pressing A.
- Tool Usage: Ensure perfectly structured JSON for battle_analyst_v2. Include all party members correctly. Avoid truncation.