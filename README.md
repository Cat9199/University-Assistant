# 🎓 Smart University Assistant | المساعد الذكي للجامعة

<div align="center">

![University Assistant](https://img.shields.io/badge/University-Assistant-blue?style=for-the-badge)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

**مشروع تخرج - كلية التربية النوعية جامعة الإسكندرية**

[العرض المباشر](#) | [التوثيق](#installation) | [الفريق](#team)

</div>

---

## 📋 نظرة عامة | Overview

لقد قمت بتطوير المساعد الذكي للجامعة كتطبيق ويب متطور مصمم خصيصاً لخدمة طلاب وأعضاء هيئة التدريس في **كلية التربية النوعية - جامعة الإسكندرية**. 

قمت بتطوير النظام ليوفر مساعد ذكي تفاعلي يمكنه الإجابة على استفسارات الطلاب حول:
- معلومات الأقسام الأكاديمية الخمسة
- أعضاء هيئة التدريس وتخصصاتهم  
- المقررات الدراسية والمناهج
- شروط القبول والتحويل
- الخدمات الطلابية والفرص الوظيفية

---

## ✨ المميزات الرئيسية | Key Features

### 🤖 **المساعد الذكي**
- دردشة تفاعلية باللغة العربية
- إجابات فورية ودقيقة على استفسارات الطلاب
- اقتراحات أسئلة سريعة
- حفظ تاريخ المحادثات

### 🏛️ **معلومات شاملة عن الكلية**
- **5 أقسام أكاديمية**: تكنولوجيا التعليم، الاقتصاد المنزلي، التربية الفنية، التربية الموسيقية، العلوم التربوية والنفسية
- معلومات مفصلة عن كل قسم وتخصصاته
- بيانات أعضاء هيئة التدريس ووسائل التواصل
- المقررات الدراسية والمناهج

### ⚙️ **لوحة إدارة متقدمة**
- إدارة معلومات الأساتذة والمقررات
- تحرير رسائل المساعد الذكي
- مراقبة استفسارات الطلاب
- تحليل إحصائيات الاستخدام

### 📱 **تصميم متجاوب**
- يعمل بسلاسة على جميع الأجهزة
- واجهة مستخدم حديثة وسهلة الاستخدام
- دعم كامل للغة العربية (RTL)

---

## 🛠️ التقنيات المستخدمة | Technologies Used

### Backend
- **Python 3.8+** - لغة البرمجة الأساسية
- **Flask** - إطار العمل الأساسي
- **SQLAlchemy** - قاعدة البيانات والـ ORM
- **SQLite** - قاعدة بيانات خفيفة وسريعة

### Frontend  
- **HTML5/CSS3** - بنية وتصميم الواجهات
- **JavaScript** - التفاعل والديناميكية
- **Tailwind CSS** - إطار عمل التصميم المتجاوب
- **Font Awesome** - الأيقونات

### المكتبات والأدوات
- **Jinja2** - محرك القوالب
- **Marked.js** - لتنسيق الماركداون
- **Prism.js** - لعرض الأكواد البرمجية
- **DeepSeek AI** - للمساعد الذكي

---

## 🏗️ هيكل المشروع | Project Structure

```
SmartUniversityAssistant/
├── 📁 app/                          # التطبيق الأساسي
│   ├── 📁 main/                     # الصفحات الرئيسية
│   │   ├── routes.py                # مسارات الصفحات الأساسية
│   │   └── __init__.py
│   ├── 📁 admin/                    # لوحة الإدارة  
│   │   ├── routes.py                # مسارات الإدارة
│   │   └── __init__.py
│   ├── 📁 api/                      # واجهة برمجة التطبيقات
│   │   ├── routes.py                # API endpoints
│   │   └── __init__.py
│   ├── 📁 templates/                # قوالب HTML
│   │   ├── 📁 main/                 # قوالب الصفحات الرئيسية
│   │   ├── 📁 admin/                # قوالب لوحة الإدارة
│   │   └── base.html                # القالب الأساسي
│   ├── 📁 static/                   # الملفات الثابتة
│   │   ├── 📁 css/                  # ملفات التصميم
│   │   ├── 📁 js/                   # ملفات JavaScript
│   │   └── 📁 images/               # الصور
│   ├── 📁 utils/                    # الأدوات المساعدة
│   │   └── ai_utils.py              # منطق المساعد الذكي
│   ├── models.py                    # نماذج قاعدة البيانات
│   └── __init__.py                  # إعداد التطبيق
├── 📄 config.py                     # إعدادات التطبيق
├── 📄 run.py                        # تشغيل التطبيق
├── 📄 create_db.py                  # إنشاء قاعدة البيانات
├── 📄 requirements.txt              # المتطلبات
├── 📄 .env                          # متغيرات البيئة
└── 📄 README.md                     # ملف التوثيق
```

---

## 🚀 التثبيت والتشغيل | Installation & Setup

### متطلبات النظام
- Python 3.8 أو أحدث
- pip (مدير حزم Python)
- Git

### خطوات التثبيت

1. **استنساخ المشروع**
   ```bash
   git clone https://github.com/Cat9199/University-Assistant.git
   cd University-Assistant
   ```

2. **إنشاء بيئة افتراضية**
   ```bash
   python -m venv venv
   
   # على Windows
   venv\Scripts\activate
   
   # على Linux/Mac
   source venv/bin/activate
   ```

3. **تثبيت المتطلبات**
   ```bash
   pip install -r requirements.txt
   ```

4. **إعداد متغيرات البيئة**
   ```bash
   # إنشاء ملف .env
   echo "SECRET_KEY=your-secret-key-here" > .env
   echo "DATABASE_URL=sqlite:///app.db" >> .env
   ```

5. **إنشاء قاعدة البيانات**
   ```bash
   python create_db.py
   ```

6. **تشغيل التطبيق**
   ```bash
   python run.py
   ```

7. **افتح المتصفح واذهب إلى**
   ```
   http://localhost:5000
   ```

---

## 📊 قاعدة البيانات | Database Schema

### الجداول الرئيسية

#### 👨‍🏫 Professors (الأساتذة)
- `id` - المعرف الفريد
- `name` - اسم الدكتور
- `department` - القسم  
- `email` - البريد الإلكتروني
- `position` - المنصب
- `specialization` - التخصص

#### 📚 Courses (المقررات)
- `id` - المعرف الفريد
- `name` - اسم المقرر
- `code` - كود المقرر
- `department` - القسم
- `description` - الوصف
- `credit_hours` - الساعات المعتمدة

#### 💬 Chat_History (تاريخ المحادثات)
- `id` - المعرف الفريد
- `user_message` - رسالة المستخدم
- `bot_response` - رد المساعد
- `timestamp` - وقت المحادثة

---

## 🎯 الاستخدام | Usage

### للطلاب
1. **استكشاف الكلية** - تصفح معلومات الأقسام والمقررات
2. **المساعد الذكي** - اسأل أي سؤال واحصل على إجابة فورية
3. **معلومات الأساتذة** - تعرف على أعضاء هيئة التدريس وتخصصاتهم
4. **الخدمات الطلابية** - معلومات عن الجداول والنتائج والأنشطة

### للإداريين
1. **لوحة الإدارة** - إدارة البيانات وتحديث المعلومات
2. **مراقبة الاستفسارات** - متابعة أسئلة الطلاب والإجابات
3. **إدارة المحتوى** - تحديث معلومات الأساتذة والمقررات

---

## 📸 لقطات الشاشة | Screenshots

<div align="center">

### الصفحة الرئيسية
![Homepage](screenshots/homepage.png)

### المساعد الذكي  
![Chat Interface](screenshots/chat.png)

### لوحة الإدارة
![Admin Panel](screenshots/admin.png)

</div>

---

## 🔮 التطوير المستقبلي | Future Enhancements

- [ ] **تطبيق موبايل** - تطوير تطبيق Android/iOS
- [ ] **إشعارات فورية** - تنبيهات للمواعيد والأخبار المهمة  
- [ ] **تكامل مع أنظمة الجامعة** - ربط مع أنظمة الجداول والنتائج
- [ ] **ذكاء اصطناعي متقدم** - تحسين دقة المساعد الذكي
- [ ] **دعم متعدد اللغات** - إضافة اللغة الإنجليزية
- [ ] **تحليلات متقدمة** - إحصائيات استخدام مفصلة

---

## 👥 فريق العمل | Development Team

<div align="center">

| الاسم | الدور | التخصص |
|-------|--------|----------|
| **[اسم الطالب 1]** | Project Manager | إدارة المشروع والتنسيق |
| **[اسم الطالب 2]** | Backend Developer | تطوير الخادم وقاعدة البيانات |
| **[اسم الطالب 3]** | Frontend Developer | تطوير واجهات المستخدم |  
| **[اسم الطالب 4]** | AI/ML Engineer | تطوير المساعد الذكي |
| **[اسم الطالب 5]** | UI/UX Designer | تصميم تجربة المستخدم |

**المشرف الأكاديمي**: د. [اسم المشرف] - كلية التربية النوعية

</div>

---

## 📄 الترخيص | License

هذا المشروع مرخص تحت [MIT License](LICENSE) - اطلع على ملف LICENSE للمزيد من التفاصيل.

---

## 🤝 المساهمة | Contributing

لقد قمت بتطوير هذا المشروع ونرحب بمساهمات الآخرين لتحسينه.

### كيفية المساهمة
1. Fork المشروع
2. إنشاء branch جديد (`git checkout -b feature/AmazingFeature`)
3. Commit التغييرات (`git commit -m 'Add some AmazingFeature'`)
4. Push إلى البranch (`git push origin feature/AmazingFeature`)
5. فتح Pull Request

---

## 📞 التواصل | Contact

**كلية التربية النوعية - جامعة الإسكندرية**

- 📧 Email: spedu-alumni@alexu.edu.eg
- 📱 Phone: 03-5454313  
- 🌐 Website: [edusp.alexu.edu.eg](https://edusp.alexu.edu.eg)
- 📍 Address: أبيس، الإسكندرية، مصر

**روابط المشروع:**
- 🔗 GitHub: [https://github.com/Cat9199/University-Assistant](https://github.com/Cat9199/University-Assistant)
- 📖 Documentation: [Wiki](https://github.com/Cat9199/University-Assistant/wiki)
- 🐛 Issues: [Bug Reports](https://github.com/Cat9199/University-Assistant/issues)

---

<div align="center">

**Made with ❤️ by Faculty of Specific Education Students**

⭐ إذا أعجبك المشروع، لا تنس إضافة نجمة على GitHub!

![Visitors](https://visitor-badge.laobi.icu/badge?page_id=Cat9199.University-Assistant)

</div>