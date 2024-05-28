def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        
        # 중간 요소가 타겟 값인 경우
        if arr[mid] == target:
            return mid
        # 중간 요소가 타겟 값보다 작은 경우, 오른쪽 절반 탐색
        elif arr[mid] < target:
            left = mid + 1
        # 중간 요소가 타겟 값보다 큰 경우, 왼쪽 절반 탐색
        else:
            right = mid - 1
    
    # 타겟 값이 배열에 없는 경우
    return -1

# 예제 배열과 타겟 값
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 7
result = binary_search(arr, target)

if result != -1:
    print(f"타겟 값 {target}은(는) 인덱스 {result}에 있습니다.")
else:
    print(f"타겟 값 {target}을(를) 배열에서 찾을 수 없습니다.")
