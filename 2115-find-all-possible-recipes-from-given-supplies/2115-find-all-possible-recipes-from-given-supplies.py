
class Solution:
    def findAllRecipes(self, recipes, ingredients, supplies):
        recipeIngredientMap = {i: j for i, j in zip(recipes, ingredients)}
        supplies = set(supplies)
        visitedRecipeStatus = dict()  # recipe : ingredientsReady?   ###    0=> No     1=> Yes     2=> under process

        def DFSrecipe(recipe):
            visitedRecipeStatus[recipe]=2
            print(recipe, visitedRecipeStatus)
            # explore the ingredients of the recipe
            if recipe in supplies:
                return 1
            elif recipe not in recipes:
                return 0

            #if recipe in visitedRecipeStatus:
            #    return 1 if visitedRecipeStatus[recipe]==1 else 0 # if recipe under process or processed and verdict is zero then NO BRO
            allIngredientsAvailableFlag = True

            for ingredients_ in recipeIngredientMap[recipe]:
                if ingredients_ not in visitedRecipeStatus: #.get(ingredients_,3)==3:
                    DFSrecipe(ingredients_)
                    #allIngredientsAvailableFlag &= True if DFSrecipe(ingredients_) else False
                if ingredients_ in supplies or visitedRecipeStatus.get(ingredients_)==1:
                    continue
                elif visitedRecipeStatus.get(ingredients_) in (0,2):
                    visitedRecipeStatus[recipe]=0
                    return  #allIngredientsAvailableFlag &= visitedRecipeStatus.get(ingredients_)
                #elif visitedRecipeStatus.get(ingredients_)==1:
                #    return 1
            #print("allIngredientsAvailableFlag=",allIngredientsAvailableFlag)
            visitedRecipeStatus[recipe]=1 #if allIngredientsAvailableFlag else 0
            #return visitedRecipeStatus[recipe]

        for recipe in recipes:
            if visitedRecipeStatus.get(recipe,3) ==3:
                print("visitedRecipeStatus.get(recipe,3) => ",visitedRecipeStatus.get(recipe,3), recipe)
                DFSrecipe(recipe)

        return [recipe for recipe in visitedRecipeStatus if visitedRecipeStatus[recipe]==1]