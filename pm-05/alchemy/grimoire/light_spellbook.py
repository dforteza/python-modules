def light_spell_allowed_ingredients():
	return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name, ingredients):
	from .light_validator import validate_ingredients

	result = validate_ingredients(ingredients)
	if "INVALID" in result:
		return f"Spell rejected: {spell_name} ({result})"
	return f"Spell recorded: {spell_name} ({result})"
