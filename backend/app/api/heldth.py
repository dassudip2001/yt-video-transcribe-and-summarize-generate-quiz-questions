from fastapi import APIRouter



router=APIRouter()



@router.get("/")
async def heldth():
    return {"message":"Server is running........"}