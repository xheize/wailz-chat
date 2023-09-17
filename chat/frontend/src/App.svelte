<script lang="ts">
  import logo from './assets/images/logo-universal.png'
  import {Login} from '../wailsjs/go/main/App.js'

  let resultText: string = ""
  let name: string
  let passwd: string

  function login(): void {
    if (passwd == undefined || name == undefined) {
      alert("올바르게 입력하시오")
      return
    }
    Login(name, passwd).then(result => {
      resultText = result
    })
  }
</script>

<main>
  <h3>Private Chat</h3>
  <div class="result" id="result">{resultText}</div>
  <div class="input-box" id="input">
    <input autocomplete="off" bind:value={name} class="input" id="name" type="text"/>
  </div>
  <div class="input-box" id="password">
    <input autocomplete="off" bind:value={passwd} class="input" id="passwd" type="text"/>
  </div>
  <div>
    <button class="btn" on:click={login}>Greet</button>
  </div>
</main>

<style>
  main {
    overflow: hidden;
  }

  .result {
    height: auto;
    line-height: 20px;
    margin: 1.5rem auto;
  }

  .input-box .input {
    border: none;
    border-radius: 3px;
    outline: none;
    height: 30px;
    line-height: 30px;
    padding: 0 10px;
    background-color: rgba(240, 240, 240, 1);
    -webkit-font-smoothing: antialiased;
  }

  .input-box .input:hover {
    border: none;
    background-color: rgba(255, 255, 255, 1);
  }

  .input-box .input:focus {
    border: none;
    background-color: rgba(255, 255, 255, 1);
  }

</style>
