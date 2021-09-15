# hsk-ddns-client
花生壳动态域名服务（DDNS）的docker客户端，启动后，会自动检测网络的公网ip，并完成DDNS解析，默认5分钟更新一次记录

使用方式：
```
docker run -d --restart=unless-stopped --name=hsk-ddns-client -e TZ=Asia/Shanghai -e hostname=<YOUR HOSTNAME> -e username=<YOUR USERNAME> -e password=<YOUR PASSWORD> raydoom/hsk-ddns-client
```
