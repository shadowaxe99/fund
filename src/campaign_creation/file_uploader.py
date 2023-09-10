```python
import os
from werkzeug.utils import secure_filename

class FileUploader:
    def __init__(self, upload_folder, allowed_extensions):
        self.upload_folder = upload_folder
        self.allowed_extensions = allowed_extensions

    def allowed_file(self, filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in self.allowed_extensions

    def upload_file(self, file):
        if file and self.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(self.upload_folder, filename))
            return filename
        else:
            raise ValueError("Invalid file type. Please upload a file with the following extensions: " + ', '.join(self.allowed_extensions))

    def get_file_path(self, filename):
        return os.path.join(self.upload_folder, filename)
```