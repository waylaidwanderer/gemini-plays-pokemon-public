# Post-Safari Zone Route & Progression Plan

## Historical Progress & Verification
- **Turn 73908**: Entered the real Warden's House (Map 0_155) at Fuchsia City (27, 27). Inside, the Warden is at (2, 3), and a pushable boulder is at (8, 4) blocking an item at (8, 3).
- **Turn 73918**: Talked to the Warden and delivered his Gold Teeth. Received **HM04 Strength**.
- **Turn 73929**: Taught HM04 Strength to ROCKY (GEODUDE) in our party.
- **Turn 73938**: Attempted to use ROCKY's STRENGTH field move from the Pokémon party menu while standing at (7, 4) in front of the boulder.
  - *Result*: The game displayed the text: "No! A new BADGE is required."
  - *Verification*: We currently possess 5 badges (Thunder Badge, Cascade Badge, Marsh Badge, Soul Badge, and Boulder Badge) but lack the Rainbow Badge. In Generation 1, the Rainbow Badge (obtained from Erika in Celadon City) is required to use Strength in the overworld.
  - *Conclusion*: We cannot push the boulder at (8, 4) yet. We must obtain the Rainbow Badge first.

## New Progression Route: Fuchsia City & Warden's House
2. **Return to Fuchsia City**: Fly back to Fuchsia City.
3. **Obtain Warden's House Item**: Enter Warden's House (Map 0_155), activate Strength, push the boulder at (8, 4), and retrieve the item at (8, 3).

## Combat Preparation & Navigation Plan
- **Gym Leader Erika's Lineup**: Victreebel (L29), Tangela (L24), Vileplume (L29).
- **Combat Strategy (Verified Turn 74102)**:
  - **Type Effectiveness Analysis**: Erika's team consists of Victreebel (Grass/Poison), Tangela (Grass), and Vileplume (Grass/Poison).
    - **DIG (Ground-type)**: Neutral (1x) against Grass/Poison (super-effective on Poison, resisted by Grass). However, it is resisted (0.5x) by pure Grass-type Tangela.
    - **BITE (Normal-type in Gen 1)**: Deals physical neutral (1x) damage against all of Erika's team.
    - **FLY (Flying-type, BIRBIE)**: Deals 2x super-effective damage against Grass-type, but BIRBIE (Level 18) is too low-level (vs Erika's Level 24-29) and fragile to survive.
  - **Tactical Decision**: We will rely strictly on GEMMY's (Level 59 BLASTOISE) neutral physical **BITE** to sweep Erika's entire team. GEMMY's massive level advantage renders type-disadvantage negligible, and BITE's high physical damage is the safest and most reliable strategy.
- **Gym Navigation & Obstacles**: Celadon Gym is located in the south of Celadon City. The path to the gym is blocked by a cuttable tree. PETAL (BELLSPROUT) is in our active party and knows **CUT**, allowing us to clear the tree and enter the Gym immediately.

## Scientific Strength Persistence & Boulder Mechanics Test Protocol (Turn 74245)
- **Objective**: Verify and document the exact overworld mechanics of STRENGTH in Gen 1, including activation, push behavior, and map transition persistence/reset rules.
- **Hypothesis**:
  1. Without STRENGTH active, the boulder at (8, 4) is completely impassable and cannot be pushed.
  2. Activating STRENGTH from the party menu (ROCKY) enables overworld boulder pushing. Walking directly into the boulder at (8, 4) from (7, 4) will push it to (9, 4).
  3. Map transition (exiting the Warden's House and re-entering) will reset the boulder to its starting position (8, 4) and deactivate the overworld STRENGTH state.
- **Step-by-step Log**:
  - **Turn 74245**: Standing at (4, 7). Walk to (7, 4) and face Right.
  - **Turn 74247**: Baseline Test. Standing at (7, 4) facing Right, we pressed Right to walk into the boulder at (8, 4) without Strength active.
    - *Result*: Movement blocked (visited 0 tiles), player remained at (7, 4). This proves that the boulder is solid and impassable by default. Baseline established!
  - **Turn 74258**: Standing at (8, 4) facing Up, we pressed A.
    - *Result*: Successfully picked up the overworld Poké Ball at (8, 3), which was a **RARE CANDY**.
  - **Turn 74261**: Initiating Map Transition Test to verify boulder coordinates and Strength state deactivation. Walked Left 4 times and Down 4 times to exit the Warden's House to Fuchsia City.