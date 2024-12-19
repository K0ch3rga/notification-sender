package main

import (
	"fmt"
	"net/http"
	"strings"
)

func main() {
	http.HandleFunc("/", handle)
	http.HandleFunc("/log", log)
	http.ListenAndServe(":8080", nil)
}

func getpath(path string) (module, mode, val string) {
	parts := strings.Split(path, "/")
	switch len(parts) {
	case 4:
		val = parts[3]
		fallthrough
	case 3:
		mode = parts[2]
		fallthrough
	case 2:
		module = parts[1]
	}
	return // Named return values are used, so just return here
}

func handle(w http.ResponseWriter, r *http.Request) {
	module, mode, val := getpath(r.URL.Path)
	fmt.Println(module, mode, val)
	http.Post(val+"/log", "application/json", r.Body)
}

func log(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello, World!")
}
