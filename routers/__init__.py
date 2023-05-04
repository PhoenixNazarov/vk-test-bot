from aiogram import Router

from .home import router as home_router
from .managment import router as management_router

router = Router()

router.include_router(management_router)
router.include_router(home_router)
