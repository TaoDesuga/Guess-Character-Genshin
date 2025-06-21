# file: test_code_checker.py

import unittest
from code_checker import check_python_code

class TestCodeChecker(unittest.TestCase):

    def test_valid_code(self):
        code = """
#IMPORT MODULE
import random
from DataGenshinCharacter import Data_Genshin_Character

#VARIABLE FUNCTION
Character = Data_Genshin_Character()

#RANDOM NAME CHARACTER
random_Character = random.choice(list(Character.keys()))

#HINT
Vision, Weapon, Gender, City, Personality = Character[random_Character]

# MAKE LIST OF
Hint = [
    f"Vision: {Vision}",
    f"Weapon: {Weapon}",
    f"Gender: {Gender}",
    f"City: {City}",
    f"Personality: {Personality}"
]

# สุ่มคำใบ้ 3 ข้อ (จาก 5)
random_Hints = random.sample(Hint, 3)

print("ยินดีต้อนรับสู่เกมส์เดาตัวละคร")
print('จาก เกมส์ GENSHIN IMPACT')
print('ลองทายด้วยการพิมพ์คำตอบดูสิ')

print('กติกาการเล่น/nคำใบ้จะถูกสุ่มขึ้นมา/nแล้วเดาให้ถูกซะ')

while True:
    print(f"คำใบ้: {random_Hints}")
    Answer = str(input("ใส่คำตอบของคุณ: "))

    if Answer == random_Character:
        print("ถูกต้อง คุณเจ๋งที่สุดในโลก")
        break
    else:
        print("ความพยายามเพียงเล็กน้อย จะสร้างคุณค่าอันยิ่งใหญ่ จงพยายามต่อไป จนกว่าจะถูก")
"""
        result = check_python_code(code)
        self.assertEqual(result["status"], "success")
        self.assertIn("greet", result["functions"])

    def test_syntax_error(self):
        code = """
#IMPORT MODULE
import random
from DataGenshinCharacter import Data_Genshin_Character

#VARIABLE FUNCTION
Character = Data_Genshin_Character()

#RANDOM NAME CHARACTER
random_Character = random.choice(list(Character.keys()))

#HINT
Vision, Weapon, Gender, City, Personality = Character[random_Character]

# MAKE LIST OF
Hint = [
    f"Vision: {Vision}",
    f"Weapon: {Weapon}",
    f"Gender: {Gender}",
    f"City: {City}",
    f"Personality: {Personality}"
]

# สุ่มคำใบ้ 3 ข้อ (จาก 5)
random_Hints = random.sample(Hint, 3)

print("ยินดีต้อนรับสู่เกมส์เดาตัวละคร")
print('จาก เกมส์ GENSHIN IMPACT')
print('ลองทายด้วยการพิมพ์คำตอบดูสิ')

print('กติกาการเล่น/nคำใบ้จะถูกสุ่มขึ้นมา/nแล้วเดาให้ถูกซะ')

while True:
    print(f"คำใบ้: {random_Hints}")
    Answer = str(input("ใส่คำตอบของคุณ: "))

    if Answer == random_Character:
        print("ถูกต้อง คุณเจ๋งที่สุดในโลก")
        break
    else:
        print("ความพยายามเพียงเล็กน้อย จะสร้างคุณค่าอันยิ่งใหญ่ จงพยายามต่อไป จนกว่าจะถูก")
"""
        result = check_python_code(code)
        self.assertEqual(result["status"], "error")
        self.assertIn("SyntaxError", result["message"])

    def test_no_functions(self):
        code = """

print("ยินดีต้อนรับสู่เกมส์เดาตัวละคร")
print('จาก เกมส์ GENSHIN IMPACT')
print('ลองทายด้วยการพิมพ์คำตอบดูสิ')

print('กติกาการเล่น/nคำใบ้จะถูกสุ่มขึ้นมา/nแล้วเดาให้ถูกซะ')

while True:
    print(f"คำใบ้: {random_Hints}")
    Answer = str(input("ใส่คำตอบของคุณ: "))

    if Answer == random_Character:
        print("ถูกต้อง คุณเจ๋งที่สุดในโลก")
        break
    else:
        print("ความพยายามเพียงเล็กน้อย จะสร้างคุณค่าอันยิ่งใหญ่ จงพยายามต่อไป จนกว่าจะถูก")
"""
        result = check_python_code(code)
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["functions"], [])

if __name__ == '__main__':
    unittest.main()
