#!/bin/bash

# 启动后端 FastAPI 服务
uvicorn app:app --host 0.0.0.0 --port 8000 &

# 启动前端静态文件服务（使用 Python 内置的 http.server）
cd /app/frontend/build
python3 -m http.server 3000 --bind 0.0.0.0 &

# 等待所有后台进程完成
wait
