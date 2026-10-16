# แปลงรหัสคีย์บอร์ดระหว่างไทย และ อังกฤษ
EN_TO_TH = {
    'q': 'ๆ', 'w': 'ไ', 'e': 'ำ', 'r': 'พ', 't': 'ะ', 'y': 'ั', 'u': 'ี', 'i': 'ร', 'o': 'น', 'p': 'ย', '[': 'บ', ']': 'ล',
    'a': 'ฟ', 's': 'ห', 'd': 'ก', 'f': 'ด', 'g': 'เ', 'h': '้', 'j': '่', 'k': 'า', 'l': 'ส', ';': 'วง', '\'': 'ๆ',
    'z': 'ผ', 'x': 'ป', 'c': 'แ', 'v': 'อ', 'b': 'ิ', 'n': 'ต', 'm': 'ม', ',': 'ท', '.': 'ใ', '/': 'ฝ',
    'Q': '๐', 'W': '"', 'E': 'ฎ', 'R': 'ฑ', 'T': 'ธ', 'Y': 'ํ', 'U': '์', 'I': 'ณ', 'O': 'ฯ', 'P': 'ญ', '{': 'บ', '}': 'ล',
    'A': 'ฤ', 'S': 'ฆ', 'D': 'ฏ', 'F': 'โ', 'G': 'ฌ', 'H': '็', 'J': '๋', 'K': 'ษ', 'L': 'ศ', ':': 'ซ', '"': '.',
    'Z': '(', 'X': ')', 'C': 'ฉ', 'V': 'ฮ', 'B': 'ฺ', 'N': '์', 'M': '?', '<': 'ฒ', '>': 'ฬ', '?': '?',
}

TH_TO_EN = {v: k for k, v in EN_TO_TH.items()}

def fix_language(text):
    # ตรวจสอบว่าข้อความส่วนใหญ่เป็นภาษาอะไร แล้วสลับเป็นอีกภาษา
    th_count = sum(1 for c in text if c in TH_TO_EN)
    en_count = sum(1 for c in text if c in EN_TO_TH)
    
    result = []
    if en_count > th_count:
        # แปลงจาก อังกฤษ -> ไทย
        for c in text:
            result.append(EN_TO_TH.get(c, c))
    else:
        # แปลงจาก ไทย -> อังกฤษ
        for c in text:
            result.append(TH_TO_EN.get(c, c))
            
    return "".join(result)

# ตัวอย่างการใช้งาน
if __name__ == "__main__":
    sample = "9hv'me9k,0eo;o"
    print(f"ข้อความเดิม: {sample}")
    print(f"ข้อความที่แก้แล้ว: {fix_language(sample)}")