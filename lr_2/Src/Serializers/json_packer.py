def to_str(item):
    if isinstance(item, dict):
        strings = []
        for key, value in item.items():
            strings.append(f"{to_str(key)}:{to_str(value)},")
        return f"{{{''.join(strings)[:-1]}}}"
    if isinstance(item, str):
        string = item.translate(str.maketrans({
            "\"": r"\"",
            "\\": r"\\",
        }))
        return f"\"{string}\""
    if item is None:
        return "null"

    return str(item)
