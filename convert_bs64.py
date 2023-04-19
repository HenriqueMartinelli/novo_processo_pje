import magic
import io
import mimetypes
import base64

def get_extension(str_base64):
    bytesData = io.BytesIO()
    bytesData.write(base64.b64decode(str_base64))
    bytesData.seek(0)
    mime = magic.from_buffer(bytesData.read(), mime=True)
    mimetype = mimetypes.guess_extension(mime)
    file_size = (len(str_base64) * 6 - str_base64.count('=') * 8) / 8
    return mime, mimetype, file_size