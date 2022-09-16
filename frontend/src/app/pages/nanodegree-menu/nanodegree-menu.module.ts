import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Routes, RouterModule } from '@angular/router';

import { IonicModule } from '@ionic/angular';

import { NanodegreeMenuPage } from './nanodegree-menu.page';
import { NanodegreeGraphicComponent } from './nanodegree-graphic/nanodegree-graphic.component';
import { NanodegreeFormComponent } from './nanodegree-form/nanodegree-form.component';

const routes: Routes = [
  {
    path: '',
    component: NanodegreeMenuPage
  }
];


@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    RouterModule.forChild(routes)
  ],
  entryComponents: [NanodegreeFormComponent],
  declarations: [NanodegreeMenuPage, NanodegreeGraphicComponent, NanodegreeFormComponent],
})
export class NanodegreeMenuPageModule {}
