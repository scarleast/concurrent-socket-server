使用环境：python2.7

结束程序：不能直接通过ctrl+c结束，需要另开一个终端，ps -ef |grep scar找到进程，kill杀死即可。

一点心得：
刚开始不太明白，为什么服务器一个端口，可以监听多个客户端。
其实，刚开始创建的sock仅仅用于监听，程序会在accept处阻塞，等待客户端接入。
每个客户端发出connect请求后，server会accept一个新的套接字，也就是clientfd。
由于clientfd接收数据recv也是阻塞的，为了实现同时多个客户端接入，就为每一个客户端数据接收处理开一个线程。
python通过treading模块创建一个线程，数据接收和处理函数为handle_client_request，作为参数，在创建线程时填入就行了。

