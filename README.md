# Telegram 媒体发送器

## 概述

这个 Python 脚本自动化了将指定文件夹中的媒体文件（照片、视频和文档）发送到 Telegram 频道的过程。它还在成功发送后删除文件，以防止重复。

## 主要特性

- 发送各种媒体类型：照片（.jpg、.jpeg、.png）、视频（.mp4）和文档（.gif、.webp）
- 连续监视文件夹以自动发送新文件
- 在成功发送后删除文件
- 按文件名字母顺序发送文件
- 在发送文件之间包含 10 秒延迟

## 安装和设置

1. **安装依赖项：**
   ```bash
   pip install -r requirements.txt

2. **创建 Telegram 机器人：**
   - 在 Telegram 上联系 BotFather 创建一个新的机器人并获取其 API 令牌。

3. **获取 channel ID:**
   - 打开要发送文件的 Telegram 频道并记录其 ID（在频道的 URL 中找到）。

4. **配置脚本:**
   - 在 telegram_media_sender.py 文件中编辑以下变量：
      - channel_id：替换为您的频道 ID。
      - folder_to_post：替换为包含您的媒体文件的文件夹路径。
      - bot_token：替换为您机器人的 API 令牌。

## 用法

1. 运行脚本：
   ```bash
   python telegram_media_sender.py

2. 脚本将开始监视指定的文件夹，并将任何新的媒体文件发送到 Telegram 频道。

## 附加说明

- **超时:**  脚本包含 1 小时的超时时间，以防止无限运行。如有需要，请在代码中调整此持续时间。
- **错误处理:** 脚本包含基本的错误处理，但请考虑针对特定情况加以增强
- **安全性:**  如果处理敏感信息，请确保采取适当的安全措施。


