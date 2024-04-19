import os
import telebot
from time import sleep
from credencials import *


channel_id = media
folder_to_post = folder
bot = telebot.TeleBot(bot_api)

import os
from time import sleep

def send_media_files(folder_path, channel_id, bot):
    """
    遍历指定文件夹中的媒体文件，并按字母顺序发送到Telegram频道。
    """
    file_list = os.listdir(folder_path)
    file_list.sort()  # 对文件列表进行字母顺序排序

    file_count = 0  # 已发送文件计数
    for filename in file_list:
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):  # 检查是否为文件
            try:
                with open(file_path, 'rb') as f:
                    title = os.path.splitext(filename)[0]  # 获取文件名（不带扩展名）
                    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                        bot.send_photo(channel_id, f, caption=title)
                        print('sent')
                        sleep(1)  # 间隔1秒

                    elif filename.lower().endswith('.mp4'):
                        bot.send_video(channel_id, f, caption=title)
                        print('sent')
                        sleep(1)  # 间隔1秒

                    elif filename.lower().endswith(('.gif', '.webp')):
                        bot.send_document(channel_id, f, caption=title)
                        print('sent')
                        sleep(1)  # 间隔1秒

                    os.remove(file_path)  # 成功发送后删除文件
                    file_count += 1

                    # 发送10个文件后暂停1小时
                    if file_count % 10 == 0:
                        print("已发送10个文件。暂停1小时...")
                        sleep(3600)  # 暂停1小时（3600秒）

            except Exception as e:
                print(f"发送文件{filename}时出错：{str(e)}")

            #sleep(10)  # 发送间隔10秒

# 示例用法:
# folder_path = '/你的/文件夹/路径'
# channel_id = '你的频道ID'
# bot = 你的Telegram Bot对象
# send_media_files(folder_path, channel_id, bot)

# 主程序入口
if __name__ == "__main__":
    while True:
        # 列出指定文件夹中的文件列表
        file_list = os.listdir(folder_to_post)
        
        # 如果文件列表为空
        if not file_list:
            print("Diretório vazio. Aguardando 15 segundos antes de verificar novamente.")
            sleep(15)  # 暂停15秒后再次检查
        else:
            # 如果文件列表不为空，则调用send_media_files函数发送文件到指定的频道
            send_media_files(folder_to_post, channel_id, bot)
