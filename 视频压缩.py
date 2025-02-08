import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip

def compress_video(input_file, output_file, bitrate='500k'):
    try:
        video = VideoFileClip(input_file)
        video.write_videofile(output_file, bitrate=bitrate)
        print(f"视频压缩成功，输出文件: {output_file}")
    except Exception as e:
        print(f"视频压缩失败: {e}")

def select_input_file():
    file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi;*.mov")])
    input_file_entry.delete(0, tk.END)
    input_file_entry.insert(0, file_path)

def select_output_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("Video Files", "*.mp4")])
    output_file_entry.delete(0, tk.END)
    output_file_entry.insert(0, file_path)

def start_compression():
    input_file = input_file_entry.get()
    output_file = output_file_entry.get()
    bitrate = bitrate_entry.get()
    compress_video(input_file, output_file, bitrate)

# 创建主窗口
root = tk.Tk()
root.title("视频压缩客户端")

# 创建输入文件选择框
input_file_label = tk.Label(root, text="输入文件:")
input_file_label.grid(row=0, column=0, padx=10, pady=10)
input_file_entry = tk.Entry(root, width=50)
input_file_entry.grid(row=0, column=1, padx=10, pady=10)
input_file_button = tk.Button(root, text="选择文件", command=select_input_file)
input_file_button.grid(row=0, column=2, padx=10, pady=10)

# 创建输出文件选择框
output_file_label = tk.Label(root, text="输出文件:")
output_file_label.grid(row=1, column=0, padx=10, pady=10)
output_file_entry = tk.Entry(root, width=50)
output_file_entry.grid(row=1, column=1, padx=10, pady=10)
output_file_button = tk.Button(root, text="选择文件", command=select_output_file)
output_file_button.grid(row=1, column=2, padx=10, pady=10)

# 创建比特率输入框
bitrate_label = tk.Label(root, text="比特率:")
bitrate_label.grid(row=2, column=0, padx=10, pady=10)
bitrate_entry = tk.Entry(root, width=20)
bitrate_entry.grid(row=2, column=1, padx=10, pady=10)
bitrate_entry.insert(0, '500k')

# 创建压缩按钮
compress_button = tk.Button(root, text="开始压缩", command=start_compression)
compress_button.grid(row=3, column=1, padx=10, pady=10)

# 运行主循环
root.mainloop()
