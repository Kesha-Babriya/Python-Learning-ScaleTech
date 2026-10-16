from django.shortcuts import render
from .models import Item
from .serializers import ItemSerializer
# Create your views here.

#method 1 : Using manually crud operation with serializer

# from rest_framework.response import Response
# from rest_framework.decorators import api_view


# @api_view(['GET'])
# def getData(request):
#     items = Item.objects.all()
#     serializer = ItemSerializer(items,many=True)

#     return Response(serializer.data)

# @api_view(['POST'])
# def addData(request):
#     serializer = ItemSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# from rest_framework import status
# # 3 UPDATE (PUT)
# @api_view(['PUT'])
# def updateItem(request, pk):
#   try:
#     item = Item.objects.get(id=pk)
#   except Item.DoesNotExist:
#     return Response(
#         {'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND
#     )

#   # instance=item નો અર્થ: આ જૂનો ડેટા છે
#   # data=request.data નો અર્થ: આ યુઝરે મોકલેલો નવો સુધારેલો ડેટા છે
#   serializer = ItemSerializer(instance=item, data=request.data)

#   if serializer.is_valid():
#     serializer.save()
#     return Response(serializer.data)

#   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # 4. DELETE (DELETE)
# @api_view(['DELETE'])
# def deleteItem(request, pk):
#   try:
#     item = Item.objects.get(id=pk)
#   except Item.DoesNotExist:
#     return Response(
#         {'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND
#     )

#   item.delete()
#   return Response(
#       {'message': 'Item successfully deleted!'}, status=status.HTTP_200_OK
#   )




#Method 2 using viewset with router nd serializer

from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class ItemViewSet(viewsets.ModelViewSet):
    # ૧. દરવાજા પર બેઠેલો ગાર્ડ કઈ કઈ ઓળખ સ્વીકારશે:
    # - બ્રાઉઝર માટે: SessionAuthentication
    # - બહારની એપ્સ માટે: TokenAuthentication
    authentication_classes = [SessionAuthentication, TokenAuthentication]

    # ૨. નિયમ: ફક્ત લોગિન થયેલા યુઝરને જ અંદર જવા દેવો
    permission_classes = [IsAuthenticated]

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    #both are keyword to use