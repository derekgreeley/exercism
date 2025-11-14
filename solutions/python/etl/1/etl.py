def transform(legacy_data):
    new_point_structure = {}
    for point_value, letters in legacy_data.items():
        for letter in letters:
            new_point_structure[letter.lower()] = point_value
    return new_point_structure
