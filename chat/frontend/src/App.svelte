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
  <div class="head">
    <div>
      <h3>접속 프로필</h3>
      <div>
        <button> </button>
      </div>
    </div>
  </div>
  <main>
    <div></div>
  </main>
  <div class="sidebar">
    <div>
      <div></div>
      <div></div>
      <div></div>
      <div></div>
    </div>
  </div>
</main>

<style>
  main {
    width: 100%;
    height: 100%;
    overflow: hidden;
    display: flex;
    flex-direction: column;
  }
  .head {
    width: 100%;
    height: 5rem;
    border-bottom: 3px solid black;
    
  }
  .sidebar {
    width: 100%;
    height: 5rem;
    border: 3px, 3px, 3px, 3px solid black;
  }

</style>
