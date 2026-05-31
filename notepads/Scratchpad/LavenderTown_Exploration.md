# Scratchpad for Lavender Town and Pokémon Tower Exploration
- **Observations**:
  - Socratic Challenge Note: GEMMY has BITE. In Gen 1, BITE is a Normal-type move. It has NO effect on Ghost-types (Gastly, Haunter) in the Pokémon Tower. We must use DIG or other non-Normal moves!

## Snorlax Capture Strategy (Poké Flute Quest)
- **Context**: Once Mr. Fuji is rescued, we receive the Poké Flute. This can wake up Snorlax blocking Route 12 and Route 16, triggering wild Level 30 Snorlax encounters.
- **Snorlax Mechanics**: Level 30, knows Rest, Body Slam, and Headbutt. Rest heals its HP and removes status, but makes it sleep.
- **Capture Strategy**:
  1. Lead with SPARKY (Pikachu L24) and immediately use THUNDER WAVE to paralyze Snorlax. Paralyzing is highly recommended as it increases catch rate permanently and reduces its threat.
  2. Switch to a lower damage attacker (like PETAL L13 or SPARKY's Quick Attack) to safely reduce its HP into the red zone.
  3. Ensure a large inventory of Great Balls (at least 15) is purchased at Lavender Town Poké Mart.
  4. If Snorlax uses Rest and falls asleep, throw Great Balls immediately as Sleep has the highest capture rate modifier.
- **Archival Plan**: Once Snorlax encounters are completed, these verified capture rules will be permanently migrated to `Mechanics/SnorlaxCaptureGuide` and region files.

## Archival Plan
- Once the climb is completed and Mr. Fuji is rescued, we will permanently migrate these verified tower-climbing rules to `Locations/LavenderTown` and create a dedicated archival notepad `Archive/LavenderTown_TowerClimb` for detailed logs. Saffron regional bypass rules will be archived in `Locations/SaffronCity` and `Mechanics/RegionalBypassRules`.

## Pokémon Tower 6F Exploration & Spatial Mapping (Turn 38041)
- **Methodical Exploration Plan**:
  - Since column 12 is blocked on rows 5-8 by tombstones, and rows 9-10 are blocked at columns 8-11, there is no direct east-west connection at rows 5-10.
  - Row 11 is blocked at columns 12-14 by tombstones.
  - Southern corridor verified as a dead end; successfully crossed to western half via Row 3 northern corridor.

## Ghost Marowak Battle-Readiness Protocol
- **Mechanics**:
  - The static spectral ghost blocking the stairs to 7F is a Level 30 Ghost of Marowak.
  - **Capture Restriction**: This ghost CANNOT be caught with any Pokéball (even with Silph Scope, attempting to throw a ball will result in it dodging/blocking). It must be defeated in battle.
  - **Combat Strategy**: Lead with GEMMY (Blastoise L45). Marowak is Ground-type, but has low Special. GEMMY's WATER GUN deals massive water damage and will easily sweep.
- **Archival Plan**: Once the tower is cleared and Mr. Fuji is rescued, all verified tower climbing and spiritual-block mechanics will be permanently migrated to `Locations/LavenderTown` and archived in `Archive/LavenderTown_TowerClimb`.

## Resources & PP Tracker (Turn 38072)
- **Moves & Status**:
  - GEMMY (Blastoise L45): DIG (8/10), TAIL WHIP (30/30), BITE (25/25), WATER GUN (23/25) [HP: 146/146]
  - BUGGY (Butterfree L13): CONFUSION (25/25), TACKLE (35/35), STRING SHOT (40/40)
  - SPARKY (Pikachu L24): THUNDERBOLT (15/15), GROWL (40/40), THUNDER WAVE (20/20), QUICK ATTACK (30/30)
- **Healing Items**:
  - HYPER POTION: 10
  - POTION: 5
  - LEMONADE: 1

## Socratic Challenge: Gen 1 Paralysis Speed Penalty Glitch (Turn 37922)
- **Mechanic**: In Generation 1, when a Pokémon is paralyzed, its Speed stat is reduced to 25%. If the status is cured in battle (e.g., using a Parlyz Heal or Full Restore), the status icon is removed, but the Speed penalty persists in the current battle round because the game does not automatically recalculate Speed upon curing unless a stat-altering move (like Agility) is used or the Pokémon is switched out.
- **Application**: Because of this stat re-application glitch, we must be highly cautious about assuming our speed is restored immediately after curing status in battle. Since we are using a HYPER POTION, we are only restoring HP, keeping the paralysis for now. Once we finish this battle, we will step on the overworld Heal Pad at (11, 9) which will clean all status conditions and properly recalculate all stats.

## Battle-Readiness Protocol: Status Cures vs. Multi-Turn Moves (Turn 37953)
- **Rule**: Never attempt a multi-turn move (like DIG or FLY) while suffering from a status condition that can cause turn loss (like Paralysis or Confusion).
- **Mathematical Proof**: Paralysis has a 25% turn-loss rate. For a single-turn move, the success rate is 75%. For a two-turn move, both turns must succeed, reducing the success rate to 56.25% (and increasing the failure rate to 43.75%).
- **Protocol**: If paralyzed, either:
  1. Use a single-turn move (like WATER GUN) which has a much higher success probability.
  2. Use a curing item (like PARLYZ HEAL) immediately on Turn 1 to completely remove the turn-loss risk before executing any complex or high-commitment moves.

## 7F Stairs Empirical Verification Plan
- **Hypothesis**: The stairs to 7F are located in the bottom-right corner of 6F at (18, 16) based on standard Pokémon Tower spiral floor layouts, while (3, 9) is physically a static tombstone block (TYPE_2889) that does not trigger any events.
- **Verification Methodology**:
  1. Navigate from (3, 10) to the bottom-right corner of the floor by walking south along Column 6 to Row 14, then going south/east to reach Column 18, Row 16.
  2. Inspect the screen overlay at (18, 16) to verify if a unique staircase tile exists.
  3. Step onto the tile to trigger the static spectral Ghost of Marowak (Level 30) using the Silph Scope, proving the exact coordinate location of the stairs and beginning the battle.
- **Test Execution Logs**:
  - Turn 38065: Stood at (3, 10) facing Up, pressed Up. Bumped into (3, 9) without triggering any dialogue or battle, proving (3, 9) is a standard solid tombstone (TYPE_2889) and not the stairs block.
  - Turn 38074: Initiated movement toward the southern corridors.