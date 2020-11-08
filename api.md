# 接口文档

## 登录

```js
// 登录方法
// t是 __hb__token
 r.a.login(this.customerNum, this.dealPwd, this.appId, this.deviceUUID, this.imgCode, t, function (t, i) {
    //
    })



 function (e, t, o) {
        "use strict";
        var i = o(4),
            s = o.n(i),
            n = o(9),
            a = o(0);
        o(3);
        t.a = {
            login: function (e, t, o, i, r, c, d) {
                var h = {
                    md5: hex_md5(c),
                    loginId: e,
                    password: t
                };
                h = s()(h), console.log("before cust login log:" + h), h = encodeURIComponent(encryptor.encrypt(h));
                var u = {
                    _hbtoken_: c,
                    encrypted: h,
                    appId: o,
                    deviceUUID: i,
                    imgCode: r
                };
                console.log("before cust login log all:" + s()(u)), n.a.post(a.a.api.custNoLogin, u, d)
            }
        }
    },

```