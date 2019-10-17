"""
封装员工的增删改查请求实现
"""

import app


class EmpCRUD:
    # 函数1:增
    def add(self, session, usernmae, mobile, workNumuber):
        myaddEmp = {
            "username": usernmae,
            "mobile": mobile,
            "workNumuber": workNumuber
        }
        return session.post(app.BASE_PATH + "user", json=myaddEmp,
                            headers={"Authorization": "Bearer " + app.TOKEN})

    # 函数2:查
    def get(self, session, userID):
        return session.get(app.BASE_PATH + "user/" + userID,
                           headers={"Authorization": "Bearer " + app.TOKEN})

    # 函数3:改
    def update(self, session, userID, username):
        # session.put("修改后的url, 后缀id", )
        return session.put(app.BASE_PATH + "user/" + userID,
                           json=username,
                           headers={"Authorization": "Bearer " + app.TOKEN}
                           )

    # 函数4:删
    def delete(self, session, userID):
        return session.delete(app.BASE_PATH + "user/" + userID,
                              headers={"Authorization": "Bearer " + app.TOKEN} )
