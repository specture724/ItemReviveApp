import tkinter as tk
from tkinter import messagebox, simpledialog
import json

class ItemReviveApp:
    def __init__(self, root, filename="items.json"):
        self.root = root
        self.root.title("物品复活程序")
        self.filename = filename
        self.load_items()

        # 设置每个字段的最大显示长度
        self.name_length = 15
        self.contact_length = 20

        # 初始化过滤结果列表
        self.filtered_items = []

        # 设置窗口布局
        self.create_widgets()

    def load_items(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                self.items = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.items = []

    def save_items(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.items, file, indent=4)

    def create_widgets(self):
        # 显示物品列表
        self.item_list = tk.Listbox(self.root, width=60, height=15, font=("Courier New", 10))
        self.item_list.pack(pady=10)
        
        # 绑定双击事件到列表项
        self.item_list.bind("<Double-1>", self.show_description)

        # 添加操作按钮
        self.btn_add = tk.Button(self.root, text="添加物品", command=self.add_item)
        self.btn_add.pack(side=tk.LEFT, padx=5, pady=5)

        self.btn_delete = tk.Button(self.root, text="删除物品", command=self.delete_item)
        self.btn_delete.pack(side=tk.LEFT, padx=5, pady=5)

        self.btn_search = tk.Button(self.root, text="查找物品", command=self.search_item)
        self.btn_search.pack(side=tk.LEFT, padx=5, pady=5)

        self.btn_show = tk.Button(self.root, text="显示所有物品", command=self.display_items)
        self.btn_show.pack(side=tk.LEFT, padx=5, pady=5)

        self.display_items()  # 初始显示所有物品

    def add_item(self):
        name = simpledialog.askstring("添加物品", "输入物品名称:")
        if name:
            description = simpledialog.askstring("添加物品", "输入物品描述:")
            contact = simpledialog.askstring("添加物品", "输入联系人信息:")

            # 检查重复项
            for item in self.items:
                if item["name"] == name and item["description"] == description and item["contact"] == contact:
                    messagebox.showwarning("警告", f"物品 '{name}' 已存在，无法重复添加。")
                    return

            # 如果没有重复，则添加物品
            item = {"name": name, "description": description, "contact": contact}
            self.items.append(item)
            self.save_items()
            self.display_items()
            messagebox.showinfo("提示", f"物品 '{name}' 已成功添加！")

    def delete_item(self):
        selected = self.item_list.curselection()
        if selected:
            index = selected[0]
            # 从已过滤的列表中删除或从总列表中删除
            if self.filtered_items:
                item = self.filtered_items.pop(index)
                self.items.remove(item)  # 从总列表中删除
            else:
                item = self.items.pop(index)
            self.save_items()
            self.display_items()
            messagebox.showinfo("提示", f"物品 '{item['name']}' 已成功删除！")
        else:
            messagebox.showwarning("警告", "请选择要删除的物品。")

    def search_item(self):
        search_name = simpledialog.askstring("查找物品", "输入要查找的物品名称:")
        if search_name:
            # 创建过滤列表并保存到 self.filtered_items
            self.filtered_items = [item for item in self.items if search_name.lower() in item["name"].lower()]
            self.item_list.delete(0, tk.END)
            if self.filtered_items:
                for item in self.filtered_items:
                    formatted_name = self.format_text(item['name'], self.name_length)
                    formatted_contact = self.format_text(item['contact'], self.contact_length)
                    self.item_list.insert(tk.END, f"{formatted_name:<{self.name_length}} | {formatted_contact}")
            else:
                messagebox.showinfo("提示", f"未找到名称包含 '{search_name}' 的物品。")

    def display_items(self):
        # 清空过滤结果并显示所有物品
        self.filtered_items = []
        self.item_list.delete(0, tk.END)
        if not self.items:
            self.item_list.insert(tk.END, "暂无物品信息。")
        else:
            for item in self.items:
                # 使用格式化文本显示名称和联系人
                formatted_name = self.format_text(item['name'], self.name_length)
                formatted_contact = self.format_text(item['contact'], self.contact_length)
                self.item_list.insert(tk.END, f"{formatted_name:<{self.name_length}} | {formatted_contact}")

    def show_description(self, event):
        # 获取双击的项的索引
        selected = self.item_list.curselection()
        if selected:
            index = selected[0]
            # 使用过滤后的列表显示详细信息
            item = self.filtered_items[index] if self.filtered_items else self.items[index]
            # 弹出一个新窗口显示物品的详细信息
            detail_window = tk.Toplevel(self.root)
            detail_window.title(f"{item['name']} - 详细信息")

            # 名称标签
            tk.Label(detail_window, text="名称:", font=("Arial", 12, "bold")).grid(row=0, column=0, sticky="w", padx=10, pady=5)
            tk.Label(detail_window, text=item["name"], font=("Arial", 12)).grid(row=0, column=1, sticky="w", padx=10, pady=5)

            # 描述标签
            tk.Label(detail_window, text="描述:", font=("Arial", 12, "bold")).grid(row=1, column=0, sticky="w", padx=10, pady=5)
            tk.Label(detail_window, text=item["description"], font=("Arial", 12), wraplength=300, justify="left").grid(row=1, column=1, sticky="w", padx=10, pady=5)

            # 联系人标签
            tk.Label(detail_window, text="联系人:", font=("Arial", 12, "bold")).grid(row=2, column=0, sticky="w", padx=10, pady=5)
            tk.Label(detail_window, text=item["contact"], font=("Arial", 12)).grid(row=2, column=1, sticky="w", padx=10, pady=5)

            # 窗口关闭按钮
            tk.Button(detail_window, text="关闭", command=detail_window.destroy).grid(row=3, column=0, columnspan=2, pady=10)

    def format_text(self, text, length):
        """格式化文本，如果超过指定长度则截断并加上省略号"""
        return text if len(text) <= length else text[:length - 3] + "..."

if __name__ == "__main__":
    root = tk.Tk()
    app = ItemReviveApp(root)
    root.mainloop()