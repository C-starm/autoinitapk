# coding: UTF-8
import uiautomator2 as u2
import os


def app_init(package_name: str):
    with test_device.watch_context() as ctx:
        ctx.when("我知道了").click()
        ctx.when("^(?!.*不同意.*)(?!.*《.*).*同意.*$").click()
        ctx.when("^.*授权.*$").click()
        ctx.when("仅使用期间允许").click()
        ctx.when("始终允许").click()
        ctx.when("^(?!.*《.*).*允许.*$").click()
        ctx.wait_stable()
    os.system("adb shell monkey -p %s 5000" % (package_name))


if __name__ == '__main__':
    device_name = "EYP0120930000325"
    test_device = u2.connect_usb(device_name)
    print(test_device.info)
    # test_device.app_start("com.android.settings")
    app_init("com.f100.android")
