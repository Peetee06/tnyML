import { Component, Input } from '@angular/core';

@Component({
    selector: 'inference',
    templateUrl: 'inference.component.html'
})
export class InferenceComponent {
    @Input() scrollpos? : number;
}
