from flask import render_template, request, redirect, url_for, flash, jsonify
from app.admin import bp
from app import db
from app.models import Professor, Course, Prompt, ChatHistory
from datetime import datetime

@bp.route('/')
def index():
    professors_count = Professor.query.count()
    courses_count = Course.query.count()
    prompts_count = Prompt.query.count()
    chat_count = ChatHistory.query.count()
    
    return render_template('admin/index.html', title="لوحة الإدارة",
                          professors_count=professors_count,
                          courses_count=courses_count,
                          prompts_count=prompts_count,
                          chat_count=chat_count)

# إدارة الدكاترة
@bp.route('/professors')
def professors():
    professors = Professor.query.all()
    return render_template('admin/professors.html', title="إدارة الدكاترة", professors=professors)

@bp.route('/professors/add', methods=['GET', 'POST'])
def add_professor():
    if request.method == 'POST':
        professor = Professor(
            name=request.form['name'],
            title=request.form['title'],
            department=request.form['department'],
            email=request.form['email'],
            office_hours=request.form['office_hours'],
            phone=request.form['phone'],
            bio=request.form['bio']
        )
        
        db.session.add(professor)
        db.session.commit()
        flash('تم إضافة الدكتور بنجاح!', 'success')
        return redirect(url_for('admin.professors'))
    
    return render_template('admin/professor_form.html', title="إضافة دكتور جديد")

@bp.route('/professors/<int:id>/edit', methods=['GET', 'POST'])
def edit_professor(id):
    professor = Professor.query.get_or_404(id)
    
    if request.method == 'POST':
        professor.name = request.form['name']
        professor.title = request.form['title']
        professor.department = request.form['department']
        professor.email = request.form['email']
        professor.office_hours = request.form['office_hours']
        professor.phone = request.form['phone']
        professor.bio = request.form['bio']
        
        db.session.commit()
        flash('تم تعديل بيانات الدكتور بنجاح!', 'success')
        return redirect(url_for('admin.professors'))
    
    return render_template('admin/professor_form.html', title="تعديل بيانات الدكتور", professor=professor)

@bp.route('/professors/<int:id>/delete', methods=['POST'])
def delete_professor(id):
    professor = Professor.query.get_or_404(id)
    db.session.delete(professor)
    db.session.commit()
    flash('تم حذف الدكتور بنجاح!', 'success')
    return redirect(url_for('admin.professors'))

# إدارة المواد الدراسية
@bp.route('/courses')
def courses():
    courses = Course.query.all()
    return render_template('admin/courses.html', title="إدارة المواد الدراسية", courses=courses)

@bp.route('/courses/add', methods=['GET', 'POST'])
def add_course():
    professors = Professor.query.all()
    
    if request.method == 'POST':
        course = Course(
            code=request.form['code'],
            name=request.form['name'],
            description=request.form['description'],
            credit_hours=int(request.form['credit_hours']),
            professor_id=int(request.form['professor_id']) if request.form['professor_id'] else None,
            semester=request.form['semester'],
            syllabus=request.form['syllabus']
        )
        
        db.session.add(course)
        db.session.commit()
        flash('تم إضافة المادة بنجاح!', 'success')
        return redirect(url_for('admin.courses'))
    
    return render_template('admin/course_form.html', title="إضافة مادة جديدة", professors=professors)

@bp.route('/courses/<int:id>/edit', methods=['GET', 'POST'])
def edit_course(id):
    course = Course.query.get_or_404(id)
    professors = Professor.query.all()
    
    if request.method == 'POST':
        course.code = request.form['code']
        course.name = request.form['name']
        course.description = request.form['description']
        course.credit_hours = int(request.form['credit_hours'])
        course.professor_id = int(request.form['professor_id']) if request.form['professor_id'] else None
        course.semester = request.form['semester']
        course.syllabus = request.form['syllabus']
        
        db.session.commit()
        flash('تم تعديل بيانات المادة بنجاح!', 'success')
        return redirect(url_for('admin.courses'))
    
    return render_template('admin/course_form.html', title="تعديل بيانات المادة", course=course, professors=professors)

@bp.route('/courses/<int:id>/delete', methods=['POST'])
def delete_course(id):
    course = Course.query.get_or_404(id)
    db.session.delete(course)
    db.session.commit()
    flash('تم حذف المادة بنجاح!', 'success')
    return redirect(url_for('admin.courses'))

# إدارة البرومبت الخاص بالمساعد الذكي
@bp.route('/prompts')
def prompts():
    prompts = Prompt.query.all()
    return render_template('admin/prompts.html', title="إدارة البرومبت", prompts=prompts)

@bp.route('/prompts/add', methods=['GET', 'POST'])
def add_prompt():
    if request.method == 'POST':
        prompt = Prompt(
            name=request.form['name'],
            content=request.form['content'],
            is_active=True if 'is_active' in request.form else False
        )
        
        db.session.add(prompt)
        db.session.commit()
        flash('تم إضافة البرومبت بنجاح!', 'success')
        return redirect(url_for('admin.prompts'))
    
    return render_template('admin/prompt_form.html', title="إضافة برومبت جديد")

@bp.route('/prompts/<int:id>/edit', methods=['GET', 'POST'])
def edit_prompt(id):
    prompt = Prompt.query.get_or_404(id)
    
    if request.method == 'POST':
        prompt.name = request.form['name']
        prompt.content = request.form['content']
        prompt.is_active = True if 'is_active' in request.form else False
        prompt.updated_at = datetime.utcnow()
        
        db.session.commit()
        flash('تم تعديل البرومبت بنجاح!', 'success')
        return redirect(url_for('admin.prompts'))
    
    return render_template('admin/prompt_form.html', title="تعديل البرومبت", prompt=prompt)

@bp.route('/prompts/<int:id>/delete', methods=['POST'])
def delete_prompt(id):
    prompt = Prompt.query.get_or_404(id)
    db.session.delete(prompt)
    db.session.commit()
    flash('تم حذف البرومبت بنجاح!', 'success')
    return redirect(url_for('admin.prompts'))

# سجل المحادثات
@bp.route('/chat-history')
def chat_history():
    history = ChatHistory.query.order_by(ChatHistory.timestamp.desc()).all()
    return render_template('admin/chat_history.html', title="سجل المحادثات", history=history)