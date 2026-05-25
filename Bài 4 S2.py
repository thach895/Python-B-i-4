

patient_age = int(input("Nhập tuổi bệnh nhân: "))

systolic_bp = int(
    input("Nhập huyết áp tâm thu (mmHg): ")
)

blood_sugar = int(
    input("Nhập đường huyết (mg/dL): ")
)


if patient_age < 0 or systolic_bp < 0 or blood_sugar < 0:

    print("\nLỖI: Dữ liệu nhập vào không hợp lệ.")

else:


    if patient_age < 75:

        if 90 <= systolic_bp <= 140:

            if blood_sugar < 150:

                print("\nKẾT QUẢ: ĐỦ ĐIỀU KIỆN PHẪU THUẬT")

            else:
                print(
                    "\nTỪ CHỐI PHẪU THUẬT: "
                    "Đường huyết quá cao."
                )

        else:
            print(
                "\nTỪ CHỐI PHẪU THUẬT: "
                "Huyết áp ngoài ngưỡng an toàn."
            )

    else:
        print(
            "\nTỪ CHỐI PHẪU THUẬT: "
            "Tuổi vượt quá giới hạn cho phép."
        )