# Pokémon Crystal Playthrough
- Started: Friday, January 16, 2026

### Current Task
- **Map 4_3**: Ecruteak City Pokémon Center.
- **Goal**: Heal Team & Adjust Party.
- **Status**: Headache (Psyduck) withdrawn. Topaz Fainted.
- **Issue**: 'A' button inputs seem to be ignored or failing to trigger Nurse Joy.
- **Plan**:
  1. Debug: Move Left -> Right -> Up -> A to reset position/orientation logic.
  2. Heal at Nurse Joy.
  3. Buy Super Potions/Repels at Mart.
  4. Go to Dance Theater (Ecruteak) to battle Kimono Girls and get HM03 Surf.

- **Map 3_13**: Tile (15, 4) is a BREAKABLE ROCK (impassable), despite being TYPE_3fe2. BFS will fail here. Go around via the Left side (Col 4).
- **Map 3_13**: Item at (14, 2) is blocked by Breakable Rock at (15, 4). Requires Rock Smash.
- **Exploration**: Checking bottom-right area (Cols 14-16) before leaving.
- **Reflection (Turn 14208)**: 
  - Progress: Healed team, taught Rock Smash. Now back in Burned Tower.
  - Plan: Smash rock at (15, 4) to access East side/Item. Avoid hole at (7, 15).
  - Hypothesis: Rock Smash opens path to new area or item. Beasts might be elsewhere (B1F center).
- **Loot**: Found HP Up at (14, 2) in Burned Tower 1F.
- **Mapping**: Warp/Hole located at (10, 9) in Burned Tower 1F. Expecting drop to B1F center.
- **Achievement**: Released the Legendary Beasts (Raikou, Entei, Suicune) from Burned Tower B1F.
- **Mapping**: Ladder to 1F located at (7, 15) in Burned Tower B1F.
### Strategy Log
- **Ecruteak Gym**:
  - **Mechanics**: Ghosts here are Poison/Ghost.
  - **Weaknesses**: Ground (Dig/Mud-Slap), Psychic.
  - **Immunities**: Normal types (Amethyst/Bolin) are immune to Ghost moves.
  - **Lesson**: Mud-Slap hits Gastly (No Levitate in Gen 2).
  - **Plan**: Teach TM28 (Dig) to Garnet for high-power Ground coverage.
- **Immediate Task**: Heal -> Teach Dig -> Buy Potions -> Re-enter Gym.
### Mechanics
- **Ecruteak Gym**: Falling into a pitfall warps to the entrance. Intentionally stepping on one is faster than walking back.