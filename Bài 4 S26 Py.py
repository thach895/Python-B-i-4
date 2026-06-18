from abc import ABC, abstractmethod


# =========================
# ABSTRACT CLASS
# =========================
class Equipment(ABC):

    @abstractmethod
    def calculate_total_damage(self):
        pass


# =========================
# WEAPON
# =========================
class Weapon(Equipment):

    def __init__(self, name, base_damage, upgrade_level=0):
        self.name = name.title()
        self.base_damage = base_damage
        self.upgrade_level = upgrade_level

    def calculate_total_damage(self):
        return self.base_damage + self.upgrade_level * 10

    def __gt__(self, other):

        if not isinstance(other, Equipment):
            print("Chỉ có thể so sánh giữa các trang bị!")
            return False

        return (
            self.calculate_total_damage()
            > other.calculate_total_damage()
        )

    def __add__(self, other):

        if not isinstance(other, Equipment):
            print("Chỉ có thể dung hợp giữa các trang bị!")
            return None

        new_name = f"Fusion({self.name} + {other.name})"

        new_base_damage = (
            self.base_damage +
            other.base_damage
        )

        new_upgrade_level = (
            self.upgrade_level +
            other.upgrade_level
        )

        return Weapon(
            new_name,
            new_base_damage,
            new_upgrade_level
        )


# =========================
# MIXIN
# =========================
class MagicMixin:

    def __init__(self, magic_power):
        self.magic_power = magic_power

    def cast_glow(self):
        print(f"{self.name} đang phát sáng ma thuật!")


# =========================
# MAGIC SWORD
# =========================
class MagicSword(Weapon, MagicMixin):

    def __init__(
            self,
            name,
            base_damage,
            upgrade_level,
            magic_power
    ):

        Weapon.__init__(
            self,
            name,
            base_damage,
            upgrade_level
        )

        MagicMixin.__init__(
            self,
            magic_power
        )

    def calculate_total_damage(self):
        return (
            self.base_damage
            + self.upgrade_level * 10
            + self.magic_power
        )


# =========================
# INVENTORY
# =========================
inventory = []


# =========================
# CHỨC NĂNG 1
# =========================
def show_inventory():

    print("\n--- KHO VŨ KHÍ CỦA NGƯỜI CHƠI ---")

    if not inventory:
        print("Kho vũ khí hiện đang trống.")
        print("Vui lòng rèn vũ khí bằng Chức năng 2 hoặc 3.")
        return

    print(
        f"{'STT':<6}|"
        f"{'Tên vũ khí':<30}|"
        f"{'Loại':<15}|"
        f"{'Cấp':<8}|"
        f"{'Sát thương tổng':<15}"
    )

    print("-" * 90)

    for i, item in enumerate(inventory, start=1):

        print(
            f"{i:<6}|"
            f"{item.name:<30}|"
            f"{type(item).__name__:<15}|"
            f"{item.upgrade_level:<8}|"
            f"{item.calculate_total_damage():<15}"
        )


# =========================
# CHỨC NĂNG 2
# =========================
def forge_weapon():

    print("\n--- RÈN VŨ KHÍ VẬT LÝ ---")

    name = input("Nhập tên vũ khí: ")

    base_damage = int(
        input("Nhập sát thương gốc: ")
    )

    if base_damage <= 0:
        print("Giá trị phải lớn hơn 0!")
        return

    upgrade_level = int(
        input("Nhập cấp cường hóa: ")
    )

    if upgrade_level <= 0:
        print("Giá trị phải lớn hơn 0!")
        return

    weapon = Weapon(
        name,
        base_damage,
        upgrade_level
    )

    inventory.append(weapon)

    print("\n>> Rèn vũ khí vật lý thành công!")
    print(f"Tên vũ khí: {weapon.name}")
    print("Loại: Weapon")
    print(f"Cấp cường hóa: {weapon.upgrade_level}")
    print(
        f"Sát thương tổng: "
        f"{weapon.calculate_total_damage()}"
    )


