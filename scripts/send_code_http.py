import requests

CODE = "xxxxxxxx"
URL = "http://52.233.88.199:80/xxxx/xxxx/xxx"

def post_form(url: str, code: str) -> requests.Response:
    return requests.post(url, data={"code": code, 
                                    "email": "federico1.santini@mail.polimi.it", 
                                    "person_code": "11059824", 
                                    "msg_code": "register", 
                                    "reset": "true"}, timeout=10)

def put_form(url: str, code: str) -> requests.Response:
    return requests.put(url, data={"msg_code": code,
                                   "email": "federico1.santini@mail.polimi.it", 
                                    "person_code": "11059824", })

def post_json(url: str, code: str) -> requests.Response:
    return requests.post(url, json={"code": code}, timeout=10)


def main() -> None:
    response = put_form(URL, CODE)
    print(f"Status: {response.status_code}")
    print(f"Body:   {response.text}")


if __name__ == "__main__":
    main()