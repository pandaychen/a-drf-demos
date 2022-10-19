# a-drf-demos
django restful framework demos all in one


-   `DjangoRestApi.swaggerEx`：基于`drf_yasg`展示API文档的测试项目




##	snippets app
```text
curl -X POST http://127.0.0.1:8000/api/v1/snippets/ --data '{"title":"test1","code":"c","language":"python"}'
{"id":1,"title":"test1","code":"c","linenos":false,"language":"python","style":"friendly"}
curl -X POST http://127.0.0.1:8000/api/v1/snippets/ --data '{"title":"test1","code":"c","language":"python"}'
{"id":1,"title":"test1","code":"c","linenos":false,"language":"python","style":"friendly"}
```

```
[root@VM_120_245_centos /data/python/a-drf-demos]# curl http://127.0.0.1:8000/api/v1/snippets/
[{"id":1,"title":"test1","code":"c","linenos":false,"language":"python","style":"friendly"},{"id":2,"title":"test1","code":"c","linenos":false,"language":"python","style":"friendly"}
```

```
[root@VM_120_245_centos /data/python/a-drf-demos]# curl http://127.0.0.1:8000/api/v1/snippets/1/
{"id":1,"title":"test1","code":"c","linenos":false,"language":"python","style":"friendly"}
```

##	参考
-	[Tutorial 1: 序列化](https://q1mi.github.io/Django-REST-framework-documentation/tutorial/1-serialization_zh/)
