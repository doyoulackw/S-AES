import tkinter as tk
from tkinter import ttk
import s_aes
import re


def is_hex_string(s):
    pattern = r'^[0-9a-fA-F]{4}$'
    return bool(re.match(pattern, s))


class Entry:
    def __init__(self):
        self.entry_1 = tk.Entry
        self.entry_2 = tk.Entry
        self.entry_3 = tk.Entry
        self.entry_4 = tk.Entry
        self.entry_5 = tk.Entry
        self.combo = ttk.Combobox

        self.s_aes = s_aes.SimpleAes
        self.key_1 = 0
        self.key_2 = -1

    def on_button_click(self, leaf):
        # 在按钮点击时执行的函数
        entry1_value = self.entry_1.get()
        entry2_value = self.entry_2.get()

        if leaf == 0:
            codes = self.combo.get()

            if not is_hex_string(entry2_value):
                result = "密钥格式不正确"
            else:
                if codes == "binary":
                    result = self.s_aes.encrypt_b(entry1_value, entry2_value)
                    if not (result == "明文内容不正确" or result == "明文格式不正确"):
                        result = self.s_aes.list_to_string(result)
                else:
                    c = self.s_aes.encrypt_c(entry1_value, entry2_value, codes)
                    result = self.s_aes.decode_h(c)

            self.entry_5.config(state="normal")
            self.entry_5.delete(0, tk.END)
            self.entry_5.insert(0, result)
            self.entry_5.config(state="readonly")

        elif leaf == 1:
            codes = self.combo.get()

            entry3_value = self.entry_3.get()
            if not (is_hex_string(entry2_value) and is_hex_string(entry3_value)):
                result = "密钥格式不正确"
            else:
                if codes == "binary":
                    result = self.s_aes.encrypt_b(entry1_value, entry2_value)
                    if not (result == "明文内容不正确" or result == "明文格式不正确"):
                        result = self.s_aes.list_to_string(result)
                        result = self.s_aes.encrypt_b(result, entry3_value)
                        result = self.s_aes.list_to_string(result)
                else:
                    c = self.s_aes.encrypt_c(entry1_value, entry2_value, codes)
                    result = self.s_aes.encrypt_b(c, entry3_value)
                    if not (result == "明文内容不正确" or result == "明文格式不正确"):
                        result = self.s_aes.list_to_string(result)
                        result = self.s_aes.decode_h(result)

            self.entry_5.config(state="normal")
            self.entry_5.delete(0, tk.END)
            self.entry_5.insert(0, result)
            self.entry_5.config(state="readonly")

        elif leaf == 2:
            codes = self.combo.get()

            entry3_value = self.entry_3.get()
            if not (is_hex_string(entry2_value) and is_hex_string(entry3_value)):
                result = "密钥格式不正确"
            else:
                if codes == "binary":
                    result = self.s_aes.encrypt_b(entry1_value, entry2_value)
                    if not (result == "明文内容不正确" or result == "明文格式不正确"):
                        result = self.s_aes.list_to_string(result)
                        result = self.s_aes.encrypt_b(result, entry3_value)
                        result = self.s_aes.list_to_string(result)
                        result = self.s_aes.encrypt_b(result, entry2_value)
                        result = self.s_aes.list_to_string(result)
                else:
                    c = self.s_aes.encrypt_c(entry1_value, entry2_value, codes)
                    result = self.s_aes.encrypt_b(c, entry3_value)
                    if not (result == "明文内容不正确" or result == "明文格式不正确"):
                        result = self.s_aes.list_to_string(result)
                        result = self.s_aes.encrypt_b(result, entry2_value)
                        result = self.s_aes.list_to_string(result)
                        result = self.s_aes.decode_h(result)

            self.entry_5.config(state="normal")
            self.entry_5.delete(0, tk.END)
            self.entry_5.insert(0, result)
            self.entry_5.config(state="readonly")

        elif leaf == 3:
            codes = self.combo.get()

            entry3_value = self.entry_3.get()
            entry4_value = self.entry_4.get()
            if not (is_hex_string(entry2_value) and is_hex_string(entry3_value) and is_hex_string(entry4_value)):
                result = "密钥格式不正确"
            else:
                if codes == "binary":
                    result = self.s_aes.encrypt_b(entry1_value, entry2_value)
                    if not (result == "明文内容不正确" or result == "明文格式不正确"):
                        result = self.s_aes.list_to_string(result)
                        result = self.s_aes.encrypt_b(result, entry3_value)
                        result = self.s_aes.list_to_string(result)
                        result = self.s_aes.encrypt_b(result, entry4_value)
                        result = self.s_aes.list_to_string(result)
                else:
                    c = self.s_aes.encrypt_c(entry1_value, entry2_value, codes)
                    result = self.s_aes.encrypt_b(c, entry3_value)
                    if not (result == "明文内容不正确" or result == "明文格式不正确"):
                        result = self.s_aes.list_to_string(result)
                        result = self.s_aes.encrypt_b(result, entry4_value)
                        result = self.s_aes.list_to_string(result)
                        result = self.s_aes.decode_h(result)

            self.entry_5.config(state="normal")
            self.entry_5.delete(0, tk.END)
            self.entry_5.insert(0, result)
            self.entry_5.config(state="readonly")

        elif leaf == 4:
            codes = self.combo.get()

            if not is_hex_string(entry2_value):
                result = "密钥格式不正确"
            else:
                if codes == "binary":
                    result = self.s_aes.decrypt_b(entry1_value, entry2_value)
                    if not (result == "密文内容不正确" or result == "密文格式不正确"):
                        result = self.s_aes.list_to_string(result)
                else:
                    c = self.s_aes.encode_h(entry1_value)
                    result = self.s_aes.decrypt_c(c, entry2_value, codes)

            self.entry_5.config(state="normal")
            self.entry_5.delete(0, tk.END)
            self.entry_5.insert(0, result)
            self.entry_5.config(state="readonly")

        elif leaf == 5:
            codes = self.combo.get()

            entry3_value = self.entry_3.get()
            if not (is_hex_string(entry2_value) and is_hex_string(entry3_value)):
                result = "密钥格式不正确"
            else:
                if codes == "binary":
                    result = self.s_aes.decrypt_b(entry1_value, entry3_value)
                    if not (result == "密文内容不正确" or result == "密文格式不正确"):
                        result = self.s_aes.list_to_string(result)
                        result = self.s_aes.decrypt_b(result, entry2_value)
                        result = self.s_aes.list_to_string(result)
                else:
                    c = self.s_aes.encode_h(entry1_value)
                    result = self.s_aes.decrypt_b(c, entry3_value)
                    if not (result == "密文内容不正确" or result == "密文格式不正确"):
                        result = self.s_aes.list_to_string(result)
                        result = self.s_aes.decrypt_c(result, entry2_value, codes)

            self.entry_5.config(state="normal")
            self.entry_5.delete(0, tk.END)
            self.entry_5.insert(0, result)
            self.entry_5.config(state="readonly")

        elif leaf == 6:
            codes = self.combo.get()

            entry3_value = self.entry_3.get()
            if not (is_hex_string(entry2_value) and is_hex_string(entry3_value)):
                result = "密钥格式不正确"
            else:
                if codes == "binary":
                    result = self.s_aes.decrypt_b(entry1_value, entry2_value)
                    if not (result == "密文内容不正确" or result == "密文格式不正确"):
                        result = self.s_aes.list_to_string(result)
                        result = self.s_aes.decrypt_b(result, entry3_value)
                        result = self.s_aes.list_to_string(result)
                        result = self.s_aes.decrypt_b(result, entry2_value)
                        result = self.s_aes.list_to_string(result)
                else:
                    c = self.s_aes.encode_h(entry1_value)
                    result = self.s_aes.decrypt_b(c, entry2_value)
                    if not (result == "密文内容不正确" or result == "密文格式不正确"):
                        result = self.s_aes.list_to_string(result)
                        result = self.s_aes.decrypt_b(result, entry3_value)
                        result = self.s_aes.list_to_string(result)
                        result = self.s_aes.decrypt_c(result, entry2_value, codes)

            self.entry_5.config(state="normal")
            self.entry_5.delete(0, tk.END)
            self.entry_5.insert(0, result)
            self.entry_5.config(state="readonly")

        elif leaf == 7:
            codes = self.combo.get()

            entry3_value = self.entry_3.get()
            entry4_value = self.entry_4.get()
            if not (is_hex_string(entry2_value) and is_hex_string(entry3_value) and is_hex_string(entry4_value)):
                result = "密钥格式不正确"
            else:
                if codes == "binary":
                    result = self.s_aes.decrypt_b(entry1_value, entry4_value)
                    if not (result == "密文内容不正确" or result == "密文格式不正确"):
                        result = self.s_aes.list_to_string(result)
                        result = self.s_aes.decrypt_b(result, entry3_value)
                        result = self.s_aes.list_to_string(result)
                        result = self.s_aes.decrypt_b(result, entry2_value)
                        result = self.s_aes.list_to_string(result)
                else:
                    c = self.s_aes.encode_h(entry1_value)
                    result = self.s_aes.decrypt_b(c, entry4_value)
                    if not (result == "密文内容不正确" or result == "密文格式不正确"):
                        result = self.s_aes.list_to_string(result)
                        result = self.s_aes.decrypt_b(result, entry3_value)
                        result = self.s_aes.list_to_string(result)
                        result = self.s_aes.decrypt_c(result, entry2_value, codes)

            self.entry_5.config(state="normal")
            self.entry_5.delete(0, tk.END)
            self.entry_5.insert(0, result)
            self.entry_5.config(state="readonly")

        elif leaf == 8:
            result = self.middle_attack()

            if len(result) == 2:
                self.entry_4.config(state="normal")
                self.entry_4.delete(0, tk.END)
                self.entry_4.insert(0, result[0])
                self.entry_4.config(state="readonly")
                self.entry_5.config(state="normal")
                self.entry_5.delete(0, tk.END)
                self.entry_5.insert(0, result[1])
                self.entry_5.config(state="readonly")
            else:
                self.entry_4.config(state="normal")
                self.entry_4.delete(0, tk.END)
                self.entry_4.insert(0, result)
                self.entry_4.config(state="readonly")
                self.entry_5.config(state="normal")
                self.entry_5.delete(0, tk.END)
                self.entry_5.insert(0, result)
                self.entry_5.config(state="readonly")

        elif leaf == 9:
            entry3_value = self.entry_3.get()

            if not is_hex_string(entry2_value):
                result = "密钥格式不正确"
            elif not is_hex_string(entry3_value):
                result = "初始向量格式不正确"
            else:
                result = ""
                if len(entry1_value) % 4 == 0:
                    init_v = entry3_value
                    for i in range(0, len(entry1_value), 4):
                        m = entry1_value[i:i+4]
                        m = hex(int(m, 16) ^ int(init_v, 16))[2:]
                        m = (4 - len(m)) * "0" + m
                        c = self.s_aes.encrypt_b(m, entry2_value)
                        if not (c == "明文内容不正确" or c == "明文格式不正确"):
                            init_v = self.s_aes.list_to_string(c)
                            result += init_v
                        else:
                            break

            self.entry_5.config(state="normal")
            self.entry_5.delete(0, tk.END)
            self.entry_5.insert(0, result)
            self.entry_5.config(state="readonly")

        elif leaf == 10:
            entry3_value = self.entry_3.get()

            if not is_hex_string(entry2_value):
                result = "密钥格式不正确"
            elif not is_hex_string(entry3_value):
                result = "初始向量格式不正确"
            else:
                result = ""
                if len(entry1_value) % 4 == 0:
                    for i in range(len(entry1_value)-4, -1, -4):
                        c = entry1_value[i:i + 4]
                        if i > 3:
                            init_v = entry1_value[i - 4:i]
                        else:
                            init_v = entry3_value
                        m = self.s_aes.decrypt_b(c, entry2_value)
                        if not (m == "密文内容不正确" or m == "密文格式不正确"):
                            m = self.s_aes.list_to_string(m)
                            m = hex(int(m, 16) ^ int(init_v, 16))[2:]
                            m = (4 - len(m)) * "0" + m
                            result = m + result
                        else:
                            break

            self.entry_5.config(state="normal")
            self.entry_5.delete(0, tk.END)
            self.entry_5.insert(0, result)
            self.entry_5.config(state="readonly")

    def middle_attack(self):
        entry1_value = self.entry_1.get()
        entry2_value = self.entry_2.get()

        for i in range(self.key_1, 2 ** 16):
            for j in range(2 ** 16):
                if i == self.key_1 and j <= self.key_2:
                    continue
                
                key_1 = hex(i)[2:]
                key_1 = (4 - len(key_1)) * "0" + key_1
                key_2 = hex(j)[2:]
                key_2 = (4 - len(key_2)) * "0" + key_2

                result_1 = self.s_aes.encrypt_b(entry1_value, key_1)
                if not (result_1 == "明文内容不正确" or result_1 == "明文格式不正确"):
                    result_1 = self.s_aes.list_to_string(result_1)
                else:
                    return result_1

                result_2 = self.s_aes.decrypt_b(entry2_value, key_2)
                if not (result_2 == "密文内容不正确" or result_2 == "密文格式不正确"):
                    result_2 = self.s_aes.list_to_string(result_2)
                else:
                    return result_2

                if result_1 == result_2:
                    self.key_1 = i
                    self.key_2 = j
                    return key_1, key_2

        return "无后续密钥对"


