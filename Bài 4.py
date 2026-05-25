print("===== HỆ THỐNG TIẾP NHẬN SINH HIỆU =====")

# Nhập dữ liệu
patient_id = input("Nhập mã bệnh nhân: ")

temp_input = input("Nhập nhiệt độ cơ thể: ")
heart_input = input("Nhập nhịp tim: ")

# Chuẩn hóa dữ liệu
temperature = float(temp_input)
heart_rate = int(heart_input)

# Hiển thị kết quả
print("\n===== KẾT QUẢ CHUẨN HÓA DỮ LIỆU =====")

print("Mã bệnh nhân:", patient_id)

print("Nhiệt độ cơ thể:", temperature, "độ C")
print("Kiểu dữ liệu hệ thống ghi nhận:", type(temperature))

print("Nhịp tim:", heart_rate, "nhịp/phút")
print("Kiểu dữ liệu hệ thống ghi nhận:", type(heart_rate))

print("\nThông báo: Dữ liệu hợp lệ. Màn hình Monitor đã sẵn sàng kết nối!")