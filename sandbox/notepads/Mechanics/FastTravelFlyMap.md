# Fast-Travel Fly Map Navigation & Mechanics

## Fly Map City Matrix & Verified Offsets
- **From Pallet Town**:
  - `Up` 1 time -> **VIRIDIAN CITY** ("To VIRIDIAN CITY")
  - `Up` 2 times -> **PEWTER CITY** ("To PEWTER CITY")
- **From Viridian City**:
  - `Down` 1 time -> **PALLET TOWN** ("To PALLET TOWN")
  - `Up` 1 time -> **PEWTER CITY** ("To PEWTER CITY")
- **From Saffron City**:
  - `Left` 1 time -> **CELADON CITY** ("To CELADON CITY")
  - `Down` 1 time, `Left` 1 time -> **PALLET TOWN** -> `Up` 1 time -> **VIRIDIAN CITY**
- **From Pewter City**:
  - `Down` 1 time -> **VIRIDIAN CITY** ("To VIRIDIAN CITY")
  - `Down` 2 times -> **PALLET TOWN** ("To PALLET TOWN")

## Field Move Execution Sequence
- Open Start Menu -> POKÉMON (index 1) -> select ZEPHYR (Slot 4) -> Option 1: FLY -> Navigate cursor to target city -> Press A to confirm flight.