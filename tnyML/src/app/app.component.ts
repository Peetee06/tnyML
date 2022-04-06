import { Component } from '@angular/core';
import { RestService } from './rest.service';
import { Weather } from './Weather';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  title = 'tnyML';


  constructor( private rs : RestService){
  }
  headers = ["day" ,"temperature", "windspeed",  "event"]
  weather : Weather[]  = [] 

  ngOnInit()
{
 this.readData();
}
    
readData() {
  this.rs.readWeather().subscribe((data: Weather[]) => {
    this.weather = data;
  })
}

      

}
