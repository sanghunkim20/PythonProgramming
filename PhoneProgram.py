friends = []

def print_friends():
    if friends:
        print("친구 목록:")
        for friend in friends:
            print(f"이름: {friend['name']}, 전화번호: {friend['phone_number']}, 이메일: {friend['email']}")
    else:
        print("친구가 없습니다.")

def add_friend():
    name = input("추가할 친구의 이름을 입력하세요: ")
    phone_number = input("전화번호를 입력하세요: ")
    email = input("이메일을 입력하세요: ")
    friends.append({'name': name, 'phone_number': phone_number, 'email': email})
    print("친구가 추가되었습니다.")

def edit_friend():
    name = input("수정할 친구의 이름을 입력하세요: ")
    for friend in friends:
        if friend['name'] == name:
            friend['name'] = input("새로운 이름을 입력하세요: ")
            friend['phone_number'] = input("새로운 전화번호를 입력하세요: ")
            friend['email'] = input("새로운 이메일을 입력하세요: ")
            print("친구 정보가 수정되었습니다.")
            return
    print("해당하는 이름의 친구를 찾을 수 없습니다.")

def delete_friend():
    name = input("삭제할 친구의 이름을 입력하세요: ")
    for friend in friends:
        if friend['name'] == name:
            friends.remove(friend)
            print("친구가 삭제되었습니다.")
            return
    print("해당하는 이름의 친구를 찾을 수 없습니다.")

def main():
    while True:
        print("\n1. 친구 출력")
        print("2. 친구 추가하기")
        print("3. 친구 수정하기")
        print("4. 친구 삭제하기")
        print("5. 종료")

        choice = input("메뉴를 선택하세요: ")

        if choice == '1':
            print_friends()
        elif choice == '2':
            add_friend()
        elif choice == '3':
            edit_friend()
        elif choice == '4':
            delete_friend()
        elif choice == '5':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()
