import { Component, Input } from '@angular/core';



@Component({
    selector: 'upload',
    templateUrl: 'upload.component.html'
})
export class UploadComponent  {
    timeLeft: number = 0;
  interval : any;

  startTimer() {
      this.timeLeft=1;
    this.interval = setInterval(() => {
      if(this.timeLeft < 50) {
        this.timeLeft++;
      } else {
          this.pauseTimer()
      
      }
    },100)
  }

  pauseTimer() {
    clearInterval(this.interval);
  }
  
}
