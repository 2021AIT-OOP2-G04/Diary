from diaries.DiarySample import DiarySample
from diaries.K20014Diary import K20014Diary
from diaries.K20054Diary import K20054Diary

# のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    K20014Diary(),
    K20054Diary(),
]

for d in diaries:
    print("-------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()

    