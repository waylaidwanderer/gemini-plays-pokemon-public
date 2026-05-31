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
- Turn 37569: Discovered that row 5 contains the Pokémon Tower building walls from column 10 to 13 (TYPE_2889), which are impassable. Row 6 is open grass (TYPE_3fe2). Route from (9, 5) to (14, 5): Down, Right x5, Up.
- Turn 37577: Entered Pokémon Tower 1F and traversed to (15, 10). Visually confirmed Mourning NPC at (13, 7), Channeler at (17, 7), and the stairs to 2F at (18, 9). Entering 2F now via: Right x3, Up.
- Turn 37586: Successfully bypassed the tombstone wall on columns 8 and 9, and reached (10, 5) on the open row 5 corridor. Moving west to column 3 via Left x7.
- Turn 37589: Located the path to the stairs to 3F. From (6, 5), row 5 is blocked at column 4 by a wall (TYPE_2889). Path to stairs at (3, 9): Down to (6, 6), Left x2 to (4, 6), Down x3 to (4, 9), Left to (3, 9). Bypasses the Old Man at (3, 7). Moving to 3F now.
- Turn 37606: Navigated to (12, 7) on 3F. Discovered that row 6 is a wide-open east-west corridor (TYPE_3fe2) running above the row 7 tombstones (15,7) and (16,7). Path to the stairs to 4F at (18, 9): Right x2 to (14, 7), Up to (14, 6), Right x3 to (17, 6), Down x3 to (17, 9), and Right to (18, 9). Moving to 4F now.

## Combat Strategy Response (Turn 37622)
- **Problem**: Channelers use Gastly/Haunter (Ghost/Poison) which can use Confuse Ray (inflicts confusion, physical self-damage) and Night Shade (fixed damage equal to level).
- **Strategy**:
  - Lead with GEMMY (Blastoise, L44).
  - Use WATER GUN (PP: 25) as the primary attack to conserve DIG (PP: 10) for tougher battles. At Level 44, GEMMY's high Special stat makes WATER GUN extremely powerful, capable of one-shotting or two-shotting Gastlys without wasting DIG.
  - If GEMMY is confused or low on HP, use HYPER POTION (we have 11) or switch to SPARKY (Pikachu, L24) for neutral THUNDERBOLT (PP: 15) or THUNDER WAVE support to paralyze targets.
  - Avoid using Normal-type moves like BITE or TACKLE, as Ghost-type is immune to them.
- **Archive Destination**: Once the climb is completed, these verified combat rules will be migrated to a permanent notepad under `Mechanics/PokemonTowerCombatGuide`.
- Turn 37636: Standing at (15, 9) after defeating the Channeler at (15, 8). Visually spotted an item ball at (12, 10). Path to collect it: Left, Down, Left x2.
- Turn 37642: Stand at (13, 10). Found the second item ball at (9, 10). Route to reach the pick-up spot at (10, 10): Right to (14, 10), Up x2 to (14, 8), Left x3 to (11, 8), Down to (11, 9), Left to (10, 9), Down to (10, 10). Standing there facing Left, we can pick it up.
- Turn 37647: Navigating to the western side of 4F. Discovered that column 10 is open down to row 14, and row 14 is a clear horizontal corridor running west (at least from column 10 to 6). Path to western stairs: Down x4 to (10, 14), Left x4 to (6, 14), then continue west off-screen.

## Southern/Western Path to 5F Stairs (Turn 37651)
- **Observations**: From (6, 14), row 14 is blocked at column 5. Path to western stairs:
  - Up to (6, 13)
  - Left to (5, 13)
  - Up x2 to (5, 11) (Faces Channeler at 5, 10 facing Down, which will trigger a battle)
  - Left to (4, 11)
  - Up to (4, 10)
  - Left to (3, 10)
  - Up to (3, 9) (Stairs to 5F)

## 5F Heal Pad Grinding & Sustainability Plan
- **Mechanic**: 5F has a purified, health-restoring zone (Heal Pad) at (10,8), (10,9), (11,8), (11,9) that fully restores HP and PP of all party members upon stepping on it.
- **Refined Grinding & Switch-Safety Protocol**:
  - **Gen 1 Switching Priority Rule**: In Gen 1, switching out a Pokémon is a high-priority action (+6 priority) that *always* occurs at the very start of the turn before the opponent can move. This means a low-level leader is 100% safe from Turn 1 moves (Confuse Ray/Night Shade) as they will be swapped out safely before the enemy can attack.
  - **Switch-Training Protocol**: Set a lower-level Pokémon (ROCKY L15, PETAL L13) as lead. On Turn 1 of wild battles, immediately switch to GEMMY (Blastoise) who will safely tank any incoming status/attack and sweep with WATER GUN.
  - **Psychic-type Offensive Bypass**: BUGGY (Butterfree L13) knows CONFUSION. Because Gastly/Haunter are Ghost/Poison-type, they are weak to Psychic! BUGGY can battle them directly using CONFUSION for easy super-effective EXP.
  - Position ourselves adjacent to the Heal Pad and walk back and forth to trigger wild encounters, stepping on the Pad after battles to instantly heal.
  
## Archival Plan
- Once the climb is completed and Mr. Fuji is rescued, we will permanently migrate these verified tower-climbing rules to `Locations/LavenderTown` and create a dedicated archival notepad `Archive/LavenderTown_TowerClimb` for detailed logs. Saffron regional bypass rules will be archived in `Locations/SaffronCity` and `Mechanics/RegionalBypassRules`.

## Pokémon Tower 5F Exploration (Turn 37672)
- **Observations**: Standing on stairs at (3, 9). Spotted a Channeler at (6, 10) facing Left. Her sight on row 10 is blocked by a tombstone at (5, 10).
- **Route to explore East along row 6**: Right to (4, 9), Up x3 to (4, 6), Right x4 to (8, 6). Bypasses the Channeler and brings the central area into view. Moving east now.

## Route from Heal Pad (11, 9) to Eastern Stairs (18, 9) on 5F
- **Observation**: Column 14/15/16 row 8/9 tombstones block direct east transit. We must loop south.
- **Path**:
  - Left x2 to (9, 9)
  - Down x3 to (9, 12)
  - Right x5 to (14, 12)
  - Up x2 to (14, 10)
  - Right x4 to (18, 10)
  - Up to (18, 9) (Stairs to 6F)
- **Status**: Checked every tile, all are open floor (TYPE_3fe2) and free of NPCs. Moving to 6F stairs now.
- Turn 37694: Arrived at (9, 12). Row 12 is completely clear to (14, 12). Bypassed the Channeler at (9, 16) who is stationary. Proceeding via Right x5, Up x2 to (14, 10).
- Turn 37696: Initiating movement from (9, 12) to the stairs at (18, 9) via (14, 12) and (14, 10).