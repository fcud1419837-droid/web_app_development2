from flask import Blueprint

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """
    首頁總覽：顯示所有科目與書籍數量。
    GET /
    """
    pass
