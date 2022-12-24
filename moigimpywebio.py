


from pywebio.input import *
from pywebio.output import *
from pywebio.pin import *
from pywebio.platform import *

def man():
  with use_scope(name='logo',clear=True):
      put_grid([[None,None,None,put_image('https://s3.gifyu.com/images/Fauget.gif',width='300',height='300'),None,None]])

  with use_scope(name='se',clear=True):
      put_grid([[None,None,None,put_select(name='g',options=['Game1','Game2','Game3']),None,None,None]])

  with use_scope(name='li',clear=True):
    put_html('<hr>')
  while True:
    pin_wait_change('g')
    if pin.g == 'Game1':
        start_1()
    if pin.g == 'Game2':
        start_2()
    if pin.g == 'Game3':
        start_3()

def start_1():#

  with use_scope('game',clear=True):
    put_html('''
<h1>Pure CSS By MoiGim PyWebIo</h1>
<form>
  <div class="board">
    <div class="field">
      <div class="grid column">
        <input type="radio" name="slot11" tabindex="-1" required>
        <input type="radio" name="slot11" tabindex="-1" required>
        <div class="disc"></div>
        <input type="radio" name="slot12" tabindex="-1" required>
        <input type="radio" name="slot12" tabindex="-1" required>
        <div class="disc"></div>
        <input type="radio" name="slot13" tabindex="-1" required>
        <input type="radio" name="slot13" tabindex="-1" required>
        <div class="disc"></div>
        <input type="radio" name="slot14" tabindex="-1" required>
        <input type="radio" name="slot14" tabindex="-1" required>
        <div class="disc"></div>
        <input type="radio" name="slot15" tabindex="-1" required>
        <input type="radio" name="slot15" tabindex="-1" required>
        <div class="disc"></div>
        <input type="radio" name="slot16" tabindex="-1" required>
        <input type="radio" name="slot16" tabindex="-1" required>
        <div class="disc"></div>

        <!--Column 1 after-->
        <div class="column">
          <input type="radio" name="slot21" tabindex="-1" required>
          <input type="radio" name="slot21" tabindex="-1" required>
          <div class="disc"></div>
          <input type="radio" name="slot22" tabindex="-1" required>
          <input type="radio" name="slot22" tabindex="-1" required>
          <div class="disc"></div>
          <input type="radio" name="slot23" tabindex="-1" required>
          <input type="radio" name="slot23" tabindex="-1" required>
          <div class="disc"></div>
          <input type="radio" name="slot24" tabindex="-1" required>
          <input type="radio" name="slot24" tabindex="-1" required>
          <div class="disc"></div>
          <input type="radio" name="slot25" tabindex="-1" required>
          <input type="radio" name="slot25" tabindex="-1" required>
          <div class="disc"></div>
          <input type="radio" name="slot26" tabindex="-1" required>
          <input type="radio" name="slot26" tabindex="-1" required>
          <div class="disc"></div>

          <!--Column 2 after-->
          <div class="column">
            <input type="radio" name="slot31" tabindex="-1" required>
            <input type="radio" name="slot31" tabindex="-1" required>
            <div class="disc"></div>
            <input type="radio" name="slot32" tabindex="-1" required>
            <input type="radio" name="slot32" tabindex="-1" required>
            <div class="disc"></div>
            <input type="radio" name="slot33" tabindex="-1" required>
            <input type="radio" name="slot33" tabindex="-1" required>
            <div class="disc"></div>
            <input type="radio" name="slot34" tabindex="-1" required>
            <input type="radio" name="slot34" tabindex="-1" required>
            <div class="disc"></div>
            <input type="radio" name="slot35" tabindex="-1" required>
            <input type="radio" name="slot35" tabindex="-1" required>
            <div class="disc"></div>
            <input type="radio" name="slot36" tabindex="-1" required>
            <input type="radio" name="slot36" tabindex="-1" required>
            <div class="disc"></div>

            <!--Column 3 after-->
            <div class="column">
              <input type="radio" name="slot41" tabindex="-1" required>
              <input type="radio" name="slot41" tabindex="-1" required>
              <div class="disc"></div>
              <input type="radio" name="slot42" tabindex="-1" required>
              <input type="radio" name="slot42" tabindex="-1" required>
              <div class="disc"></div>
              <input type="radio" name="slot43" tabindex="-1" required>
              <input type="radio" name="slot43" tabindex="-1" required>
              <div class="disc"></div>
              <input type="radio" name="slot44" tabindex="-1" required>
              <input type="radio" name="slot44" tabindex="-1" required>
              <div class="disc"></div>
              <input type="radio" name="slot45" tabindex="-1" required>
              <input type="radio" name="slot45" tabindex="-1" required>
              <div class="disc"></div>
              <input type="radio" name="slot46" tabindex="-1" required>
              <input type="radio" name="slot46" tabindex="-1" required>
              <div class="disc"></div>

              <!--Column 4 after-->
              <div class="column">
                <input type="radio" name="slot51" tabindex="-1" required>
                <input type="radio" name="slot51" tabindex="-1" required>
                <div class="disc"></div>
                <input type="radio" name="slot52" tabindex="-1" required>
                <input type="radio" name="slot52" tabindex="-1" required>
                <div class="disc"></div>
                <input type="radio" name="slot53" tabindex="-1" required>
                <input type="radio" name="slot53" tabindex="-1" required>
                <div class="disc"></div>
                <input type="radio" name="slot54" tabindex="-1" required>
                <input type="radio" name="slot54" tabindex="-1" required>
                <div class="disc"></div>
                <input type="radio" name="slot55" tabindex="-1" required>
                <input type="radio" name="slot55" tabindex="-1" required>
                <div class="disc"></div>
                <input type="radio" name="slot56" tabindex="-1" required>
                <input type="radio" name="slot56" tabindex="-1" required>
                <div class="disc"></div>

                <!--Column 5 after-->
                <div class="column">
                  <input type="radio" name="slot61" tabindex="-1" required>
                  <input type="radio" name="slot61" tabindex="-1" required>
                  <div class="disc"></div>
                  <input type="radio" name="slot62" tabindex="-1" required>
                  <input type="radio" name="slot62" tabindex="-1" required>
                  <div class="disc"></div>
                  <input type="radio" name="slot63" tabindex="-1" required>
                  <input type="radio" name="slot63" tabindex="-1" required>
                  <div class="disc"></div>
                  <input type="radio" name="slot64" tabindex="-1" required>
                  <input type="radio" name="slot64" tabindex="-1" required>
                  <div class="disc"></div>
                  <input type="radio" name="slot65" tabindex="-1" required>
                  <input type="radio" name="slot65" tabindex="-1" required>
                  <div class="disc"></div>
                  <input type="radio" name="slot66" tabindex="-1" required>
                  <input type="radio" name="slot66" tabindex="-1" required>
                  <div class="disc"></div>

                  <!--Column 6 after-->
                  <div class="column">
                    <input type="radio" name="slot71" tabindex="-1" required>
                    <input type="radio" name="slot71" tabindex="-1" required>
                    <div class="disc"></div>
                    <input type="radio" name="slot72" tabindex="-1" required>
                    <input type="radio" name="slot72" tabindex="-1" required>
                    <div class="disc"></div>
                    <input type="radio" name="slot73" tabindex="-1" required>
                    <input type="radio" name="slot73" tabindex="-1" required>
                    <div class="disc"></div>
                    <input type="radio" name="slot74" tabindex="-1" required>
                    <input type="radio" name="slot74" tabindex="-1" required>
                    <div class="disc"></div>
                    <input type="radio" name="slot75" tabindex="-1" required>
                    <input type="radio" name="slot75" tabindex="-1" required>
                    <div class="disc"></div>
                    <input type="radio" name="slot76" tabindex="-1" required>
                    <input type="radio" name="slot76" tabindex="-1" required>
                    <div class="disc"></div>

                    <!--Column 7 after-->
                    <div class="column"></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="front"></div>
  </div>
  <button type="reset">New Game</button>
</form>
<style>
body {
  margin: 0;
  font-family: "Helvetica", "Verdana", "Roboto", sans-serif;
}

h1 {
  margin: 0 0 15px;
  padding: 15px;
  color: #fff;
  font-size: 40px;
  font-weight: normal;
  text-align: center;
  background-color: #1f90ff;
}

form {
  display: flex;
  flex-flow: column nowrap;
  align-items: center;
}

.board {
  position: relative;
  width: 450px;
  height: 450px;
}

.field {
  position: absolute;
  top: 0;
  left: 15px;
  padding: 75px 0 0 0;
  box-sizing: border-box;
  width: 420px;
  height: 435px;
  overflow: hidden;
  cursor: not-allowed;
}

.grid {
  display: inline-flex;
  flex-flow: column wrap;
  position: relative;
  min-width: 420px;
  height: 360px;
  counter-reset: player 1;
}

.column {
  display: inline-flex;
  flex-flow: column wrap;
  height: 360px;
}

.front {
  position: absolute;
  top: 60px;
  border: 15px solid #007fff;
  border-radius: 4px;
  box-sizing: border-box;
  width: 450px;
  height: 390px;
  pointer-events: none;
  background: radial-gradient(circle, transparent, transparent 18px, #007fff 20px, #007fff 23px, #1f90ff 23px, #1f90ff 36px, #007fff) center top/60px 60px;
}

/* Invisible inputs */
input {
  display: none;
  position: absolute;
  top: -90px;
  margin: 0;
  width: 60px;
  height: 450px;
  cursor: pointer;
  opacity: 0;
}
input:indeterminate {
  display: initial;
}
/* Inputs for red */
.column > input:nth-of-type(2n) {
  right: 360px;
}
.column > .column > input:nth-of-type(2n) {
  right: 300px;
}
.column > .column > .column > input:nth-of-type(2n) {
  right: 240px;
}
.column > .column > .column > .column > input:nth-of-type(2n) {
  right: 180px;
}
.column > .column > .column > .column > .column > input:nth-of-type(2n) {
  right: 120px;
}
.column > .column > .column > .column > .column > .column > input:nth-of-type(2n) {
  right: 60px;
}
.column > .column > .column > .column > .column > .column > .column > input:nth-of-type(2n) {
  right: 0;
}
/* Inputs for yellow */
.column > input:nth-of-type(2n+1) {
  left: 0;
}
.column > .column > input:nth-of-type(2n+1) {
  left: 60px;
}
.column > .column > .column > input:nth-of-type(2n+1) {
  left: 120px;
}
.column > .column > .column > .column > input:nth-of-type(2n+1) {
  left: 180px;
}
.column > .column > .column > .column > .column > input:nth-of-type(2n+1) {
  left: 240px;
}
.column > .column > .column > .column > .column > .column > input:nth-of-type(2n+1) {
  left: 300px;
}
.column > .column > .column > .column > .column > .column > .column > input:nth-of-type(2n+1) {
  left: 360px;
}

/* Disc */
.disc {
  position: relative;
  top: 0;
  width: 60px;
  height: 60px;
  color: #fff;
  background: radial-gradient(circle, currentcolor 12px, #666 13px, currentcolor 14px, currentcolor 21px, #666 22px, transparent 23px, transparent) center/60px;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.2s, top 0s 0.2s, color 0s 0.2s;
}

/* Red's turn */
input:hover + .disc {
  color: #ff010b;
  opacity: 1;
  transition: opacity 0.2s, top 0s;
}
input:checked + .disc {
  color: #ff010b;
  opacity: 1;
}
/* Yellow's turn */
input:hover + input + .disc {
  color: #ffd918;
  opacity: 1;
  transition: opacity 0.2s, top 0s;
}
input:checked + input + .disc {
  color: #ffd918;
  opacity: 1;
}

/* Height and time of disc fall per row */
input:hover + .disc:nth-of-type(1),
input:hover + input + .disc:nth-of-type(1){
  top: -75px;
}
input:checked + .disc:nth-of-type(1),
input:checked + input + .disc:nth-of-type(1){
  transition: top 0.14s cubic-bezier(0.56, 0, 1, 1);
}
input:hover + .disc:nth-of-type(2),
input:hover + input + .disc:nth-of-type(6n+2) {
  top: -135px;
}
input:checked + .disc:nth-of-type(2),
input:checked + input + .disc:nth-of-type(2){
  transition: top 0.19s cubic-bezier(0.56, 0, 1, 1);
}
input:hover + .disc:nth-of-type(3),
input:hover + input + .disc:nth-of-type(3) {
  top: -195px;
}
input:checked + .disc:nth-of-type(3),
input:checked + input + .disc:nth-of-type(3) {
  transition: top 0.23s cubic-bezier(0.56, 0, 1, 1);
}
input:hover + .disc:nth-of-type(4),
input:hover + input + .disc:nth-of-type(4) {
  top: -255px;
}
input:checked + .disc:nth-of-type(4),
input:checked + input + .disc:nth-of-type(4) {
  transition: top 0.26s cubic-bezier(0.56, 0, 1, 1);
}
input:hover + .disc:nth-of-type(5),
input:hover + input + .disc:nth-of-type(5){
  top: -315px;
}
input:checked + .disc:nth-of-type(5),
input:checked + input + .disc:nth-of-type(5){
  transition: top 0.29s cubic-bezier(0.56, 0, 1, 1);
}
input:hover + .disc:nth-of-type(6n),
input:hover + input + .disc:nth-of-type(6n) {
  top: -375px;
}
input:checked + .disc:nth-of-type(6n),
input:checked + input + .disc:nth-of-type(6n) {
  transition: top 0.32s cubic-bezier(0.56, 0, 1, 1);
}

/* Fix stuck disc */
input:checked + .disc,
input:checked + input + .disc {
  top: 0 !important;
}

/* Tracking turns */
input:checked + .disc {
  counter-increment: player 2;
}
input:checked + input + .disc {
  counter-increment: player -2;
}

.grid::after {
  content: counter(player, lower-roman);
  display: inline-block;
  max-width: 840px;
  min-width: 420px;
  letter-spacing: 375px;
  font-family: monospace;
  font-size: 1px;
  overflow: hidden;
}

/* Draw outcome */
form:valid .column > .column > .column > .column > .column > .column > .column > .column::after {
  content: "It's a draw!";
  z-index: 1;
  position: absolute;
  left: 0;
  top: -75px;
  width: 420px;
  height: 435px;
  visibility: visible;
  color: #1f90ff;
  font-size: 30px;
  text-align: center;
  line-height: 60px;
  cursor: initial;
  pointer-events: auto;
  animation: outcome 1.5s;
}

/* Red column win */
input:checked + .disc + input + input:checked + .disc + input + input:checked + .disc + input + input:checked ~ .column::after,
/* Red row win */
input:nth-of-type(2):checked ~ .column > input:nth-of-type(2):checked ~ .column > input:nth-of-type(2):checked ~ .column > input:nth-of-type(2):checked ~ .column::after,
input:nth-of-type(4):checked ~ .column > input:nth-of-type(4):checked ~ .column > input:nth-of-type(4):checked ~ .column > input:nth-of-type(4):checked ~ .column::after,
input:nth-of-type(6):checked ~ .column > input:nth-of-type(6):checked ~ .column > input:nth-of-type(6):checked ~ .column > input:nth-of-type(6):checked ~ .column::after,
input:nth-of-type(8):checked ~ .column > input:nth-of-type(8):checked ~ .column > input:nth-of-type(8):checked ~ .column > input:nth-of-type(8):checked ~ .column::after,
input:nth-of-type(10):checked ~ .column > input:nth-of-type(10):checked ~ .column > input:nth-of-type(10):checked ~ .column > input:nth-of-type(10):checked ~ .column::after,
input:nth-of-type(12):checked ~ .column > input:nth-of-type(12):checked ~ .column > input:nth-of-type(12):checked ~ .column > input:nth-of-type(12):checked ~ .column::after,
/* Red diagonal win */
input:nth-of-type(2):checked ~ .column > input:nth-of-type(4):checked ~ .column > input:nth-of-type(6):checked ~ .column > input:nth-of-type(8):checked ~ .column::after,
input:nth-of-type(4):checked ~ .column > input:nth-of-type(6):checked ~ .column > input:nth-of-type(8):checked ~ .column > input:nth-of-type(10):checked ~ .column::after,
input:nth-of-type(6):checked ~ .column > input:nth-of-type(8):checked ~ .column > input:nth-of-type(10):checked ~ .column > input:nth-of-type(12):checked ~ .column::after,
input:nth-of-type(8):checked ~ .column > input:nth-of-type(6):checked ~ .column > input:nth-of-type(4):checked ~ .column > input:nth-of-type(2):checked ~ .column::after,
input:nth-of-type(10):checked ~ .column > input:nth-of-type(8):checked ~ .column > input:nth-of-type(6):checked ~ .column > input:nth-of-type(4):checked ~ .column::after,
input:nth-of-type(12):checked ~ .column > input:nth-of-type(10):checked ~ .column > input:nth-of-type(8):checked ~ .column > input:nth-of-type(6):checked ~ .column::after {
  content: "Red wins! :)";
  z-index: 2;
  position: absolute;
  left: 0;
  top: -75px;
  width: 420px;
  height: 435px;
  visibility: visible;
  color: #ff010b;
  font-size: 30px;
  text-align: center;
  line-height: 60px;
  cursor: initial;
  pointer-events: auto;
  animation: outcome 1s;
}

/* Yellow column win */
input:checked + input + .disc + input:checked + input + .disc + input:checked + input + .disc + input:checked ~ .column::after,
/* Yellow row win */
input:nth-of-type(1):checked ~ .column > input:nth-of-type(1):checked ~ .column > input:nth-of-type(1):checked ~ .column > input:nth-of-type(1):checked ~ .column::after,
input:nth-of-type(3):checked ~ .column > input:nth-of-type(3):checked ~ .column > input:nth-of-type(3):checked ~ .column > input:nth-of-type(3):checked ~ .column::after,
input:nth-of-type(5):checked ~ .column > input:nth-of-type(5):checked ~ .column > input:nth-of-type(5):checked ~ .column > input:nth-of-type(5):checked ~ .column::after,
input:nth-of-type(7):checked ~ .column > input:nth-of-type(7):checked ~ .column > input:nth-of-type(7):checked ~ .column > input:nth-of-type(7):checked ~ .column::after,
input:nth-of-type(9):checked ~ .column > input:nth-of-type(9):checked ~ .column > input:nth-of-type(9):checked ~ .column > input:nth-of-type(9):checked ~ .column::after,
input:nth-of-type(11):checked ~ .column > input:nth-of-type(11):checked ~ .column > input:nth-of-type(11):checked ~ .column > input:nth-of-type(11):checked ~ .column::after,
/* Yellow diagonal win */
input:nth-of-type(1):checked ~ .column > input:nth-of-type(3):checked ~ .column > input:nth-of-type(5):checked ~ .column > input:nth-of-type(7):checked ~ .column::after,
input:nth-of-type(3):checked ~ .column > input:nth-of-type(5):checked ~ .column > input:nth-of-type(7):checked ~ .column > input:nth-of-type(9):checked ~ .column::after,
input:nth-of-type(5):checked ~ .column > input:nth-of-type(7):checked ~ .column > input:nth-of-type(9):checked ~ .column > input:nth-of-type(11):checked ~ .column::after,
input:nth-of-type(7):checked ~ .column > input:nth-of-type(5):checked ~ .column > input:nth-of-type(3):checked ~ .column > input:nth-of-type(1):checked ~ .column::after,
input:nth-of-type(9):checked ~ .column > input:nth-of-type(7):checked ~ .column > input:nth-of-type(5):checked ~ .column > input:nth-of-type(3):checked ~ .column::after,
input:nth-of-type(11):checked ~ .column > input:nth-of-type(9):checked ~ .column > input:nth-of-type(7):checked ~ .column > input:nth-of-type(5):checked ~ .column::after {
  content: "Yellow wins! :)";
  z-index: 2;
  position: absolute;
  left: 0;
  top: -75px;
  width: 420px;
  height: 435px;
  visibility: visible;
  color: #ffd918;
  font-size: 30px;
  text-align: center;
  line-height: 60px;
  background: linear-gradient(#fff 60px, transparent 60px, transparent);
  cursor: initial;
  pointer-events: auto;
  animation: outcome 1s;
}

/* Button style */
button {
  margin: 20px auto;
  border: none;
  border-radius: 2px;
  padding: 12px 18px;
  font-size: 16px;
  text-transform: uppercase;
  cursor: pointer;
  color: #fff;
  background: #2196f3 center;
  box-shadow: 0 0 4px #999;
  outline: none;
  transition: background 0.5s;
}
button:hover {
  background: #47a7f5 radial-gradient(circle, transparent 1%, #47a7f5 1%) center/15000%;
}
button:active {
  background-color: #6eb9f7;
  background-size: 100%;
  transition: background 0s;
}

@keyframes outcome {
  0% {
    opacity: 0;
  }
  35% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}
</style>
''')

