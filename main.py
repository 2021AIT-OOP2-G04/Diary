from diaries.DiarySample import DiarySample
from diaries.WatanabeDiary import WatanabeDiary
from diaries.K20014Diary import K20014Diary

# のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    K20014Diary(),
  　　　　WatanabeDiary()
]


for d in diaries:
    print("-------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()

    