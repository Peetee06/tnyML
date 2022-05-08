import { Component, Input } from '@angular/core';

@Component({
    selector: 'preprocessing',
    templateUrl: 'preprocessing.component.html'
})
export class PreprocessingComponent {
    @Input() scrollpos? : number;
}
