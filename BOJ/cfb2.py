import bisect


def min_moves_to_catch(teachers, david):
    # 선생님들의 위치를 이진 탐색하기 위해 정렬
    teachers.sort()

    # 이진 탐색을 통해 David 위치에 가까운 선생님을 찾음
    idx = bisect.bisect_left(teachers, david)

    # 가장 가까운 선생님과의 거리를 계산
    dist_left = float('inf') if idx == 0 else abs(teachers[idx - 1] - david)
    dist_right = float('inf') if idx == len(teachers) else abs(teachers[idx] - david)

    # 최소 이동 횟수 반환
    return min(dist_left, dist_right)


# 입력 처리
t = int(input())  # 테스트 케이스의 수
for _ in range(t):
    n, m, q = map(int, input().split())  # n: 셀의 수, m: 선생님 수, q: 쿼리 수
    teachers = list(map(int, input().split()))  # 선생님들의 위치
    queries = list(map(int, input().split()))  # David의 위치 쿼리들

    # 각 쿼리에 대해 결과 출력
    for david in queries:
        print(min_moves_to_catch(teachers, david))
