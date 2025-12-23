import pandas as pd
import numpy as np

def generate_malicious_ip_data(n_samples=10000):
    np.random.seed(42)
    
    # 1. عدد محاولات الدخول الفاشلة (المهاجمين عادة لديهم رقم عالي)
    attempts = np.random.randint(1, 100, n_samples)
    
    # 2. هل يستخدم VPN؟ (المهاجمون يميلون لاستخدامه بنسبة أعلى)
    is_vpn = np.random.choice([0, 1], size=n_samples, p=[0.8, 0.2])
    
    # 3. تكرار الطلبات في الثانية (Request Frequency)
    frequency = np.random.uniform(0.1, 50.0, n_samples)
    
    # 4. تصنيف الدولة (1: آمنة جداً، 10: خطرة جداً بناءً على تقارير عالمية)
    country_rank = np.random.randint(1, 11, n_samples)
    
    # بناء معادلة منطقية لتحديد هل هو خبيث (Target)
    # الـ IP يكون خبيثاً إذا زادت المحاولات، وكان يستخدم VPN، وكان التكرار عالياً
    score = (attempts * 0.4) + (is_vpn * 20) + (frequency * 0.5) + (country_rank * 2)
    
    # إذا تجاوز السكور حد معين نعتبره خبيث (1)، وإلا فهو نظيف (0)
    is_malicious = (score > 45).astype(int)
    
    # إنشاء الجدول
    df = pd.DataFrame({
        'attempts': attempts,
        'is_vpn': is_vpn,
        'frequency': frequency,
        'country_rank': country_rank,
        'is_malicious': is_malicious
    })
    
    # حفظ البيانات في ملف CSV
    df.to_csv('ips_data.csv', index=False)
    print(f"✅ تم إنشاء ملف 'ips_data.csv' بنجاح مع {n_samples} سجل!")

if __name__ == "__main__":
    generate_malicious_ip_data()