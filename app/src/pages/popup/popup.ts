import { Component } from '@angular/core';
import { IonicPage, NavController,PopoverController, NavParams } from 'ionic-angular';
import{ HelpPage} from '../help/help';
/**
 * Generated class for the PopupPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-popup',
  templateUrl: 'popup.html',
})
export class PopupPage {

  constructor(public navCtrl: NavController, public navParams: NavParams, public popoverCtrl: PopoverController) {
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad PopupPage');
  }
  presentPopover() {
    console.log('1');
    const help = this.popoverCtrl.create(HelpPage);
    help.present();
    console.log('2');
}
}
