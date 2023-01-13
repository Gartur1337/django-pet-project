from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from .serializers import *
from .permissions import *
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly|IsAdminUser, )

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        if not pk:
          return Post.objects.all()
        
        return Post.objects.filter(pk=pk)


# class PostAPIView(APIView):
#     def get(self, request, *args, **kwargs):
#         pk = kwargs.get("pk")
#         lst = Post.objects.all()
            
#         if not pk:
#             return Response({'Posts': PostSerializer(lst, many=True).data})

#         try:
#             instance = Post.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})  
        
#         serializer = PostSerializer(data=request.data, instance=instance)
#         return Response({"post": serializer.data})

#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save() 

#         return Response({'post': serializer.data})

# class PostAPIUViewUpdate(APIView):

#     def get(self, request, *arg, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})

#         try:
#             instance = Post.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
        
#         return Response({'title': instance.title, 
#                         'author': instance.author, 
#                         'content': instance.content,
#                         'time_create': instance.time_create,
#                         'time_update': instance.time_update,
#                         'is_published': instance.is_published,
#                         'cat': str(instance.cat) })

#     def put(self, request, *arg, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
        
#         try:
#             instance = Post.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})

#         serializer = PostSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save() 
        
#         return Response({'post': serializer.data})

# class PostAPIUViewDestroy(APIView):

#     def get(self, request, *arg, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})

#         try:
#             instance = Post.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
            
#         return Response({'title': instance.title, 
#                         'author': instance.author, 
#                         'content': instance.content,
#                         'time_create': instance.time_create,
#                         'time_update': instance.time_update,
#                         'is_published': instance.is_published,
#                         'cat': str(instance.cat) })

#     def delete(self, request, *arg, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
        
#         try:
#             instance = Post.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
        
#         if instance:
#             instance.delete()
#             return Response({"post": "delete post " + str(pk)})
#         else:
#             return Response({"error": "Object does not exists"})