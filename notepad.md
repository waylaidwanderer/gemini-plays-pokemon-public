# Pokémon Crystal Playthrough
- Started: Friday, January 16, 2026

### Current Status
- **Location**: Olivine City (Map 1_14).
- **Goal**: Heal party at Olivine Pokemon Center.
- **Next Step**: Descend to 1F -> Exit Lighthouse -> Pokemon Center.

### Objectives
- **Primary**: Obtain SecretPotion from Cianwood Pharmacy.
- **Secondary**: Heal Amphy at the Lighthouse.
- **Tertiary**: Return to Cianwood Pharmacy.

### Important Notes
- **Mechanic**: The Pokémon menu remembers the last cursor position. Re-entering it does NOT reset to Slot 1.
- **Mechanic**: Fly map uses List Selection (Up/Down) for towns, not spatial movement.
- **Critical Success**: Garnet (Typhlosion) retrieved! He is in Slot 6 (135/135 HP).
- **Immediate Goal**: Heal the rest of the team at the Pokemon Center.
- **Next Step**: Exit Center -> Buy Potions -> Return to Cianwood or call Jasmine?
- **Quest State**: Pharmacist in Cianwood only gave lore. Soft-lock suspicion. Plan: Talk to Jasmine again to reset/confirm flag.

### Lighthouse Navigation (For Ascent)
- **Map IDs**: 1F = 3_42, 2F = 3_43.
- **Route to Top**:
  1. **1F -> 2F**: Stairs at (3,11).
  2. **2F -> 3F**: Stairs at (5,3). (Verified marker exists).
  3. **3F -> 4F**: Stairs at (13,3) (Right Side).
  4. **4F -> 3F (Center)**: Drop down hole at (9,3) to reach 3F Center.
  5. **3F (Center) -> 4F (Center)**: Stairs at (9,5).
  6. **4F (Center) -> 5F (Center)**: Stairs at (9,7).
  7. **5F (Center) -> 6F**: Stairs at (9,15).
- **Reflection (Turn 19196)**: Recovered Typhlosion from PC bug. Currently trying to heal but got interrupted by Arnie. Need to finish healing, reorder party, and buy supplies.
- **Quest Status**: Pharmacist gave lore, no potion.
- **Hypothesis**: Must speak to Jasmine again to confirm the quest flag or trigger a specific dialogue state.
- **Immediate Plan**: Heal -> Reorder Party (Garnet lead) -> Mart -> Lighthouse (Talk to Jasmine).
- **Turn 19204**: Difficulty healing. Previous attempts with `advance_dialogue` failed to update HP. Attempting again with deliberate focus.
- **Plan**: Heal -> Party Menu (Garnet to Slot 1) -> Mart -> Lighthouse.