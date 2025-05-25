import os
import json
import requests
from app.models import Prompt, Professor, Course
from app import db
from flask import current_app

def get_active_prompt():
    """الحصول على البرومبت النشط من قاعدة البيانات"""
    prompt = Prompt.query.filter_by(is_active=True).first()
    if not prompt:
        return "أنت مساعد ذكي للجامعة، قسم حاسب آلي بكلية التربية النوعية. تساعد الطلاب في معرفة معلومات عن الدكاترة والمواد الدراسية والمنهج."
    return prompt.content

def build_context():
    """بناء سياق المعلومات من قاعدة البيانات عن الدكاترة والمواد الدراسية"""
    context = []
    
    # إضافة معلومات الدكاترة
    professors = Professor.query.all()
    if professors:
        professor_info = "معلومات الدكاترة:\n"
        for prof in professors:
            professor_info += f"- الاسم: {prof.name}, اللقب: {prof.title}, القسم: {prof.department}, البريد الإلكتروني: {prof.email}\n"
            if prof.office_hours:
                professor_info += f"  الساعات المكتبية: {prof.office_hours}\n"
        context.append(professor_info)
    
    # إضافة معلومات المواد الدراسية
    courses = Course.query.all()
    if courses:
        course_info = "المواد الدراسية:\n"
        for course in courses:
            course_info += f"- الكود: {course.code}, الاسم: {course.name}, الساعات المعتمدة: {course.credit_hours}\n"
            if course.professor:
                course_info += f"  أستاذ المادة: {course.professor.name}\n"
            if course.description:
                course_info += f"  وصف المادة: {course.description}\n"
        context.append(course_info)
    
    return "\n".join(context)

def generate_ai_response(user_message):
    """
    توليد استجابة من نموذج DeepSeek-V3 عبر Together AI API بناءً على رسالة المستخدم
    
    Args:
        user_message (str): رسالة المستخدم
        
    Returns:
        str: استجابة المساعد الذكي
    """
    api_url = current_app.config.get('TOGETHER_API_URL')
    api_key = current_app.config.get('TOGETHER_API_KEY')
    model = current_app.config.get('TOGETHER_MODEL', 'deepseek-ai/deepseek-v3')
    
    # بناء سياق المحادثة
    active_prompt = get_active_prompt()
    context = build_context()
    
    system_message = active_prompt + "\n\n" + context
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ],
        "temperature": 0.7,
        "max_tokens": 800
    }
    
    try:
        # Try to connect to the Together AI API
        try:
            # زيادة مدة الـ timeout لتجنب انقطاع الاتصال
            response = requests.post(api_url, headers=headers, json=payload, timeout=120)
            response.raise_for_status()
            result = response.json()
            return result.get("choices", [{}])[0].get("message", {}).get("content", "عذراً، لم أتمكن من فهم السؤال. يرجى إعادة صياغة سؤالك.")
        except requests.exceptions.RequestException as e:
            print(f"Together API request failed, using fallback: {str(e)}")
            # Fallback for development: simulate a response
            return generate_mock_response(user_message, active_prompt, context)
    except Exception as e:
        print(f"Error generating AI response: {str(e)}")
        return "حدثت مشكلة في الاتصال بالمساعد الذكي. الرجاء المحاولة مرة أخرى لاحقاً."

def generate_mock_response(user_message, prompt, context):
    """
    توليد استجابة محاكاة للتطوير عندما يتعذر الاتصال بالواجهة البرمجية
    """
    # Simple fallback responses based on keywords
    user_message_lower = user_message.lower()
    
    if any(word in user_message_lower for word in ["السلام", "مرحبا", "اهلا"]):
        return "وعليكم السلام! أنا المساعد الذكي للجامعة. كيف يمكنني مساعدتك اليوم؟"
    
    if any(word in user_message_lower for word in ["دكتور", "دكاترة", "استاذ", "مدرس"]):
        professors = Professor.query.all()
        if professors:
            response = "هؤلاء هم الدكاترة المسجلين في النظام:\n\n"
            for prof in professors[:3]:  # Limit to first 3 professors if available
                response += f"- {prof.title} {prof.name} - {prof.department}\n"
            if len(professors) > 3:
                response += "\n... وغيرهم. يمكنك السؤال عن دكتور محدد للحصول على معلومات أكثر."
            return response
        return "لا يوجد حاليًا معلومات عن الدكاترة في النظام. يرجى التواصل مع إدارة الموقع."
    
    if any(word in user_message_lower for word in ["مادة", "مقرر", "كورس", "درس"]):
        courses = Course.query.all()
        if courses:
            response = "هذه بعض المواد الدراسية المسجلة في النظام:\n\n"
            for course in courses[:3]:  # Limit to first 3 courses
                response += f"- {course.name} ({course.code}) - {course.credit_hours} ساعات معتمدة\n"
            if len(courses) > 3:
                response += "\n... وغيرها. يمكنك السؤال عن مادة محددة للحصول على معلومات أكثر."
            return response
        return "لا يوجد حاليًا معلومات عن المواد الدراسية في النظام. يرجى التواصل مع إدارة الموقع."
    
    # Default response
    return "أنا المساعد الذكي للجامعة، وأستطيع مساعدتك في معرفة معلومات عن الدكاترة والمواد الدراسية. يرجى طرح سؤال محدد."