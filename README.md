

# 🛡️ AI-Powered IP Security & Classification System

نظام ذكي يعتمد على **تعلم الآلة (Machine Learning)** لتصنيف عناوين الـ IP (آمنة أو خبيثة) مع واجهة رسومية عصرية وتخزين النتائج في قاعدة بيانات **MySQL**.

## 🚀 مميزات المشروع
- **ML Model:** يستخدم خوارزمية `RandomForestClassifier` لتحليل سلوك الـ IP.
- **Modern GUI:** واجهة مستخدم احترافية باستخدام `CustomTkinter`.
- **Database Integration:** ربط مباشر مع `MySQL` لحفظ سجلات الفحص.
- **Modular Code:** تقسيم الكود إلى ملفات منفصلة (التدريب، إدارة القاعدة، الواجهة).

## 🛠️ التقنيات المستخدمة (Tech Stack)
- **لغة البرمجة:** Python 3.13
- **المكتبات:** Pandas, Scikit-learn, Joblib, CustomTkinter
- **قواعد البيانات:** MySQL

## 📂 هيكل المشروع (Project Structure)
- `generate_data.py`: لتوليد بيانات وهمية للتدريب.
- `train.py`: لتدريب نموذج الذكاء الاصطناعي وحفظه.
- `db_manager.py`: كود الاتصال والتعامل مع قاعدة البيانات.
- `gui_app.py`: الواجهة الرسومية والتشغيل النهائي.
- `ip_dataset.csv`: ملف البيانات المستخدم للتعلم.