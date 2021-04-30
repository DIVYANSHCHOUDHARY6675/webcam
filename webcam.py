import cv2
import dropbox
import time
import random
start_time=time.time()
def take_snapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        image_name="img"+str(number)+".png"
        cv2.imwrite(image_name,frame)
        start_time=time.time
        result=False
    return image_name 
    print ("I cought you in my camera")    
    videoCaptureObject.release()
    cv2.destroyAllWindows()
def upload_file(image_name):
     access_token = 'DtQORd8HHi0AAAAAAAAAAcgW4AfYA4e7LqXNpURfFabwmeqEq9zYvwJp_kuBdAz9'
     file=image_name
     file_from=file
     file_to="/test/"+image_name
     dbx=dropbox.Dropbox( access_token)
     with open (file_from,"rb") as f:
         dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
         print ("file uploaded")
def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=take_snapshot()
            upload_file(name)
            
main()            
            


