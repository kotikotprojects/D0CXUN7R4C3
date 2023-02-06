import os.path
import tempfile
import zipfile
import shutil


class ExtractedDocument:
    def __init__(self, path: str):
        self.documentroot = None
        self.app = None
        self.core = None
        if zipfile.is_zipfile(path):
            self.documentroot = tempfile.mkdtemp()
            zipfile.ZipFile(path).extractall(self.documentroot)
            self.app = os.path.join(self.documentroot, 'docProps', 'app.xml')
            self.core = os.path.join(self.documentroot, 'docProps', 'core.xml')

    def pack(self, path):
        with zipfile.ZipFile(path, "w", compresslevel=9, compression=zipfile.ZIP_DEFLATED) as z:
            for root, dirs, files in os.walk(self.documentroot):
                for file in files:
                    z.write(os.path.join(root, file),
                            os.path.relpath(os.path.join(root, file),
                                            self.documentroot))

    def remove(self):
        try:
            shutil.rmtree(self.documentroot, True)
        except Exception as e:
            print(f'Error while removing {self.documentroot}: {e}, remove it manually if you want')
