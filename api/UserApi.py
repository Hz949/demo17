"""
封装登录请求

"""
import app


class UserLogin:
    # 登录请求
    def login(self, session, mobile, password):
        return session.post(app.BASE_PATH + "login",
                            json={"mobile": mobile, "password": password})
