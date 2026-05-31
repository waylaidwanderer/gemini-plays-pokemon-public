# Scratchpad for Lavender Town and Pokémon Tower Exploration
- **Turn 37559**: Standing at (8, 6) on Map 0_4 (Lavender Town) facing Right.
- **Immediate Goal**: Walk east to column 14, then walk Up to (14, 5) to enter the Pokémon Tower.
- **Route to Tower Entrance (14, 5)**:
  - (8, 6) -> (9, 6) (Right)
  - (9, 6) -> (10, 6) (Right)
  - (10, 6) -> (11, 6) (Right)
  - (11, 6) -> (12, 6) (Right)
  - (12, 6) -> (13, 6) (Right)
  - (13, 6) -> (14, 6) (Right)
  - (14, 6) -> (14, 5) (Up)
- **Observations**:
  - NPC (SPRITE_cdfc) is standing at (12, 7) or (13, 7) facing Left. Wait, last turn he was reported at (12, 7). He seems to be moving.
  - Socratic Challenge Note: GEMMY has BITE. In Gen 1, BITE is a Normal-type move. It has NO effect on Ghost-types (Gastly, Haunter) in the Pokémon Tower. We must use DIG or other non-Normal moves!

## Pokémon Tower Combat Strategy (Turn 37562)
- **Problem**: Pidgeotto's GUST and general Normal-type moves do absolutely 0 damage to Ghost/Poison Pokémon (Gastly, Haunter) in Pokémon Tower.
- **Combat Readiness**:
  - **GEMMY (BLASTOISE, Level 44)**: Knows DIG (Ground-type, PP: 10), which deals super-effective damage to Ghost/Poison types. Will be our primary sweeper in the tower.
  - **SPARKY (PIKACHU, Level 24)**: Knows THUNDERBOLT (Electric-type, PP: 15), which deals neutral damage. Can be used for cleanup or back-up.
  - **Other Moves**: Do not use BITE (GEMMY) or TACKLE (BUGGY, ROCKY) as they are Normal-type in Gen 1 and will deal no damage.
- **Execution Tracking**:
  - Start Turn: 37562
  - Date/Time: Sunday, May 31, 2026 at 7:05 AM PDT
- Floors 1F-4F have been successfully climbed and fully navigated.

## Combat Strategy Response (Turn 37622)
- **Problem**: Channelers use Gastly/Haunter (Ghost/Poison) which can use Confuse Ray (inflicts confusion, physical self-damage) and Night Shade (fixed damage equal to level).
- **Strategy**:
  - Lead with GEMMY (Blastoise, L44).
  - Use WATER GUN (PP: 25) as the primary attack to conserve DIG (PP: 10) for tougher battles. At Level 44, GEMMY's high Special stat makes WATER GUN extremely powerful, capable of one-shotting or two-shotting Gastlys without wasting DIG.
  - If GEMMY is confused or low on HP, use HYPER POTION (we have 11) or switch to SPARKY (Pikachu, L24) for neutral THUNDERBOLT (PP: 15) or THUNDER WAVE support to paralyze targets.
  - Avoid using Normal-type moves like BITE or TACKLE, as Ghost-type is immune to them.
- **Archive Destination**: Once the climb is completed, these verified combat rules will be migrated to a permanent notepad under `Mechanics/PokemonTowerCombatGuide`.

## 5F Heal Pad Grinding & Sustainability Plan
- **Mechanic**: 5F has a purified, health-restoring zone (Heal Pad) at (10,8), (10,9), (11,8), (11,9) that fully restores HP and PP of all party members upon stepping on it.
- **Refined Grinding & Switch-Safety Protocol**:
  - **Gen 1 Switching Priority Rule**: In Gen 1, switching out a Pokémon is a high-priority action (+6 priority) that *always* occurs at the very start of the turn before the opponent can move. This means a low-level leader is 100% safe from Turn 1 moves (Confuse Ray/Night Shade) as they will be swapped out safely before the enemy can attack.
  - **Switch-Training Protocol**: Set a lower-level Pokémon (ROCKY L15, PETAL L13) as lead. On Turn 1 of wild battles, immediately switch to GEMMY (Blastoise) who will safely tank any incoming status/attack and sweep with WATER GUN.
  - **Psychic-type Offensive Bypass**: BUGGY (Butterfree L13) knows CONFUSION. Because Gastly/Haunter are Ghost/Poison-type, they are weak to Psychic! BUGGY can battle them directly using CONFUSION for easy super-effective EXP.
  - Position ourselves adjacent to the Heal Pad and walk back and forth to trigger wild encounters, stepping on the Pad after battles to instantly heal.
  
## Archival Plan
- Once the climb is completed and Mr. Fuji is rescued, we will permanently migrate these verified tower-climbing rules to `Locations/LavenderTown` and create a dedicated archival notepad `Archive/LavenderTown_TowerClimb` for detailed logs. Saffron regional bypass rules will be archived in `Locations/SaffronCity` and `Mechanics/RegionalBypassRules`.

## Pokémon Tower 6F Exploration (Turn 37744)
- **Observations**: Standing on the stairs at (18, 9).
- **Local Layout & Boundaries**:
  - Columns 19+ are off-screen or wall borders (TYPE_2889).
  - Row 9 is open floor (TYPE_3fe2) going left to column 14.
  - Rows 7, 8, and 10 are also open floor (TYPE_3fe2).
  - Tombstones block row 11 at (14, 11), (16, 11), and (17, 11). Row 11 has an open floor at (15, 11).
  - Bypassing tombstones requires looping through open horizontal corridors.
  - An NPC (Channeler) is visible at (16, 5).
- **Immediate Goal**: Explore west along the open corridors to locate items, trainers, and the stairs to 7F. We will start by walking Left to clear the immediate eastern block.
- **Route**:
  - From (18, 9), walk Left 4 times to (14, 9). This is clear, open floor (TYPE_3fe2) all the way.

## Resources & PP Tracker (Turn 37744)
- **Moves**:
  - GEMMY (Blastoise L45): DIG (10/10), TAIL WHIP (30/30), BITE (25/25), WATER GUN (24/25)
  - BUGGY (Butterfree L13): CONFUSION (25/25), TACKLE (35/35), STRING SHOT (40/40)
  - SPARKY (Pikachu L24): THUNDERBOLT (15/15), GROWL (40/40), THUNDER WAVE (20/20), QUICK ATTACK (30/30)
- **Healing Items**:
  - HYPER POTION: 11
  - POTION: 5
  - LEMONADE: 1
- Turn 37769: Arrived at (14, 9) facing Left. Discovered a Channeler at (12, 10) facing Right, and tombstones blocking direct west movement. However, Column 15 is a wide-open corridor of TYPE_3fe2 from Row 9 down to at least Row 13. We will loop south along Column 15 to find the bottom corridor.