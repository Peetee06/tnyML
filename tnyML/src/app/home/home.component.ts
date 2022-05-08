import { Component, HostListener, Input, Output } from '@angular/core';
import { AppComponent } from '../app.component';
import { RestService } from '../rest.service';
import { Weather } from '../Weather';
@Component({
    selector: 'home',
    templateUrl: 'home.component.html',
    styleUrls: ['./home.component.scss']
})
export class HomeComponent {

    constructor(private rs : RestService) {

    }
    headers = ["day" ,"temperature", "windspeed",  "event"]
  weather : Weather[]  = [] 
  number : number=0;
 @Input() scrollpos? : number;



  items = Array.from({length: 100000}).map((_, i) => `Item #${i}`);

  ngOnInit()
{
 this.readData();
 console.log(this.number);
}
    
readData() {
  this.rs.readWeather().subscribe((data: Weather[]) => {
    this.weather = data;
  })
}



}
