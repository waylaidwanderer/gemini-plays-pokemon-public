# Abandoned Undersea Team Siara Laboratory (Location 3)

## Elevator Mechanics (`6, 15`)
- **Floor Selector (`5F, 4F, 3F, 2F, 1F`)**: Stepping into any elevator doorway (`5, 4` on `1F`, `36, 5` on `2F`) warps to `(6, 15)` inside the elevator and automatically opens the 5-floor menu (cursor defaults to `5F`).
  - Selecting a valid unlocked floor plays a ~5500ms elevator ride animation and **automatically warps Asher out of the elevator** onto the destination floor (verified Turns 34386-34388).
  - **Floor Access**:
    - `1F`: Entrance Stairwell (`5, 5`; connects south at `5, 15` to the Location 3 Cave Passage `28, 8`).
    - `2F`: Unlocked initially; warps to `(36, 6)` (verified Turn 34388).
    - `5F`: Displays *"UNAUTHORIZED PERSONEL / EC CARD IS REQUIRED"* until the **EC Card** is obtained (verified Turn 34385).

## Floor 2F (`36, 6` Elevator Exit)
- **Elevator Lobby (`33-38, 5-10`)**:
  - **Elevator Doorway (`36, 5`)**: Enters the elevator (`6, 15`).
  - **Locked Northern Security Door (`30-31, 6`)**: Blocks a northern room containing a **gold item ball** at `(30, 4)`.
  - **Professor Ivo's HuPhone Briefing (`37, 6`, Turns 34389-34391)**:
    - Stepping onto `(37, 6)` triggers a HuPhone call from **Professor Ivo**, who explains that while the elevator is running on a backup generator, everything else in the facility is offline because the **main generator** is not running.
    - Because the security doors cannot be opened without power, Asher must **find the generator room and turn the main generator back on**.
    - Ivo also warns Asher that the abandoned laboratory is crawling with **Eclipsed Pokémon**.
  - **Purple Wall Plaque (`38, 5`)**: Reads *"B2F / Lobby"* (confirming `1F–5F` on the elevator panel correspond to subterranean undersea levels `B1F–B5F`, verified Turn 34391).
  - **Wild Eclipsed Pokémon Encounters**:
    - Floor tiles inside the Abandoned Undersea Laboratory can trigger wild **Eclipsed Pokémon** encounters (such as **Eclipsed Pikachu**♀ Lv40, which knows `Eclipse Zap`) even while a Repel / Super Repel is active (verified Turn 34393).
    - Wild Eclipsed Pokémon can be fled from normally via `Run` (*"Got away safely!"*, verified Turn 34396) or targeted with Poké Balls (verified Turn 34395).
  - **Western Corridor (`23-33, 8-9`)**:
    - **Purple Wall Plaque (`27, 7`)**: Reads *"Doors are password protected! / If you forgot the code for a door, find the computer displaying it."* (verified Turn 34398).
    - **Bookshelves (`23-26, 7-8`)**: Located along the northern wall.
    - **Purple Door Mat (`25, 9`)**: Southern doorway mat leading into an adjacent room.
  - **Southern Corridor (`34-35, 10-13+`)**: Extends south past the yellow crates at `(36, 12-13)`.