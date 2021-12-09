from diaries.AbstractDiary import AbstractDiary

class AonoDiary(AbstractDiary):

    def get_date(self):
        return "2021-12-09"

    def get_summary(self):
        return "今日は初めてのチーム開発だった。"

    def get_author(self):
        return "Aono"