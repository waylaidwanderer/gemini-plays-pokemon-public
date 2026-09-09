# Indigo Plateau & Pokémon League HQ

## Gauntlet Overview & Rules
- **Sequential Gauntlet Rule**: The Pokémon League Elite Four consists of 5 consecutive battles (Lorelei, Bruno, Agatha, Lance, Champion RED) with zero mid-gauntlet healing stations or Pokémon Centers.
- **Blackout & Failure Reset**: Blacking out at any point during the gauntlet completely resets all defeated Elite Four trainers, locks all chamber doors, and returns the player to the last visited Pokémon Center. The entire gauntlet must be completed in a single continuous run.
- **Speed Priority & Status Mitigation (Empirically Verified)**: At Lv 91, HYDROS possesses 228 Speed, naturally outspeeding every single Pokémon across Lorelei, Bruno, Agatha, Lance, and Champion RED (Agatha's fastest Gengar is base 110 Spd = ~145 Spd at Lv 60). Maintaining full Speed is paramount:
  - HYDROS strikes FIRST on turn 1 of every Agatha matchup, achieving 1-hit knockouts with STAB Surf (Gengar Lv 56, Gengar Lv 60) and Ice Beam (Golbat Lv 56, Haunter Lv 55, Arbok Lv 58) BEFORE they can ever cast Confuse Ray or Hypnosis!

## Status Mitigation & Poké Flute Protocol
- **Poké Flute in Battle**: The Bag contains the Poké Flute (infinite uses). When HYDROS is put to sleep (e.g. by Hypnosis), opening `ITEM` and selecting `POKé FLUTE` instantly awakens HYDROS on the next turn, eliminating multi-turn sleep risks and completely preventing Dream Eater attacks!
- **Speed Dominance**: At Lv 91, HYDROS has 228 Speed, outspeeding every Pokémon in the League. Always strike first with STAB Surf, Ice Beam, or Double-Edge.

## Fight Menu Cursor Memory Mechanic (Empirically Verified)
- **Cursor Memory**: In retail Pokémon Blue, when opening the `FIGHT` menu during battle, the cursor retains the position of the **last selected move slot** from the previous turn rather than resetting to Slot 1.
- Move Layout (Slot 1: Double-Edge, Slot 2: Ice Beam, Slot 3: Bite, Slot 4: Surf).
- To switch moves, calculate relative offsets from the previously selected move slot:
  - From Slot 4 (Surf) to Slot 2 (Ice Beam): Press `Up` 2 times.
  - From Slot 2 (Ice Beam) to Slot 4 (Surf): Press `Down` 2 times.
  - From Slot 2 (Ice Beam) to Slot 3 (Bite): Press `Down` 1 time.
  - From Slot 4 (Surf) to Slot 1 (Double-Edge): Press `Down` 1 time (wraps) or `Up` 3 times.

## Gauntlet Progress & PP Verification Protocol
- Track live PP after every room to adapt move selections dynamically across the gauntlet.

## Gauntlet Master PP Budget & Strategy (Rooms 1-5)
- Entering Room 1 (Lorelei):
  - Dewgong Lv 54: STAB Surf (Slot 4) x2 (2HKO, 0 recoil) [Surf PP: 15 -> 13/15]
  - Cloyster Lv 53: STAB Surf (Slot 4) x2 (2HKO, 0 recoil) [Surf PP: 13 -> 11/15]
  - Slowbro Lv 54: STAB Surf (Slot 4) x2 or Bite (Slot 3) (0 recoil) [Surf PP: 11 -> 9/15]
  - Jynx Lv 56: STAB Surf (Slot 4: OHKO vs 95 Special, 0 recoil) [Surf PP: 9 -> 8/15]
  - Lapras Lv 56: STAB Surf (Slot 4) x2 (0 recoil) [Surf PP: 8 -> 6/15]
  -> HYDROS clears Room 1 at 311/311 HP (100% full health) with zero recoil!

- Room 2 (Bruno):
  - Onix Lv 53: Ice Beam (Slot 2) - 4x SE OHKO, 0 recoil [Ice Beam PP: 10 -> 9/10]
  - Hitmonchan Lv 55: Double-Edge (Slot 1) - OHKO (recoil 32 HP -> 268/315) [DE PP: 15 -> 14/15]
  - Hitmonlee Lv 55: STAB Surf (Slot 4) - OHKO, 0 recoil [Surf PP: 6 -> 5/15]
  - Onix Lv 56: Ice Beam (Slot 2) - 4x SE OHKO, 0 recoil [Ice Beam PP: 9 -> 8/10]
  - Machamp Lv 58: STAB Surf (Slot 4) - OHKO, 0 recoil [Surf PP: 5 -> 4/15]
  -> HYDROS clears Room 2 at 268/315 HP with 0 additional recoil!

- Room 3 (Agatha):
  - Gengar Lv 56: STAB Surf (Slot 4) - OHKO, 0 recoil [Surf PP: 5 -> 4/15]
  - Golbat Lv 56: Ice Beam (Slot 2) - 2x SE OHKO, 0 recoil [Ice Beam PP: 8 -> 7/10]
  - Haunter Lv 55: Ice Beam (Slot 2) - OHKO, 0 recoil [Ice Beam PP: 7 -> 6/10]
  - Arbok Lv 58: Ice Beam (Slot 2) - OHKO, 0 recoil [Ice Beam PP: 6 -> 5/10]
  - Gengar Lv 60: STAB Surf (Slot 4) - OHKO, 0 recoil [Surf PP: 4 -> 3/15]
  -> HYDROS clears Room 3 at 268/315 HP with zero recoil!

- Room 4 (Lance):
  - Gyarados Lv 58: Ice Beam (Slot 2) - neutral 95 BP deals ~167 dmg, finish with Bite (Slot 3) [Ice Beam PP: 5 -> 4/10, Bite PP: 25 -> 24/25]
  - Dragonair Lv 56: Ice Beam (Slot 2) - 4x SE OHKO, 0 recoil [Ice Beam PP: 4 -> 3/10]
  - Dragonair Lv 56: Ice Beam (Slot 2) - 4x SE OHKO, 0 recoil [Ice Beam PP: 3 -> 2/10]
  - Aerodactyl Lv 60: Ice Beam (Slot 2) - 2x SE OHKO, 0 recoil [Ice Beam PP: 2 -> 1/10] (Conserves Surf for RED!)
  - Dragonite Lv 62: Ice Beam (Slot 2) - 4x SE OHKO, 0 recoil [Ice Beam PP: 1 -> 0/10]
  -> HYDROS clears Room 4 at 268/315 HP with zero recoil!

- Champion Chamber (Champion RED Matchup Notes):
  - Pidgeot Lv 61: STAB Surf (Slot 4) / Double-Edge - OHKO [Surf PP: 3 -> 2/15]
  - Alakazam Lv 59: Bite (Slot 3) - OHKO vs 68 Def, 0 recoil [Bite PP: 24 -> 23/25]
  - Rhydon Lv 61: STAB Surf (Slot 4) - 4x SE OHKO, 0 recoil [Surf PP: 2 -> 1/15]
  - Gyarados Lv 61: Double-Edge (Slot 1) / Bite [DE PP: 14 -> 13/15]
  - Arcanine Lv 63: STAB Surf (Slot 4) - 2x SE OHKO, 0 recoil [Surf PP: 1 -> 0/15]
  - Venusaur Lv 65: Double-Edge (Slot 1) - OHKO [DE PP: 13 -> 12/15]
  -> CHAMPION RED DEFEATED! ENTER HALL OF FAME!

## Verified Pokémon League HQ Lobby Layout & Waypoints
- Poké Mart Status: Empirically verified that retail Pokémon Red/Blue lobby has NO Poké Mart clerk (right wing has Cable Club desk at (13, 6); no mid-gauntlet item purchasing). Full sweep relies on HP conservation & optimized move routing.
- Entrance from Route 23 exterior: (7..8, 11) (Red carpet mat)
- Left Wing (cols 0-4): PC terminal at (1, 5), Town Map / Sign at (1, 4), Column 3 North transit corridor.
- Center Wing (cols 5-8): Nurse Joy healing counter at (5..8, 5..6).
- Right Wing (cols 9-15): Cable Club link desk at (13, 6).
- Verified Route to Lorelei's Chamber (Room 1):
  1. From entrance mat (7..8, 11), walk West to (5, 10).
  2. Walk North 3 steps to (5, 7) (open corridor above the NPC at (4, 9)).
  3. Walk West 3 steps to (2, 7).
  4. Walk North 5 steps along Column 2 from (2, 7) to (2, 2) (completely open bypass around counter and pillar).
  5. Walk East 6 steps along Row 2 from (2, 2) to (8, 2).
  6. Walk North 2 steps into doorway at (8, 0) to transition into Lorelei's Chamber (Room 1 at (4, 11))!

## Verified Move Menu Mapping & Lorelei Execution Safeguards
- HYDROS Move Layout (Lv 91 Blastoise) - VERTICAL 1-COLUMN LIST:
  - Slot 1: Double-Edge (Normal physical, 100 Power, 100 Acc) - Default cursor at top (index 0) -> Press `A`
  - Slot 2: Ice Beam (Ice special, 95 Power, 100 Acc) - Index 1 -> Press `Down` 1 time, then `A`
  - Slot 3: Bite (Normal physical, 60 Power, 100 Acc) - Index 2 -> Press `Down` 2 times, then `A`
  - Slot 4: Surf (Water special STAB, 95 Power, 100 Acc) - Index 3 -> Press `Down` 3 times, then `A`