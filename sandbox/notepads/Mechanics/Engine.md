# Engine & Technical Mechanics

## Tool Compatibility
- **stun_npc**: Unsupported in Pokémon Sors due to custom ROM hack memory layout (Error: Map objects data is unavailable).

## Bag & Inventory UI Navigation (Verified Turns 517 & 603)
- **Pocket Navigation**: Bag pockets are cycled horizontally using D-Pad Left/Right.
- **Pocket Sequence**: `Items` <-> `Key Items` <-> `Poké Balls`.
  - Pressing `Left` from `Poké Balls` moves to `Key Items`.
  - Pressing `Left` from `Key Items` moves to `Items`.
  - Pressing `Right` from `Items` moves to `Key Items`.
  - Pressing `Right` from `Key Items` moves to `Poké Balls`.
- **In-Battle Bag**: Opens directly into the active/last pocket (Poké Balls pocket preserves selection). Selecting Poké Ball opens a sub-menu (`Use` / `Cancel`).