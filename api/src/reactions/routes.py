from fastapi import APIRouter

router = APIRouter()


@router.get('/')
def reactions_list(request):
    return {'id': 1}
