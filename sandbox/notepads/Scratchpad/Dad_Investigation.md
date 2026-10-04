# Scratchpad: Post-Tremor Investigation & Progression Hypotheses

## Core Active Progression Barriers
- **Metro Turnstile (19, 21)**: Scripted barrier triggers verbatim "I should find dad first!" and forces Asher south to (19, 22). Gates train platform to Amor City.
- **Route 2 Eastern Exit (52, 19-22)**: Scripted barrier triggers verbatim "I can't go yet... I have things to do!" and forces Asher west.

## Hypotheses & Test Protocols

### Hypothesis H1: Metro Station Lobby Fixtures Audit (Concluded Turn 26628)
- **Result**: Tested Timetable (23, 24), scanner pillars (18, 21 & 20, 21), turnstile gate (19, 21), and west seating (16, 22-24). Standard physical collision checks revealed no hidden items or direct 'A' triggers. Platform seats audited empty. Turnstile walk-over continues to display "I should find dad first!".

### Hypothesis H2: Route 1 Localized Survey (Concluded Turn 26693 - Falsified)
- **Result**: Bug Catcher Duke (45, 12), Lass Sonia (27, 15), Youngster Mike (29, 20), and Roadside Cottage boy (6, 7) all produced identical pre-tremor static dialogue. Falsification criteria met.
- **Conclusion**: Route 1 received zero post-tremor state changes. Backtracking south to Lancio Town is formally aborted. Investigation shifts focus away from southern overland routes toward unexamined systems and localized town triggers.

### Hypothesis H3: Sovio City Localized Triggers & Novel Interactions (Concluded - Falsified)
- **Premise**: Testing whether unexamined NPC interactions, inventory items, or system triggers in Sovio City advance the story state or reveal Jackson's whereabouts.
- **Protocol & Falsification Criteria**:
  1. Target A (Pokémon Center Camper at 5, 7): Concluded Turn 26716 - Falsified. Tested with Antidote in inventory; repeated static humor dialogue ("My weedle got poisoned... / Ironic isn't it?") with zero choice prompts or quest triggers.
  2. Target B (Central Park Couple at 33, 22 & 43-45, 23-26): Concluded Turn 26735 - Falsified. Interviewed blonde girl at (44, 26); repeated verbatim static text ("I'm supposed to meet someone here, but he doesn't seem to show up... Was I catfished?") with zero choice prompts or quest triggers. Both NPCs are static ambient humor.
  3. Target C (System & Inventory Items Audit): Concluded Turn 26741 - Falsified. Key Items pocket holds only HuPhone (registered to SELECT) and TM Case. Items pocket holds Potion, Poison Barb, Antidote. Zero event items, passes, or equipment present.
- **Hypothesis H3 Conclusion**: Falsified across all targets.

### Hypothesis H4: Sovio Sewers Eastern Storage Platform (Abandoned - Invalid)
- **Status**: Formally abandoned per critique and prior exhaustive multi-directional collision checks. Jackson was never imprisoned in the sewers (he investigated outside in Sovio City during the tremor, while sewer grunts awaited Marie). The storage door is a static scenery fixture. Sovio Sewers are fully exhausted for main story progression.

### Hypothesis H5: HuPhone Regional World Map & Destination Inspection (Active)
- **Premise**: Investigating unexplored menu capabilities and regional mechanics per critique. The HuPhone contains an interactive World Map with hover banners and a permanent marker pin on Solare Island. We are testing whether interacting with the World Map (hovering, pressing 'A' on towns/landmarks, testing Select/Start) reveals fast-travel options, story destination markers, or quest clues regarding Jackson's whereabouts.
- **Protocol**:
  1. Open HuPhone via SELECT button in Sovio City overworld (48, 18).
  2. Launch World Map app.
  3. Move cursor to examine key regional nodes: Solare Island (marker pin), Amor City, Sovio City, Lancio Town, Inizio Isle.
  4. Test button interactions ('A', 'Select', 'Start') on each location and record system responses.
- **World Map Findings (Turn 26780)**:
  - Hovering cursor over nodes updates top-left banner dynamically (e.g. "Amor City / Amor Dept.", "Sovio City / Metro Station", "Route 4", "Route 16").
  - The yellow marker pin with black tip represents the Player's current location (Asher at Sovio City), not a fixed story marker.
  - Pressing 'A' on location nodes is completely inert: zero menus, zero fast-travel prompts. World Map is a passive navigational reference.