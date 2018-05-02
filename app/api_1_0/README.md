# API返回的常见HTTP状态码
```textmate
HTTP状态码                    名称                    说明
200 OK                      （成功）                   请求成功完成
201 Created                 （已创建）                 请求成功完成并创建了一个新资源
400 Bad request             （坏请求）                 请求不可用或不一致
401 Unauthorized            （未授权）                 请求未包含认证信息
403 Forbidden               （禁止）                   请求中发送的认证密令无权访问目标
404 Notfound                （未找到）                 URL 对应的资源不存在
405 Method not allowed      （不允许使用的方法）        指定资源不支持请求使用的方法
500 Internal server error   （内部服务器错误）          处理请求的过程中发生意外错误
```
# Flasky API资源
```textmate
资源URL                               方法              说明
/users/<int:id>                     GET             一个用户
/users/<int:id>/posts/              GET             一个用户发布的博客文章
/users/<int:id>/timeline/           GET             一个用户所关注用户发布的文章
/posts/                             GET 、 POST      所有博客文章
/posts/<int:id>                     GET 、 PUT       一篇博客文章
/posts/<int:id/>comments/           GET 、 POST      一篇博客文章中的评论
/comments/                          GET             所有评论
/comments/<int:id>                  GET             一篇评论
``` 