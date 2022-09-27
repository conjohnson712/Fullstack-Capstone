import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { AuthService } from './auth.service';
import { environment } from 'src/environments/environment';

export interface Nanodegree {
  id: number;
  title: string;
  path: Array<{
          name: string,
          weeks: number,
          difficulty: number
        }>;
}

@Injectable({
  providedIn: 'root'
})
export class NanodegreesService {

  url = environment.apiServerUrl;

  public items: {[key: number]: Nanodegree} //= {};
  = {
                              1: {
                              id: 1,
                              title: 'Intro to Computer Basics',
                              path: [
                                    {
                                      name: 'The Power Button: Where It All Begins',
                                      weeks: 1,
                                      difficulty: 1
                                    },
                                    {
                                      name: 'Understanding Those Pesky Logins',
                                      weeks: 3,
                                      difficulty: 1
                                    },
                                  ]
                            },
                            2: {
                              id: 2,
                              title: 'Intermediate Computer Knowledge',
                              path: [

                                    {
                                      name: 'Microsoft Word',
                                      weeks: 2,
                                      difficulty: 2
                                    },
                                    {
                                      name: 'Microsoft Excel',
                                      weeks: 2,
                                      difficulty: 2
                                    },
                                    {
                                      name: 'Microsoft Powerpoint',
                                      weeks: 2,
                                      difficulty: 2
                                     },
                                  ]
                            },
                            3: {
                              id: 3,
                              title: 'Beginner Video Game Development',
                              path: [
                                    {
                                      name: 'Creating Text-Based Adventures',
                                      weeks: 3,
                                      difficulty: 3
                                    },
                                    {
                                      name: 'Creating 2D Side-Scroller Games',
                                      weeks: 3,
                                      difficulty: 3
                                    },
                                    {
                                      name: 'Creating 3D Games and FPS',
                                      weeks: 3,
                                      difficulty: 3
                                    },
                                  ]
                            }
    };


  constructor(private auth: AuthService, private http: HttpClient) { }

  getHeaders() {
    const header = {
      headers: new HttpHeaders()
        .set('Authorization',  `Bearer ${this.auth.activeJWT()}`)
    };
    return header;
  }

  getNanodegrees() {
    if (this.auth.can('get:nanodegrees-detail')) {
      this.http.get(this.url + '/nanodegrees-detail', this.getHeaders())
      .subscribe((res: any) => {
        this.nanodegreesToItems(res.nanodegrees);
        console.log(res);
      });
    } else {
      this.http.get(this.url + '/nanodegrees', this.getHeaders())
      .subscribe((res: any) => {
        this.nanodegreesToItems(res.nanodegrees);
        console.log(res);
      });
    }

  }

  saveNanodegree(nanodegree: Nanodegree) {
    if (nanodegree.id >= 0) { // patch
      this.http.patch(this.url + '/nanodegrees/' + nanodegree.id, nanodegree, this.getHeaders())
      .subscribe( (res: any) => {
        if (res.success) {
          this.nanodegreesToItems(res.nanodegrees);
        }
      });
    } else { // insert
      this.http.post(this.url + '/nanodegrees', nanodegree, this.getHeaders())
      .subscribe( (res: any) => {
        if (res.success) {
          this.nanodegreesToItems(res.nanodegrees);
        }
      });
    }

  }

  deleteNanodegree(nanodegree: Nanodegree) {
    delete this.items[nanodegree.id];
    this.http.delete(this.url + '/nanodegrees/' + nanodegree.id, this.getHeaders())
    .subscribe( (res: any) => {

    });
  }

  nanodegreesToItems( nanodegrees: Array<Nanodegree>) {
    for (const nanodegree of nanodegrees) {
      this.items[nanodegree.id] = nanodegree;
    }
  }
}
