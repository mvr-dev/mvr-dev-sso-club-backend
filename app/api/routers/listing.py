# api/routers/listings_minimal.py
from typing import List, Optional
from fastapi import APIRouter, Depends, Path, Query

from api.routers.users import get_current_auth_user
from data.models.user import User

router = APIRouter()


@router.post("/")
async def create_listing(community_id: int,user : User = Depends(get_current_auth_user)):
    user.name
    """Создать предложение услуги/товара"""
    return {"message": f"Listing created in community {community_id}"}


@router.get("/")
async def get_listings(
    community_id: int,
    type: Optional[str] = Query(None, description="service/product"),
    category: Optional[str] = None,
    search: Optional[str] = None,
    page: int = 1,
    size: int = 20,
    user : User = Depends(get_current_auth_user)
):
    user.name
    """Получить список предложений"""
    return {
        "community_id": community_id,
        "total": 0,
        "page": page,
        "size": size,
        "items": []
    }


@router.get("/{listing_id}")
async def get_listing(community_id: int, listing_id: int, user : User = Depends(get_current_auth_user)):
    """Получить предложение по ID"""
    user.name
    return {"listing_id": listing_id, "community_id": community_id}


@router.put("/{listing_id}")
async def update_listing(community_id: int, listing_id: int,user : User = Depends(get_current_auth_user)):
    user : User = Depends(get_current_auth_user)
    """Обновить предложение"""
    return {"message": f"Listing {listing_id} updated"}


@router.delete("/{listing_id}")
async def delete_listing(community_id: int, listing_id: int,user : User = Depends(get_current_auth_user)):
    """Удалить предложение"""
    user.name
    return {"message": f"Listing {listing_id} deleted"}


# @router.get("/categories/list")
# async def get_categories(community_id: int,user : User = Depends(get_current_auth_user)):
#     """Получить категории"""
#     user.name
#     return ["Category 1", "Category 2", "Category 3"]


@router.post("/{listing_id}/favorite")
async def add_to_favorites(community_id: int, listing_id: int,user : User = Depends(get_current_auth_user)):
    user.name
    """Добавить в избранное"""
    return {"message": "Added to favorites"}


@router.get("/my/listings")
async def get_my_listings(community_id: int,user : User = Depends(get_current_auth_user)):
    user.name
    """Мои предложения"""
    return {"items": []}


@router.get("/my/favorites")
async def get_my_favorites(community_id: int,user : User = Depends(get_current_auth_user)):
    user.name
    """Избранное"""
    return {"items": []}