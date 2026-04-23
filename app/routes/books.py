from flask import Blueprint

books_bp = Blueprint('books', __name__)

@books_bp.route('/subjects/<int:subject_id>/books/new', methods=['GET', 'POST'])
def new_book(subject_id):
    """
    新增書籍：顯示表單或接收表單資料建立書籍。
    GET /subjects/<id>/books/new
    POST /subjects/<id>/books/new
    """
    pass

@books_bp.route('/books/<int:book_id>', methods=['GET'])
def book_detail(book_id):
    """
    書籍詳細：顯示書本資訊、心得與評分。
    GET /books/<id>
    """
    pass

@books_bp.route('/books/search', methods=['GET'])
def search_books():
    """
    書籍搜尋：透過 ?q= 參數查詢書籍名稱並顯示結果。
    GET /books/search
    """
    pass
