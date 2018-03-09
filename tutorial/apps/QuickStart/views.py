from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status


class ListUsers(APIView):
    """
    获取系统用户列表
    """

    # 权限认证方式
    authentication_classes = (authentication.SessionAuthentication,)
    # 访问权限配置
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, format=None):
        username_list = [user.username for user in User.objects.all()]
        return Response(data=username_list, status=status.HTTP_200_OK)
