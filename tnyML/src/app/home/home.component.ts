import { Component, HostListener, Input, Output } from '@angular/core';
import { AppComponent } from '../app.component';
import { RestService } from '../rest.service';
import { ModelData } from '../ModelData';
import { ModelInference } from '../ModelInference';


@Component({
  selector: 'home',
  templateUrl: 'home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent {
  models: string[] = [];
  selectedModelDescr: string;
  htmlelement: HTMLElement;
  selectedFile : File = null;
  fileuploaded : boolean = false;
  hideWelcome : boolean = false;
  started : boolean = false;
  imageToShow: any;
  result : ModelInference;


  constructor(public rs: RestService) {
  }

  ngOnInit() {
    this.result = new ModelInference(0, "");
    this.getModels();
  }
  scroll(element: string) {
   this.hideWelcome = true;
  setTimeout(()=> {this.started = true}, 1000)
  }

  public getModels() {
    this.rs.getModels().subscribe((data: string[]) => {
      this.models = data;
      console.log(this.models[0]);
    })
  }
  selectedModel(modelId : string){
    this.selectedModelDescr = modelId;
    console.log(modelId);
    //this.scroll("upload");
  }

  onFileSelected(event:any){
    this.selectedFile = event.target.files[0];
  }

  onUpload(){
    this.imageToShow = null;
    const fd = new FormData;
    fd.append('file', this.selectedFile, this.selectedFile.name);
    this.rs.uploadFile(fd);
    
  }

  showImage(){
    
     this.rs.downloadFile(this.selectedFile.name).subscribe((img : Blob) => 
     {
       this.createImageFromBlob(img);
     });
    this.rs.startRecognition(this.selectedModelDescr,this.selectedFile.name) 
    .subscribe((data : ModelInference) => {
      this.result = data;
      console.log(data)
    });

  }
  createImageFromBlob(image: Blob) {
    let reader = new FileReader();
    reader.addEventListener("load", () => {
       this.imageToShow = reader.result;
    }, false);
 
    if (image) {
       reader.readAsDataURL(image);
    }
 }

}