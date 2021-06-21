# dishrank

### project structure

![img](/img/src.svg)

### testcase

```
>>> pytest

rootdir: ~/projects/dishrank, configfile: pytest.ini
plugins: env-0.6.2
collected 2 items

tests/test_routers.py::test_success_signin PASSED
tests/test_routers.py::test_fail_signin PASSED
```

### docker-compose

```
docker-compose -f ./docker-compose.yml up --build
```

### [docs](http://127.0.0.1:8000/docs)

![img](/img/doc.png)

### remarks

1. password 配合測驗採用明碼儲存及驗證。
2. 未設計 create/update/delete user api。
3. db 僅做初始化動作，未使用 migrate 機制。
4. testcase 僅寫 external 層的測試案例



