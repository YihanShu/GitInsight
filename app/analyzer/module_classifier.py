def classify(files):
    if not files:
        return "Unknown"

    text = " ".join(files)

    if "Battery" in text:
        return "Battery"
    if "Power" in text:
        return "Power"
    if "SMBus" in text:
        return "SMBus"
    if "Keyboard" in text:
        return "Keyboard"

    return "General"