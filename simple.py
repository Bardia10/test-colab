# expense_tracker.py
from fastapi import FastAPI
import requests
# لیست جهانی برای ذخیره هزینه‌ها
expenses = []

# تابع اضافه کردن هزینه
def add_expense():
    description = input("توضیح هزینه را وارد کنید: ")
    while True:
        try:
            amount = float(input("مبلغ هزینه را وارد کنید: "))
            break
        except ValueError:
            print("لطفاً مبلغ را به صورت عددی وارد کنید.")
    
    expense = {"description": description, "amount": amount}
    expenses.append(expense)
    print(f"هزینه '{description}' به مبلغ {amount} با موفقیت اضافه شد.")

# تابع نمایش لیست هزینه‌ها
def view_expenses():
    pass

# تابع محاسبه مجموع هزینه‌ها
def calculate_total_expenses():
    pass

# تابع ذخیره هزینه‌ها در فایل
def save_expenses_to_file():
    pass

# حلقه اصلی برنامه
def main():
    print("به برنامه مدیریت هزینه‌ها خوش آمدید!")
    print("گزینه‌ها:")
    print("1. اضافه کردن هزینه")
    print("2. مشاهده لیست هزینه‌ها")
    print("3. محاسبه مجموع هزینه‌ها")
    print("4. ذخیره هزینه‌ها در فایل")
    print("5. خروج")

    while True:
        choice = input("لطفاً گزینه مورد نظر را وارد کنید (1-5): ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            calculate_total_expenses()
        elif choice == '4':
            save_expenses_to_file()
        elif choice == '5':
            print("خداحافظ!")
            break
        else:
            print("گزینه نامعتبر است. لطفاً دوباره تلاش کنید.")

#changes from Mohammadzadeh

router = FastAPI()

#check user registration fastapi router
@router.get("/check_register")
async def get_user_info(name: str):
    if name.lower() == 'ahmad':
        print("welcome Ahmad :)")
    elif name.lower() == ("amir mohammad" or "amir_mohammad"):
        print("Welcome Amir Mohammad :)")
    elif name.lower() == 'bardia':
        print("welcome Bardia :)")
    elif name.lower() == 'gazal bagheri':
        print("welcome Gazal :)")
    elif name.lower() == ("mohammad javad" or "mohammad_javad"):
        print("Welcome Mohammad Javad :)")
    elif name.lower() == 'kimia mahdavi':
        print("welcome Kimia :)")
    else:
        print("Sorry we are so sorry! you don't have access to this application.")
        print('-' * 50)
        print("for further information, contact to one of the aland group team members!")
        print('-' * 50)
        

# اجرای برنامه
if __name__ == "__main__":
    main()

# some random change to see if I can do push command using git

# پایان برنامه