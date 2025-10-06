def name_subst(name, text):
    return text.replace("ZZZ", name)

sallie = name_subst("Sallie", "My friend, ZZZ, won an award.")
print(sallie)

print(name_subst("Fred", "Jamie and ZZZ flew over the trees."))