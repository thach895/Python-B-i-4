product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20,
        "sold": 5
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 8,
        "sold": 3
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 3,
        "sold": 7
    }
]

while True:
    print("\n===== HỆ THỐNG VẬN HÀNH CỬA HÀNG YODY =====")
    print("1. Hiển thị danh sách sản phẩm và cảnh báo tồn kho")
    print("2. Bán sản phẩm cho khách hàng")
    print("3. Nhập thêm hàng vào kho")
    print("4. Xem báo cáo doanh thu")
    print("5. Thoát chương trình")

    choice = input("Nhập lựa chọn: ")

    match choice:

        case "1":
            if len(product_list) == 0:
                print("Danh sách sản phẩm hiện đang trống.")
            else:
                print("\nDanh sách sản phẩm hiện tại:")

                for i in range(len(product_list)):
                    product = product_list[i]

                    if product["quantity"] == 0:
                        status = "Hết hàng"
                    elif product["quantity"] <= 5:
                        status = "Sắp hết hàng"
                    else:
                        status = "Còn hàng"

                    print(
                        f"{i + 1}. Mã SP: {product['product_id']} | "
                        f"Tên: {product['product_name']} | "
                        f"Giá: {product['price']} | "
                        f"Tồn kho: {product['quantity']} | "
                        f"Đã bán: {product['sold']} | "
                        f"Trạng thái: {status}"
                    )

        case "2":
            product_id = input(
                "Nhập mã sản phẩm khách muốn mua: "
            ).strip().upper()

            quantity_buy = input(
                "Nhập số lượng khách mua: "
            )

            if not quantity_buy.isdigit():
                print("Số lượng mua/Nhập kho không hợp lệ")
                continue

            quantity_buy = int(quantity_buy)

            if quantity_buy <= 0:
                print("Số lượng mua/Nhập kho không hợp lệ")
                continue

            found = False

            for product in product_list:
                if product["product_id"] == product_id:
                    found = True

                    if quantity_buy > product["quantity"]:
                        print("Số lượng trong kho không đủ để bán")
                        break

                    product["quantity"] -= quantity_buy
                    product["sold"] += quantity_buy

                    total_money = quantity_buy * product["price"]

                    print("Bán hàng thành công")
                    print(
                        f"Số tiền khách cần thanh toán: {total_money}"
                    )

                    break

            if not found:
                print("Không tìm thấy sản phẩm cần bán")

        case "3":
            product_id = input(
                "Nhập mã sản phẩm cần nhập thêm: "
            ).strip().upper()

            quantity_import = input(
                "Nhập số lượng nhập thêm: "
            )

            if not quantity_import.isdigit():
                print("Số lượng mua/Nhập kho không hợp lệ")
                continue

            quantity_import = int(quantity_import)

            if quantity_import <= 0:
                print("Số lượng mua/Nhập kho không hợp lệ")
                continue

            found = False

            for product in product_list:
                if product["product_id"] == product_id:
                    found = True

                    product["quantity"] += quantity_import

                    print("Nhập kho thành công")

                    break

            if not found:
                print("Không tìm thấy sản phẩm cần nhập kho")

        case "4":
            total_revenue = 0
            max_sold = 0
            best_seller = ""

            has_revenue = False

            print("\n===== BÁO CÁO DOANH THU CỬA HÀNG YODY =====")

            for i in range(len(product_list)):
                product = product_list[i]

                revenue = (
                    product["price"] * product["sold"]
                )

                total_revenue += revenue

                if product["sold"] > 0:
                    has_revenue = True

                print(
                    f"{i + 1}. {product['product_name']} | "
                    f"Đã bán: {product['sold']} | "
                    f"Doanh thu: {revenue}"
                )

                if product["sold"] > max_sold:
                    max_sold = product["sold"]
                    best_seller = product["product_name"]

            if not has_revenue:
                print("Chưa có doanh thu phát sinh.")
            else:
                print(f"\nTổng doanh thu: {total_revenue}")
                print(
                    f"Sản phẩm bán chạy nhất: {best_seller}"
                )

        case "5":
            print("Thoát chương trình.")
            break

        case _:
            print(
                "Lựa chọn không hợp lệ, vui lòng nhập lại!"
            )