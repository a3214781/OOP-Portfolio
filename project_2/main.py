from necromancer import Necromancer
from summoning_ritual import (
    skeleton_warrior_ritual,
    vengeful_ghost_ritual,
    putrid_zombie_ritual,
    phantom_guardian_ritual,
)

# create a necromancer with an initial collection of resources
print("=== Necromancer Game ===")
necromancer = Necromancer("Malachar", necrotic=15, spirit=15, bone=15, flesh=15, ectoplasm=40)
print(necromancer)
print()

# perform several successful summons
skeleton = necromancer.summon_undead(skeleton_warrior_ritual)
ghost = necromancer.summon_undead(vengeful_ghost_ritual)
print(f"Resources after summoning: {necromancer.inventory}")
print(f"Controlled undead: {len(necromancer.controlled_undead)}")
print()

# attempt a ritual that cannot currently be performed
failed_attempt = necromancer.summon_undead(phantom_guardian_ritual)
print(f"Summon result: {failed_attempt}")
print(f"Resources unchanged: {necromancer.inventory}")
print()

# collect additional resources and perform the ritual again
necromancer.collect_resources(necrotic=10, spirit=10, bone=10, flesh=10, ectoplasm=30)
print(f"Resources after collecting: {necromancer.inventory}")
guardian = necromancer.summon_undead(phantom_guardian_ritual)
print()

# level one controlled undead creature
if skeleton is not None:
    print(f"Before levelling: {skeleton}")
    necromancer.level_undead(skeleton.get_unit_id())
    print(f"After levelling:  {skeleton}")
print()

# dismiss one controlled undead creature
if ghost is not None:
    necromancer.dismiss_undead(ghost.get_unit_id())
print()

print(necromancer)


# inheritance check
'''
from undead import Undead, WarriorUndead, CursedUndead

print()
for undead in necromancer.controlled_undead:
    print(f"{undead.get_name()} is an Undead:", isinstance(undead, Undead))
print("skeleton is a WarriorUndead:", isinstance(skeleton, WarriorUndead))
print("guardian is a WarriorUndead:", isinstance(guardian, WarriorUndead) if guardian else "guardian was None")

if skeleton is not None:
    skeleton.command()
if guardian is not None:
    guardian.command()
'''