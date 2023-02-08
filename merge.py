from pymol import cmd, stored

def merge(sel1, sel2):

    name1 = cmd.get_names("objects", 0, str(sel1))
    name2 = cmd.get_names("objects", 0, str(sel2))
    cmd.create(str(name1)+str(name2), sel1+" or "+sel2)

cmd.extend("merge", merge);