import logging

logging.basicConfig(
    filename="roster_app.log",
    level=logging.INFO,
    format="[%(asctime)s] - [%(levelname)s] - %(message)s"
)

roster = [
    {
        "player_id": "P01",
        "name": "Faker",
        "role": "Mid Lane",
        "salary": 5000.0,
        "status": "Active"
    },
    {
        "player_id": "P02",
        "name": "Oner",
        "role": "Jungle",
        "salary": 3500.0,
        "status": "Active"
    },
    {
        "player_id": "P03",
        "name": "Ruler",
        "role": "ADC",
        "salary": 6000.0,
        "status": "Benched"
    }
]


def find_player_by_id(roster_list, player_id):
    for player in roster_list:
        if player["player_id"] == player_id:
            return player
    return None


def calculate_actual_pay(player_dict):
    if player_dict["status"] == "Benched":
        return player_dict["salary"] * 0.5
    return player_dict["salary"]


def display_roster(roster_list):
    logging.info("Coach viewed the team roster.")

    if not roster_list:
        print("Đội hình hiện đang trống.")
        return

    print("\n--- ĐỘI HÌNH RIKKEI ESPORTS ---")
    print(
        f"{'ID':<8} | {'Tên tuyển thủ':<20} | {'Vị trí':<15} | {'Lương':<12} | {'Trạng thái'}"
    )
    print("-" * 90)

    for player in roster_list:
        try:
            status = player["status"]
        except KeyError:
            status = "Unknown"

        name = player["name"]

        if status == "Benched":
            name += " [DỰ BỊ]"

        print(
            f"{player['player_id']:<8} | "
            f"{name:<20} | "
            f"{player['role']:<15} | "
            f"{player['salary']:<12,.1f} | "
            f"{status}"
        )


def sign_player(roster_list):
    print("\n--- CHIÊU MỘ TUYỂN THỦ MỚI ---")

    player_id = input("Nhập mã tuyển thủ: ").strip().upper()

    if find_player_by_id(roster_list, player_id):
        print(f"Lỗi: Mã tuyển thủ {player_id} đã tồn tại.")
        logging.warning(
            f"Failed to sign player - Duplicate player ID {player_id}"
        )
        return

    name = input("Nhập tên tuyển thủ: ").strip().title()
    role = input("Nhập vị trí thi đấu: ").strip().title()

    while True:
        try:
            salary = float(
                input("Nhập mức lương hàng tháng: ")
            )

            if salary <= 0:
                print("Lương phải là số dương. Vui lòng nhập lại.")
                continue

            break

        except ValueError:
            print("Lương phải là số. Vui lòng nhập lại.")
            logging.warning(
                "Failed to sign player - Invalid salary input"
            )

    roster_list.append(
        {
            "player_id": player_id,
            "name": name,
            "role": role,
            "salary": salary,
            "status": "Active"
        }
    )

    print(f"\nThành công: Đã chiêu mộ tuyển thủ {name}.")
    logging.info(
        f"Signed new player {name} with salary {salary}"
    )


def update_player_status(roster_list):
    print("\n--- CẬP NHẬT LƯƠNG & TRẠNG THÁI THI ĐẤU ---")

    player_id = input(
        "Nhập mã tuyển thủ cần cập nhật: "
    ).strip().upper()

    player = find_player_by_id(
        roster_list,
        player_id
    )

    if player is None:
        print(
            f"Không tìm thấy tuyển thủ mang mã {player_id}."
        )
        logging.warning(
            f"Failed to update player - Player ID {player_id} not found"
        )
        return

    print(f"\nTuyển thủ: {player['name']}")
    print(f"Vị trí: {player['role']}")
    print(f"Lương hiện tại: {player['salary']}")
    print(f"Trạng thái hiện tại: {player['status']}")

    print("\n1. Cập nhật lương")
    print("2. Cập nhật trạng thái thi đấu")

    choice = input(
        "Chọn chức năng cập nhật (1-2): "
    )

    if choice == "1":

        old_salary = player["salary"]

        while True:
            try:
                new_salary = float(
                    input("Nhập mức lương mới: ")
                )

                if new_salary <= 0:
                    print(
                        "Lương phải là số dương. Vui lòng nhập lại."
                    )
                    continue

                player["salary"] = new_salary

                logging.info(
                    f"Updated player {player_id} salary "
                    f"from {old_salary} to {new_salary}"
                )

                print(
                    f"Thành công: Đã cập nhật lương cho tuyển thủ {player_id}."
                )
                break

            except ValueError:
                print(
                    "Lương phải là số. Vui lòng nhập lại."
                )

    elif choice == "2":

        print("\n1. Active")
        print("2. Benched")

        status_choice = input(
            "Nhập lựa chọn trạng thái (1-2): "
        )

        if status_choice == "1":
            player["status"] = "Active"

        elif status_choice == "2":
            player["status"] = "Benched"

        else:
            print("Lựa chọn không hợp lệ.")
            return

        logging.info(
            f"Updated player {player_id} status to {player['status']}"
        )

        print(
            f"Thành công: Đã cập nhật trạng thái cho tuyển thủ {player_id}."
        )


def generate_payroll_report(roster_list):
    print("\n--- BÁO CÁO QUỸ LƯƠNG HÀNG THÁNG ---")

    if not roster_list:
        print("Đội hình hiện đang trống. Tổng quỹ lương: 0.0")
        return

    total_payroll = 0

    print(
        f"{'ID':<8} | {'Tên tuyển thủ':<15} | {'Trạng thái':<10} | {'Lương gốc':<12} | {'Lương thực nhận'}"
    )
    print("-" * 90)

    try:

        for player in roster_list:

            actual_pay = calculate_actual_pay(player)

            total_payroll += actual_pay

            print(
                f"{player['player_id']:<8} | "
                f"{player['name']:<15} | "
                f"{player['status']:<10} | "
                f"{player['salary']:<12,.1f} | "
                f"{actual_pay:,.1f}"
            )

    except KeyError as error:

        print("Lỗi: Một tuyển thủ đang bị thiếu dữ liệu.")

        logging.error(
            f"Missing key while generating payroll report: {error}"
        )

        total_payroll = 0

    print("-" * 90)
    print(
        f"Tổng quỹ lương hàng tháng: {total_payroll:,.1f}"
    )

    logging.info(
        f"Generated monthly payroll report. Total: {total_payroll}"
    )


def display_menu():
    print("\n===== HỆ THỐNG QUẢN LÝ ĐỘI HÌNH RIKKEI ESPORTS =====")
    print("1. Xem đội hình thi đấu hiện tại")
    print("2. Chiêu mộ tuyển thủ mới")
    print("3. Cập nhật lương & Trạng thái thi đấu")
    print("4. Báo cáo quỹ lương hàng tháng")
    print("5. Thoát hệ thống")
    print("==================================================")


def main():
    while True:

        display_menu()

        choice = input(
            "Chọn chức năng (1-5): "
        )

        if choice == "1":
            display_roster(roster)

        elif choice == "2":
            sign_player(roster)

        elif choice == "3":
            update_player_status(roster)

        elif choice == "4":
            generate_payroll_report(roster)

        elif choice == "5":
            logging.info("Roster system shutdown.")
            print("Đã thoát hệ thống.")
            break

        else:
            print("Lựa chọn không hợp lệ.")
            logging.warning(
                "Invalid menu choice selected"
            )


main()