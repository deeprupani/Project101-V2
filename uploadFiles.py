import dropbox
import os

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root,dirs,files in os.walk(file_from):
            for name in files:
                local_path = os.path.join(root, name)
                relative_path=os.path.relpath(local_path,file_from)
                dropbox_path=os.path.join(file_to,relative_path)
                print(local_path)
                with open (local_path,'rb') as f:
                 dbx.files_upload(f.read(),dropbox_path,dropbox.files.WriteMode.overwrite)
               #with open (local_path,'rb') as f:
                #    dbx.files_upload(f.read(),dropbox_path,mode=WriteMode('overwrite'))
            
def main():
    access_token ='sl.BEZvHbimypPsQY5MaifDn4FzmbznkVbjVvbZc5H2Z0axRPipXIjwDuonUkIjeGxU699uE6aL1kzm3CSYwfMoImE9L5BdJ6mjMu7CgRNviL17C_9pJvka9beJ6AWrDM5VgptxgzXIGVlh'
    transferData = TransferData(access_token)
    file_from = str(input("Enter the File Path to transfer "))
    file_to = input("Enter the full path to upload to Dropbox ")
    transferData.upload_file(file_from, file_to)
    print("File has been moved")

main()             
