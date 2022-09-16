import { Component, OnInit } from '@angular/core';
import { NanodegreesService, Nanodegree } from '../../services/nanodegrees.service';
import { ModalController } from '@ionic/angular';
import { NanodegreeFormComponent } from './nanodegree-form/nanodegree-form.component';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-nanodegree-menu',
  templateUrl: './nanodegree-menu.page.html',
  styleUrls: ['./nanodegree-menu.page.scss'],
})
export class NanodegreeMenuPage implements OnInit {
  Object = Object;

  constructor(
    private auth: AuthService,
    private modalCtrl: ModalController,
    public Nanodegrees: NanodegreesService
    ) { }

  ngOnInit() {
    this.Nanodegrees.getNanodegrees();
  }

  async openForm(activeNanodegree: Nanodegree = null) {
    if (!this.auth.can('get:nanodegrees-detail')) {
      return;
    }

    const modal = await this.modalCtrl.create({
      component: NanodegreeFormComponent,
      componentProps: { Nanodegree: activeNanodegree, isNew: !activeNanodegree }
    });

    modal.present();
  }

}
