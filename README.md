# 智能合同风险审计系统

基于 Next.js、Ollama 和 NSGA-III 构建的合同风控审计链路系统。

## 环境要求

为了稳定运行本系统，环境需要满足以下依赖要求：

### 1. Python 环境

- **版本**: Python 3.8 或更高版本 (建议 3.10+)
- 系统使用 Python 引擎执行 RAG 的本地语义检索计算和 NSGA-III 目标博弈算法

### 2. Node.js 环境

- **版本**: Node.js 18.x 或更高版本 (用于运行 Next.js 前端及服务端流式响应)

### 3. Ollama

请确保安装 Ollama 客户端并在本地服务 (默认端口 `127.0.0.1:11434`) 开启。运行系统前需要从 Ollama 预先 Pull 以下模型：

- **`deepseek-r1:8b`**: 用于大文件初探和合同核心要素的提纯拆解。
- **`qwen3.5:4b`**: 作为多领域专家矩阵 (法律、经济、管理) 并发执行审计与评分。
- **`qwen3-embedding:0.6b`**: 作为词境嵌入模型，用于将本地判例与法规转化为向量匹配 (目前备用)。

## 快速启动

1. 进入项目根目录并安装 NPM 依赖：

```bash
cd program
npm install
```

2. 启动 Next.js 开发服务：

```bash
npm run dev
```

3. 打开浏览器访问 [http://localhost:3000](http://localhost:3000)。
4. 如果 Ollama 引擎处于运行状态，首页左下角将显示 `ONLINE`。随后即可上传 PDF/DOCX 文件进行流式审计分析。
