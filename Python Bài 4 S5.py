
number_of_rooms = int(input("Nhập số lượng phòng học: "))

if number_of_rooms <= 0:
    print("Số lượng phòng học không hợp lệ")

else:

    for room in range(1, number_of_rooms + 1):

        print(f"\n===== Phòng học {room} =====")

        number_of_rows = int(input("Nhập số hàng ghế: "))

        seats_per_row = int(input("Nhập số ghế mỗi hàng: "))

        if number_of_rows <= 0 or seats_per_row <= 0:
            print("Dữ liệu phòng học không hợp lệ. Bỏ qua phòng này")
            continue

        if number_of_rows > 10 or seats_per_row > 10:
            print("Phòng quá lớn. Dừng nhập dữ liệu")
            break

        print("\nSơ đồ chỗ ngồi:")

        for row in range(number_of_rows):

            for seat in range(seats_per_row):
                print("*", end="")

            print()