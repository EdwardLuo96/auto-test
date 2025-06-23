# test_cases/test_auth.py
import os
import pytest
import requests
import allure
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()
BASE_URL = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com")


@pytest.fixture
def mock_auth_session():
    """模拟认证会话 - 用于测试演示"""
    with allure.step("创建模拟认证会话"):
        session = requests.Session()
        # 添加模拟认证头
        session.headers.update({
            "Authorization": "Bearer mock_token_for_testing",
            "Content-Type": "application/json"
        })
        allure.attach(
            str(session.headers),
            name="Session Headers",
            attachment_type=allure.attachment_type.TEXT
        )
        yield session
        session.close()


@allure.epic("API 测试")
@allure.feature("认证测试")
class TestAuthentication:
    @allure.story("模拟认证请求")
    @allure.title("测试带模拟认证的GET请求")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.tag("smoke", "authentication")
    @pytest.mark.api
    @pytest.mark.auth
    def test_mock_authenticated_request(self, mock_auth_session):
        """模拟带认证的请求测试"""
        with allure.step("发送GET请求"):
            response = mock_auth_session.get(f"{BASE_URL}/posts/1")

            # 添加响应内容到报告
            allure.attach(
                response.text,
                name="API Response",
                attachment_type=allure.attachment_type.JSON
            )

            # 添加curl命令到报告
            curl_command = f"curl -X GET {BASE_URL}/posts/1 -H 'Authorization: Bearer mock_token_for_testing'"
            allure.attach(
                curl_command,
                name="CURL Command",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("验证响应"):
            assert response.status_code == 200, "请求应成功"
            assert response.json()["id"] == 1, "应返回ID为1的post"







# # test_cases/test_auth.py
# import pytest
# import requests
# from test_login import BASE_URL
#
# @pytest.fixture
# def auth_session():
#     """创建带认证的会话"""
#     from requests import Session
#     session = Session()
#
#     # 先获取token（如果API有登录端点）
#     login_url = f"{BASE_URL}/login"
#     credentials = {
#         "username": "test_user",
#         "password": "test_pass"
#     }
#     auth_response = requests.post(login_url, json=credentials)
#     token = auth_response.json()["token"]
#
#     # 设置会话headers
#     session.headers.update({
#         "Authorization": f"Bearer {token}",
#         "Content-Type": "application/json"
#     })
#     yield session
#     session.close()
#
#
# @pytest.mark.api
# def test_session_based_auth(auth_session):
#     """使用会话保持认证状态的测试"""
#     response = auth_session.get(f"{BASE_URL}/protected/data")
#     assert response.status_code == 200