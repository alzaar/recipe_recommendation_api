from rest_framework.views import APIView
from django.http import JsonResponse

# from rest_framework import authentication, permissions
from gpt_service.core_service import GPTRecipeService


class RecipesView(APIView):
    authentication_classes = []
    permission_classes = []
    recipe_service = GPTRecipeService()

    def get(self, request, format=None):
        recipe = self.recipe_service.fetch_recipe()
        return JsonResponse({"recipe": recipe})
