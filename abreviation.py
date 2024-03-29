import keyboard
#pour arrêter le programme : keyboard.unhook_all()

# on trie les abréviations par ordre alphabétique
# A
keyboard.add_abbreviation("ajd", "aujourd'hui ")

# B
keyboard.add_abbreviation("bv", "bien vu ")
keyboard.add_abbreviation("bcp", "beaucoup ")

# C
keyboard.add_abbreviation("cad", "c'est à dire ")
keyboard.add_abbreviation("cest", "c'est ")
keyboard.add_abbreviation("c", "c'est ")
keyboard.add_abbreviation("ca", "ça ")
keyboard.add_abbreviation("cine", "cinéma ")
keyboard.add_abbreviation("ciné", "cinéma ")

# D
keyboard.add_abbreviation("dc", "donc ")
keyboard.add_abbreviation("dvpt", "développement ")
keyboard.add_abbreviation("dp", "du coup ")
keyboard.add_abbreviation("ds", "dans ")
keyboard.add_abbreviation("deja", "déjà ")

# E

# F
keyboard.add_abbreviation("ft", "fait ")

# G
keyboard.add_abbreviation("gd", "grand")
keyboard.add_abbreviation("gds", "grands")
keyboard.add_abbreviation("gde", "grande")
keyboard.add_abbreviation("gdes", "grandes")
keyboard.add_abbreviation("gg", "bien joué ")
keyboard.add_abbreviation("grv", "grave ")
keyboard.add_abbreviation("gauvain", "Gauvain ")

# H

# I
keyboard.add_abbreviation("imprt", "important ")

# J
keyboard.add_abbreviation("jms", "jamais ")
keyboard.add_abbreviation("jsp", "je ne sais pas ")
keyboard.add_abbreviation("jss", "je sais ")
keyboard.add_abbreviation("jpp", "je ne peux pas ")

# K

# L
keyboard.add_abbreviation("l'aprem", "l'après-midi ")
keyboard.add_abbreviation("lucie", "Lucie ")
keyboard.add_abbreviation("lucas", "Lucas ")
keyboard.add_abbreviation("lola", "Lola ")

# M
keyboard.add_abbreviation("milan", "Milan ")
keyboard.add_abbreviation("mm", "même ")
keyboard.add_abbreviation("ms", "mais ")
keyboard.add_abbreviation("mcdo", "McDo ")
keyboard.add_abbreviation("maelys", "Maëlys ")

# N
keyboard.add_abbreviation("nn", "non ")
keyboard.add_abbreviation("ns", "nous ")

# O
keyboard.add_abbreviation("oe", "ouais ")

# P
keyboard.add_abbreviation("pk", "pourquoi ")
keyboard.add_abbreviation("ps", "pas ")
keyboard.add_abbreviation("pr", "pour ")
keyboard.add_abbreviation("pdt", "pendant ")
keyboard.add_abbreviation("ptr", "peut-être ")
keyboard.add_abbreviation("pt", "point ")

# Q
keyboard.add_abbreviation("qqc", "quelque chose ")
keyboard.add_abbreviation("qqun", "quelqu'un ")
keyboard.add_abbreviation("qd", "quand ")

# R

# S
keyboard.add_abbreviation("srmt", "surement ")
keyboard.add_abbreviation("srt", "surtout ")
keyboard.add_abbreviation("st", "sont ")
keyboard.add_abbreviation("ss", "suis ")
keyboard.add_abbreviation("svt", "SVT ")
keyboard.add_abbreviation("spc", "SPC ")

# T
keyboard.add_abbreviation("tjs", "toujours ")
keyboard.add_abbreviation("tt", "tout ")
keyboard.add_abbreviation("ts", "tous ")
keyboard.add_abbreviation("tps", "temps ")

# U

# V
keyboard.add_abbreviation("vrmt", "vraiment ")
keyboard.add_abbreviation("vs", "vous ")

# W

# X

# Y

# Z

stop = False
while not stop:
    stop = input("if you want to stop replacements, write 'stop' and press enter ")
    
    if stop == "stop":
        stop = True
    else:
        stop = False

keyboard.unhook_all()