import { Component, Input } from '@angular/core';

@Component({
    selector: 'evaluation',
    templateUrl: 'evaluation.component.html'
})
export class EvaluationComponent {
    @Input() scrollpos? : number;
}
