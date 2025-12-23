from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
import requests

app = Flask(__name__)
CORS(app)

model = joblib.load('ip_shielder_model.pkl')

def get_ip_details(ip_address):
    # استخدام API مجاني لجلب بيانات الـ IP
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}?fields=status,countryCode,mobile,proxy,hosting")
        data = response.json()
        if data['status'] == 'success':
            # تحويل البيانات لخصائص يفهمها المودل الخاص بنا
            return {
                "is_vpn": 1 if (data.get('proxy') or data.get('hosting')) else 0,
                "country_rank": 5, # يمكن تطويرها لتعطي رقماً بناءً على الدولة
                "attempts": 1,     # قيمة افتراضية للفحص الفردي
                "frequency": 1.0   # قيمة افتراضية
            }
    except:
        return None

@app.route('/predict_real', methods=['POST'])
def predict_real():
    data = request.get_json()
    target_ip = data.get('ip')
    
    # 1. جلب البيانات الحقيقية من المواقع العالمية
    real_features = get_ip_details(target_ip)
    
    if not real_features:
        return jsonify({"error": "تعذر جلب بيانات الـ IP"}), 400

    # 2. تمرير البيانات للمودل
    input_data = pd.DataFrame([real_features])
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]
    
    return jsonify({
        "ip": target_ip,
        "is_vpn": real_features['is_vpn'],
        "decision": "BLOCK ⛔" if prediction == 1 else "ALLOW ✅",
        "threat_score": f"{probability * 100:.2f}%"
    })

if __name__ == '__main__':
    app.run(port=5000, debug=True)