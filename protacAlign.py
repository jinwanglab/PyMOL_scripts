from pymol import cmd, stored


def protacAlign(sel1, sel2, protac):

    # align warhead with target protein
    # 4172, RIPK1T2I

    cmd.select("select_warhead_1", protac + " and name N34")
    cmd.select("select_warhead_2", protac + " and name N33")
    cmd.select("select_warhead_3", protac + " and name N35")
    cmd.select("select_warhead_4", protac + " and name C4")
    cmd.select("select_warhead_5", protac + " and name C6")
    cmd.select("select_target_1", sel1 + " and name N1")
    cmd.select("select_target_2", sel1 + " and name N2")
    cmd.select("select_target_3", sel1 + " and name N3")
    cmd.select("select_target_4", sel1 + " and name C5")
    cmd.select("select_target_5", sel1 + " and name C2")

    cmd.pair_fit("select_target_1", "select_warhead_1",
                 "select_target_2", "select_warhead_2",
                 "select_target_3", "select_warhead_3",
                 "select_target_4", "select_warhead_4",
                 "select_target_5", "select_warhead_5")

    # clean up selection
    cmd.delete("select_warhead_1")
    cmd.delete("select_warhead_2")
    cmd.delete("select_warhead_3")
    cmd.delete("select_warhead_4")
    cmd.delete("select_warhead_5")
    cmd.delete("select_target_1")
    cmd.delete("select_target_2")
    cmd.delete("select_target_3")
    cmd.delete("select_target_4")
    cmd.delete("select_target_5")

    # align E3 ligand with E3ligase
    # 4172VHL
    cmd.select("select_E3ligand_1", protac + " and name C31")
    cmd.select("select_E3ligand_2", protac + " and name C7")
    cmd.select("select_E3ligand_3", protac + " and name N36")
    cmd.select("select_E3_1", sel2 + " and name CBG")
    cmd.select("select_E3_2", sel2 + " and name CAZ")
    cmd.select("select_E3_3", sel2 + " and resn 4YY and name N")

    cmd.pair_fit("select_E3_1", "select_E3ligand_1",
                 "select_E3_2", "select_E3ligand_2",
                 "select_E3_3", "select_E3ligand_3")

    cmd.delete("select_E3_1");
    cmd.delete("select_E3_2");
    cmd.delete("select_E3_3");
    cmd.delete("select_E3ligand_1");
    cmd.delete("select_E3ligand_2");
    cmd.delete("select_E3ligand_3")
