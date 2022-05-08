import { Component, Input } from '@angular/core';

@Component({
    selector: 'training',
    templateUrl: 'training.component.html'
})
export class TrainingComponent {
    show_progress : boolean = false;
    button_text : string = "Start Training"
    myClass: string ="progress";
    @Input() scrollpos? : number;

    showtraining()
    {
        this.show_progress = !this.show_progress ;
        if (this.show_progress)
            this.button_text = "Stop Training";
        else 
            this.button_text = "Start Training";
    }
}
