# I. Battle Intel

## A. Type Effectiveness Chart (Verified)
- **Super Effective (2x):** Psychic > Ghost/Poison; Ghost > Psychic; Electric > Rock/Water; CUT (Normal) > VICTREEBEL (Grass/Poison); Flying > Grass/Poison; Psychic > Flying; Ice > Ground; Ground > Poison; Ground > Fire; Rock > Fire; Fighting > Rock; Flying > Fighting; Water > Fire.
- **Not Very Effective (0.5x):** Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic; Bite (Normal) !> HAUNTER (Ghost/Poison); Ice !> Gyarados (Water/Flying); Poison !> Poison; Ice !> Water; Poison !> Ground; Normal !> Rock.
- **Immune (0x):** Flying immune to Ground; Ground immune to Electric; MUK immune to Poison; HYPNO immune to STUN SPORE; MUK immune to THUNDER WAVE; MAROWAK immune to POISON GAS.

## B. Trainer Rosters & Movesets
### Giovanni (Viridian Gym)
- **Dugtrio (Lv53):** Knows Rock Slide.
- **Nidoqueen (Lv54):** Knows Body Slam, Earthquake.
- **Persian (Lv55):** Knows Bubblebeam (Water), Slash, Hyper Beam (Normal), Thunderbolt (Electric).

### Beauty (Route 15)
- **Golduck (Lv 35):** Knows Confusion.
- **Wigglytuff (Lv 35):** Knows Defense Curl.

# II. Game Mechanics & Tile Types

- **`ground`**: Standard walkable tile.
- **`impassable`**: Walls, objects, cannot be traversed.
- **`spinner_up`, `spinner_down`, `spinner_left`, `spinner_right`**: Forces movement in the specified direction until a `spinner_stop` tile or another obstacle is hit.
- **`spinner_stop`**: Stops movement from a spinner tile.

# III. Viridian Gym Spinner Map Notes
- This is a complex spinner maze. Defeated trainers become impassable obstacles. Manual pathing is unreliable; a specialized solver is needed.