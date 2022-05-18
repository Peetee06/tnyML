import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Weather } from './Weather';

@Injectable({
  providedIn: 'root'
})
export class RestService {

  constructor(private http : HttpClient) { }
  weatherUrl : string = "http://127.0.0.1:5000/api/getData/";

  ngOnInit(){
  }

  readWeather()
  {
    return this.http.get<Weather[]>(this.weatherUrl);
  }
}
