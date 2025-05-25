from flask import request, jsonify
from app.api import bp
from app import db
from app.models import Professor, Course, Prompt, ChatHistory
from app.utils.ai_utils import generate_ai_response

@bp.route('/chat', methods=['POST'])
def chat():
    data = request.json
    if not data or 'message' not in data:
        return jsonify({'error': 'لم يتم توفير رسالة'}), 400

    user_message = data['message']
    
    # الحصول على استجابة من المساعد الذكي
    ai_response = generate_ai_response(user_message)
    
    # حفظ المحادثة في قاعدة البيانات
    chat_entry = ChatHistory(
        user_query=user_message,
        assistant_response=ai_response
    )
    db.session.add(chat_entry)
    db.session.commit()
    
    return jsonify({
        'response': ai_response
    })

@bp.route('/professors', methods=['GET'])
def get_professors():
    professors = Professor.query.all()
    return jsonify([professor.to_dict() for professor in professors])

@bp.route('/professors/<int:id>', methods=['GET'])
def get_professor(id):
    professor = Professor.query.get_or_404(id)
    return jsonify(professor.to_dict())

@bp.route('/courses', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    return jsonify([course.to_dict() for course in courses])

@bp.route('/courses/<int:id>', methods=['GET'])
def get_course(id):
    course = Course.query.get_or_404(id)
    return jsonify(course.to_dict())

@bp.route('/prompts/active', methods=['GET'])
def get_active_prompt():
    prompt = Prompt.query.filter_by(is_active=True).first()
    if not prompt:
        return jsonify({'error': 'لا يوجد برومبت نشط'}), 404
    return jsonify(prompt.to_dict())