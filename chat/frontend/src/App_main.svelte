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
  <head>
    <div>
      <h3>접속 프로필</h3>
    </div>
  </head>
  <main>
    <td>
      <tr>
        testing
      </tr>
    </td>
  </main>
  <sidebar>
    <div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
    </div>
  </sidebar>
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
