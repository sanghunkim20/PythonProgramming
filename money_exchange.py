def change_greedy(total_change, coin_types):
    count = 0
    for coin in coin_types:
        count += total_change // coin  # 사용할 수 있는 동전의 최대 개수
        total_change %= coin  # 남은 거스름돈 갱신
    return count

# 동전의 종류
coin_types = [500, 100, 50, 10]
# 거슬러 줘야 할 총 금액
total_change = 1260

# 거스름돈에 필요한 최소 동전의 개수를 계산
minimum_coins = change_greedy(total_change, coin_types)
print(f"거슬러 줘야 할 최소 동전의 개수: {minimum_coins}")
