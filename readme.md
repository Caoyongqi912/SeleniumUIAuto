# SeleniumUIAuto

使用Selenium + Allure + Pytest + Docker + Redis + Jenkins 做web UI自动化


### **pytest**

记录与分享一些pytest使用。便于在编写用例时的疑查补漏

---

#### 结构

- 模块级 
  - `setup_module`
  - `teardown_module`
  - 不在类中的函数有用
- 函数级 
  - `setup_function`
  - `teardown_function)`
  - 不在类中的函数有用
- 类级
  - `setup_class`
  - `teardown_class`
  - 只在类中前后运行一次。
- 方法级 
  - `setup_method`
  - `teardown_methond`
  - 运行在类中方法始末

---

#### 执行

此次试验了`pytest.main` 函数执行。传入`List args`

```python
args = ["-n 20", "-s", "-v", case_path, '--alluredir', xml_report_path]
```

- -n  指定运行进程数量
- -v  详细打印
- -case_path 测试地址 
- -s 关闭捕捉,输出打印信息 
- -q 减少测试的运行冗长
- -x 出现一条测试用例失败就退出测试。在调试阶段非常有用，当测试用例失败时，应该先调试通过，而不是继续执行测试用例。
- -k 指定匹配用例名称表达式
  - -k http  
- --reruns 3 失败后重新运行n次，
  - --reruns 3 --reruns-delay 延迟时间1s

#### Mark

##### mark (标记)

- 标记用例，运行时可选择是否执行

```python
@pytest.mark.runit
def test_01():
  pass

def test_02():
  pass
```

- 当运行时

  ```
  pytest.main(["-s","-m=runit"])
  ```

  此时只会执行`test_01` 反之 `-m not runit`

##### mark.skip（跳过）

- 场景
  - 调试时不想执行该用例
  - 标记某个平台无法运行的用例
- 增加条件`skipif` 在某种条件下 通过，否则跳过该用例

##### mark.xfail（失败）

- 场景

  - 功能尚未实现或未修复的错误。测试用果实尽管会失败。标记为`xpass`

  ```python
   @pytest.xfail(reason='该功能尚未完成')
    def test_one(self,):
      print("test_one方法执行" )
      assert 1==1
  ```



---

##### 运行指定用例

- 只执行一部分用例，通过类名与方法命名实现 

- 如运行某个类中的方法函数

  - ```
    pytest -v test_demo.py::TestDemo::test_demo_01
    ```

- 运行整个类

  - ```
    pytest -v test_demo.py::TestDemo	
    ```

- 选择多个节点

  - ```shell
    pytest -v test_demo.py::TestDemo test_server.py::TestServer::test_server_01
    ```



---

#### FIXTURE

> 可以更加灵活的命名实现类似`setup` `teardown` 方法
>
> Fixture  = setup+teardown

```python
def myfixtrue():
  self.get(url)
  yield self.driver
  self.quit()
```

 `yield` 之前的代码是前置，后边的是后置

```python
@pytest.mark.usefixtrue("myfixtrue")
def test_demo():
	assert 1 = 2
  
@pytest.mark.usefixtrue("myfixtrue")
class TestDemo:
	pass

```

- 参数化

在fixtrue 中增加`@pytest.fixtrue(params=[1,2,3])`

```python
test_user_data1=[{'user':'linda','password':'888888'},
                 {'user':'servenruby','password':'123456'},
                 {'user':'test01','password':''}]
test_user_data2=[{'q':'中国平安','count':3,'page':1},
                 {'q':'阿里巴巴','count':2,'page':2},
                 {'q':'pdd','count':3,'page':1}]

@pytest.fixture(scope='module')
def login_r(request):
    #这是接受不了输入的参数，接收一个参数
    user=request.param['user']
    pwd=request.param['password']
    print('\n用户名:%s,密码:%s'%(user,pwd))

@pytest.fixture(scope='module')
def query_param(request):
    q=request.param['q']
    count=request.param['count']
    page=request.param['page']
    print('查询的搜索词%s'%q)
    return request.param
  
  
#这是pytest的数据驱动,indeirect=True是把login_r当作函数去执行
#从下往上执行
#两个数据进行组合测试，有3*3个测试用例执行(test_user_data1的个数*test_user_data2的个数
@pytest.mark.parametrize('query_param',test_user_data2,indirect=True)
@pytest.mark.parametrize('login_r',test_user_data1,indirect=True)
def test_login(login_r,query_param):
    #登陆用例
    print(login_r)
    print(query_param)

```

---



#### 执行顺序

> 想要考虑用例的执行顺序，如增加的数据先执行，删除的用例后执行
>

`pytest-ordering`

在测试方法上增加装饰器

- `pytest.mark.last`
- `pytest.mark.run(order=1)`

---
### **Allure**	

- 功能
  - `allure.feature("name")`
- 子功能
  - `allure.story("name")`

- 步骤

  - `allure.step("name")`

- 描述

  ```
  def testcase():
  	"""
  	这是描述
  	"""
  	assert 
  ```

- 等级`allure.severity("blocker")`

  1、 Blocker级别：中断缺陷（客户端程序无响应，无法执行下一步操作）
  2、 Critical级别：临界缺陷（ 功能点缺失）
  3、 Normal级别：普通缺陷（数值计算错误）
  4、 Minor级别：次要缺陷（界面错误与UI需求不符）
  5、 Trivial级别：轻微缺陷（必输项无提示，或者提示不规范）

- `Issue和testcase`

  ```
  @allure.issue("http://www.baidu.com")
      @allure.testcase('http://bug.com/user-login-Lw==.html', name='点击我跳转禅道')
  ```

- 标题与说明

  ```
  @allure.title("用例标题")
  @allure.description("这里是对test_0用例的一些详细说明")
  ```

  

---

### **docker**

- 拉取镜像

```shell
docker pull selenium/hub
docker pull selenium/node-chrome
docker pull redis:lastest
```

- 生成

```shell
docker run -p 4444:4444 -d --name seleniumHub selenium/hub
docker run -P -d --link seleniumHub:hub --name seleniumChrome --shm-size=512m selenium/node-chrome
docker run -d -p 5900:5900 --link seleniumHub:hub selenium/node-chrome-debug
```
```shell
docker run --name=hub -p 4444:4444 -e GRID_TIMEOUT=30000 -e GRID_THROW_ON_CAPABILITY_NOT_PRESENT=true -e GRID_NEW_SESSION_WAIT_TIMEOUT=5000 -e GRID_BROWSER_TIMEOUT=15000 -e GRID_CLEAN_UP_CYCLE=30000 -d selenium/hub
docker run --name=chrome -p 5900:5900 -e NODE_MAX_INSTANCES=5 -e NODE_MAX_SESSION=5 -e NODE_REGISTER_CYCLE=5000 --link seleniumHub -d selenium/node-chrome-debug
docker run --name redis -p 6379:6379 -d redis --requirepass "123456"
```


- `SeleniumBaseConfig.py` 配置

```python
 driver = webdriver.Remote("http://localhost:4444/wd/hub", desired_capabilities=chrome_capabilities,
                                      options=options())
```

- debug 
  - 使用vnc
  - 访问`localhost:5900`

