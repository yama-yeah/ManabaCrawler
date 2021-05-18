# ManabaCrawler
manabaをcrawlするやつ

**required python3.9<=**

```bash
git clone https://github.com/t4t5u0/ManabaCrawler
cd ManabaCrawler
pip install -r requirements.txt
vim config.ini # 学籍番号とパスワード
python main.py
```
出力例 次回修正でmd形式に吐き出す機能を追加予定
![20210516003100](https://user-images.githubusercontent.com/48282855/118369405-2c910200-b5de-11eb-85a4-d4fb71bff8c3.png)


## 要件
- [x] [manaba](https://manaba.fun.ac.jp/ct/home) にログインして、セッションを握る
- [x] (未提出の)課題一覧を取得する
- [ ] (未提出の)課題一覧を定期的に取得する(外部から叩いてもいい)
- [ ] GitHubにIssueとして登録するため、専用の辞書型で出力する
