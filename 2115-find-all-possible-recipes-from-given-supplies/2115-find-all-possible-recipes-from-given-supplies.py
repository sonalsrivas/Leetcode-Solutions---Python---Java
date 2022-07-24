
class Solution:
    def findAllRecipes(self, recipes, ingredients, supplies):
        recipeIngredientMap = {i: j for i, j in zip(recipes, ingredients)}
        supplies = set(supplies)
        visitedRecipeStatus = dict()  # recipe : ingredientsReady?   ###    0=> No     1=> Yes     2=> under process

        def DFSrecipe(recipe):
            visitedRecipeStatus[recipe]=2
            # explore the ingredients of the recipe
            if recipe not in recipes:
                return 0

            for ingredients_ in recipeIngredientMap[recipe]:
                if ingredients_ not in visitedRecipeStatus and ingredients_ not in supplies: #.get(ingredients_,3)==3:
                    DFSrecipe(ingredients_)

                if ingredients_ in supplies or visitedRecipeStatus.get(ingredients_)==1:
                    continue
                elif visitedRecipeStatus.get(ingredients_) in (0,2):
                    visitedRecipeStatus[recipe]=0
                    return

            visitedRecipeStatus[recipe]=1

        for recipe in recipes:
            if visitedRecipeStatus.get(recipe,3) ==3:
                DFSrecipe(recipe)

        return [recipe for recipe in visitedRecipeStatus if visitedRecipeStatus[recipe]==1]
    