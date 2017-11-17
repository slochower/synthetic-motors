input_file = '../CSD/1540441.xyz'
bond_atom_names = ['C13', 'C14']
output_prefix = 'dihedral-'
scan_increment = 10


def make_file():
    with open(file_name, 'w') as f:
        f.write("import chimera\n")
        f.write("from chimera import runCommand as rc\n")
        f.write("from chimera import replyobj\n")
        f.write("import os\n")
        f.write("file_names = [fn for fn in os.listdir(\".\") if fn.endswith(\".pdb\")]\n")
        f.write("for fn in file_names[{}:{}]:\n".format(begin, end))
        f.write("       rc(\"open \" + fn)\n")
        f.write("       rc(\"color purple :UNK\")\n")
        f.write("       rc(\"color byhet\")\n")
        f.write("       rc(\"surf\")\n")


dihedral

for i in range...
    make_file...


from chimera import runCommand

open file

rotation 1 :16.b@ca,cb

rotation reverse 1 step
write()
