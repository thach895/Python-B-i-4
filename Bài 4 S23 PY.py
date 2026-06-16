import random
import string
from datetime import datetime
from colorama import Fore, init

init(autoreset=True)

student_records = [
    {
        "student_id": "SV001",
        "name": "Nguyễn Văn A",
        "scores": [8.5, 7.0, 9.0]
    },
    {
        "student_id": "SV002",
        "name": "Trần Thị B",
        "scores": [4.0, 5.5, 5.0]
    },
    {
        "student_id": "SV003",
        "name": "Lê Văn C",
        "scores": [9.5, 9.0, 8.5]
    }
]


def calculate_average(scores):
    valid_scores = []

    for score in scores:
        if isinstance(score, (int, float)):
            valid_scores.append(score)

    if len(valid_scores) == 0:
        return 0

    return sum(valid_scores) / len(valid_scores)


def classify_student(average):
    if average >= 8:
        return "Giỏi"
    elif average >= 6.5:
        return "Khá"
    elif average >= 5:
        return "Trung bình"
    else:
        return "Yếu"


def display_student_scores(records):

    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    print("\n--- DANH SÁCH ĐIỂM SINH VIÊN ---")

    for index, student in enumerate(records, start=1):

        average = calculate_average(
            student["scores"]
        )

        rank = classify_student(
            average
        )

        print(
            f"{index}. "
            f"[{student['student_id']}] "
            f"{student['name']} | "
            f"Điểm: {student['scores']} | "
            f"ĐTB: {average:.2f} - {rank}"
        )

    print("---------------------------------")


def normalize_student_names(records):

    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    print("\n--- CHUẨN HÓA TÊN SINH VIÊN ---")

    for student in records:

        normalized_name = " ".join(
            student["name"].split()
        ).title()

        student["name"] = normalized_name

        print(
            f"{student['student_id']}: "
            f"{student['name']}"
        )

    print(">> Đã chuẩn hóa toàn bộ tên sinh viên.")


def generate_assignment_code():

    characters = (
        string.ascii_uppercase +
        string.digits
    )

    code = "".join(
        random.choice(characters)
        for _ in range(4)
    )

    return f"PY-{code}"


def export_learning_report(records):

    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    total_students = len(records)

    passed_students = 0
    failed_students = 0

    for student in records:

        average = calculate_average(
            student["scores"]
        )

        if average >= 5:
            passed_students += 1
        else:
            failed_students += 1

    report_time = datetime.now()

    with open(
        "learning_report.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "===== BÁO CÁO HỌC TẬP =====\n"
        )

        file.write(
            f"Thời gian tạo: "
            f"{report_time}\n\n"
        )

        file.write(
            f"Tổng số sinh viên: "
            f"{total_students}\n"
        )

        file.write(
            f"Số sinh viên đạt yêu cầu: "
            f"{passed_students}\n"
        )

        file.write(
            f"Số sinh viên cần cải thiện: "
            f"{failed_students}\n"
        )

    print("\n--- XUẤT BÁO CÁO HỌC TẬP ---")
    print(
        f"Tổng số sinh viên: "
        f"{total_students}"
    )
    print(
        f"Số sinh viên đạt yêu cầu: "
        f"{passed_students}"
    )
    print(
        f"Số sinh viên cần cải thiện: "
        f"{failed_students}"
    )

    print(
        Fore.GREEN +
        ">> Đã xuất báo cáo ra file learning_report.txt"
    )


def main():

    while True:

        print("\n===== HỆ THỐNG TIỆN ÍCH HỌC TẬP RIKKEI ACADEMY =====")
        print("1. Xem danh sách sinh viên và điểm trung bình")
        print("2. Chuẩn hóa tên sinh viên")
        print("3. Sinh mã bài tập ngẫu nhiên")
        print("4. Xuất báo cáo học tập")
        print("5. Thoát chương trình")
        print("====================================================")

        try:

            choice = int(
                input(
                    "Chọn chức năng (1-5): "
                )
            )

            if choice == 1:

                display_student_scores(
                    student_records
                )

            elif choice == 2:

                normalize_student_names(
                    student_records
                )

            elif choice == 3:

                print(
                    "\n--- SINH MÃ BÀI TẬP ---"
                )

                print(
                    "Mã bài tập của bạn là:",
                    generate_assignment_code()
                )

            elif choice == 4:

                export_learning_report(
                    student_records
                )

            elif choice == 5:

                print(
                    "Cảm ơn bạn đã sử dụng hệ thống!"
                )

                break

            else:

                print(
                    "Chức năng không hợp lệ. "
                    "Vui lòng chọn từ 1 đến 5."
                )

        except ValueError:

            print(
                "Chức năng không hợp lệ. "
                "Vui lòng chọn từ 1 đến 5."
            )


if __name__ == "__main__":
    main()