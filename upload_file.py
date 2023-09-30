import os, tempfile
from fastapi import APIRouter, UploadFile, File
from starlette.responses import JSONResponse
from tasks import mockup_task

router = APIRouter()

@router.post("/upload-file")
async def upload_case(file: UploadFile = File(...)):
    temp_dir = tempfile.TemporaryDirectory()
    temp_file_path = os.path.join(temp_dir.name, file.filename)

    with open(temp_file_path, 'wb+') as temp_file:
        temp_file.write(await file.read())

    file_info = os.stat(temp_file_path)

    mockup_task.delay(12, 23)

    return JSONResponse(content={
        'detail': 'file uploaded successfully (processing in background)',
        'file_path': temp_file_path,
        'file_size': file_info.st_size,
        'created_at': file_info.st_ctime,
        'modified_at': file_info.st_mtime,
    })