# encoding:utf-8
from django.http import HttpResponse


def request_info(request):
    """
    基本请求接口
    :return:
    """
    data = "image is not cap!"
    return HttpResponse(data)


def run():
    """
    测试开始
    :return:
    """


if __name__ == '__main__':
    run()
