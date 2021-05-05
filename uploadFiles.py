import os
import dropbox
from dropbox.files import WriteMode

class TransferData():
    def __init__(self,accessToken):
        self.accessToken=accessToken
    def upload_file(self,source,dest):
        dbx=dropbox.Dropbox(self.accessToken)
        for root,dir,files in os.walk(source):
            for fileName in files:

                localpath=os.path.join(root,fileName)
                relativepath=os.path.relpath(localpath,source)
                dropboxpath=os.path.join(dest,relativepath)
                with open(localpath,"rb") as f:
                    dbx.files_upload(f.read(),dropboxpath,mode=WriteMode("overwrite"))


accessToken="sl.AwPenhNu2pQUOpl0dUpf1zdP0czBlfU3kxz79vAgTK0zBx_KYsIx5qJNGHIgzFdSfNo5uNWKdetTAk0cT4LiwpDxQHFI-nxiVhFisWHZrZE66Iudf0BCqNxbABLaiAi4scgE-ZPQdBo"
t1=TransferData(accessToken)
source="ClassProjects"
dest="/CLASSPROJECT"
t1.upload_file(source,dest)

