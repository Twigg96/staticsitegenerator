def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            heading = line[1:]
            heading = heading.strip()
            return heading
    raise Exception("There is no h1")
