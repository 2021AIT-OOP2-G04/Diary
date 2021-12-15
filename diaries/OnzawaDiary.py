from diaries.AbstractDiary import AbstractDiary

class OnzawaDiary(AbstractDiary):


    def get_date(self):
        return "2021-12-09"

    def get_summary(self):
        return """オブジェクト指向プログラミング演習2のグループワークでリーダーになった。説明についていけず、しっかりできているか心配です。
        メンバーとコミュニケーションをしっかり取れるよう頑張りたいです。"""
    
    def get_author(self):
        return "Onzawa"