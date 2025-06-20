# 🚀 自动化测试框架（Selenium + Pytest + Allure）

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.8+-green)](https://selenium.dev/)
[![Pytest](https://img.shields.io/badge/Pytest-8.4+-yellow)](https://docs.pytest.org/)
[![Allure](https://img.shields.io/badge/Allure%20Report-2.24+-orange)](https://docs.qameta.io/allure/)

电商平台全流程自动化测试框架，覆盖 Web UI 和 API 测试，集成可视化测试报告与 CI/CD 支持。

## 🌟 核心功能

- ✅ **Web 自动化测试**：基于 Selenium 实现登录→选品→结算全流程
- ✅ **REST API 测试**：使用 Requests 测试认证/商品/订单接口
- ✅ **Page Object 模式**：高可维护性代码结构
- ✅ **Allure 报告**：包含截图、请求日志和性能趋势
- ✅ **CI/CD 就绪**：GitHub Actions 集成示例

## 🛠 技术栈

| 技术                | 用途                          |
|---------------------|-------------------------------|
| Selenium WebDriver  | Web 页面自动化交互            |
| Pytest              | 测试框架与用例管理            |
| Requests            | HTTP API 测试                 |
| Allure              | 生成可视化测试报告            |
| Page Object         | 页面元素与业务逻辑解耦        |

## 🚦 快速开始

### 前置要求
- Python 3.10+
- Chrome 浏览器
- [ChromeDriver](https://chromedriver.chromium.org/)

### 安装步骤
# 克隆仓库
git clone https://github.com/yourusername/auto-test-framework.git
cd auto-test-framework

# 创建虚拟环境（可选）
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows

# 安装依赖
pip install -r requirements.txt

运行测试
# 运行 Web 测试（Selenium）
pytest test_cases/web_test --alluredir=./allure-results

# 运行 API 测试
pytest test_cases/api_test --alluredir=./allure-results

# 生成报告
allure serve ./allure-results
📊 报告示例
https://docs/allure-demo.png
(截图路径：docs/allure-demo.png)

🧩 项目结构
text
├── test_cases/
│   ├── web_test/          # Web 自动化测试
│   │   ├── test_login.py
│   │   └── test_checkout.py
│   └── api_test/          # API 测试
│       ├── test_auth.py
│       └── test_products.py
├── pages/                 # Page Object 类
│   ├── login_page.py
│   └── cart_page.py
├── utils/                 # 工具类
│   ├── config_loader.py
│   └── screenshot.py
├── requirements.txt       # 依赖清单
└── pytest.ini            # Pytest 配置
🌐 CI/CD 集成
GitHub Actions 配置示例：

yaml
name: Test Suite
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
      - name: Run Tests
        run: |
          pip install -r requirements.txt
          pytest --alluredir=./allure-results
      - name: Upload Report
        uses: actions/upload-artifact@v2
        with:
          name: allure-report
          path: ./allure-results
📚 学习资源
Selenium 官方文档

Pytest 最佳实践

Allure 报告定制

🤝 贡献指南
欢迎提交 Issue 或 PR！请确保：

遵循现有代码风格

添加对应的测试用例

更新相关文档

项目持续维护中 - 更多企业级功能正在开发

text

---

### 🎯 使用建议：
1. **替换占位信息**：
   - 将 `yourusername` 改为您的 GitHub 用户名
   - 添加真实的 Allure 报告截图（保存为 `docs/allure-demo.png`）

2. **扩展内容**：
   - 在 `## 🌟 核心功能` 部分添加您的特色实现
   - 如果是企业项目，可添加 **测试覆盖率徽章**

3. **个性化**：
   ```markdown
   ## 🏆 项目亮点
   - 实现华为云 API 测试规范对接
   - 支持多环境配置（dev/staging/prod）
   - 集成企业微信通知功能