def start_2():
  with use_scope('game', clear=True):
    put_html('''<h1>Pure CSS By MoiGim Using PyWebIo</h1>
<form>
    <div class="discs">
        <input id="one" type="text" tabindex="-1" readonly>
        <input name="one" type="radio" tabindex="-1" checked>
        <input name="one" type="radio" tabindex="-1">
        <input name="one" type="radio" tabindex="-1">
        <label for="one"></label>
        <div class="disc one"></div>

        <input id="two" type="text" tabindex="-1" readonly>
        <input name="two" type="radio" tabindex="-1" checked>
        <input name="two" type="radio" tabindex="-1">
        <input name="two" type="radio" tabindex="-1">
        <label for="two"></label>
        <div class="disc two"></div>

        <input id="three" type="text" tabindex="-1" readonly>
        <input name="three" type="radio" tabindex="-1" checked>
        <input name="three" type="radio" tabindex="-1">
        <input name="three" type="radio" tabindex="-1">
        <label for="three"></label>
        <div class="disc three"></div>

        <input id="four" type="text" tabindex="-1" readonly>
        <input name="four" type="radio" tabindex="-1" checked>
        <input name="four" type="radio" tabindex="-1">
        <input name="four" type="radio" tabindex="-1">
        <label for="four"></label>
        <div class="disc four"></div>

        <input id="five" type="text" tabindex="-1" readonly>
        <input name="five" type="radio" tabindex="-1" checked>
        <input name="five" type="radio" tabindex="-1">
        <input name="five" type="radio" tabindex="-1">
        <label for="five"></label>
        <div class="disc five"></div>

        <input id="six" type="text" tabindex="-1" readonly>
        <input name="six" type="radio" tabindex="-1" checked>
        <input name="six" type="radio" tabindex="-1">
        <input name="six" type="radio" tabindex="-1">
        <label for="six"></label>
        <div class="disc six"></div>

        <input id="zero" type="text" tabindex="-1" readonly>

        <div class="spacer a"></div>
        <div class="separator ab"></div>
        <div class="spacer b"></div>
        <div class="separator bc"></div>
        <div class="spacer c"></div>

        <div class="tower a"></div>
        <div class="tower b"></div>
        <div class="tower c"></div>

        <div class="win">You win! :)</div>
    </div>
    <div class="bottom"></div>
    <button type="reset">New Game</button>
</form>

<style>/* Controls/Logic */
label,
input {
  position: absolute;
  top: -10vmin;
  margin: 0;
  border: 0;
  padding: 0;
  width: 30vmin;
  height: 52.5vmin;
  cursor: pointer;
  opacity: 0;
  pointer-events: none;
  -webkit-tap-highlight-color: transparent;
}
input:nth-child(6n + 2),
input:checked + input + input + label {
  left: 0;
}
input:nth-child(6n + 3),
input:checked + input + label {
  left: 30vmin;
}
input:nth-child(6n + 4),
input:checked + label {
  left: 60vmin;
}

label,
input:hover,
input[readonly]:focus + input,
input[readonly]:focus + input + input,
input[readonly]:focus + input + input + input {
  pointer-events: initial;
}
input[readonly],
input:nth-child(6n + 2):checked ~ input:nth-child(6n + 2),
input:nth-child(6n + 3):checked ~ input:nth-child(6n + 3),
input:nth-child(6n + 4):checked ~ input:nth-child(6n + 4) {
  pointer-events: none;
}

#one ~ input,
#one ~ label {
  z-index: 6;
}
#two ~ input,
#two ~ label {
  z-index: 5;
}
#three ~ input,
#three ~ label {
  z-index: 4;
}
#four ~ input,
#four ~ label {
  z-index: 3;
}
#five ~ input,
#five ~ label {
  z-index: 2;
}
#six ~ input,
#six ~ label {
  z-index: 1;
}

input#zero {
  z-index: 7;
}
input#zero:focus {
  pointer-events: none;
}
input[readonly]:focus + input:checked ~ #zero {
  left: 0;
  pointer-events: initial;
}
input[readonly]:focus + input + input:checked ~ #zero {
  left: 30vmin;
  pointer-events: initial;
}
input[readonly]:focus + input + input + input:checked ~ #zero {
  left: 60vmin;
  pointer-events: initial;
}

/* Discs */
.discs {
  position: relative;
  display: flex;
  flex-flow: column wrap;
  justify-content: flex-end;
  margin: 10vmin auto 0;
  width: 90vmin;
  height: 35vmin;
}

.disc {
  z-index: 1;
  border-radius: 1vmin;
  height: 4vmin;
  pointer-events: none;
  transition: order 0.3s step-end;
}
input:checked + input + input + label + .disc {
  order: 3;
}
input:checked + input + label + .disc {
  order: 6;
}
input:checked + label + .disc {
  order: 9;
}

input:focus + input:checked + input + input + label + .disc {
  order: 1;
  transition: order 0s;
  animation: float 3s ease-in-out infinite alternate;
}
input:focus + input + input:checked + input + label + .disc {
  order: 4;
  transition: order 0s;
  animation: float 3s ease-in-out infinite alternate;
}
input:focus + input + input + input:checked + label + .disc {
  order: 7;
  transition: order 0s;
  animation: float 3s ease-in-out infinite alternate;
}
@keyframes float {
  50% {
    transform: translateY(-1vmin);
  }
}

input:focus + input:hover + input + input + label + .disc,
input + input:active + input + input + label + .disc {
  order: 1;
}
input:focus + input + input:hover + input + label + .disc,
input + input + input:active + input + label + .disc {
  order: 4;
}
input:focus + input + input + input:hover + label + .disc,
input + input + input + input:active + label + .disc {
  order: 7;
}

.one {
  margin: 0 10vmin;
  width: 10vmin;
  background: linear-gradient(to right, #eea668, #ed7e1d, #e67e22);
}
.two {
  margin: 0 8vmin;
  width: 14vmin;
  background: linear-gradient(to right, #8ac4ea, #0f9fff, #3498db);
}
.three {
  margin: 0 6vmin;
  width: 18vmin;
  background: linear-gradient(to right, #f0d775, #fc0, #e6bd19);
}
.four {
  margin: 0 4vmin;
  width: 22vmin;
  background: linear-gradient(to right, #666, #000, #333);
}
.five {
  margin: 0 2vmin;
  width: 26vmin;
  background: linear-gradient(to right, #7ee2a8, #09f16a, #2ecc71);
}
.six {
  width: 30vmin;
  background: linear-gradient(to right, #f2a097, #ff3a24, #e74c3c);
}

/* Spacers/Separators */
.spacer {
  width: 30vmin;
  height: 1px;
  flex-grow: 0;
  pointer-events: none;
  transition: flex 0.3s;
}
.separator {
  width: 0;
  height: 100%;
}
.a {
  order: 2;
}
.ab {
  order: 3;
}
.b {
  order: 5;
}
.bc {
  order: 6;
}
.c {
  order: 8;
}

input[readonly]:focus + input:hover ~ .a,
input[readonly]:focus + input + input:hover ~ .b,
input[readonly]:focus + input + input + input:hover ~ .c {
  transition: flex 0s;
  flex-grow: 1;
}
input[readonly]:focus + input:checked ~ .a,
input[readonly]:focus + input + input:checked ~ .b,
input[readonly]:focus + input + input + input:checked ~ .c {
  flex-grow: 1;
}

/* Winning */
.win {
  z-index: 7;
  position: absolute;
  left: 0;
  right: 0;
  top: -10vmin;
  bottom: -7.5vmin;
  color: #966f33;
  font-family: Arial, sans-serif;
  font-size: 6vmin;
  line-height: 17.5vmin;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.3s;
}
input:nth-child(6n + 4):checked
  ~ input:nth-child(6n + 4):checked
  ~ input:nth-child(6n + 4):checked
  ~ input:nth-child(6n + 4):checked
  ~ input:nth-child(6n + 4):checked
  ~ input:nth-child(6n + 4):checked
  ~ .win {
  opacity: 1;
  pointer-events: initial;
}

/* Everything Else */
body {
  margin: 0;
  background-color: #ffffff;
}

h1 {
  margin: 0;
  padding: 5vmin;
  color: rgba(0, 0, 0, 0.5);
  font-family: Arial, sans-serif;
  font-size: 7.5vmin;
  font-weight: lighter;
  text-align: center;
  background: linear-gradient(
      to right,
      rgba(150, 111, 51, 0.4),
      rgba(150, 111, 51, 0.2)
    ),
    repeating-linear-gradient(
      to right,
      #eec487,
      #eec487 3vmin,
      #f3cf9a 3vmin,
      #f3cf9a 6vmin,
      #f8d8a2 6vmin,
      #f8d8a2 9vmin,
      #f1ca88 9vmin,
      #f1ca88 12vmin,
      #f4d09e 12vmin,
      #f4d09e 15vmin,
      #faddb0 15vmin,
      #faddb0 18vmin,
      #eec88a 18vmin,
      #eec88a 21vmin
    );
}

form {
  text-align: center;
}

.tower {
  position: absolute;
  top: 7.5vmin;
  border-radius: 1vmin;
  width: 5vmin;
  height: 30vmin;
  background: linear-gradient(to right, #d7b889, #b27315, #966f33);
}
.a {
  left: 12.5vmin;
}
.b {
  left: 42.5vmin;
}
.c {
  left: 72.5vmin;
}

.bottom {
  position: relative;
  display: block;
  margin: 0 auto;
  border-radius: 1vmin;
  width: 95vmin;
  height: 7.5vmin;
  background: linear-gradient(to right, rgba(255, 255, 255, 0.3), transparent),
    linear-gradient(
      #b27315,
      #966f33 13%,
      #faddb0 14.5%,
      #faddb0 27.5%,
      #966f33 29%,
      #966f33 42%,
      #faddb0 43.5%,
      #d7b889 56.5%,
      #966f33 58%,
      #966f33 71%,
      #d7b889 72.5%,
      #d7b889 85.5%,
      #966f33 87%,
      #b27315
    );
}

button {
  margin: 7.5vmin auto;
  border: none;
  border-radius: 1vmin;
  width: 35vmin;
  height: 10vmin;
  font-size: 4vmin;
  color: rgba(0, 0, 0, 0.5);
  background: linear-gradient(to right, #c39550, #966f33);
  outline: none;
  cursor: pointer;
  transition: background 0.3s;
}
button:hover {
  background: linear-gradient(to right, #caa163, #a77b39);
}
button:active {
  background: linear-gradient(to right, #cf9844, #9e6f29);
}
</style>''')

