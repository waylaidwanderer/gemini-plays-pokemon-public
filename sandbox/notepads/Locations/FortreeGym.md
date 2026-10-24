# Location: Fortree Gym

## Overview
The sixth Pokémon Gym in the Hoenn League, located in Fortree City. Specializes in Flying-type Pokémon. Led by Gym Leader Winona.

## Gym Leader & Rewards
- Gym Leader: Winona
- Badge: Feather Badge (enables HM02 Fly outside battle, obedience up to Lv 70)
- TM: TM40 Aerial Ace
- Winona's Team (Emerald):
  1. Swablu (Lv 29, Normal/Flying): Defeated easily by Leaf Blade / Rock Tomb.
  2. Tropius (Lv 29, Grass/Flying): Double-resists Grass. Counter with Rock Tomb (2x super effective).
  3. Pelipper (Lv 30, Water/Flying): Uses Protect; Winona uses Hyper Potion. OHKO by Sage's Leaf Blade (Special STAB).
  4. Skarmory (Lv 31, Steel/Flying): Physical defense is 140, but Special Defense is only 70! Winona burns both Hyper Potions here. Counter with Special attacks (Pursuit) or Rock Tomb.
  5. Altaria (Lv 33, Dragon/Flying): Uses Dragon Dance (+Atk, +Spe), Aerial Ace, Earthquake, DragonBreath. Weak to Rock (2x). When weakened, use Quick Attack (+1 priority) to bypass Dragon Dance speed boosts and strike first!

## Master Navigation Guide & Canonical Solution
- Reset Mechanic:
  - Stepping Down from (15, 24) on entrance mat warps outside to Fortree City at (22, 12).
  - Stepping Up from (22, 12) re-enters Fortree Gym at (15, 23). Resets all turnstiles to default State 0. All defeated trainers remain cleared.
- Lower Gym Master Path:
  1) Turnstile 1: From (15, 23), step Up to (15, 22), Row 22 to (12, 22), push Left to (11, 22).
  2) Turnstile 2: Row 22 to (6, 22), push Left to (4, 22).
  3) Turnstile 3 Transit: Down to row 21, East to (4, 21), ascend Col 4 to (4, 16).
  4) Transit: Row 16 East to (7, 16), North to (7, 14).
  5) Turnstile 4: Push Down from (7, 14) into (7, 15) to clear Column 9.
  6) Turnstile 5 & Ascend to Upper Gym:
     - From (7, 14), step Right 2 to (9, 14).
     - Walk Up 2 along Column 9 to (9, 12).
     - Step Left to (8, 12).
     - Push Right into (9, 12) (`hold Right 800` or solid push) to rotate Turnstile 5 out of Column 9!
     - Walk straight North up the opened Column 9: (9, 11) -> (9, 10) -> (9, 9) -> (9, 8).
     - At Row 8, walk Left to (6, 8) / (5, 8) at the Upper Chamber entrance.

- Gate B Courtyard Entry Mechanism (Verified Turns 12446-12455):
  Pushing Up directly from (5, 7) or (5, 8) while Gate B is horizontal fails to enter the courtyard.
  Prerequisite sequence to enter courtyard from Row 8:
  1) From (5, 7)/(5, 8), walk East along Row 8 to (7, 8).
  2) Push Up at (7, 8) into Gate B's eastern arm at (7, 7) to rotate Gate B.
  3) Step Down to (7, 8) and walk West to (5, 8).
  4) From (5, 8), execute `hold Up 800`, which cleanly moves through Gate B into the courtyard at (5, 5).
  5) Step Up to (5, 4) and turn Right into (6, 4) onto the open Row 4 walkway straight to Winona at (15, 3)!

- Upper Chamber Canonical Solution (The Master Circuit):
  1) Arrive at (5, 8) on Row 8 from Lower Gym.
  2) CRITICAL PREREQUISITE - Pre-rotate Turnstile C from Row 8:
     - In default State 0, Turnstile C has no North arm at (2, 5). It must be pre-rotated BEFORE pushing Gate A UP!
     - From (5, 8), walk West along Row 8: (4, 8) -> (3, 8) -> (2, 8) -> (1, 8).
     - Walk North along Column 1: (1, 8) -> (1, 7) -> (1, 6).
     - Push Right into (2, 6) (`hold Right 800`) to rotate Turnstile C (now has North arm at 2, 5!).
     - Walk South down Col 1 to (1, 8), then East along Row 8 back to (5, 8).
  3) Enter Courtyard:
     - From (5, 8), push Gate B UP (`hold Up 800`) at (5, 7) to step into courtyard at (5, 4).
  4) Rotate Gate A:
     - From (5, 4), push Gate A UP into (5, 2) (`hold Up 800`).
     - Gate A rotates clockwise to {North, West}, opening Row 4 at (6, 4).
     - Player lands in northern alcove at (5, 2).
  5) Northern Circuit to Row 8:
     - Walk West along Row 2: (5, 2) -> (4, 2) -> (3, 2) -> (2, 2).
     - Walk South down Column 2: (2, 2) -> (2, 3) -> (2, 4) -> (2, 5).
     - Push Turnstile C DOWN from (2, 5) into (2, 8) onto Row 8 (`hold Down 800`).
     - Walk East along Row 8: (2, 8) -> (3, 8) -> (4, 8) -> (5, 8).
  6) Re-enter Courtyard:
     - Gate A remains rotated (Row 4 is open!). From (5, 8), push Gate B UP (`hold Up 800`) to step into courtyard at (5, 4).
  7) Walk to Winona:
     - At (5, 4), turn Right into (6, 4) on Row 4!
     - Walk East along Row 4: (6, 4) -> (7, 4) -> (8, 4) -> (9, 4) -> (10, 4) -> (11, 4) -> (12, 4) -> (13, 4) -> (14, 4) -> (15, 4).
     - Step North onto platform ramp at (15, 3) facing Gym Leader Winona at (15, 2)!

## Victory Record
- Gym Leader Winona: [DEFEATED - Turn 12839]! Earned Feather Badge and received TM40 Aerial Ace. Winona registered in Match Call. HM02 Fly can now be used in the field!

## Verified Exit Route Mechanics (Turns 12842-12852)
- Gate B (Upper Chamber): Pushing South from (5, 6) with `hold Down 800` cleanly rotates Gate B counterclockwise and lands player at (5, 8)/(5, 9).
- Route 9 Corridor: Row 9 from Col 5 to Col 9 is open, connecting to Column 9 heading south to Row 14, then West to (7, 14) and South to (7, 16).
- Lower Gym Turnstile 2: From (4, 22), pushing East with `hold Right 800` against the West arm cleanly rotates Turnstile 2 clockwise, landing player at (7, 22) and opening Row 22 east to Col 10.
- Lower Gym Turnstile 1: From (10, 22), pushing East with `hold Right 800` rotates Turnstile 1 and lands player at (13, 22) / (14, 22).
- Exit Warp: Stepping Down from (15, 24) warps player outside to Fortree City at (22, 12).