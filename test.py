import json
import os
import base64

DATA_FILE = "passwords.json"

# Khởi tạo file nếu chưa có
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({}, f)

# Hàm load data
def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# Hàm save data
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Mã hóa password (base64 đơn giản)
def encode_password(password):
    return base64.b64encode(password.encode("utf-8")).decode("utf-8")

# Giải mã password
def decode_password(enc_password):
    return base64.b64decode(enc_password.encode("utf-8")).decode("utf-8")

# Thêm tài khoản
def add_account():
    site = input("Nhập tên site/app: ").strip()
    username = input("Nhập username/email: ").strip()
    password = input("Nhập password: ").strip()

    data = load_data()
    data[site] = {
        "username": username,
        "password": encode_password(password)
    }
    save_data(data)
    print(f"[✓] Đã lưu {site}!\n")

# Xem tất cả tài khoản
def view_accounts():
    data = load_data()
    if not data:
        print("Chưa có tài khoản nào.\n")
        return
    print("Danh sách tài khoản:")
    for site, info in data.items():
        print(f"- {site}: {info['username']} | {decode_password(info['password'])}")
    print()

# Tìm kiếm tài khoản
def search_account():
    query = input("Nhập tên site cần tìm: ").strip()
    data = load_data()
    found = False
    for site, info in data.items():
        if query.lower() in site.lower():
            print(f"- {site}: {info['username']} | {decode_password(info['password'])}")
            found = True
    if not found:
        print("Không tìm thấy tài khoản nào.\n")
    print()

# Xóa tài khoản
def delete_account():
    site = input("Nhập tên site cần xóa: ").strip()
    data = load_data()
    if site in data:
        confirm = input(f"Bạn có chắc muốn xóa {site}? (y/n): ").lower()
        if confirm == 'y':
            del data[site]
            save_data(data)
            print(f"[✓] Đã xóa {site}\n")
    else:
        print("Không tìm thấy tài khoản.\n")

# Menu chính
def main():
    while True:
        print("=== PASSWORD MANAGER ===")
        print("1. Thêm tài khoản")
        print("2. Xem tất cả tài khoản")
        print("3. Tìm kiếm tài khoản")
        print("4. Xóa tài khoản")
        print("5. Thoát")

        choice = input("Chọn một mục: ").strip()
        if choice == "1":
            add_account()
        elif choice == "2":
            view_accounts()
        elif choice == "3":
            search_account()
        elif choice == "4":
            delete_account()
        elif choice == "5":
            print("Bye! 👋")
            break
        else:
            print("Lựa chọn không hợp lệ.\n")

if __name__ == "__main__":
    main()
