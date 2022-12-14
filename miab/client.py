from typing import Any, Optional
import base64 
import requests as r

class MailInABox:
    def __init__(self, host: str, email: str, password: str):
        self.host = host
        self.email = email
        self.access_token = base64.b64encode(bytes(f"{email}:{password}", "utf-8")).decode()
        self.base = f"https://{self.host}/admin"

    @staticmethod
    def add_params(kwargs: Any) -> str:
        if kwargs:
            return "?" + "&".join([f"{k}={v}" for k, v in kwargs.items()])
        else:
            return ""

    @staticmethod
    def error_handling(response: r.Response):
        if response.status_code != 200:
            raise ValueError(f"Non 200 response code: {response.content}")

    def get(self, endpoint: str, **kwargs) -> r.Response:
        url = f"{self.base}{endpoint}"
        headers = {"Authorization": f"Basic {self.access_token}"}
        url += self.add_params(kwargs)
        response = r.get(url=url, headers=headers)
        self.error_handling(response)
        return response

    def post(self, endpoint: str, **kwargs) -> r.Response:
        url = f"{self.base}{endpoint}"
        headers = {"Authorization": f"Basic {self.access_token}"}
        response = r.post(url=url, headers=headers, data=kwargs)
        self.error_handling(response)
        return response

    def mail_users(self, format: str):
        return self.get("/mail/users", format=format).json()

    def mail_aliases(self, format: str):
        return self.get("/mail/aliases", format=format).json()

    def mail_aliases_add(self, update_if_exists: int, address: str, forwards_to: str, permitted_senders: Optional[str]):
        return self.post(
            "/mail/aliases/add", 
            update_if_exists=update_if_exists,
            address=address, 
            forwards_to=forwards_to, 
            permitted_senders=permitted_senders
        ).content

    def mail_aliases_remove(self, address: str):
        return self.post("/mail/aliases/remove", address=address).content
