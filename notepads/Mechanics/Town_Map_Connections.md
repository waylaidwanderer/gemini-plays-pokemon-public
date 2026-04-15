Town Map Navigation Rules:
- The Town Map interface is node-based, not a free-roaming grid.
- The cursor snaps directly between valid city/town nodes.
- Do NOT guess long sequences of directional inputs. Instead, use single steps to systematically map and verify the connections between cities.
- TODO: Systematically map the directional connections between visited cities (e.g., 'From Pewter City, pressing Down goes to Viridian City') to ensure reliable future travel.
Fly Map Confirmed Connections:
- Pallet Town: Up->Viridian, Down->Fuchsia, Right->None, Left->None
- Viridian City: Up->Pewter, Down->Pallet, Right->None, Left->None
- Pewter City: Down->Viridian, Up->Cerulean, Right->None, Left->None
- Cerulean City: Down->Pewter, Up->None, Left->None, Right->None
- Fuchsia City: Up->Pallet, Down->None, Left->None, Right->None