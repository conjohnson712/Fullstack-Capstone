import { Component, OnInit, Input } from '@angular/core';
import { Nanodegree } from 'src/app/services/nanodegrees.service';

@Component({
  selector: 'app-nanodegree-graphic',
  templateUrl: './nanodegree-graphic.component.html',
  styleUrls: ['./nanodegree-graphic.component.scss'],
})
export class NanodegreeGraphicComponent implements OnInit {
  @Input() nanodegree: Nanodegree;

  constructor() { }

  ngOnInit() {}

}