def start_3():
  with use_scope('game', clear=True):
    put_grid([[None,None,None,put_html('''<form id="tictactoe">
  <input type="radio" name="cell-0" id="cell-0-x" />
  <input type="radio" name="cell-0" id="cell-0-o" />
  <input type="radio" name="cell-1" id="cell-1-x" />
  <input type="radio" name="cell-1" id="cell-1-o" />
  <input type="radio" name="cell-2" id="cell-2-x" />
  <input type="radio" name="cell-2" id="cell-2-o" />
  <input type="radio" name="cell-3" id="cell-3-x" />
  <input type="radio" name="cell-3" id="cell-3-o" />
  <input type="radio" name="cell-4" id="cell-4-x" />
  <input type="radio" name="cell-4" id="cell-4-o" />
  <input type="radio" name="cell-5" id="cell-5-x" />
  <input type="radio" name="cell-5" id="cell-5-o" />
  <input type="radio" name="cell-6" id="cell-6-x" />
  <input type="radio" name="cell-6" id="cell-6-o" />
  <input type="radio" name="cell-7" id="cell-7-x" />
  <input type="radio" name="cell-7" id="cell-7-o" />
  <input type="radio" name="cell-8" id="cell-8-x" />
  <input type="radio" name="cell-8" id="cell-8-o" />

  <div id="board" class="center">
    <div class="tile" id="tile-0">
      <label for="cell-0-x"></label>
      <label for="cell-0-o"></label>
      <div></div>
    </div>
    <div class="tile" id="tile-1">
      <label for="cell-1-x"></label>
      <label for="cell-1-o"></label>
      <div></div>
    </div>
    <div class="tile" id="tile-2">
      <label for="cell-2-x"></label>
      <label for="cell-2-o"></label>
      <div></div>
    </div>
    <div class="tile" id="tile-3">
      <label for="cell-3-x"></label>
      <label for="cell-3-o"></label>
      <div></div>
    </div>
    <div class="tile" id="tile-4">
      <label for="cell-4-x"></label>
      <label for="cell-4-o"></label>
      <div></div>
    </div>
    <div class="tile" id="tile-5">
      <label for="cell-5-x"></label>
      <label for="cell-5-o"></label>
      <div></div>
    </div>
    <div class="tile" id="tile-6">
      <label for="cell-6-x"></label>
      <label for="cell-6-o"></label>
      <div></div>
    </div>
    <div class="tile" id="tile-7">
      <label for="cell-7-x"></label>
      <label for="cell-7-o"></label>
      <div></div>
    </div>
    <div class="tile" id="tile-8">
      <label for="cell-8-x"></label>
      <label for="cell-8-o"></label>
      <div></div>
    </div>
  </div>
  <div id="end">
    <div id="message" class="center">
      <div>
        <input type="reset" for="tictactoe" value="Play again" />
      </div>
    </div>
  </div>
</form>
<style>@import url('https://fonts.googleapis.com/css?family=Mandali|Raleway:900&display=swap');

input[type="radio"] {
  position: absolute;
  top: -9999em;
}




#board {
  width: 50vmin;
  height: 50vmin;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-template-rows: 1fr 1fr 1fr;
}

.tile {
  margin: 5%;
  position: relative;
}

.tile label,
.tile div {
  display: block;
  height: 100%;
  width: 100%;
  position: absolute;
  top: 0;
  left: 0;
  background: rgba(0,0,0,0.10);
  font-family: Raleway, Courier, 'Courier New', Sans, sans-serif;
  font-weight: bolder;
}

.tile div {
  display: none;
  overflow: hidden;
  text-shadow: 0 1px 6px rgba(0,0,0,0.85)
}

label[for$='-x'] {
  z-index: 1;
}

input:checked ~ #board label[for$='-o'] {
  z-index: 2;
}

input:checked ~ input:checked ~ #board label[for$='-x'] {
  z-index: 3;
}

input:checked ~ input:checked ~ input:checked ~ #board label[for$='-o'] {
  z-index: 4;
}

input:checked ~ input:checked ~ input:checked ~ input:checked ~ #board label[for$='-x'] {
  z-index: 5;
}

input:checked ~ input:checked ~ input:checked ~ input:checked ~ input:checked ~ #board label[for$='-o'] {
  z-index: 6;
}

input:checked ~ input:checked ~ input:checked ~ input:checked ~ input:checked ~ input:checked ~ #board label[for$='-x'] {
  z-index: 7;
}

input:checked ~ input:checked ~ input:checked ~ input:checked ~ input:checked ~ input:checked ~ input:checked ~ #board label[for$='-o'] {
  z-index: 8;
}

input:checked ~ input:checked ~ input:checked ~ input:checked ~ input:checked ~ input:checked ~ input:checked ~ input:checked ~ #board label[for$='-x'] {
  z-index: 9;
}

input[id*='-0-']:checked ~ #board label[for*='-0-'],
input[id*='-1-']:checked ~ #board label[for*='-1-'],
input[id*='-2-']:checked ~ #board label[for*='-2-'],
input[id*='-3-']:checked ~ #board label[for*='-3-'],
input[id*='-4-']:checked ~ #board label[for*='-4-'],
input[id*='-5-']:checked ~ #board label[for*='-5-'],
input[id*='-6-']:checked ~ #board label[for*='-6-'],
input[id*='-7-']:checked ~ #board label[for*='-7-'],
input[id*='-8-']:checked ~ #board label[for*='-8-'] {
  display: none;
}

input[id*='-0-']:checked ~ #board #tile-0 div,
input[id*='-1-']:checked ~ #board #tile-1 div,
input[id*='-2-']:checked ~ #board #tile-2 div,
input[id*='-3-']:checked ~ #board #tile-3 div,
input[id*='-4-']:checked ~ #board #tile-4 div,
input[id*='-5-']:checked ~ #board #tile-5 div,
input[id*='-6-']:checked ~ #board #tile-6 div,
input[id*='-7-']:checked ~ #board #tile-7 div,
input[id*='-8-']:checked ~ #board #tile-8 div {
  display: block;
}

input[id*='-0-x']:checked ~ #board #tile-0 div::before,
input[id*='-1-x']:checked ~ #board #tile-1 div::before,
input[id*='-2-x']:checked ~ #board #tile-2 div::before,
input[id*='-3-x']:checked ~ #board #tile-3 div::before,
input[id*='-4-x']:checked ~ #board #tile-4 div::before,
input[id*='-5-x']:checked ~ #board #tile-5 div::before,
input[id*='-6-x']:checked ~ #board #tile-6 div::before,
input[id*='-7-x']:checked ~ #board #tile-7 div::before,
input[id*='-8-x']:checked ~ #board #tile-8 div::before {
  content: "X";
  background: #004974;
  color: #89dcf6;
}

input[id*='-0-o']:checked ~ #board #tile-0 div::before,
input[id*='-1-o']:checked ~ #board #tile-1 div::before,
input[id*='-2-o']:checked ~ #board #tile-2 div::before,
input[id*='-3-o']:checked ~ #board #tile-3 div::before,
input[id*='-4-o']:checked ~ #board #tile-4 div::before,
input[id*='-5-o']:checked ~ #board #tile-5 div::before,
input[id*='-6-o']:checked ~ #board #tile-6 div::before,
input[id*='-7-o']:checked ~ #board #tile-7 div::before,
input[id*='-8-o']:checked ~ #board #tile-8 div::before {
  content: "O";
  background: #a60011;
  color: #ffc7b5;
}

.tile label:hover {
  cursor: pointer;
  background: rgba(0,0,0,0.25);
}

.tile label::before,
.tile div::before {
  color: #000;
  position: absolute;
  text-align:center;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 7.5vmin;
  font-weight: bold;
}

.tile div::before {
  padding: 100%;
}

.tile label[for$='-o']:hover::before {
  content: "O";
}

.tile label[for$='-x']:hover::before {
  content: "X";
}

#tile-0 {
  grid-column: 1;
  grid-row: 1;
}
#tile-0 label,
#tile-0 div {
  border-radius: 10% 0 0 0;
}
#tile-1 {
  grid-column: 2;
  grid-row: 1;
}
#tile-2 {
  grid-column: 3;
  grid-row: 1;
}
#tile-2 label,
#tile-2 div {
  border-radius: 0 10% 0 0;
}
#tile-3 {
  grid-column: 1;
  grid-row: 2;
}
#tile-4 {
  grid-column: 2;
  grid-row: 2;
}
#tile-5 {
  grid-column: 3;
  grid-row: 2;
}
#tile-6 {
  grid-column: 1;
  grid-row: 3;
}
#tile-6 label,
#tile-6 div {
  border-radius: 0 0 0 10%;
}
#tile-7 {
  grid-column: 2;
  grid-row: 3;
}
#tile-8 {
  grid-column: 3;
  grid-row: 3;
}
#tile-8 label,
#tile-8 div {
  border-radius: 0 0 10% 0;
}

#end {
  background: rgba(255,255,255,0.85);
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: none;
}

#message {
  text-align: center;
  font-size: 2rem;
  line-height: 2.2rem;
  font-weight: bold;
}

#message::before {
  content: "Tied game!"
}

#message input {
  background: #000;
  color: #fff;
  font-size: 1rem;
  padding: 0.5rem 1.75rem;
  margin: auto auto;
  margin-top: 2rem;
}

input:checked ~ input:checked ~ input:checked ~ input:checked ~ input:checked ~ input:checked ~ input:checked ~ input:checked ~ input:checked ~ #end,
#cell-0-x:checked ~ #cell-1-x:checked ~ #cell-2-x:checked ~ #end,
#cell-3-x:checked ~ #cell-4-x:checked ~ #cell-5-x:checked ~ #end,
#cell-6-x:checked ~ #cell-7-x:checked ~ #cell-8-x:checked ~ #end,
#cell-0-x:checked ~ #cell-3-x:checked ~ #cell-6-x:checked ~ #end,
#cell-1-x:checked ~ #cell-4-x:checked ~ #cell-7-x:checked ~ #end,
#cell-2-x:checked ~ #cell-5-x:checked ~ #cell-8-x:checked ~ #end,
#cell-0-x:checked ~ #cell-4-x:checked ~ #cell-8-x:checked ~ #end,
#cell-2-x:checked ~ #cell-4-x:checked ~ #cell-6-x:checked ~ #end,
#cell-0-o:checked ~ #cell-1-o:checked ~ #cell-2-o:checked ~ #end,
#cell-3-o:checked ~ #cell-4-o:checked ~ #cell-5-o:checked ~ #end,
#cell-6-o:checked ~ #cell-7-o:checked ~ #cell-8-o:checked ~ #end,
#cell-0-o:checked ~ #cell-3-o:checked ~ #cell-6-o:checked ~ #end,
#cell-1-o:checked ~ #cell-4-o:checked ~ #cell-7-o:checked ~ #end,
#cell-2-o:checked ~ #cell-5-o:checked ~ #cell-8-o:checked ~ #end,
#cell-0-o:checked ~ #cell-4-o:checked ~ #cell-8-o:checked ~ #end,
#cell-2-o:checked ~ #cell-4-o:checked ~ #cell-6-o:checked ~ #end {
  display: block;
}

#cell-0-x:checked ~ #cell-1-x:checked ~ #cell-2-x:checked ~ #end #message::before,
#cell-3-x:checked ~ #cell-4-x:checked ~ #cell-5-x:checked ~ #end #message::before,
#cell-6-x:checked ~ #cell-7-x:checked ~ #cell-8-x:checked ~ #end #message::before,
#cell-0-x:checked ~ #cell-3-x:checked ~ #cell-6-x:checked ~ #end #message::before,
#cell-1-x:checked ~ #cell-4-x:checked ~ #cell-7-x:checked ~ #end #message::before,
#cell-2-x:checked ~ #cell-5-x:checked ~ #cell-8-x:checked ~ #end #message::before,
#cell-0-x:checked ~ #cell-4-x:checked ~ #cell-8-x:checked ~ #end #message::before,
#cell-2-x:checked ~ #cell-4-x:checked ~ #cell-6-x:checked ~ #end #message::before {
  content: "Player 1 won!";
}

#cell-0-o:checked ~ #cell-1-o:checked ~ #cell-2-o:checked ~ #end #message::before,
#cell-3-o:checked ~ #cell-4-o:checked ~ #cell-5-o:checked ~ #end #message::before,
#cell-6-o:checked ~ #cell-7-o:checked ~ #cell-8-o:checked ~ #end #message::before,
#cell-0-o:checked ~ #cell-3-o:checked ~ #cell-6-o:checked ~ #end #message::before,
#cell-1-o:checked ~ #cell-4-o:checked ~ #cell-7-o:checked ~ #end #message::before,
#cell-2-o:checked ~ #cell-5-o:checked ~ #cell-8-o:checked ~ #end #message::before,
#cell-0-o:checked ~ #cell-4-o:checked ~ #cell-8-o:checked ~ #end #message::before,
#cell-2-o:checked ~ #cell-4-o:checked ~ #cell-6-o:checked ~ #end #message::before {
  content: "Player 2 won!";
}</style>'''),None,None]])





if __name__ == '__main__':
    import argparse
    from pywebio.platform.tornado_http import start_server as start_http_server
    from pywebio import start_server as start_ws_server

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    parser.add_argument("--http", action="store_true", default=False,
                        help='Whether to enable http protocol for communicates')
    args = parser.parse_args()

    if args.http:
        start_http_server(man, port=args.port, debug=False)
    else:
        # Since some cloud server may close idle connections (such as heroku),
        # use `websocket_ping_interval` to  keep the connection alive
        start_ws_server(man, port=args.port, websocket_ping_interval=30,debug=False)
