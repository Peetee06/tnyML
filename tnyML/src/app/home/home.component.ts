import { Component, HostListener, Input, Output } from '@angular/core';
import { AppComponent } from '../app.component';
import { RestService } from '../rest.service';
import { ModelData } from '../ModelData';

@Component({
  selector: 'home',
  templateUrl: 'home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent {
  models: ModelData[] = [];
  selectedModelId: number;
  htmlelement: HTMLElement;
  selectedFile : File = null;
  fileuploaded : boolean = false;
  started : boolean = false;
  imageToShow: any;


  constructor(public rs: RestService) {
  }

  ngOnInit() {
    this.getModels();
  }
  scroll(element: string) {

    this.htmlelement = document.getElementById(element);
    this.started = true;
    this.htmlelement.scrollIntoView({ behavior: 'smooth' });
  }

  public getModels() {
    this.rs.getModels().subscribe((data: ModelData[]) => {
      this.models = data;
    })
  }
  selectedModel(modelId : number){
    this.selectedModelId = modelId;
    console.log(modelId);
    //this.scroll("upload");
  }

  onFileSelected(event:any){
    this.selectedFile = event.target.files[0];
  }

  onUpload(){

    const fd = new FormData;
    fd.append('file', this.selectedFile, this.selectedFile.name);
    this.rs.uploadFile(fd);
 
  }

  showImage(){
    this.rs.downloadFile(this.selectedFile.name).subscribe((img : Blob) => 
    {
      this.createImageFromBlob(img);
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