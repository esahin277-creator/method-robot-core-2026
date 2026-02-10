from src.agents.strategist_agent import Strategist
from src.agents.verifier_agent import Verifier
from src.collectors.master_collector import MasterCollector

def run_precision_analysis(topic):
    # 1. Veri Toplama
    raw_data = MasterCollector().collect_all(topic)
    
    # 2. Birinci Analiz (Stratejist)
    initial_report = Strategist().analyze(raw_data)
    
    # 3. Doğrulama ve Hata Ayıklama (Verifier)
    # Verifier, sonucu %100 doğruluğa ulaştırana kadar loop'a sokar.
    final_result, confidence_score = Verifier().cross_check(initial_report, raw_data)
    
    if confidence_score < 0.99:
        print("Hata Payı Yüksek! Yeniden analiz ediliyor...")
        return run_precision_analysis(topic) # Öz-Yineleme (Recursive)
    
    return final_result

if __name__ == "__main__":
    result = run_precision_analysis("Gürbulak Sınır Kapısı Tır Yoğunluğu")
    print(f"Sıfır Hataya Yakın Sonuç: {result}")
