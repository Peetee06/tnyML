import { HttpClient } from '@angular/common/http';
import { Component, Input } from '@angular/core';



@Component({
    selector: 'upload',
    templateUrl: 'upload.component.html'
})
export class UploadComponent  {
    timeLeft: number = 0;
  interval : any;
selectedFile : File = null;

constructor(private http: HttpClient) {}

  onFileSelected(event:any){
    this.selectedFile = event.target.files[0];
  }

  onUpload(){
    const fd = new FormData;
    fd.append('file', this.selectedFile, this.selectedFile.name);
     this.http.post('http://127.0.0.1:5001/api/uploadfile', fd)
     .subscribe(response => console.log(response))

  }
  startTimer() {

    //   this.timeLeft=1;
    // this.interval = setInterval(() => {
    //   if(this.timeLeft < 50) {
    //     this.timeLeft++;
    //   } else {
    //       this.pauseTimer()
      
    //   }
    // },100)
  }

  pauseTimer() {
   // clearInterval(this.interval);
  }
  
}
