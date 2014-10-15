from nan_expand import nan_expand


def iterations_of_nan_expand(expanded):
	new = "Not a "
	if expanded == "":
		c = 0
	elif new not in expanded:
		return False
	elif new in expanded:
		c = expanded.count(new)
	return c
	dif = nan_expand(c)
	if diff == expanded:
		return c
	else:
		return False

print(iterations_of_nan_expand("Show these people"))
