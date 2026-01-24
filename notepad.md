# Pokémon Crystal Playthrough
- Started: Friday, January 16, 2026
- Current Location: National Park (Map 3_15)

### Immediate Goals
1. **Find Floria**: Explore the North-East corner of the National Park.
2. **Find Exit to Route 36**: Likely in the North-East.
3. **Get SquirtBottle**: Return to Flower Shop after finding Floria.

### Quest Log
- **Badges**: Zephyr, Hive, Plain.
- **Party**: All Healthy (Garnet Poisoned).
- **Mail Quest**: Active.
- **Contest**: Not entered (lack of Sport Balls/Bug Catching logic).

### Strategic Notes
- **Poison Alert**: Garnet is poisoned. No Antidote in bag. Prioritize reaching a Pokemon Center (Violet City East?) or finding Floria quickly.
- **SquirtBottle**: Requires Plain Badge (Have), inspecting tree (Done), and finding Floria.
- **Map Intel**: "North Gate" at (25,3) was invalid. Heading South-East to find the East Exit (Route 36).
### Reflection (Turn 11510)
- **Tool Ideas**:
  1. `battle_agent`: Handle type matchups and move selection intelligently.
  2. `path_validator`: Verify if blocked paths are truly blocked or just unseen.
  3. `inventory_manager`: Automate healing/item usage.
  4. `dialogue_parser`: Extract quest info from logs.
  5. `move_learner`: Logic for learning new moves/forgetting old ones.
- **Battle Strategy**: Ensure move selection accounts for UI layout (Vertical List vs Grid). Visuals imply vertical list on this screen.