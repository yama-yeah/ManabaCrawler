# ManabaCrawler
manabaをcrawlするやつ

```bash
git clone https://github.com/t4t5u0/ManabaCrawler
cd ManabaCrawler
pip install -r requirements.txt
vim config.ini # 学籍番号とパスワード
python main.py
```
## 要件
- [manaba](https://manaba.fun.ac.jp/ct/home) にログインして、セッションを握る
- (未提出の)課題一覧を取得する
- (未提出の)課題一覧を定期的に取得する(外部から叩いてもいい)
- GitHubにIssueとして登録するため、専用の辞書型で出力する