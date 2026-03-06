# grep.py

def grep(pattern, flags, files):
    flag_set = set(flags.split()) if flags else set()

    show_line_numbers = "-n" in flag_set
    show_file_names_only = "-l" in flag_set
    case_insensitive = "-i" in flag_set
    invert_match = "-v" in flag_set
    match_entire_line = "-x" in flag_set

    multiple_files = len(files) > 1
    results = []

    def matches(line: str) -> bool:
        text = line
        target = pattern

        if case_insensitive:
            text = text.lower()
            target = target.lower()

        if match_entire_line:
            ok = text == target
        else:
            ok = target in text

        return not ok if invert_match else ok

    for filename in files:
        matched_this_file = False

        with open(filename) as f:
            for line_number, raw_line in enumerate(f, start=1):
                line = raw_line.rstrip("\n")

                if matches(line):
                    if show_file_names_only:
                        matched_this_file = True
                        break

                    parts = []
                    if multiple_files:
                        parts.append(filename)
                    if show_line_numbers:
                        parts.append(str(line_number))
                    parts.append(line)

                    results.append(":".join(parts))

        if show_file_names_only and matched_this_file:
            results.append(filename)

    return "".join(result + "\n" for result in results)