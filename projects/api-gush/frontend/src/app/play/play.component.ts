import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-play',
  templateUrl: './play.component.html',
  styleUrls: ['./play.component.scss']
})
export class PlayComponent implements OnInit {

  myName = "Akhil"

  constructor() { }

  ngOnInit(): void {
  }

  callFunc1(){
    console.log("function called")
  }

}