# =========================
# CHỨC NĂNG 3
# =========================
def forge_magic_sword():

    print("\n--- RÈN KIẾM MA THUẬT ---")

    name = input(
        "Nhập tên kiếm ma thuật: "
    )

    base_damage = int(
        input("Nhập sát thương gốc: ")
    )

    if base_damage <= 0:
        print("Giá trị phải lớn hơn 0!")
        return

    upgrade_level = int(
        input("Nhập cấp cường hóa: ")
    )

    if upgrade_level <= 0:
        print("Giá trị phải lớn hơn 0!")
        return

    magic_power = int(
        input("Nhập sức mạnh phép thuật: ")
    )

    if magic_power <= 0:
        print("Giá trị phải lớn hơn 0!")
        return

    sword = MagicSword(
        name,
        base_damage,
        upgrade_level,
        magic_power
    )

    inventory.append(sword)

    print("\n>> Rèn kiếm ma thuật thành công!")
    print(f"Tên vũ khí: {sword.name}")
    print("Loại: MagicSword")
    print(f"Cấp cường hóa: {sword.upgrade_level}")
    print(f"Sát thương gốc: {sword.base_damage}")
    print(f"Sức mạnh phép thuật: {sword.magic_power}")
    print(
        f"Sát thương tổng: "
        f"{sword.calculate_total_damage()}"
    )


# =========================
# CHỨC NĂNG 4
# =========================
def appraisal():

    print("\n--- THẨM ĐỊNH VŨ KHÍ ---")

    if len(inventory) < 2:
        print(
            "Cần ít nhất 2 vũ khí trong kho để thẩm định!"
        )
        return

    w1 = inventory[0]
    w2 = inventory[1]

    print("Vũ khí thứ nhất:")
    print(
        f"{w1.name} | "
        f"Loại: {type(w1).__name__} | "
        f"Sát thương: {w1.calculate_total_damage()}"
    )

    print("\nVũ khí thứ hai:")
    print(
        f"{w2.name} | "
        f"Loại: {type(w2).__name__} | "
        f"Sát thương: {w2.calculate_total_damage()}"
    )

    if w1 > w2:
        print(
            f"\nKết quả: "
            f"{w1.name} mạnh hơn {w2.name}."
        )

    elif w2 > w1:
        print(
            f"\nKết quả: "
            f"{w2.name} mạnh hơn {w1.name}."
        )

    else:
        print(
            "\nKết quả: Hai vũ khí có sức mạnh ngang nhau."
        )


# =========================
# CHỨC NĂNG 5
# =========================
def fusion():

    print("\n--- DUNG HỢP VŨ KHÍ ---")

    if len(inventory) < 2:
        print(
            "Cần ít nhất 2 vũ khí trong kho để dung hợp!"
        )
        return

    w1 = inventory[0]
    w2 = inventory[1]

    print("Đang dung hợp 2 vũ khí đầu tiên trong kho...")

    print(
        f"\nVũ khí 1: {w1.name}"
        f" | Cấp: {w1.upgrade_level}"
        f" | Sát thương: {w1.base_damage}"
    )

    print(
        f"Vũ khí 2: {w2.name}"
        f" | Cấp: {w2.upgrade_level}"
        f" | Sát thương: {w2.base_damage}"
    )

    new_weapon = w1 + w2

    inventory.pop(0)
    inventory.pop(0)

    inventory.append(new_weapon)

    print("\n>> Dung hợp vũ khí thành công!")

    print(f"Đã xóa khỏi kho: {w1.name}")
    print(f"Đã xóa khỏi kho: {w2.name}")

    print(f"\nVũ khí mới: {new_weapon.name}")
    print("Loại: Weapon")
    print(
        f"Cấp cường hóa: "
        f"{new_weapon.upgrade_level}"
    )

    print(
        f"Sát thương tổng: "
        f"{new_weapon.calculate_total_damage()}"
    )


# =========================
# MENU
# =========================
def main():

    while True:

        print("\n===== LÒ RÈN VŨ KHÍ RIKKEI STUDIOS =====")
        print("1. Xem kho vũ khí")
        print("2. Rèn Vũ khí Vật lý")
        print("3. Rèn Kiếm Ma Thuật")
        print("4. Thẩm định vũ khí")
        print("5. Dung hợp vũ khí")
        print("6. Thoát game")
        print("========================================")

        choice = input(
            "Chọn chức năng (1-6): "
        )

        if choice == "1":
            show_inventory()

        elif choice == "2":
            forge_weapon()

        elif choice == "3":
            forge_magic_sword()

        elif choice == "4":
            appraisal()

        elif choice == "5":
            fusion()

        elif choice == "6":
            print(
                "Thoát Lò Rèn. "
                "Hẹn gặp lại Anh hùng!"
            )
            break

        else:
            print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()