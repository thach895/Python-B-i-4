import re


class MenuItem:
    service_charge = 0.0

    def __init__(self, item_id, item_name, base_price):
        self.item_id = item_id
        self.item_name = item_name.title()
        self.__base_price = base_price
        self.__is_available = True

    @property
    def base_price(self):
        return self.__base_price

    @base_price.setter
    def base_price(self, new_price):
        if new_price <= 0:
            print("Giá đồ uống phải lớn hơn 0!")
            print("Giá cũ được giữ nguyên.")
            return

        self.__base_price = new_price

    @property
    def is_available(self):
        return self.__is_available

    def toggle_availability(self):
        self.__is_available = not self.__is_available

    def calculate_selling_price(self):
        return int(
            self.__base_price
            + self.__base_price * MenuItem.service_charge
        )

    @classmethod
    def update_service_charge(cls, new_rate):
        if new_rate >= 0:
            cls.service_charge = new_rate

    @staticmethod
    def is_valid_item_id(item_code):
        pattern = r"^[A-Z]{2}\d{2}$"
        return bool(re.match(pattern, item_code))


menu_db = [
    MenuItem("CF01", "Cà Phê Đen", 30000),
    MenuItem("CF02", "Bạc Xỉu", 45000),
    MenuItem("TE01", "Trà Đào Cam Sả", 50000)
]


def find_item(item_id):
    for item in menu_db:
        if item.item_id == item_id:
            return item
    return None


while True:
    print("\n===== HỆ THỐNG QUẢN LÝ THỰC ĐƠN RIKKEI COFFEE =====")
    print("1. Xem thực đơn & Giá niêm yết")
    print("2. Thêm món mới vào menu")
    print("3. Cập nhật trạng thái (Hết hàng/Còn hàng)")
    print("4. Điều chỉnh giá gốc của món")
    print("5. Cập nhật phụ phí dịch vụ toàn hệ thống")
    print("6. Thoát chương trình")
    print("======================================================")

    choice = input("Chọn chức năng (1-6): ")

    if choice == "1":
        print("\n--- THỰC ĐƠN RIKKEI COFFEE ---")

        for index, item in enumerate(menu_db, start=1):
            status = (
                "Đang bán"
                if item.is_available
                else "Hết hàng"
            )

            print(
                f"{index}. "
                f"Mã: {item.item_id} | "
                f"Tên: {item.item_name:<15} | "
                f"Trạng thái: {status:<10} | "
                f"Giá niêm yết: "
                f"{item.calculate_selling_price():,} VNĐ"
            )

    elif choice == "2":
        print("\n--- THÊM MÓN MỚI VÀO MENU ---")

        item_id = input("Nhập mã món: ").strip()

        if not MenuItem.is_valid_item_id(item_id):
            print("\nMã món không hợp lệ!")
            print(
                "Mã món phải gồm 2 chữ cái "
                "in hoa và 2 chữ số."
            )
            print("Ví dụ: CF01.")
            continue

        if find_item(item_id):
            print("\nMã món đã tồn tại!")
            continue

        item_name = input("Nhập tên món: ")

        try:
            base_price = int(
                input("Nhập giá gốc: ")
            )
        except ValueError:
            print("Giá không hợp lệ!")
            continue

        if base_price <= 0:
            print("Giá đồ uống phải lớn hơn 0!")
            continue

        menu_db.append(
            MenuItem(item_id, item_name, base_price)
        )

        print("\nThêm món mới thành công!")

    elif choice == "3":
        print("\n--- CẬP NHẬT TRẠNG THÁI MÓN ---")

        item_id = input(
            "Nhập mã món cần cập nhật: "
        ).strip()

        item = find_item(item_id)

        if not item:
            print("Không tìm thấy món!")
            continue

        item.toggle_availability()

        if item.is_available:
            print(
                f">> Đã cập nhật "
                f"{item.item_name} thành ĐANG BÁN!"
            )
        else:
            print(
                f">> Đã cập nhật "
                f"{item.item_name} thành HẾT HÀNG!"
            )

    elif choice == "4":
        print(
            "\n--- ĐIỀU CHỈNH GIÁ GỐC CỦA MÓN ---"
        )

        item_id = input(
            "Nhập mã món cần đổi giá: "
        ).strip()

        item = find_item(item_id)

        if not item:
            print("Không tìm thấy món!")
            continue

        try:
            new_price = int(
                input("Nhập giá tiền mới: ")
            )
        except ValueError:
            print("Giá không hợp lệ!")
            continue

        old_price = item.base_price

        item.base_price = new_price

        if item.base_price != old_price:
            print("Cập nhật giá gốc thành công!")

    elif choice == "5":
        print(
            "\n--- CẬP NHẬT PHỤ PHÍ DỊCH VỤ "
            "TOÀN HỆ THỐNG ---"
        )

        print(
            f"Phụ phí hiện tại: "
            f"{MenuItem.service_charge * 100:.0f}%"
        )

        try:
            new_rate = float(
                input(
                    "Nhập phụ phí mới "
                    "(VD 0.1 = 10%): "
                )
            )
        except ValueError:
            print("Dữ liệu không hợp lệ!")
            continue

        MenuItem.update_service_charge(new_rate)

        print(
            "Cập nhật phụ phí dịch vụ "
            "thành công!"
        )

    elif choice == "6":
        print(
            "\nCảm ơn bạn đã sử dụng "
            "hệ thống Rikkei Coffee!"
        )
        break

    else:
        print("Vui lòng chọn từ 1 đến 6.")