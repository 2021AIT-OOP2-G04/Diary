from diaries.DiarySample import DiarySample
from diaries.K20014Diary import K20014Diary
from diaries.K20047Diary import K20047Diary


# のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    K20014Diary(),
    K20014Diary(),
    K20047Diary(),
]

for d in diaries:
    print("-------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()

    