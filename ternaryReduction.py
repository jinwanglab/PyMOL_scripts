from pymol import cmd, stored
from tqdm import tqdm


def ternaryReduction(success_list: list):
    # Cleaning up ternary complexes with the same anchor points and directions. i.e., Remove redundancy
    print("Cleaning up similar ternary structures...")
    delete_set = set()

    for i in tqdm(range(1, len(success_list)), desc="Ternary Processing:", leave=True, ncols=100):
        tqdm.write("\n* Examining " + success_list[i])
        for j in range(0, i):
            if success_list[j] in delete_set:
                tqdm.write(str(success_list[j]) + " has already been in delete_list")
                continue

            rmsd = cmd.align(str(success_list[i]) + " and (chain A or chain P)", str(success_list[j]) +
                             " and (chain A or chain P)", cycles=0)[0]

            if rmsd >= 1:
                tqdm.write(
                    str(success_list[j]) + " has different structure with " + success_list[i] + ". RMSD = " + str(rmsd))
                cmd.align(str(success_list[i]) + " and chain A", str(success_list[j]) + " and chain A")
                # Different structures will be aligned with TargetProtein

            else:
                tqdm.write(str(success_list[i]) + " has similar structure with " + success_list[j] + ". RMSD = " + str(
                    rmsd) + ". Removing " + success_list[i] + "...")
                delete_set.add(success_list[i])
                break
    print("Objects to be deleted: " + str(delete_set))
    print(str(len(delete_set)) + " objects has been deleted \n")

    for ternary in delete_set:
        cmd.delete(ternary)

    output_ternary = cmd.get_object_list()[2:]
    print("Non-redundant ternary complexes: " + str(len(output_ternary)) + "\n")
