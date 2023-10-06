from fastapi import APIRouter, Request, Body, UploadFile, File
from src.service.contents_service import ContentsService
from src.entity.contents import ContentsEntity, ConsultContentInformation, UpdateContents

contents_router = APIRouter()

contents_service = ContentsService()


@contents_router.post('/upload/file')
async def read_contents(request: Request, data_contents: ContentsEntity = Body(...),
                        file: UploadFile = File(..., alias="content_pdf")):
    user_id = ""
    contents = await contents_service.create_contents(user_id, data_contents, file)
    return contents


@contents_router.post('/search')
def search_contents(request: Request, search_content: ConsultContentInformation):
    user_id = request.state.user_id
    contents = contents_service.search_info_embedding_by_OpeIA(user_id, search_content)
    return contents


@contents_router.post('/search/nlCloud')
def search_contents(request: Request, search_content: ConsultContentInformation):
    user_id = request.state.user_id
    contents = contents_service.search_info_embedding_by_nlCloud(user_id, search_content)
    return contents


@contents_router.put('/update/{content_id}')
async def update_contents(request: Request, data_content: UpdateContents, content_id: str,
                          file: UploadFile | None = None):
    user_id = request.state.user_id
    contents = await contents_service.upload_content(content_id, user_id, data_content, file)
    return contents
