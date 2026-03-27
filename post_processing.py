"""Post-processing steps for translated subtitle files."""


def merge_absorbed_lines(events: list[dict]) -> list[dict]:
    """Merge empty translated dialogue lines into their neighbors.

    When the translator absorbs a line's content into a neighboring line,
    the absorbed line gets an empty translation. This extends the previous
    dialogue's end time to cover the absorbed line, then removes it.

    If an empty line has no previous dialogue (e.g. first line), it extends
    the next dialogue's start time backward instead.
    """
    # Find indices of empty dialogue lines
    empty_indices = set()
    for i, event in enumerate(events):
        if event["type"] == "Dialogue" and event["text"] == "":
            empty_indices.add(i)

    if not empty_indices:
        return events

    # For each empty line, merge timing into neighbor
    for i in sorted(empty_indices):
        # Find previous dialogue (non-empty)
        prev_idx = None
        for j in range(i - 1, -1, -1):
            if events[j]["type"] == "Dialogue" and j not in empty_indices:
                prev_idx = j
                break

        if prev_idx is not None:
            events[prev_idx]["end"] = events[i]["end"]
        else:
            # No previous dialogue — extend next dialogue's start backward
            for j in range(i + 1, len(events)):
                if events[j]["type"] == "Dialogue" and j not in empty_indices:
                    events[j]["start"] = events[i]["start"]
                    break

    # Remove empty lines
    merged = [e for i, e in enumerate(events) if i not in empty_indices]

    return merged
