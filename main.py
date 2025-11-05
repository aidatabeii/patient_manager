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



if  __name__ == "__main__":       
   print ("=== تست توابع load_data / save_data ===")
patients = load_data()
print("داده‌های فعلی (بارگذاری شده از فایل):")
if not patients:
        print("  (فهرست خالی است)")
else:
        for i, p in enumerate(patients, 1):
            print(f"  {i}. {p['name']} - {p['age']} - {p['disease']}")


if not patients:
        sample = {"name": "نمونه_آیدا", "age": 25, "disease": "Healthy"}
        patients.append(sample)
        save_data(patients)
        print("\nفایل خالی بود؛ یک رکورد نمونه ذخیره شد. حالا مجدداً بارگذاری می‌کنیم:")
        patients2 = load_data()
        for i, p in enumerate(patients2, 1):
            print(f"  {i}. {p['name']} - {p['age']} - {p['disease']}")
else:
        print("\nبرای تستِ نوشتن، فایل رو پاک کن یا محتواش رو خالی کن و برنامه رو دوباره اجرا کن.")
