package main

import (
	"bytes"
	"context"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
)

// App struct
type App struct {
	ctx context.Context
}

// NewApp creates a new App application struct
func NewApp() *App {
	return &App{}
}

// startup is called when the app starts. The context is saved
// so we can call the runtime methods
func (a *App) startup(ctx context.Context) {
	a.ctx = ctx
}

func (a *App) shutdown(ctx context.Context) {
	a.ctx = ctx
}

func (a *App) menu(ctx context.Context) {
	a.ctx = ctx
}

type loginSet struct {
	Name 		string `json:"name"`
	Password 	string `json:"passwd"`
}

func (a *App) Login(id string, password string) string {
	loginData := loginSet{Name: id, Password: password}
	pbytes, _ := json.Marshal(loginData)
	buff := bytes.NewBuffer(pbytes)
	resp, err := http.Post("http://127.0.0.1:3000/login","application/json", buff)
    if err != nil {
        panic(err)
    }
 
    defer resp.Body.Close()
 
    // 결과 출력
    data, err := io.ReadAll(resp.Body)
    if err != nil {
        panic(err)
    }
	fmt.Println(string(data))
    return fmt.Sprintf("%s\n", string(data))
	// return fmt.Sprintf("Hello %s, It's show time!", id)
}

