# 流程圖文件（FLOWCHART）

**專案名稱：** 讀書筆記本系統  
**文件版本：** v1.0  
**建立日期：** 2026-04-23  
**參考文件：** docs/PRD.md、docs/ARCHITECTURE.md  

---

## 1. 使用者流程圖（User Flow）

描述使用者從開啟網站到完成各項操作的完整路徑。

```mermaid
flowchart LR
    A([使用者開啟網頁]) --> B[首頁：科目總覽]

    B --> C{要執行什麼操作？}

    C -->|管理科目| D[科目列表頁]
    C -->|搜尋書籍| S[搜尋頁]

    %% 科目操作
    D --> D1{科目操作}
    D1 -->|新增科目| D2[填寫科目名稱與描述]
    D2 --> D3[送出表單]
    D3 --> D[科目列表頁]

    D1 -->|查看科目| E[科目詳細頁：書籍列表]
    D1 -->|刪除科目| D4[確認刪除]
    D4 --> D[科目列表頁]

    %% 書籍操作
    E --> E1{書籍操作}
    E1 -->|新增書籍| F[填寫書名 / 作者 / 評分 / 心得]
    F --> F1[送出表單]
    F1 --> E[科目詳細頁]

    E1 -->|查看書籍| G[書籍詳細頁：心得與評分]
    E1 -->|刪除書籍| E2[確認刪除]
    E2 --> E[科目詳細頁]

    %% 搜尋
    S --> S1[輸入關鍵字]
    S1 --> S2[顯示搜尋結果]
    S2 -->|點擊書籍| G[書籍詳細頁]
    S2 -->|返回| B
```

---

## 2. 系統序列圖（Sequence Diagram）

以下分別針對「新增書籍」與「搜尋書籍」兩個核心功能，描述系統內部的資料流動。

### 2.1 新增書籍流程

```mermaid
sequenceDiagram
    actor User as 使用者
    participant Browser as 瀏覽器
    participant Flask as Flask Route<br/>(books.py)
    participant Model as Book Model<br/>(SQLAlchemy)
    participant DB as SQLite 資料庫

    User->>Browser: 點擊「新增書籍」按鈕
    Browser->>Flask: GET /subjects/<id>/books/new
    Flask-->>Browser: 回傳新增書籍表單頁面

    User->>Browser: 填寫書名、作者、評分、心得並送出
    Browser->>Flask: POST /subjects/<id>/books/new
    Flask->>Flask: 驗證表單資料（書名不可為空）

    alt 驗證失敗
        Flask-->>Browser: 回傳錯誤提示，留在表單頁
    else 驗證成功
        Flask->>Model: 建立 Book 物件
        Model->>DB: INSERT INTO books (...)
        DB-->>Model: 寫入成功
        Model-->>Flask: 回傳新書籍物件
        Flask-->>Browser: 302 重導向到科目詳細頁
        Browser->>Flask: GET /subjects/<id>
        Flask-->>Browser: 顯示更新後的書籍列表
    end
```

### 2.2 搜尋書籍流程

```mermaid
sequenceDiagram
    actor User as 使用者
    participant Browser as 瀏覽器
    participant Flask as Flask Route<br/>(books.py)
    participant Model as Book Model<br/>(SQLAlchemy)
    participant DB as SQLite 資料庫

    User->>Browser: 在搜尋框輸入關鍵字並按下搜尋
    Browser->>Flask: GET /books/search?q=關鍵字
    Flask->>Model: 呼叫 search(keyword)
    Model->>DB: SELECT * FROM books WHERE title LIKE '%keyword%'
    DB-->>Model: 回傳符合的書籍列表
    Model-->>Flask: 回傳書籍物件列表
    Flask-->>Browser: 渲染 search.html（顯示搜尋結果）
    Browser-->>User: 顯示所有符合書名的書籍
```

### 2.3 新增科目流程

```mermaid
sequenceDiagram
    actor User as 使用者
    participant Browser as 瀏覽器
    participant Flask as Flask Route<br/>(subjects.py)
    participant Model as Subject Model<br/>(SQLAlchemy)
    participant DB as SQLite 資料庫

    User->>Browser: 點擊「新增科目」
    Browser->>Flask: GET /subjects/new
    Flask-->>Browser: 回傳新增科目表單

    User->>Browser: 填寫科目名稱並送出
    Browser->>Flask: POST /subjects/new
    Flask->>Flask: 驗證科目名稱不為空

    alt 驗證失敗
        Flask-->>Browser: 回傳錯誤提示
    else 驗證成功
        Flask->>Model: 建立 Subject 物件
        Model->>DB: INSERT INTO subjects (...)
        DB-->>Model: 寫入成功
        Flask-->>Browser: 302 重導向到科目列表頁
    end
```

---

## 3. 功能清單對照表

| 功能編號 | 功能名稱 | URL 路徑 | HTTP 方法 | 對應 Controller |
|--------|--------|---------|---------|----------------|
| F-07 | 首頁科目總覽 | `/` | GET | `main.py` |
| F-01 | 科目列表 | `/subjects` | GET | `subjects.py` |
| F-01 | 新增科目（表單頁） | `/subjects/new` | GET | `subjects.py` |
| F-01 | 新增科目（送出） | `/subjects/new` | POST | `subjects.py` |
| F-06 | 科目書籍列表 | `/subjects/<id>` | GET | `subjects.py` |
| F-01 | 刪除科目 | `/subjects/<id>/delete` | POST | `subjects.py` |
| F-02、F-03、F-04 | 新增書籍（表單頁） | `/subjects/<id>/books/new` | GET | `books.py` |
| F-02、F-03、F-04 | 新增書籍（送出） | `/subjects/<id>/books/new` | POST | `books.py` |
| F-03、F-04 | 書籍詳細頁 | `/books/<id>` | GET | `books.py` |
| F-05 | 書籍搜尋 | `/books/search?q=<keyword>` | GET | `books.py` |

---

## 4. 頁面轉換關係圖

描述各頁面之間的導覽關係（使用者可以從哪些頁面跳到哪些頁面）。

```mermaid
flowchart TD
    A["🏠 首頁 /"] --> B["📚 科目列表 /subjects"]
    A --> S["🔍 搜尋頁 /books/search"]

    B --> C["📝 新增科目 /subjects/new"]
    B --> D["📖 科目詳細 /subjects/id"]

    C -->|送出成功| B
    D --> E["➕ 新增書籍 /subjects/id/books/new"]
    D -->|刪除科目| B

    E -->|送出成功| D
    D --> F["📄 書籍詳細 /books/id"]

    S --> F
    F -->|返回| D
```
