from diaries.DiarySample import DiarySample
from diaries.K20014Diary import K20014Diary
from diaries.aonoDiary import AonoDiary

# のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    K20014Diary(),
    AonoDiary(),
]

for d in diaries:
    print("-------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()

    