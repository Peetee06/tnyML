import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { RestService } from './rest.service';
import { HttpClientModule } from '@angular/common/http';
import { NavbarComponent } from './navbar/navbar.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HomeComponent } from './home/home.component';
import { UploadComponent } from './upload/upload.component';
import { PreprocessingComponent } from './preprocessing/preprocessing.component';
import { InferenceComponent } from './inference/inference.component';
import { EvaluationComponent } from './evaluation/evaluation.component';
import { TrainingComponent } from './training/training.component';



@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    HomeComponent,
    UploadComponent,
    PreprocessingComponent,
    InferenceComponent,
    EvaluationComponent, 
    TrainingComponent
    
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    BrowserAnimationsModule,
   
  ],
  providers: [RestService],
  bootstrap: [AppComponent]
})
export class AppModule { }
