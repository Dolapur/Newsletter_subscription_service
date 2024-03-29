
from .models import Subscriber, Content
from .serializers import *
from .tasks import send_newsletter
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.viewsets import ModelViewSet
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.request import Request
from rest_framework.permissions import IsAdminUser, BasePermission
from django.contrib.auth.models import AnonymousUser


class SubscriberViewSet(ModelViewSet):
    serializer_class = SubscriberSerializer

    http_method_names = ["post", "delete"]

    @swagger_auto_schema(
        operation_summary="Subscribe to Newsletter",
        operation_description="Subscribe to my newsletter, I promise not to bombard you.",
        responses={201: SubscriberSerializer(), 400: "Bad Request",},
    )
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Successfully subscribed'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Unsubscribe newsletter",
        operation_description="Unsubscribe newsletter.",
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        email = kwargs.get('email')
        if email:
            try:
                subscriber = Subscriber.objects.get(email=email)
                subscriber.delete()
                return Response({'message': 'Successfully unsubscribed'}, status=status.HTTP_204_No_CONTENT)
            except Subscriber.DoesNotExist:
                return Response({'error': 'Subscriber not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'error': 'Email not provided'}, status=status.HTTP_400_BAD_REQUEST)


class ContentViewSet(ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = [IsAdminUser]

    http_method_names = ["get", "post", "patch", "delete"]

    @swagger_auto_schema(
        operation_summary="Get all newsletter (admin/staff only)",
        operation_description="Get all newsletter (admin only)",
        responses={200: ContentSerializer(many=True),
            403: "Forbidden",
        }
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create-newsletter (admin/staff only)",
        operation_description="Create-newsletter (admin/staff only)",
        responses={201: ContentSerializer(),
            403: "Forbidden",
        }
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Sending newsletter
        send_newsletter.delay(serializer.validated_data.get("title"), serializer.validated_data.get("body"))

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @swagger_auto_schema(
        operation_summary="Retrieve a newsletter (admin/staff only)",
        operation_description="Retrieve newsletter (admin/staff only)",
        responses={200: ContentSerializer()}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partial Update of a newsletter (admin/staff only)",
        operation_description="Update specific fields of a newsletter (admin/staff only)",
        responses={200: ContentSerializer()},
        request_body=UpdateContentSerializer,
    )
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = UpdateContentSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Delete a newsletter (admin/staff only)",
        operation_description="Delete a specific newsletter (admin/staff only)",
        responses={204: "No Content"}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
