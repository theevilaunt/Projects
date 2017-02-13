def menu(wine, entree, dessert='jello'):
  return{'wine': wine, 'entree': entree, 'dessert': dessert}

print("%s" % menu('chardonnay', 'chicken', 'tiramisu'))

print("%s" % menu('chardonnay', 'chicken'))
