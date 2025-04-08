from rest_framework.response import Response
from rest_framework import status


def get_success_response_200(data):
    return Response(data={"success": True, "data": data}, status=status.HTTP_200_OK)


def get_success_response_201(data):
    return Response(data={"success": True, "data": data}, status=status.HTTP_201_CREATED)


def get_error_response_400(message="Invalid Request made!"):
    return Response(data={"success": False, "errors": message}, status=status.HTTP_400_BAD_REQUEST)


def get_error_response_403(message="Forbidden Request!"):
    return Response(data={"success": False, "errors": message}, status=status.HTTP_403_FORBIDDEN)


def get_error_response_404(message="Not Found!"):
    return Response(data={"success": False, "errors": message}, status=status.HTTP_404_NOT_FOUND)


def get_error_response_401(message="Un-Authorised access request made!"):
    return Response(data={"success": False, "errors": message}, status=status.HTTP_401_UNAUTHORIZED)


def get_error_response_406(message="UnAcceptable request!"):
    return Response(
        data={"success": False, "errors": message},
        status=status.HTTP_406_NOT_ACCEPTABLE,
    )


def get_error_response_500(message="Something went wrong!"):
    return Response(
        data={"success": False, "errors": message},
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )
