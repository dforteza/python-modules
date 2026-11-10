from .light_spellbook import light_spell_allowed_ingredients

def validate_ingredients(ingredients : str) -> str:
    low_ingredients = ingredients.lower()
    for i in light_spell_allowed_ingredients():
        if i in low_ingredients:
            return (f'{ingredients} - VALID')
    return (f'{ingredients} - INVALID')