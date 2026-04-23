from flask import Blueprint

subjects_bp = Blueprint('subjects', __name__, url_prefix='/subjects')

@subjects_bp.route('/', methods=['GET'])
def list_subjects():
    """
    科目列表：列出所有科目。
    GET /subjects
    """
    pass

@subjects_bp.route('/new', methods=['GET', 'POST'])
def new_subject():
    """
    新增科目：顯示表單或接收表單資料建立科目。
    GET /subjects/new
    POST /subjects/new
    """
    pass

@subjects_bp.route('/<int:subject_id>', methods=['GET'])
def subject_detail(subject_id):
    """
    科目詳細：顯示該科目的詳細資訊與關聯的書籍列表。
    GET /subjects/<id>
    """
    pass

@subjects_bp.route('/<int:subject_id>/delete', methods=['POST'])
def delete_subject(subject_id):
    """
    刪除科目：刪除指定科目及其關聯的書籍。
    POST /subjects/<id>/delete
    """
    pass
