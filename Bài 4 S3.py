print("===== HỆ THỐNG KHAI BÁO NHÂN SỰ MỚI =====")

while True:

    new_employees = int(input(
        "Vui lòng nhập số lượng nhân sự mới trong tháng này: "
    ))

    if new_employees > 0:
        print("✅ Ghi nhận thành công!")
        print("Số nhân sự mới là:", new_employees)
        break
    else:
        print(" LỖI: Số lượng phải lớn hơn 0. Vui lòng nhập lại!")