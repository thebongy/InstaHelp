import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams, PopoverController } from 'ionic-angular';
import {PopupPage} from "../popup/popup";
/**
 * Generated class for the MainPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-main',
  templateUrl: 'main.html',
})
export class MainPage {

  constructor(public navCtrl: NavController, public navParams: NavParams, public popoverCtrl: PopoverController) {
    
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad MainPage');
  }
  presentPopover() {
    const popover = this.popoverCtrl.create(PopupPage);
    popover.present();

}}
