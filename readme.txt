python项目开发标准
1. 项目结构
    my_project/
    │
    ├── README.md                # 项目描述和使用说明
    ├── LICENSE                   # 开源许可证
    ├── setup.py                  # 包安装脚本
    ├── requirements.txt          # 项目依赖包列表
    ├── .gitignore                # Git忽略文件列表
    ├── docs/                     # 文档目录
    │   └── ...
    ├── my_project/               # 主代码目录，与项目同名
    │   ├── __init__.py           # 初始化文件，使目录成为包
    │   ├── module1.py            # 模块文件
    │   ├── module2.py            # 模块文件
    │   └── ...                   # 更多模块或子包
    ├── tests/                    # 测试目录
    │   ├── __init__.py           # 初始化测试包
    │   ├── test_module1.py       # 测试模块文件
    │   └── test_module2.py       # 测试模块文件
    └── scripts/                  # 脚本目录（如果有的话）
        └── script1.py            # 示例脚本

2. 代码风格
    PEP 8：遵循 PEP 8 规范，这是Python的官方编码风格指南。
    命名约定：
        变量和函数名使用小写加下划线（如 my_variable）
        类名使用首字母大写的单词（如 MyClass）
        常量名全部大写加下划线（如 MY_CONSTANT）
3. 创建虚虚环境
    python -m venv myenv
    source myenv/bin/activate  # macOS/Linux
    # .\myenv\Scripts\activate  # Windows
4. 依赖管理
    1. 在 requirements.txt 文件中列出项目的所有依赖项，并使用 pip freeze > requirements.txt 来生成该文件。也可以使用 setup.py 来定义包的元数据和依赖项
    2. 使用pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/安装所有依赖包
5. 单元测试
    编写单元测试以确保代码的正确性。可以使用 unittest 或 pytest 等测试框架。通常将测试文件放在 tests/ 目录下，并命名为 test_*.py
6. 版本控制
    使用 Git 进行版本控制，并遵循标准的 Git 工作流程：
        创建 .gitignore 文件以排除不需要跟踪的文件和目录。
        使用有意义的提交信息。
        定期推送代码到远程仓库