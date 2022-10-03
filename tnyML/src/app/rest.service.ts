import { Injectable } from '@angular/core';
import { HttpClient, HttpEventType } from '@angular/common/http';
import { ModelData } from './ModelData';
import { finalize, Observable, Subscription } from 'rxjs';
import { ModelInference } from './ModelInference';

@Injectable({
  providedIn: 'root'
})
export class RestService {
  uploadProgress: number = 0;
  uploadSub: Subscription;
  uploadedSuccess: boolean = false;

  constructor(private http: HttpClient) { }
  backendApi: string = "http://127.0.0.1:5001/api/";
  modelURI: string = "models";
  fileuploadPath: string = "files"
  filedownload: string = "files/"
  modelpath: string = "models/"

  ngOnInit() {
  }

  getModels() {
    return this.http.get<string[]>(this.backendApi + this.modelURI);
  }


  downloadFile(filename: string): Observable<Blob> {
    return this.http.get(this.backendApi + this.filedownload + filename, {
      responseType: 'blob' });
  }


  uploadFile(fd: FormData) {
    this.uploadedSuccess = false;
    const upload$ = this.http.post(this.backendApi + this.fileuploadPath, fd, {
      reportProgress: true,
      observe: 'events'
    })
      .pipe(
        finalize(() => this.reset())
      );
    this.uploadSub = upload$.subscribe(event => {
      if (event.type == HttpEventType.UploadProgress) {
        this.uploadProgress = Math.round(100 * (event.loaded / event.total));
      }
    })
  }

  startRecognition(model_name: string, image_url: string) : Observable<ModelInference>{
    image_url = '{ "url": "http://127.0.0.1:5001/api/files/' + image_url + '"}';
    var image_json = JSON.parse(image_url)
    return this.http.post<ModelInference>(this.backendApi + this.modelpath + model_name, image_json)

  }

  reset() {
    this.uploadProgress = null;
    this.uploadSub = null;
    this.uploadedSuccess = true;
    
  }

}
