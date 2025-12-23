from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
# تصحيح السطر: السماح لجميع الروابط بالوصول (هذا ضروري للمنصات)
CORS(app, resources={r"/*": {"origins": "*"}}) 

# تحميل المودل
try:
    model = joblib.load('ip_shielder_model.pkl')
    print("✅ تم تحميل مودل الذكاء الاصطناعي بنجاح!")
except:
    print("❌ خطأ: لم يتم العثور على ملف ip_shielder_model.pkl. تأكد من تشغيل train_model.py أولاً.")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        print(f"📥 بيانات مستلمة: {data}") # لمراقبة الطلبات في الـ Terminal
        
        # تحويل البيانات لإطار بيانات (DataFrame)
        input_data = pd.DataFrame([{
            'attempts': int(data['attempts']),
            'is_vpn': int(data['is_vpn']),
            'frequency': float(data['frequency']),
            'country_rank': int(data['country_rank'])
        }])
        
        # التوقع
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]
        
        return jsonify({
            "decision": "BLOCK ⛔" if prediction == 1 else "ALLOW ✅",
            "threat_score": f"{probability * 100:.2f}%",
            "is_malicious": bool(prediction)
        })
    except Exception as e:
        print(f"❌ حدث خطأ أثناء المعالجة: {e}")
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    # تشغيل السيرفر
    app.run(host='127.0.0.1', port=5000, debug=True)