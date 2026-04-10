from fastapi import APIRouter, Depends
import api.dependensies as dependensies
from services.isuggestions_service import ISuggestionsService
from typing import List

router = APIRouter()

@router.get("/names",response_model=List[str])
async def getNames(prefix:str ="", suggestionsService: ISuggestionsService = Depends(dependensies.get_names_suggestions_service)):
    # print(suggestionsService.getNames())
    return await suggestionsService.getSuggestion(prefix)

@router.get("/surnames",response_model=List[str])
async def getSurames(prefix:str ="", suggestionsService: ISuggestionsService = Depends(dependensies.get_surnames_suggestion_service)):
    return await suggestionsService.getSuggestion(prefix)

@router.get('/cities',response_model=List[str])
async def getCities(prefix:str = "", suggestionsService: ISuggestionsService = Depends(dependensies.get_cities_suggestion_service)):
    return await suggestionsService.getSuggestion(prefix)

@router.get('/streets',response_model=List[str])
async def getStreets(prefix:str = "", suggestionService:ISuggestionsService = Depends(dependensies.get_streets_suggestion_service)):
    return await suggestionService.getSuggestion(prefix)