from .dark_spellbook import dark_spell_allowed_ingredients

def dark_validate_ingredients(ingredients : str) -> str:
    low_ingredients = ingredients.lower()
    for i in dark_spell_allowed_ingredients():
        if i in low_ingredients:
            return (f'{ingredients} - VALID')
    return (f'{ingredients} - INVALID')