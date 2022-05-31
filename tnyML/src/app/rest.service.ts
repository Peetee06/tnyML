import { Injectable } from '@angular/core';
import { HttpClient, HttpEventType } from '@angular/common/http';
import { ModelData } from './ModelData';
import { finalize, Observable, Subscription } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class RestService {
  uploadProgress:number = 0;
  uploadSub: Subscription;
  uploadedSuccess: boolean = false;

  constructor(private http : HttpClient) { }
  backendApi: string = "http://127.0.0.1:5000/api/";
  modelURI : string = "models";
  fileuploadPath: string ="uploadfile"
  filedownload: string ="getfile/"

  ngOnInit(){
  }

  getModels()
  {
    return this.http.get<ModelData[]>(this.backendApi+this.modelURI);
  }


  downloadFile(filename : string): Observable<Blob>{
    return this.http.get(this.backendApi+this.filedownload+filename, { responseType: 'blob' });
 //   return this.http.get(this.backendApi+this.filedownload+filename);
  }


  uploadFile(fd : FormData)
  {
    this.uploadedSuccess = false;
    const upload$ = this.http.post(this.backendApi+this.fileuploadPath, fd, {
      reportProgress:true,
      observe:'events'})
      .pipe(
        finalize(()=>this.reset())
        );
        this.uploadSub = upload$.subscribe(event => {
          if (event.type == HttpEventType.UploadProgress) {
            this.uploadProgress = Math.round(100 * (event.loaded / event.total));
          }
        })
  }

  reset() {
    this.uploadProgress = null;
    this.uploadSub = null;
    this.uploadedSuccess = true;
  }

}
