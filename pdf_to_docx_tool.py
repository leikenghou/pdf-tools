from pdf2docx import Converter
import os

def pdf_to_docx(pdf_path, docx_path):
    try:
        cv = Converter(pdf_path)
        cv.convert(docx_path, start=0, end=None)
        cv.close()
    except Exception as e:
        print(f'转换出错: {e}')
        raise  # 将异常重新抛出，以便在调用方捕获

def batch_pdf_to_docx(input_folder, output_folder):
    # 获取输入文件夹中的所有 PDF 文件
    pdf_files = [f for f in os.listdir(input_folder) if f.endswith('.pdf')]

    # 批量处理每个 PDF 文件
    for pdf_file in pdf_files:
        pdf_path = os.path.join(input_folder, pdf_file)
        docx_file = os.path.splitext(pdf_file)[0] + '.docx'
        docx_path = os.path.join(output_folder, docx_file)

        try:
            pdf_to_docx(pdf_path, docx_path)
            print(f'转换完成: {pdf_file}')
        except Exception as e:
            print(f'转换出错: {e}')



