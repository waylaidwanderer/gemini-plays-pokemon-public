# Post-Safari Zone Route & Progression Plan

## Historical Progress & Verification
- **Turn 73908**: Entered the real Warden's House (Map 0_155) at Fuchsia City (27, 27). Inside, the Warden is at (2, 3), and a pushable boulder is at (8, 4) blocking an item at (8, 3).
- **Turn 73918**: Talked to the Warden and delivered his Gold Teeth. Received **HM04 Strength**.
- **Turn 73929**: Taught HM04 Strength to ROCKY (GEODUDE) in our party.
- **Turn 73938**: Attempted to use ROCKY's STRENGTH field move from the Pokémon party menu while standing at (7, 4) in front of the boulder.
  - *Result*: The game displayed the text: "No! A new BADGE is required."
  - *Verification*: We currently possess 5 badges (Thunder Badge, Cascade Badge, Marsh Badge, Soul Badge, and Boulder Badge) but lack the Rainbow Badge. In Generation 1, the Rainbow Badge (obtained from Erika in Celadon City) is required to use Strength in the overworld.
  - *Conclusion*: We cannot push the boulder at (8, 4) yet. We must obtain the Rainbow Badge first.
- **Turns 74185-74198**: Challenged and defeated Erika at Celadon Gym, obtaining the **Rainbow Badge** and TM21 (Mega Drain).
- **Turns 74245-74267**: Successfully tested and documented Strength overworld boulder mechanics inside the Warden's House. Collected the blocked item at (8, 3), which was a **RARE CANDY**. Verified map transitions reset boulder positions and deactivate Strength.

## Next Target: Route 19, Route 20, and Cinnabar Island
- [ ] **Navigate to Seafoam Islands & Cinnabar Island**: Swim South along Route 19, then West along Route 20. Navigate through Seafoam Islands (Route 20) and continue West to Cinnabar Island.
- [ ] **Defeat Blaine**: Secure our 7th badge (Volcano Badge) at Cinnabar Gym.

## Cinnabar Mansion Deep B1F Routing & Switch Matrix (Turn 75675)
- **Active Exploration Mission**: Locate and retrieve the Secret Key.
- **Switch Matrix (State A vs. State B)**:
  - We currently have Statue 2 (2F, (2, 11)) in **State B** (Toggled).
  - This has opened Gate 1 (1F, (25, 13)) but closed Gate 4 (1F, (21, 17)) and Gate 5 (1F, (26, 27)).
  - To reach the basement (B1F), we must find the correct path. Historically, B1F is accessed via a pit on 3F.
  - The Secret Pit is at (11, 12) on 3F. This pit is currently blocked by Gate 2 (Col 11) being CLOSED.
  - Wait! To open Gate 2 on 3F, we need to find Statue 3 on 3F Left!
  - We are currently on 3F. We must systematically search 3F Left (southwest and northwest chambers) to find Statue 3 and toggle it.

## Empirical Badge Boost Audit PC Navigation Protocol (Turn 75675)
- **Objective**: Safely deposit BUGGY (Butterfree) and withdraw SLUDGY (Muk, Level 39) to conduct the Badge-Boost Multiplier Empirical Audit.
- **PC Navigation Sequence (Cinnabar PC, standing at (4, 3) facing Up)**:
  1. Press 'A' to boot up GEM's PC.
  2. Select `BILL'S PC` (cursor starts on it, press 'A').
  3. Select `DEPOSIT PKMN` (press Down once, then 'A').
  4. In the party list, navigate to BUGGY (index 4):
     - Press Down 3 times (moves from SPARKY -> ROCKY -> BIRBIE -> BUGGY).
     - **CRITICAL**: Confirm the cursor is pointing at BUGGY and NOT GEMMY (index 5).
     - Press 'A' to deposit BUGGY.
  5. Select `WITHDRAW PKMN` (press Up once from Deposit PKMN, or press 'A' on Withdraw PKMN).
  6. In Box 1, locate SLUDGY (Muk, Level 39) at index 1:
     - The cursor starts on index 1 (SLUDGY).
     - Press 'A' to withdraw SLUDGY.
  7. Select `SEE YA!` to log off and exit the PC.

## Cinnabar Gym Blaine Matchup Preparation Strategy
- **Opponent Profile**: Gym Leader Blaine utilizes a Fire-type lineup (typically Growlithe, Ponyta, Rapidash, Arcanine, all around Level 42-47).
- **Type Effectiveness**: Fire is weak to Water, Ground, and Rock (taking 2x damage).
- **GEMMY (Level 59 BLASTOISE) Offensive Plan**:
  - **Priority Move 1: SURF** (Water, Special, Power 95, 100% Accuracy).
    - *Calculation*: Benefitting from same-type attack bonus (STAB), base power becomes 142.5. Against Blaine's Fire-types, it deals 2x super-effective damage, yielding an effective base power of **285** with 100% accuracy.
    - *Utility*: This is our ultimate sweeping move. At Level 59, GEMMY's Special stat will guarantee a one-shot KO on every single member of Blaine's team, entirely eliminating combat RNG.
  - **Priority Move 2: HYDRO PUMP** (Water, Special, Power 120, 80% Accuracy).
    - *Utility*: While even more powerful (effective base power 360), its 80% accuracy introduces unnecessary miss risk. We will only use this if SURF PP is fully depleted.
  - **Priority Move 3: DIG** (Ground, Physical, Power 100, 100% Accuracy).
    - *Utility*: Ground is also 2x super-effective against Fire, but in Gen 1 DIG is a 2-turn move, giving opponents a turn to act or use status moves. SURF is infinitely more efficient.

## Cinnabar Island & Pokémon Mansion Prep Strategy (Turn 74754)

- **PP & HP Management**:
  - Heal the party fully at the Cinnabar Pokémon Center to restore all HP and PP.
  - Keep 7 Hyper Potions and 1 Full Restore in our bag for mid-exploration healing.
  - Retain the ELIXER to restore GEMMY's PP if needed during the deep exploration.
- **Cinnabar Mart Purchase Priorities**:
  - Purchase 2-3 **Escape Ropes** (for instant exit after finding the Secret Key).
  - Purchase 5-10 **Full Heals** (to cure status effects from wild Koffing/Weezing/Grimmer).
  - Purchase **Ultra Balls** (for high-level wild encounters).