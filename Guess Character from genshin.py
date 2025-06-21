from tkinter import *
import random
from DataGenshinCharacter import Data_Genshin_Character

# INITIALIZE
ayaka = Tk()
ayaka.title("APP-D-BY-TAO")
ayaka.geometry("720x1080")

Character = Data_Genshin_Character()

# VARIABLES
txt = StringVar()

# HEADING
Label(ayaka, text="ยินดีต้อนรับสู่เกมส์เดาตัวละคร").pack()
Label(ayaka, text="จาก เกมส์ GENSHIN IMPACT").pack()
Label(ayaka, text="ลองทายด้วยการพิมพ์คำตอบดูสิ").pack()
Label(ayaka, text="กติกาการเล่น\nคำใบ้จะถูกสุ่มขึ้นมา\nแล้วเดาให้ถูกซะ").pack()

# HINT LABEL (จะถูกอัปเดตทุกคำถาม)
hint_Label = Label(ayaka, text='', font=("Arial", 14), wraplength=600, fg="blue")
hint_Label.pack(pady=10)

# ENTRY
Entry(ayaka, textvariable=txt).pack()

# RESULT LABEL
result_Label = Label(ayaka, text='', font=("Arial", 12))
result_Label.pack(pady=10)

# FUNCTION
def next_question():
    global random_Character
    random_Character = random.choice(list(Character.keys()))
    Vision, Weapon, Gender, City, Personality = Character[random_Character]
    hints = [
        f"Vision: {Vision}",
        f"Weapon: {Weapon}",
        f"Gender: {Gender}",
        f"City: {City}",
        f"Personality: {Personality}"
    ]
    random_Hints = random.sample(hints, 3)
    hint_Label.config(text="\n".join(random_Hints))
    txt.set("")
    result_Label.config(text="")

def check_Answer():
    Answer = txt.get().strip()
    if Answer.lower() == random_Character.lower():
        result_Label.config(text="✅ ถูกต้อง คุณเจ๋งที่สุดในโลก", fg='green')
        ayaka.after(1500, next_question)  # เปลี่ยนคำถามหลัง 1.5 วิ
    else:
        result_Label.config(text="❌ ผิดนะ ลองอีกครั้ง!", fg='red')

# BUTTON
Button(ayaka, text='ส่งคำตอบ', command=check_Answer).pack()

# เริ่มคำถามแรก
next_question()

# LOOP
ayaka.mainloop()
