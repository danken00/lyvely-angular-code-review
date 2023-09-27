import {Component} from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'lyvely-angular-code-review';

  changeColour() {
    const b = document.getElementById('background-sky');

    if (b) {
      if (b.classList.contains('night')) {
        b.classList.remove('night');
        b.classList.add('day');
      } else {
        b.classList.remove('day');
        b.classList.add('night');
      }
    }
  }
}
