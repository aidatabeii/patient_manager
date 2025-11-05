from typing import List, Dict
DATA_FILE = "patients.txt"

def load_data() -> List[Dict]:
    """
    خواندن داده‌ها از فایل patients.txt
    هر خط فرمت: name,age,disease
    خروجی: لیست دیکشنری‌ها: [{"name":..., "age":..., "disease":...}, ...]
    """
    patients = []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")
                if len(parts) != 3:
                    # اگر فرمت خط درست نیست، ازش می‌گذریم (یا می‌تونیم لاگ کنیم)
                    print(f"[warning] خط با فرمت نادرست نادیده گرفته شد: {line}")
                    continue
                name, age_str, disease = parts
                try:
                    age = int(age_str)
                except ValueError:
                    print(f"[warning] سن نامعتبر برای {name}: {age_str} — نادیده گرفته شد")
                    continue
                patients.append({"name": name, "age": age, "disease": disease})
    except FileNotFoundError:
        # اگر فایل وجود نداشت، برمی‌گردونیم لیست خالی (بدون خطا)
        pass
    return patients

def save_data(patients: List[Dict]) -> None:
    """
    ذخیره‌ی لیست بیماران در فایل patients.txt
    هر بیمار در یک خط با فرمت: name,age,disease
    """
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        for p in patients:
             f.write(f"{p['name']},{p['age']},{p['disease']}\n")


def add_patient(patients: List[Dict]) -> None:
    name = input("نام بیمار: ").strip()
    if not name:
        print("نام خالی است — اضافه نشد.")
        return
    try:
        age = int(input("سن: ").strip())
    except ValueError:
        print("ورودی سن نامعتبر است — اضافه نشد.")
        return
    disease = input("بیماری: ").strip()
    patients.append({"name": name, "age": age, "disease": disease})
    save_data(patients)
    print("✅ بیمار با موفقیت افزوده شد.")

def show_patients(patients: List[Dict]) -> None:
    if not patients:
        print("\n(فهرست بیماران خالی است.)")
        return
    print("\n--- لیست بیماران ---")
    for i, p in enumerate(patients, 1):
        print(f"{i}. {p['name']} - {p['age']} سال - {p['disease']}")
    print("----------------------")

def delete_patient(patients: List[Dict]) -> None:
    if not patients:
        print("لیست خالی است؛ چیزی برای حذف نیست.")
        return
    name = input("نام بیمار برای حذف: ").strip()
 
    for p in patients:
        if p['name'] == name:
            patients.remove(p)
            save_data(patients)
            print(f"🗑️ بیمار '{name}' حذف شد.")
            return
    print("❌ بیماری با این نام پیدا نشد.")

# ----- رابط کاربری -----
def show_menu() -> None:
    print("\n=== سامانه مدیریت بیماران ===")
    print("1. افزودن بیمار جدید")
    print("2. نمایش لیست بیماران")
    print("3. حذف بیمار")
    print("4. خروج")

def main() -> None:
    patients = load_data()

    while True:
        show_menu()
        choice = input("عدد گزینه مورد نظر را وارد کنید: ").strip()

        if choice == "1":
            add_patient(patients)
        elif choice == "2":
            show_patients(patients)
        elif choice == "3":
            delete_patient(patients)
        elif choice == "4":
            save_data(patients)
            print("✅ اطلاعات ذخیره شد. خداحافظ!")
            break
        else:
            print("❌ گزینه نامعتبر! لطفاً دوباره تلاش کنید.")

if __name__ == "__main__":
    main()            

  
