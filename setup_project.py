import os

# 定义项目结构
structure = {
    "api_test_project": {
        "test_cases": ["test_login.py", "test_orders.py"],
        "utils": ["api_client.py", "data_utils.py"],
        "reports": [],
        "conftest.py": None,
        "requirements.txt": None
    }
}

# 创建文件和目录
for root, contents in structure.items():
    os.makedirs(root, exist_ok=True)
    for dirname, files in contents.items():
        if isinstance(files, list):
            dirpath = os.path.join(root, dirname)
            os.makedirs(dirpath, exist_ok=True)
            for file in files:
                open(os.path.join(dirpath, file), 'a').close()
        else:
            open(os.path.join(root, dirname), 'a').close()

print("项目结构创建完成！")