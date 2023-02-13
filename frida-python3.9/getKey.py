import frida
import sys

# 连接手机设备
rdev = frida.get_remote_device()

# Hook手机上的那个APP（app的包名字）
# 注意事项：在运行这个代码之前，一定要先在手机上启动app
session = rdev.attach("com.eteasun.nanhang")  # 车智赢+
"""

"""
scr = """
Java.perform(function () {

    // 包.类
    var AccountUtils = Java.use("com.eteasun.nanhang.utils.AccountUtils");


    // Hook，替换
    AccountUtils.getKey.implementation = function(context){
        console.log(context);
      

        // 执行原来的方法
        var sign = this.getKey(context);
        console.log(sign);
        return sign;


    }

});
"""

script = session.create_script(scr)


def on_message(message, data):
    print(message, data)


script.on("message", on_message)

script.load()
sys.stdin.read()
