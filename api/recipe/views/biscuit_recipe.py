from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from apps.recipe.models.biscuit_recipe import BiscuitRecipe
from api.recipe.serializers.biscuit_recipe import BiscuitRecipeSerializer, BiscuitRecipeDetailSerializer


def is_have(res, idx):
    for i, r in enumerate(res):
        if r['biscuit']['id'] == idx:
            return True, i
    return False, -1


class RecipeListAPIView(APIView):

    def post(self, request):
        biscuit = request.data.get('biscuit')
        products = request.data.get('products')
        try:
            for product in products:
                serializer = BiscuitRecipeSerializer(data={'biscuit': biscuit, **product})
                serializer.is_valid(raise_exception=True)
                serializer.save()
        except Exception as e:
            raise ValidationError(e)
        return Response({"message": "created successfully"}, status=status.HTTP_201_CREATED)

    def get(self, request):
        recipes = BiscuitRecipe.objects.all()
        data = BiscuitRecipeDetailSerializer(recipes, many=True).data
        res = []

        for d in data:
            idx = d['biscuit']['id']
            check, i = is_have(res, idx)
            if check:
                d.pop('biscuit')
                res[i]['products'].append(d)
            else:
                res.append({'biscuit': d.pop('biscuit'), 'products': [d]})

        return Response(res)


class RecipeDetailAPIView(APIView):
    def put(self, request, *args, **kwargs):
        from apps.biscuit.utils.biscuit import get_biscuit
        data = request.data
        biscuit_id = self.request.GET.get('biscuit_id', None)
        biscuit = get_biscuit(biscuit_id)
        BiscuitRecipe.objects.filter(biscuit=biscuit).delete()
        try:
            for i in data:
                serializer = BiscuitRecipeSerializer(data=i)
                serializer.is_valid(raise_exception=True)
                serializer.save()
        except Exception as e:
            raise ValidationError(e)
        return Response({'message': 'updated successfully'}, status=status.HTTP_202_ACCEPTED)

    def get(self, request, *args, **kwargs):
        from apps.biscuit.utils.biscuit import get_biscuit, get_biscuit_recipe
        biscuit_id = self.request.GET.get('biscuit_id', None)
        get_biscuit = get_biscuit(biscuit_id)
        recipes = get_biscuit_recipe(get_biscuit)
        serializer = BiscuitRecipeDetailSerializer(recipes, many=True)
        return Response(serializer.data)
