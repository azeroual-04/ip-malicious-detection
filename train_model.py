import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

# 1. تحميل البيانات التي أنشأناها
print("⌛ جاري تحميل البيانات...")
df = pd.read_csv('ips_data.csv')

# 2. تقسيم البيانات إلى ميزات (X) وهدف (y)
# الميزات: الأشياء التي يراقبها النظام
# الهدف: النتيجة (خبيث أو نظيف)
X = df[['attempts', 'is_vpn', 'frequency', 'country_rank']]
y = df['is_malicious']

# 3. تقسيم البيانات (80% للتدريب و 20% للاختبار)
# هذا يضمن أننا نختبر المودل ببيانات لم يراها من قبل
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. اختيار الخوارزمية (الغابة العشوائية - Random Forest)
# هي من أقوى الخوارزميات للتعامل مع البيانات الجدولية وتصنيفها
print("🧠 جاري تدريب الذكاء الاصطناعي...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5. تقييم المودل
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ تم التدريب! دقة النموذج هي: {accuracy * 100:.2f}%")

# 6. حفظ "المخ" (المودل) في ملف لاستخدامه في المنصة
joblib.dump(model, 'ip_shielder_model.pkl')
print("💾 تم حفظ المودل بنجاح في ملف: ip_shielder_model.pkl")