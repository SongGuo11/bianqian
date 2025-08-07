import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import json
import os

class StickyNotesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("便笺")
        self.root.geometry("300x300+100+100")
        self.root.attributes('-topmost', True)  # 设置窗口置顶
        
        # 创建菜单栏
        self.create_menu()
        
        # 创建文本区域
        self.create_text_area()
        
        # 加载保存的内容（如果存在）
        self.load_content()
        
        # 状态变量
        self.is_topmost = True
        self.file_path = None

    def create_menu(self):
        # 创建菜单栏
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # 文件菜单
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="文件", menu=file_menu)
        file_menu.add_command(label="新建", command=self.new_note)
        file_menu.add_command(label="打开", command=self.open_note)
        file_menu.add_command(label="保存", command=self.save_note)
        file_menu.add_command(label="另存为", command=self.save_as_note)
        file_menu.add_separator()
        file_menu.add_command(label="退出", command=self.exit_app)
        
        # 视图菜单
        view_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="视图", menu=view_menu)
        self.topmost_var = tk.BooleanVar()
        self.topmost_var.set(True)
        view_menu.add_checkbutton(label="窗口置顶", 
                                 variable=self.topmost_var,
                                 command=self.toggle_topmost)
        
        # 帮助菜单
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="帮助", menu=help_menu)
        help_menu.add_command(label="关于", command=self.show_about)

    def create_text_area(self):
        # 创建文本区域
        self.text_area = tk.Text(self.root, wrap=tk.WORD, undo=True)
        self.text_area.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # 创建滚动条
        scrollbar = tk.Scrollbar(self.text_area)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_area.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.text_area.yview)
        
        # 绑定事件
        self.text_area.bind('<Control-s>', lambda e: self.save_note())
        self.text_area.bind('<Control-o>', lambda e: self.open_note())
        self.text_area.bind('<Control-n>', lambda e: self.new_note())

    def toggle_topmost(self):
        # 切换窗口置顶状态
        self.is_topmost = self.topmost_var.get()
        self.root.attributes('-topmost', self.is_topmost)

    def new_note(self):
        # 新建便笺
        if self.text_area.get(1.0, tk.END).strip() and \
           messagebox.askyesno("确认", "是否保存当前内容？"):
            self.save_note()
        
        self.text_area.delete(1.0, tk.END)
        self.file_path = None
        self.root.title("便笺")

    def open_note(self):
        # 打开便笺
        file_path = filedialog.askopenfilename(
            title="打开便笺",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(1.0, content)
                    self.file_path = file_path
                    self.root.title(f"便笺 - {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("错误", f"无法打开文件：{str(e)}")

    def save_note(self):
        # 保存便笺
        if self.file_path:
            try:
                content = self.text_area.get(1.0, tk.END)
                with open(self.file_path, 'w', encoding='utf-8') as file:
                    file.write(content)
            except Exception as e:
                messagebox.showerror("错误", f"无法保存文件：{str(e)}")
        else:
            self.save_as_note()

    def save_as_note(self):
        # 另存为便笺
        file_path = filedialog.asksaveasfilename(
            title="保存便笺",
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        
        if file_path:
            try:
                content = self.text_area.get(1.0, tk.END)
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(content)
                self.file_path = file_path
                self.root.title(f"便笺 - {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("错误", f"无法保存文件：{str(e)}")

    def load_content(self):
        # 加载默认内容（如果存在）
        try:
            if os.path.exists("default_note.txt"):
                with open("default_note.txt", 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.text_area.insert(1.0, content)
        except Exception as e:
            pass  # 忽略加载错误

    def save_content(self):
        # 保存内容到默认文件
        try:
            content = self.text_area.get(1.0, tk.END)
            with open("default_note.txt", 'w', encoding='utf-8') as file:
                file.write(content)
        except Exception as e:
            pass  # 忽略保存错误

    def exit_app(self):
        # 退出应用
        self.save_content()
        self.root.destroy()

    def show_about(self):
        # 显示关于信息
        messagebox.showinfo("关于", "便笺工具 v1.0\n具有窗口置顶功能")

def main():
    root = tk.Tk()
    app = StickyNotesApp(root)
    root.protocol("WM_DELETE_WINDOW", app.exit_app)
    root.mainloop()

if __name__ == "__main__":
    main()