from app import create_app, db
from app.models import Professor, Course, Prompt

app = create_app()

with app.app_context():
    # Create tables
    db.create_all()
    
    # Add a default prompt if none exists
    if not Prompt.query.count():
        default_prompt = Prompt(
            name="البرومبت الافتراضي",
            content="""أنت مساعد ذكي للجامعة، قسم حاسب آلي بكلية التربية النوعية. 
مهمتك مساعدة الطلاب في الإجابة على أسئلتهم المتعلقة بالدكاترة والمواد الدراسية والمنهج.
قدم إجابات دقيقة ومختصرة وودية. استخدم المعلومات المتاحة لك حول الدكاترة والمقررات 
الدراسية للإجابة على استفسارات الطلاب بشكل مفيد.""",
            is_active=True
        )
        db.session.add(default_prompt)
        db.session.commit()
        print("تم إنشاء البرومبت الافتراضي")

    print("تم إنشاء قاعدة البيانات بنجاح!")