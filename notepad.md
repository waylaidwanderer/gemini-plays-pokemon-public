# Legendary Roamer Hunt
- **Strategy**: Ecruteak Shuffle. Transition between Route 37 and Ecruteak City to force roamer movement, then pace in grass.
- **Repel Trick**: Lead ICARUS (Lv 19 Pidgeotto). Wild levels on Route 37/38 are 13-16. Roamers are Lv 40.
- **Repel Step Tracking**: Applied Turn 44681.
  - Turn 44682-44691: 114 steps total.
  - Turn 44692: +20 steps (134 total).
  - Steps remaining: 66
- **Roamer Tracking**:
  - Route 37: Active hunting area.
  - Route 38: Secondary hunting area.
- **Agent Advice (legendary_tracker)**:
  - Target: Raikou or Entei.
  - Route recommendation: Route 37 or 38 (near Ecruteak City).
  - Ball recommendation: Master Ball (Roamers flee on Turn 1 or use Roar).
  - Lead Pokemon: Any Pokemon between Level 17 and Level 39.
  - Tracking: Use Pokedex "Area" function after the first encounter to intercept.
- **Catching Strategy**: Use Master Ball immediately on the first roamer encounter.

# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- DOOR: Warp tile.
- TALL_GRASS (Grass): Traversable. Triggers wild Pokémon encounters.
- WATER: Requires HM SURF to traverse.
- LEDGE: One-way jump.
- HEADBUTT_TREE: Impassable.
- WARP_CARPET: Warp tile at map boundaries.
- LEDGE_HOP_DOWN: One-way ledge (Down).
- LEDGE_HOP_RIGHT: One-way ledge (Right).
- LEDGE_HOP_LEFT: One-way ledge (Left).
- COUNTER: Impassable. Interact with NPCs behind them.
- STAIRCASE/ESCALATOR: Warp tile.

# Type Effectiveness Chart (Verified)
- Fire -> Grass: Super effective.
- Water -> Fire: Super effective.
- Electric -> Water: Super effective.
- Ground -> Poison: Super effective.
- Psychic -> Poison: Super effective.
- Ghost -> Psychic: Super effective.
- Ice -> Flying: Super effective.
- Fighting -> Normal: Super effective.
- Water -> Water: Not very effective.
- Fire -> Fire: Not very effective.

# Pokemon Information & Movesets
- Party (6/6):
  1. ICARUS (Lv19 Pidgeotto): FLY, SAND-ATTACK, GUST, QUICK ATTACK.
  2. Calcifer (Lv64 Typhlosion): FLAMETHROWER, RETURN, SMOKESCREEN, THUNDERPUNCH.
  3. KIMCHI (Lv52 Gloom): FLASH, PETAL DANCE, CUT, SLEEP POWDER.
  4. GNEISS (Lv55 Graveler): EARTHQUAKE, DEFENSE CURL, STRENGTH, ROLLOUT.
  5. GORP (Lv50 Snorlax): SURF, REST, BODY SLAM, ROLLOUT.
  6. XENON (Lv44 Haunter): HYPNOSIS, CONFUSE RAY, NIGHT SHADE, DREAM EATER.
- PC Storage: Box 1 (10/20): LARVITAR (Lv20), SCYTHER (Lv14), SEEL (Lv24), MANTINE (Lv20), KRABBY (Lv22), TENTACOOL (Lv17), KRABBY (Lv10), DRATINI (Lv15), SPINARAK (Lv13), POLIWAG (Lv12).

# Lessons Learned
- **Menu Navigation**: Cursor memory is persistent. Split deep navigation into chunks < 50 buttons.
- **Fly**: Only works outdoors.
- **Suicune (Crystal)**: Static encounter at Tin Tower. Not a roamer.
- **Repel Trick**: Use a lead with level between local wild and target legendary.