class Window:
    @staticmethod
    def main():
        # 创建主窗口
        root = tk.Tk()
        root.title("ttk.Notebook 示例")
        root.geometry("500x400+510+230")

        # 创建分页标签控件
        notebook = ttk.Notebook(root)

        # 创建第一个选项卡
        tab_1 = ttk.Notebook(notebook)
        notebook.add(tab_1, text="加密")

        tab_1_1 = ttk.Frame(notebook)
        tab_1.add(tab_1_1, text="普通加密")
        tab_1_2 = ttk.Frame(notebook)
        tab_1.add(tab_1_2, text="双重加密")
        tab_1_3 = ttk.Frame(notebook)
        tab_1.add(tab_1_3, text="三重加密(32bits)")
        tab_1_4 = ttk.Frame(notebook)
        tab_1.add(tab_1_4, text="三重加密(48bits)")

        # 创建第二个选项卡
        tab_2 = ttk.Notebook(notebook)
        notebook.add(tab_2, text="解密")

        tab_2_1 = ttk.Frame(notebook)
        tab_2.add(tab_2_1, text="普通解密")
        tab_2_2 = ttk.Frame(notebook)
        tab_2.add(tab_2_2, text="双重解密")
        tab_2_3 = ttk.Frame(notebook)
        tab_2.add(tab_2_3, text="三重解密(32bits)")
        tab_2_4 = ttk.Frame(notebook)
        tab_2.add(tab_2_4, text="三重解密(48bits)")

        tab_3 = ttk.Frame(notebook)
        notebook.add(tab_3, text="中间相遇攻击")

        tab_4 = ttk.Notebook(notebook)
        notebook.add(tab_4, text="密码分组链(CBC)模式")
        tab_4_1 = ttk.Frame(notebook)
        tab_4.add(tab_4_1, text="加密")
        tab_4_2 = ttk.Frame(notebook)
        tab_4.add(tab_4_2, text="解密")

        # 将 ttk.Notebook 放置在主窗口中
        notebook.pack()

        Window.page(tab_1_1, 0)
        Window.page(tab_1_2, 1)
        Window.page(tab_1_3, 2)
        Window.page(tab_1_4, 3)
        Window.page(tab_2_1, 4)
        Window.page(tab_2_2, 5)
        Window.page(tab_2_3, 6)
        Window.page(tab_2_4, 7)
        Window.page(tab_3, 8)
        Window.page(tab_4_1, 9)
        Window.page(tab_4_2, 10)

        # 放大 ttk.Notebook 以适应窗口大小
        notebook.pack(fill=tk.BOTH, expand=True)

        # 启动主循环
        root.mainloop()

    @staticmethod
    def page(root, leaf):
        entry = Entry()

        # 设置行和列的权重
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

        # 创建 ttk.Frame 实例
        frame = ttk.Frame(root)
        frame.grid(row=0, column=0, padx=10, pady=10)

        # 创建输入框
        label_1 = tk.Label(frame)
        entry.entry_1 = ttk.Entry(frame)
        label_2 = tk.Label(frame)
        entry.entry_2 = ttk.Entry(frame)
        label_3 = tk.Label(frame)
        entry.entry_3 = ttk.Entry(frame)
        label_4 = tk.Label(frame)
        entry.entry_4 = ttk.Entry(frame)
        label_5 = tk.Label(frame)
        entry.entry_5 = ttk.Entry(frame, state="readonly")

        label_6 = tk.Label(frame, text="编码:")
        entry.combo = ttk.Combobox(frame)
        entry.combo.configure(width=10)
        entry.combo["value"] = ("binary", "ascii", "gbk", "gb2312", "gb18030")
        entry.combo.set("binary")
        entry.combo["state"] = "readonly"

        # 创建按钮
        button = ttk.Button(root)
        button.grid(row=1, column=0, padx=10, pady=10)
        button.config(command=lambda: entry.on_button_click(leaf))

        label_1.grid(row=0, column=0, padx=20, pady=10)
        entry.entry_1.grid(row=0, column=1, padx=20, pady=10)
        label_2.grid(row=1, column=0, padx=20, pady=10)
        entry.entry_2.grid(row=1, column=1, padx=20, pady=10)

        if leaf == 0 or leaf == 4:
            if leaf == 0:
                label_1.config(text="明文")
                label_5.config(text="密文")
                button.config(text="加密")
            elif leaf == 4:
                label_1.config(text="密文")
                label_5.config(text="明文")
                button.config(text="解密")

            label_2.config(text="密钥")
            label_5.grid(row=2, column=0, padx=20, pady=10)
            entry.entry_5.grid(row=2, column=1, padx=20, pady=10)
            label_6.grid(row=3, column=0, padx=20, pady=10)
            entry.combo.grid(row=3, column=1, padx=20, pady=10)
        elif leaf == 1 or leaf == 2 or leaf == 5 or leaf == 6:
            if leaf == 1 or leaf == 2:
                label_1.config(text="明文")
                label_5.config(text="密文")
                button.config(text="加密")
            elif leaf == 5 or leaf == 6:
                label_1.config(text="密文")
                label_5.config(text="明文")
                button.config(text="解密")

            label_2.config(text="密钥1")
            label_3.config(text="密钥2")
            label_3.grid(row=2, column=0, padx=20, pady=10)
            entry.entry_3.grid(row=2, column=1, padx=20, pady=10)
            label_5.grid(row=3, column=0, padx=20, pady=10)
            entry.entry_5.grid(row=3, column=1, padx=20, pady=10)
            label_6.grid(row=4, column=0, padx=20, pady=10)
            entry.combo.grid(row=4, column=1, padx=20, pady=10)
        elif leaf == 3 or leaf == 7:
            if leaf == 3:
                label_1.config(text="明文")
                label_5.config(text="密文")
                button.config(text="加密")
            elif leaf == 7:
                label_1.config(text="密文")
                label_5.config(text="明文")
                button.config(text="解密")

            label_2.config(text="密钥1")
            label_3.config(text="密钥2")
            label_3.grid(row=2, column=0, padx=20, pady=10)
            entry.entry_3.grid(row=2, column=1, padx=20, pady=10)
            label_4.config(text="密钥3")
            label_4.grid(row=3, column=0, padx=20, pady=10)
            entry.entry_4.grid(row=3, column=1, padx=20, pady=10)
            label_5.grid(row=4, column=0, padx=20, pady=10)
            entry.entry_5.grid(row=4, column=1, padx=20, pady=10)
            label_6.grid(row=5, column=0, padx=20, pady=10)
            entry.combo.grid(row=5, column=1, padx=20, pady=10)
        elif leaf == 8:
            label_1.config(text="明文")
            label_2.config(text="密文")
            label_4.config(text="密钥1")
            label_4.grid(row=2, column=0, padx=20, pady=10)
            entry.entry_4.config(state="readonly")
            entry.entry_4.grid(row=2, column=1, padx=20, pady=10)
            label_5.config(text="密钥2")
            label_5.grid(row=3, column=0, padx=20, pady=10)
            entry.entry_5.grid(row=3, column=1, padx=20, pady=10)
            button.config(text="破解")

            label_6.destroy()
            entry.combo.destroy()
        elif leaf == 9 or leaf == 10:
            if leaf == 9:
                label_1.config(text="明文")
                label_5.config(text="密文")
                button.config(text="加密")
            elif leaf == 10:
                label_1.config(text="密文")
                label_5.config(text="明文")
                button.config(text="解密")

            label_2.config(text="密钥")
            label_3.config(text="初始向量")
            label_3.grid(row=2, column=0, padx=20, pady=10)
            entry.entry_3.grid(row=2, column=1, padx=20, pady=10)
            label_5.grid(row=3, column=0, padx=20, pady=10)
            entry.entry_5.grid(row=3, column=1, padx=20, pady=10)

            label_6.destroy()
            entry.combo.destroy()
