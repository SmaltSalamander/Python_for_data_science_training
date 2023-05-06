def all_thing_is_obj(object: any) -> int:
    output = object.__class__.__name__.capitalize()
    if isinstance(object, str):
        output = f"{object} is in the kitchen"
    if isinstance(object, (list, dict, tuple, set, str)):
        print(f"{output} : {type(object)}")
    else:
        print("Type not found")
    return 42
