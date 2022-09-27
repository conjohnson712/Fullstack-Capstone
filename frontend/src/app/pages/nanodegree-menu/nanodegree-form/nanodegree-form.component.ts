import { Component, OnInit, Input } from '@angular/core';
import { Nanodegree, NanodegreesService } from 'src/app/services/nanodegrees.service';
import { ModalController } from '@ionic/angular';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-nanodegree-form',
  templateUrl: './nanodegree-form.component.html',
  styleUrls: ['./nanodegree-form.component.scss'],
})
export class NanodegreeFormComponent implements OnInit {
  @Input() nanodegree: Nanodegree;
  @Input() isNew: boolean;

  constructor(
    public auth: AuthService,
    private modalCtrl: ModalController,
    private nanodegreeService: NanodegreesService
    ) { }

  ngOnInit() {
    if (this.isNew) {
      this.nanodegree = {
        id: -1,
        title: '',
        path: []
      };
      this.addCourse();
    }
  }

  customTrackBy(index: number, obj: any): any {
    return index;
  }

  addCourse(i: number = 0) {
    this.nanodegree.path.splice(i + 1, 0, {name: '', weeks: 1, difficulty: 1});
  }

  removeCourse(i: number) {
    this.nanodegree.path.splice(i, 1);
  }

  closeModal() {
    this.modalCtrl.dismiss();
  }

  saveClicked() {
    this.nanodegreeService.saveNanodegree(this.nanodegree);
    this.closeModal();
  }

  deleteClicked() {
    this.nanodegreeService.deleteNanodegree(this.nanodegree);
    this.closeModal();
  }
}
