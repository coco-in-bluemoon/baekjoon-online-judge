def solution(hour, minute):
    minute_delta = 45

    MINUTE_PER_HOUR = 60
    HOUR_PER_DAY = 24

    hour_alarm = hour
    minute_alarm = minute - minute_delta

    if minute_alarm < 0:
        minute_alarm += MINUTE_PER_HOUR
        hour_alarm = hour - 1

    if hour_alarm < 0:
        hour_alarm += HOUR_PER_DAY

    return [hour_alarm, minute_alarm]


if __name__ == "__main__":
    assert solution(10, 10) == [9, 25]
    assert solution(0, 30) == [23, 45]
    assert solution(23, 40) == [22, 55]

    hour, minute = map(int, input().split())
    answer = solution(hour, minute)
    print('%d %d' % (answer[0], answer[1]))
