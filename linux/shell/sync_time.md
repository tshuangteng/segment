## Linux同步Windows时间解决方案


### 启动Windows系统的NTP服务

1.修改注册表
使用win + R 组合键在运行窗口中输入regedit，打开注册表编辑器。

![image](https://user-images.githubusercontent.com/62510752/200186004-5c2e52e6-3219-4a25-b5c6-dd9fa57f253a.png)

依次展开数据项目，计算机\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\W32Time\TimeProviders\NtpServer，把Enabled设置为1，为打开NTP服务，操作如下图所示。

![image](https://user-images.githubusercontent.com/62510752/200186045-6208946a-0bbd-4370-933b-7d1d4de36b4d.png)

依次打开，计算机\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\W32Time\Config，并把AnnounceFlags的值设置为5（系统默认为a），操作如下图所示。

![image](https://user-images.githubusercontent.com/62510752/200186076-adac2062-1c1d-4540-8460-2bc543fb8d52.png)

2.启动NTP服务
使用win + R 组合键在运行窗口中输入services.msc，打开服务。

![image](https://user-images.githubusercontent.com/62510752/200186142-df47cc32-0185-43c4-8e84-950ae38436a6.png)

在服务项中找到Windows Time

![image](https://user-images.githubusercontent.com/62510752/200186151-ad56c0e4-982a-47da-b96b-4e44db9e8eef.png)

设置为自动后确定，点击右键重新启动此服务，至此服务启动成功。

![image](https://user-images.githubusercontent.com/62510752/200186162-b3f5e0c7-b1b6-4ea2-9de4-d22f5691b5f1.png)

注：启动和关闭windows NTP的方式，还可以使用命令行来管理

启动：net start w32time
停止：net stop w32time

3.本机测试
在cmd窗口中输入w32tm /stripchart /computer:127.0.0.1 ，如果有回显则服务正常。
![image](https://user-images.githubusercontent.com/62510752/200186249-d009e7eb-ed30-4eee-9b10-be3997121aea.png)

4.说明

服务端部署成功后，如果要为客户端提供服务的话需要开放udp协议中的123端口，或者根据自身安全情况关闭防火墙。客户端下可以使用ntpdate命令来同步服务器时间，也可以使用chrony服务。
该ntp服务的IP就是该机器的IP地址，先假定是172.16.30.23


### Linux客户端同步NTP的时间

1.安装ntpdate服务

```shell
sudo apt-get install ntpdate
```

2.Linux宿主机使用sudo权限下的crontab定时同步时间

```
sudo crontab -e
```

编辑添加如下，定时任务
```
* * * * * sleep 15; ntpdate 172.16.30.23
```

### 容器使用

启动容器时挂载时间文件/etc/localtime，命令如下

```
sudo nvidia-docker run -itd --net=host --device /dev/universalEthernet:/dev/universalEthernet -e NVIDIA_VISIBLE_DEVICES=0 -v /etc/localtime:/etc/localtime --name sdm sdm:v20221101 /bin/bash
```



参考：https://baijiahao.baidu.com/s?id=1721039734284430556&wfr=spider&for=pc
