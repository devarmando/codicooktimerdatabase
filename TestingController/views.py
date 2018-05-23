from django.shortcuts import render
from .models import Recipe,Role,Privilege,Tag,Profile,User
from .serializers import RecipeSerializer,RoleSerializer,PrivilegeSerializer,TagSerializer,ProfileSerializer,UserSerializer
from rest_framework.viewsets import *
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class RecipeViewSet(ModelViewSet):
    queryset = Recipe.objects.all().order_by('id')
    serializer_class = RecipeSerializer
    
    
class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all().order_by('id')
    serializer_class = RoleSerializer
    
class PrivilegeViewSet(ModelViewSet):
    queryset = Privilege.objects.all().order_by('id')
    serializer_class = PrivilegeSerializer
    
class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all().order_by('id')
    serializer_class = TagSerializer
    
class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all().order_by('id')
    serializer_class = ProfileSerializer
    
class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    
    @action(detail=False)
    def IsUser(self, request):
        queryset = User.objects.filter()
    
        U = self.request.query_params.get('x', None)
        U = U.split("[AND]")
        
        print (U)
        if (U is not None):
            queryset = queryset.filter(UCrendential=U[0], PCrendential= U[1] )
            serializer = UserSerializer(queryset, many=True)
        queryset = queryset.filter(UCrendential=U[0], PCrendential= U[1] )
        serializer = UserSerializer(queryset, many=True) 
        return Response(serializer.data)
        
    @action(detail=False)
    def UserRecipes(self, request):
        queryset = Recipe.objects.filter()
    
        U = self.request.query_params.get('x', None)
        U = U.split("[AND]")
        
        print (U)
        if (U is not None):
            queryset = queryset.filter(UserId=U[0])
            serializer = RecipeSerializer(queryset, many=True)
            
        queryset = queryset.filter(UserId=U[0])
        serializer = RecipeSerializer(queryset, many=True) 
        return Response(serializer.data)
            
   

    