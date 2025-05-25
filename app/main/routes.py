from flask import render_template, request, jsonify
from app.main import bp
from app.models import Professor, Course, Prompt
from app.utils.ai_utils import generate_ai_response

@bp.route('/')
@bp.route('/index')
def index():
    return render_template('main/index.html', title="المساعد الذكي للجامعة")

@bp.route('/chat')
def chat():
    return render_template('main/chat.html', title="تحدث مع المساعد")

@bp.route('/about')
def about():
    professors = Professor.query.all()
    courses = Course.query.all()
    return render_template('main/about.html', title="عن المساعد", professors=professors, courses=courses)