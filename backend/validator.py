# validator.py

def validate_data(age, weight, height, sleep):

    if age < 15 or age > 80:
        return False

    if weight < 20 or weight > 200:
        return False

    if height < 100 or height > 250:
        return False

    if sleep < 1 or sleep > 15:
        return False
    return True