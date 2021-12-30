# All_Auto

# All_Auto

##python+pytest-app自动化 介绍

{**重构app自动化进行了数据分离使用了pytest进行重组}

####软件架构说明
#####语言：python 3.6.0

####框架说明

    case = 存在case 的目录
    data = 测试数据存在目录，数据化使用
    driver = 创建多个设备，设备驱动初始化目录
    lib = 存在依赖文件底层库的目录
    logs = 日志存放目录
    page = 页面对象存放目录
    public = 存放各种方法的目录
    report = 存放报告目录
    resource = 资源包
    test_run = 运行测试用例目录，以后集成web+ios+H5做变量使用
    conftest.py = 封装了一个全局调用的方法配合case使用，每次case执行完成后返回首页，便于执行后面的用例
    main.py = 启动文件
    run.bat = shell 启动命令
    requirements.txt = 所需要应用的库


#### 安装教程

1.  pip install -r requirements.txt 安装需要的库
2.  配置python环境变量

#### 使用说明

    1、使用机型：虚拟机-网易mumu
    注：我的电脑有时候使用adb 链接虚拟机不成，使用adb kill-server && adb server && adb shell 后再运行adb device
    2、框架Python+uiautomator2+pytest
    3、环境准备 python3.6，预装的工具在resource文件下




#### 基本目录说明
### case
>存放case的目录
![case-test_smoke](image/case-test_smoke.jpg)
>
>>使用@pytest.mark.parametrize 装饰器+对应yml文件的参数，进行case的执行
>
>>例如test_a读取yml文件中的参数进行验证 assert判断是否存在

### data
>测试数据存放目录
>支持json、xml等

>case的对比及参数化数据，现在使用的是yml形式，形式如下：
![data-base_data](image/data-base_data.jpg)
>
>其他格式请自行百度
>
### Page
>本目录存放页面对象
>
>例如home类中，存放的都是首页的基本操作对象，对象中有不同操作的方法并与home类的调用，以此类推\
>>每次添加新的page类都要引用init中的方法\
![page-home](image/page-home.jpg)
>
### public
>公共方法
>包含系统方法、应用方法
>
>基本的操作方法，封装到Public下，方便后面调用
>例如：find_class、find_id登录定位方法
>
>init是定义读取的配置文件 
>BASE_CONF = get_data(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config.ini"))['App']
>
![public-App_page](image/public-App_page.jpg)