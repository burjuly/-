from operator import itemgetter

# Алгоритм:
# 1. Четным временным меткам присваиваем "start", нечетным -"end"
# 2. Считаем кол-во "start"
# 3. Если кол-во "start" == 3 и встречаем "end", то считаем дельту между текущим timestamp и предыдущим 

def appearance(intervals):
    tmp = sorted(intervals['tutor']) + sorted(intervals['pupil']) + sorted(intervals['lesson'])

    starts = [['start', value] for i, value in enumerate(tmp) if i % 2 == 0]
    ends = [['end', value] for i, value in enumerate(tmp) if i % 2 != 0]
    times = sorted(starts + ends, key=itemgetter(1))
 
    result, count_start = 0, 0
    for i, value in enumerate(times):
        if value[0] == 'start':
            count_start += 1
        else:
            if count_start == 3:
                result += times[i][1] - times[i - 1][1]
            count_start -= 1
    return(result)

tests = [
    {'data': 
        {'lesson': [1594663200, 1594666800],
        'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
        'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
        'answer': 3117},
    {'data': 
        {'lesson': [1594702800, 1594706400],
        'pupil': [1594702789, 1594704500, 1594702807, 1594704542,
            1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582,
            1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480,
            1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875,
            1594706502, 1594706503, 1594706524, 1594706524, 1594706579,
            1594706641],
        'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
        'answer': 3577},
    {'data': 
        {'lesson': [1594692000, 1594695600],
        'pupil': [1594692033, 1594696347],
        'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
        'answer': 3565 }
        ]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        expected_answer = test['answer']
        print(f'My answer {test_answer}, Expected answer {expected_answer}')
        #assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'