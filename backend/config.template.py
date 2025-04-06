# AI Service Configuration
# 通过配置文件来自定义 OpenAI (或支持OpenAI接口规范的)的模型。
AI_CONFIG = {
    "base_url": "https://open.bigmodel.cn/api/paas/v4/",
    "api_key": "your_api_key_here",  # 替换为你的 API 密钥
    "model": "glm-4-flash",
}

# STT Service Configuration
# 通过配置文件来自定义 Whisper 模型的大小。模型大小会影响转录的准确度和速度：
# tiny: 最快但准确度最低
# base: 平衡速度和准确度
# small/medium: 更高的准确度，但需要更多资源
# large: 最高准确度，但需要最多资源
STT_CONFIG = {
    "whisper_model": "tiny",  # 可选值: tiny, base, small, medium, large
    "beam_size": 5,  # 集束搜索的大小，越大准确率越高，但速度越慢
    "language": "zh",  # 用来选择视频转文字的语言
    "vad_filter": True,  # 是否开启VAD过滤，开启后会过滤掉语音中的静音部分，提高转文字的准确率
}
