from fastapi import APIRouter

router = APIRouter()


@router.get('/')
def accounts_list(request):
    return {'id': 1}
