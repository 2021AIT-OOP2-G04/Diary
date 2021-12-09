from diaries.DiarySample import DiarySample
from diaries.k20119 import K20119diary

# のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(),
           K20119diary()]


for d in diaries:
    print("-------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
