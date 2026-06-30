# Project Learning Page Generator Skill

## 概述

本 Skill 定义了一套标准化流程，用于分析任意软件项目并生成一个交互式 HTML 学习页面。通过亮色主题、代码高亮、知识测验和响应式设计，帮助用户（或你自己）快速理解项目架构和核心机制。

---

## 使用场景

- 快速上手一个新的开源项目或内部仓库
- 为团队沉淀项目知识库
- 作为 Code Review 或技术分享的辅助材料
- 学习优秀项目的架构设计模式

---

## 执行流程

### Phase 1: 项目分析

1. **扫描项目结构**
   - 使用 `ls` / `find` 查看顶层目录和关键子目录
   - 识别项目类型（Python/Node/Go 等）和框架

2. **阅读核心文件**
   - 入口文件（`main.py`, `index.js`, `main.go` 等）
   - 配置文件（了解依赖和运行方式）
   - 核心模块（按职责分层阅读：编排层 → 业务层 → 工具层）
   - 提示词/模板文件（如果有 Agent 系统）

3. **提取关键概念**
   - 架构模式（ReAct, State Machine, DAG 等）
   - 核心数据结构
   - 关键算法或决策逻辑
   - 模块间的调用关系

### Phase 2: 内容设计

将分析结果组织为以下标准章节（根据项目类型灵活调整）：

| 章节 | 内容 | 可选交互 |
|------|------|----------|
| 项目概览 | 项目背景、设计目标、核心特性 | 特性卡片网格 |
| 项目结构 | 文件树 + 职责说明 | 可折叠目录 |
| 架构设计 | 分层架构图、数据流图 | 流程图/表格 |
| 核心模块 A | 关键代码 + 详细注释 | 代码高亮 |
| 核心模块 B | ... | ... |
| 状态/数据流 | 状态管理、数据传递 | 状态转换图 |
| 工具/基础设施 | 外部依赖、工具封装 | 工具卡片 |
| 知识测验 | 8-10 道选择题 | 点击交互 + 解析 |

### Phase 3: HTML 生成

#### 技术栈

- **单文件 HTML**：所有 CSS/JS 内联，无需构建工具
- **highlight.js**：代码语法高亮（GitHub 亮色主题）
- **纯 CSS 响应式**：Flexbox + Grid + Media Query
- **原生 JavaScript**：无框架依赖

#### 样式规范（亮色主题）

```css
:root {
    --bg-primary: #ffffff;
    --bg-secondary: #f6f8fa;
    --text-primary: #1f2328;
    --text-secondary: #656d76;
    --accent-blue: #0969da;
    --accent-green: #1a7f37;
    --accent-purple: #8250df;
    --accent-orange: #cf4b00;
    --accent-red: #cf222e;
    --border-color: #d0d7de;
}
```

#### 布局结构

```
┌─────────────────────────────────────┐
│  Navbar (fixed, 56px)               │
├──────────┬──────────────────────────┤
│          │                          │
│ Sidebar  │    Main Content          │
│ (260px)  │    (max-width: 900px)    │
│ fixed    │                          │
│          │                          │
└──────────┴──────────────────────────┘
```

#### 响应式断点

- **Desktop (>1024px)**: 完整侧边栏 + 顶部导航
- **Tablet (640-1024px)**: 侧边栏变抽屉（汉堡菜单触发）
- **Mobile (<640px)**: 单列布局，卡片全宽，字体缩小

#### 交互组件

1. **侧边栏导航**
   - 点击切换内容区块
   - 当前项高亮（蓝色左边框 + 背景色）
   - 移动端：汉堡按钮触发抽屉 + 遮罩层

2. **代码块**
   - `<pre><code class="language-python">`
   - highlight.js 自动高亮
   - 添加行内注释（HTML 实现）

3. **测验系统**
   - `data-answer` 标记正确答案
   - 点击后禁用选项，显示对错 + 解析
   - CSS 过渡动画

4. **流程图**
   - 纯 CSS 实现（flex 布局 + 箭头符号）
   - 不同节点类型不同颜色

### Phase 4: 部署与访问

```bash
# 使用 npx serve 启动静态服务器
npx serve -l tcp://0.0.0.0:8888 <html-directory>

# 获取访问链接
# 1. 获取本机 IP
curl -s http://169.254.169.254/latest/meta-data/local-ipv4  # 云服务器
curl -s ifconfig.me  # 公网 IP（如有）

# 2. 构造链接
# http://<ip>:8888/
```

---

## 代码模板

### 最小可复用 HTML 骨架

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{PROJECT_NAME} 学习指南</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
    <script>hljs.highlightAll();</script>
    <style>
        /* CSS Variables + Reset */
        :root { --bg-primary: #ffffff; --bg-secondary: #f6f8fa; ... }
        * { margin: 0; padding: 0; box-sizing: border-box; }

        /* Layout */
        .navbar { position: fixed; top: 0; left: 0; right: 0; height: 56px; ... }
        .layout { display: flex; margin-top: 56px; }
        .sidebar { width: 260px; position: fixed; ... }
        .main-content { margin-left: 260px; max-width: 900px; padding: 40px 48px; }

        /* Components */
        .content-section { display: none; }
        .content-section.active { display: block; }
        .card { border: 1px solid var(--border-color); border-radius: 12px; padding: 24px; }
        .quiz-option { ... }
        .quiz-option.correct { border-color: var(--accent-green); background: #dafbe1; }
        .quiz-option.wrong { border-color: var(--accent-red); background: #ffebe9; }

        /* Responsive */
        @media (max-width: 1024px) {
            .sidebar { transform: translateX(-100%); transition: transform 0.3s; }
            .sidebar.open { transform: translateX(0); }
            .main-content { margin-left: 0; }
        }
    </style>
</head>
<body>
    <nav class="navbar">...</nav>
    <div class="layout">
        <aside class="sidebar">...</aside>
        <main class="main-content">
            <section id="section1" class="content-section active">...</section>
            <section id="section2" class="content-section">...</section>
        </main>
    </div>
    <script>
        function showSection(id) {
            document.querySelectorAll('.content-section').forEach(s => s.classList.remove('active'));
            document.getElementById(id).classList.add('active');
        }
        // Quiz logic...
    </script>
</body>
</html>
```

---

## 批量输出策略

当 HTML 内容较多时，采用分块生成策略：

1. **先写骨架**：HTML 框架 + CSS + JS 交互逻辑
2. **分批填充内容**：
   - Batch 1: 概览 + 架构 + 项目结构
   - Batch 2: 核心模块代码分析
   - Batch 3: 状态/数据流 + 工具系统
   - Batch 4: 测验题目 + 最终检查
3. **每次追加**：使用 `cat >> file.html` 或编辑工具追加到 `</main>` 之前

---

## 质量检查清单

- [ ] 所有代码片段有语法高亮
- [ ] 关键代码有中文注释说明
- [ ] 测验题目覆盖核心概念
- [ ] 移动端侧边栏可正常展开/收起
- [ ] 内容区块切换流畅
- [ ] 无外部依赖（除 highlight.js CDN）
- [ ] 亮色主题，对比度足够

