
from tkinter import Tk, filedialog, Label, Button, messagebox
from pdf_to_docx_tool import batch_pdf_to_docx

def select_input_folder():
    input_folder = filedialog.askdirectory()
    input_folder_label.config(text=f'输入文件夹: {input_folder}')

def select_output_folder():
    output_folder = filedialog.askdirectory()
    output_folder_label.config(text=f'输出文件夹: {output_folder}')

def convert_pdfs():
    input_folder = input_folder_label.cget("text").split(": ")[1]
    output_folder = output_folder_label.cget("text").split(": ")[1]

    try:
        batch_pdf_to_docx(input_folder, output_folder)
        status_label.config(text='转换完成')
    except Exception as e:
        status_label.config(text=f'出错: {e}')
        messagebox.showerror("错误", f"转换出错: {e}")

# 创建主窗口
root = Tk()
root.title("PDF to Word Converter")

# 设置窗口大小 400 * 200
root.geometry("400x200")  


# 选择输入文件夹按钮
select_input_button = Button(root, text="选择输入文件夹", command=select_input_folder)
select_input_button.pack()

# 选择输出文件夹按钮
select_output_button = Button(root, text="选择输出文件夹", command=select_output_folder)
select_output_button.pack()

# 标签显示选择的文件夹路径
input_folder_label = Label(root, text="输入文件夹: ")
input_folder_label.pack()

output_folder_label = Label(root, text="输出文件夹: ")
output_folder_label.pack()

# 转换按钮
convert_button = Button(root, text="开始转换", command=convert_pdfs)
convert_button.pack()

# 显示转换状态的标签
status_label = Label(root, text="")
status_label.pack()


