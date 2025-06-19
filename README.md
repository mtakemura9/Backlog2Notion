```markdown:README.md
# Backlog2Notion API

Backlogの課題（チケット）をフィルター条件で取得し、Notionに貼り付けやすいMarkdown形式で返すAPIです。  
**FastAPI**を使っており、Python初心者でもセットアップ・拡張しやすい構成です。

---

## 🚀 機能概要

- **Backlog課題取得API**  
  プロジェクトID・担当者・状態などでBacklog課題を絞り込み取得
- **Notion貼り付け用Markdown出力**  
  取得した課題をNotionの空白ページにそのまま貼り付けて表形式で見やすく表示

---

## 🖥️ 動作環境

- macOS（Apple Silicon/Mシリーズ）対応
- Windows/Linuxは未検証
- Python 3.8以上

---

## 🐍 Pythonのインストール方法（macOS/Mシリーズ）

1. **Homebrewが未インストールの場合：**

    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

2. **Pythonのインストール：**

    ```bash
    brew install python
    ```

3. **バージョン確認：**

    ```bash
    python3 --version
    ```

---

## 🏃‍♂️ セットアップ手順

### 1. リポジトリのクローン

```bash
git clone <このリポジトリのURL>
cd <リポジトリディレクトリ>
```

### 2. 仮想環境（venv）の作成と有効化

```bash
python3 -m venv venv
source venv/bin/activate
```
- **仮想環境の再起動方法：**
    - 一度ターミナルを閉じて再度開き、`source venv/bin/activate` を再実行

### 3. pipの自動アップグレードについて

- venv作成直後はpipが古い場合があります。  
- **pipをアップグレードする場合は注意してください。**  
    依存関係の問題が起きる場合は、`pip install --upgrade pip` を実行してください。

```bash
pip install --upgrade pip
```

### 4. 必要パッケージのインストール

```bash
pip install fastapi uvicorn httpx pydantic
```

### 5. 設定ファイルの作成

`.env` ファイルを作成し、以下を記入してください：

```
BACKLOG_SPACE_ID=your-space-id
BACKLOG_API_KEY=your-api-key
```

### 6. サーバー起動

```bash
uvicorn main:app --reload
```

---

## 🌐 FastAPI ドキュメント

- 公式ドキュメント: [https://fastapi.tiangolo.com/ja/](https://fastapi.tiangolo.com/ja/)
- 英語版: [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)

---

## 🛠️ Visual Studio Codeおすすめ拡張機能

- **Python**（Microsoft公式）
- **Pylance**（型チェック・補完強化）
- **autoDocstring**（docstring自動生成）
- **dotenv**（.envファイル編集支援）
- **FastAPI**（API開発支援）
- **REST Client**（APIテスト用）

---

## 🎯 使い方

### 1. 課題取得API

`POST /get-backlog-by-filter`

#### リクエスト例

```json
{
  "project_id": "12345",
  "assignee_id": "67890",
  "status_id": "3",
  "count": 10
}
```

#### レスポンス例

```json
{
  "notion_markdown": "| チケット | 状態 | 担当者 |\n|:---|:---|:---|\n| [タスクA](https://xxx.backlog.com/view/BLG-1) | 未対応 | 山田 | ..."
}
```

#### Notionへの貼り付け

- レスポンスの`notion_markdown`をコピーして、Notionの空白ページに貼り付けるだけでOK！

---

## 🛠️ 主な構成ファイル

- `main.py` … FastAPIアプリ本体・エンドポイント定義
- `services/backlog_service.py` … Backlog API呼び出し＆Markdown生成ロジック
- `backlog_models.py` … Backlog APIレスポンス用データモデル
- `config/settings.py` … 設定管理

---

## 🧑‍💻 次の機能開発予定（例）

- Notion API連携による自動登録
- チケットの自動同期・定期実行
- Slack通知や他サービス連携
- より細かいフィルタリング・検索
- Web UIでの操作

---

## 📝 ライセンス

MIT License（商用・個人利用ともに自由）

---

## 💡 補足・カスタマイズ

- Python初心者でも、`main.py`や`services/backlog_service.py`を編集するだけで機能追加できます。
- BacklogやNotionのAPI仕様が変わった場合も、`backlog_models.py`を修正すればOK。
- 何か困ったら [FastAPI公式ドキュメント](https://fastapi.tiangolo.com/ja/) も参考にしてください。

---


## 📝 その他・推奨項目

- **バージョン管理**：`git`推奨。mainブランチ以外での開発を推奨します。
- **Issue/PR管理**：GitHubのIssueやPull Requestでバグ報告・要望・提案を歓迎します。
- **セキュリティ**：APIキーや個人情報は必ず`.env`で管理し、リポジトリに含めないでください。
- **動作確認**：macOS Mシリーズ以外の動作は未保証です。動作報告歓迎！

---

**質問・要望・バグ報告はIssueやPRでどうぞ！  
あなたのフィードバックがこのプロジェクトをより良くします。**
```