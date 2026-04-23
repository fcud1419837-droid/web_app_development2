# 路由設計文件（ROUTES）

## 1. 路由總覽表格

| 功能 | HTTP 方法 | URL 路徑 | 對應模板 | 說明 |
|---|---|---|---|---|
| 首頁總覽 | GET | `/` | `templates/index.html` | 顯示所有科目與書籍數量 |
| 科目列表 | GET | `/subjects` | `templates/subjects/list.html` | 列出所有科目 |
| 新增科目頁面 | GET | `/subjects/new` | `templates/subjects/new.html` | 顯示新增科目表單 |
| 建立科目 | POST | `/subjects/new` | — | 接收表單，存入 DB，重導向至科目列表 |
| 科目詳細(含書籍) | GET | `/subjects/<id>` | `templates/subjects/detail.html` | 顯示該科目的書籍列表 |
| 刪除科目 | POST | `/subjects/<id>/delete`| — | 刪除科目及關聯書籍，重導向至科目列表 |
| 新增書籍頁面 | GET | `/subjects/<id>/books/new`| `templates/books/new.html` | 顯示新增書籍表單 |
| 建立書籍 | POST | `/subjects/<id>/books/new`| — | 接收表單，存入 DB，重導向至科目詳細 |
| 書籍詳細 | GET | `/books/<id>` | `templates/books/detail.html` | 顯示書本資訊、心得與評分 |
| 書籍搜尋 | GET | `/books/search` | `templates/books/search.html` | 透過 `?q=` 參數查詢書籍名稱並顯示結果 |

## 2. 每個路由的詳細說明

### 2.1 首頁與全域路由 (`app/routes/main.py`)
- **`GET /`**
  - **輸入**: 無
  - **處理邏輯**: 從 DB 取得所有 `Subject`，並計算每個科目的關聯書籍數量。
  - **輸出**: 渲染 `index.html`。
  - **錯誤處理**: 無特殊錯誤。

### 2.2 科目相關路由 (`app/routes/subjects.py`)
- **`GET /subjects`**
  - **輸出**: 渲染 `subjects/list.html`，顯示所有科目。
- **`GET /subjects/new`**
  - **輸出**: 渲染 `subjects/new.html` 顯示表單。
- **`POST /subjects/new`**
  - **輸入**: 表單欄位 `name`、`description`。
  - **處理邏輯**: 驗證 `name` 不得為空。呼叫 `Subject.save()` 儲存。
  - **輸出**: 重導向至 `/subjects`。
  - **錯誤處理**: 若 `name` 為空，回傳 `subjects/new.html` 並顯示錯誤訊息。
- **`GET /subjects/<id>`**
  - **輸入**: URL 參數 `id`。
  - **處理邏輯**: 透過 `Subject.get_by_id(id)` 查詢。
  - **輸出**: 渲染 `subjects/detail.html` 顯示該科目資訊與書籍列表。
  - **錯誤處理**: 找不到科目時回傳 404。
- **`POST /subjects/<id>/delete`**
  - **處理邏輯**: 呼叫 `Subject.delete()`。
  - **輸出**: 重導向至 `/subjects`。

### 2.3 書籍相關路由 (`app/routes/books.py`)
- **`GET /subjects/<id>/books/new`**
  - **輸出**: 渲染 `books/new.html` 顯示表單（需先檢查 subject 是否存在）。
- **`POST /subjects/<id>/books/new`**
  - **輸入**: 表單欄位 `title`、`author`、`rating`、`review` 等。
  - **處理邏輯**: 驗證 `title` 不為空。建立 `Book` 並呼叫 `save()` 儲存。
  - **輸出**: 重導向至 `/subjects/<id>`。
- **`GET /books/<id>`**
  - **輸入**: URL 參數 `id`。
  - **處理邏輯**: 透過 `Book.get_by_id(id)` 查詢。
  - **輸出**: 渲染 `books/detail.html`。
- **`GET /books/search`**
  - **輸入**: URL 參數 `q`。
  - **處理邏輯**: 呼叫 `Book.search(q)` 取得結果清單。
  - **輸出**: 渲染 `books/search.html`。

## 3. Jinja2 模板清單

所有的模板都會繼承 `base.html`，以共用導覽列及基礎樣式。

1. `templates/base.html` (全站共用版型)
2. `templates/index.html` (首頁)
3. `templates/subjects/list.html` (科目列表)
4. `templates/subjects/new.html` (新增科目)
5. `templates/subjects/detail.html` (科目詳細/書籍列表)
6. `templates/books/new.html` (新增書籍)
7. `templates/books/detail.html` (書籍詳細)
8. `templates/books/search.html` (搜尋結果)
