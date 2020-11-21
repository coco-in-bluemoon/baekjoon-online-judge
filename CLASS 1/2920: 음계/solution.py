def solution(notes):
    start_note = notes[0]
    if start_note not in [1, 8]:
        return 'mixed'

    status = 'ascending' if start_note == 1 else 'descending'

    NUM_NOTE = 8

    for index, note in enumerate(notes):
        if status == 'ascending':
            if note != (index + 1):
                return 'mixed'
        elif status == 'descending':
            if note != (NUM_NOTE - index):
                return 'mixed'

    return status


if __name__ == "__main__":
    notes = [1, 2, 3, 4, 5, 6, 7, 8]
    assert solution(notes) == 'ascending'

    notes = [8, 7, 6, 5, 4, 3, 2, 1]
    assert solution(notes) == 'descending'

    notes = [8, 1, 7, 2, 6, 3, 5, 4]
    assert solution(notes) == 'mixed'

    notes = list(map(int, input().split()))
    answer = solution(notes)
    print(answer)
