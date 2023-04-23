from fastapi import APIRouter
from src.accounts.routes import router as accounts_router
from src.articles.routes import router as articles_router
from src.reactions.routes import router as reactions_router

# API Router
api_router = APIRouter()
api_router.include_router(accounts_router, prefix='/accounts')
api_router.include_router(articles_router, prefix='/articles')
api_router.include_router(reactions_router, prefix='/reactions')
