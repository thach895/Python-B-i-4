number_of_forms = int(input("Nhập số lượng phiếu đăng ký: "))

if number_of_forms <= 0:
    print("Số lượng phiếu đăng ký không hợp lệ")
else:

    for i in range(1, number_of_forms + 1):

        print(f"\nNhập phiếu đăng ký thứ {i}:")

        register_data = input()


        parts = register_data.split("|")

        if len(parts) != 4:
            print("Dữ liệu đăng ký không hợp lệ. Bỏ qua phiếu này")
            continue

        full_name = parts[0].strip().title()
        course_name = parts[1].strip().title()
        student_id = parts[2].strip().upper()
        email = parts[3].strip().lower()

        if "@" not in email:
            print("Email không hợp lệ. Bỏ qua phiếu này")
            continue

        if len(student_id) < 5:
            print("Mã học viên không hợp lệ. Bỏ qua phiếu này")
            continue

        course_code = course_name.upper().replace(" ", "-")
        confirm_code = student_id + "_" + course_code

        print("===== PHIẾU ĐĂNG KÝ ĐÃ CHUẨN HÓA =====")
        print(f"Học viên: {full_name}")
        print(f"Khóa học: {course_name}")
        print(f"Mã học viên: {student_id}")
        print(f"Email: {email}")
        print(f"Mã xác nhận: {confirm_code}")