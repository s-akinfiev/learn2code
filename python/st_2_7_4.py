# rect_width, rect_height, w, h = map(int, input().split())

# width_count = (rect_width % w != 0) * (rect_height // h)
# height_count = (rect_height % h != 0) * (rect_width // w)
# total = width_count + height_count + ((rect_width % w != 0) or (rect_height % h !=0))



import sys
from io import StringIO


code = '''
rect_width, rect_height, w, h = map(int, input().split())

width_count = (rect_width % w != 0) * (rect_height // h)
height_count = (rect_height % h != 0) * (rect_width // w)
total = width_count + height_count + ((rect_width % w != 0) and (rect_height % h !=0))

'''

if __name__ == '__main__':
    tests = (
        (1, 1, 1, 1, 0),
        (1, 1, 2, 2, 1),
        (2, 2, 1, 1, 0),
        (3, 2, 2, 3, 2),
        (4, 6, 2, 3, 0),
        (5, 6, 2, 3, 2),
        (6, 5, 2, 3, 3),
        (5, 5, 2, 2, 5),
        (5, 5, 3, 3, 3),
        (8, 8, 4, 2, 0),
        (8, 8, 3, 3, 5),
        (9, 4, 4, 2, 2),
        (9, 4, 2, 4, 1),
        (3, 3, 5, 5, 1),
        (1, 5, 2, 2, 3),
        (10, 3, 20, 2, 2),
        (10, 10, 3, 4, 6),
        (7, 3, 2, 3, 1),
        (7, 3, 3, 2, 4),
        (100, 100, 7, 9, 26),
    )

    passed = 0
    for *params, answer in tests:
        sys.stdin = StringIO(' '.join(map(str, params)))
        namespace = {}
        exec(code, namespace)
        result = namespace['total']

        if result == answer:
            passed += 1
        else:
            print(f'Входные данные {params}, ожидается {answer}, получено {result}')

    print(f'Пройдено {passed}/{len(tests)} тестов')