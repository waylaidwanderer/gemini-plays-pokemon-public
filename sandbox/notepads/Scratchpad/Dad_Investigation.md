# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Core Blockers & Status
- **Metro Turnstile**: Stepping onto (19, 21) triggers "I should find dad first!" and forces Asher 1 step down to (19, 22) (re-verified active Turn 15518).
- **Route 2 Gate**: Stepping onto (52, 19-22) triggers "I can't go yet... I have things to do!" (re-verified active Turn 15374).
- **Jackson Status**: Captured by Team Siara during tremor cutscene (Turn 1666). Marie broadcast radio retreat on Turn 2682. Jackson's whereabouts remain the central progression gate.

## Verified / Settled Locations
- **Sovio Metro Lobby**:
  - Timetable Board (columns 21-23): Verified Turns 7149, 14276-14278 as decorative flavor text ("It's a timetable showing various destinations!").
  - Platform Attendant at (22, 19): Inaccessible behind solid north brick wall at row 23; platform passage gated at turnstile (19, 21).
- **Global Storage Systems (Verified Turns 14291-14315)**: HuPhone Mailbox ('There's no Mail here.'), HuPhone Item Storage ('There are no items.'), and Someone's PC Box 1 (0 Pokémon) audited 100% empty. Party size/composition does not gate turnstile blocker.

## Active Hypotheses & Strategic Focus
- **Hypothesis D1 (Jackson / Valora Surface Progression Trigger Investigation)**:
  - **Rationale**: The Metro turnstile strictly blocks train boarding with 'I should find dad first!'. Jackson ran outside to investigate the tremor, and Team Siara retreated from the sewers. If Jackson is not in the audited sewer platform, either Jackson escaped to a surface location, an NPC holds critical dialogue regarding the tremor/Jackson, or a regional event flag must be triggered.
  - **Execution Record**:
    - Step 1 (Sovio Metro Lobby, Turn 15518): Turnstile passage at (19, 21) tested directly; confirmed strictly blocked by scripted trigger 'I should find dad first!' forcing 1 step Down to (19, 22). Zero NPCs present in lobby.
    - Step 2 (Sovio Pokémon Center, Turns 15526-15530): Straw-hat Camper at (5, 7) re-checked with zero active quests; confirmed ambient joke dialogue regarding Weedle ('Ironic isn't it?'). Boy at (8, 6) confirmed ambient PC tutorial dialogue.
    - Step 3 (Route 1 & Lancio Town Regional Investigation - IN PROGRESS, Turn 15542+): Transitioned onto Route 1 at (53, 4). Moving southwest to Lancio Town to test 3 specific falsifiable hypotheses:
      (a) Ivo Lab Basement Stairs (12, 7): Test if barrier text ('I probably shouldn't head down here...') has updated post-sewer clearing.
      (b) Lancio Harbor Dock (32-34, 25): Test if Harry or ferry transport has returned to provide passage to Inizio Isle.
      (c) Route 1 / Lancio Field Moves: Re-evaluate Cut Tree at (5, 44) and check town residents for field ability equipment.

## Settled Hypotheses
- **Hypothesis SS3 (Eastern Storage Room Platform - 100% SETTLED & ARCHIVED)**:
  - Status: Settled Turn 15480. Red mat at (37, 14) confirms text "Its a simple storage room..." facing South (Turn 15470) and solid south void collision with zero warp (Turn 15472). Platform perimeter walls (rows 11-15, cols 36-39) confirmed solid with inert 'A'. The storage room is an empty ambient set piece post-retreat; Jackson is definitively not here.
- **Hypothesis SS2 (Western Gauntlet & Lower Western Floor Probe - 100% SETTLED & ARCHIVED)**:
  - Status: Settled Turn 15341. Systematic boundary audit of rows 22-28, columns 6-19: (11, 28-26) floor, (11, 25) solid ledge, (10-6, 26) floor & puddle, (6, 26) west wall, (6, 27-28) floor, (6, 29) south void. Zero hidden rooms, NPCs, or progression triggers along audited corridors.
