def get_max_animal(animals: list[str])-> str:
    if not animals:
        return ""
    return max(animals, key = len)

if __name__ == "__main__":
    animals = ["cat", "snake", "elephant", "dog"]
    result = get_max_animal(animals)
    print(result)
    