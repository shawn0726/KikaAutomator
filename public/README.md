# All_Auto
## public
####公共方法
>包含系统方法、应用方法
>
>基本的操作方法，封装到Public下，方便后面调用
>例如：find_class、find_id登录定位方法
>
>init是定义读取的配置文件 
>BASE_CONF = get_data(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config.ini"))['App']
